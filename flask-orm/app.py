from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "orm_secure_key"

# 1. Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 2. The ORM Model
class User(db.Model):
    __tablename__ = 'usernames'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# --- ROUTES ---

@app.route("/")
def home():
    # Load the app on login.html as requested
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("username")
    pw = request.form.get("password")
    
    # Check if user exists (READ)
    user = User.query.filter_by(username=name).first()

    if user:
        if user.password == pw:
            session['user'] = user.username
            return redirect(url_for('changepass'))
        else:
            flash("❌ Incorrect password!")
            return redirect(url_for('home'))
    else:
        # User does not exist, redirect to signup
        flash("❌ User does not exist. Please sign up first.")
        return redirect(url_for('signup_page'))

@app.route("/signup_page")
def signup_page():
    return render_template("signup.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("username")
    pw = request.form.get("password")

    # Double check if user already exists
    existing_user = User.query.filter_by(username=name).first()
    if existing_user:
        flash(" Username already taken!")
        return redirect(url_for('signup_page'))

    # CREATE: Add new user
    new_user = User(username=name, password=pw)
    db.session.add(new_user)
    db.session.commit()
    
    flash(" Account created! Please log in.")
    return redirect(url_for('home'))

@app.route("/change", methods=["GET", "POST"])
def changepass():
    if 'user' not in session:
        return redirect(url_for('home'))

    username = session['user']
    user = User.query.filter_by(username=username).first()

    if request.method == "POST":
        current_pw = request.form.get("current_password")
        new_pw = request.form.get("new_password")

        if user.password == current_pw:
            # UPDATE
            user.password = new_pw
            db.session.commit()
            flash(" Password updated successfully!")
        else:
            flash(" Current password incorrect!")
            
    return render_template("changepassword.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)