from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = "secure_key_123"

def get_db_connection():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        database="assignment",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def home():
    # REMOVE session.clear() from here!
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    print(f"DEBUG: Login attempt for {username}") # CHECK TERMINAL FOR THIS

    db = get_db_connection()
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM usernames WHERE username = %s", (username,))
            user_record = cursor.fetchone()

            if user_record:
                if user_record['password'] == password:
                    print("DEBUG: Password Correct")
                    session['user'] = username
                    return redirect(url_for('changepass'))
                else:
                    print("DEBUG: Password INCORRECT")
                    flash("Incorrect password for this user!")
                    return redirect(url_for('home'))
            else:
                print("DEBUG: Creating new user")
                cursor.execute("INSERT INTO usernames (username, password) VALUES (%s, %s)", (username, password))
                db.commit()
                session['user'] = username
                return redirect(url_for('changepass'))
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return f"Database Error: {e}"
    finally:
        db.close()

@app.route("/change", methods=["GET", "POST"])
def changepass():
    if 'user' not in session:
        return redirect(url_for('home'))

    username = session['user']
    db = get_db_connection()
    
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM usernames WHERE username = %s", (username,))
            user_record = cursor.fetchone()
            
            if not user_record:
                session.clear()
                return render_template("user_not_found.html", name=username)

            if request.method == "POST":
                current_pw = request.form.get("current_password")
                new_pw = request.form.get("new_password")

                if user_record['password'] == current_pw:
                    cursor.execute("UPDATE usernames SET password = %s WHERE username = %s", (new_pw, username))
                    db.commit()
                    flash("✅ Password updated successfully!")
                    return redirect(url_for('changepass'))
                else:
                    flash("❌ Current password incorrect!")
                    return redirect(url_for('changepass'))

    finally:
        db.close()

    return render_template("changepassword.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)