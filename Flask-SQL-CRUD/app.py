import pymysql
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "super_secret_key"

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '123456',
    'database': 'assignment',
    'port': 3306,
}

def get_db_connection():
    return pymysql.connect(**db_config)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=['POST'])
def submit():
    user = request.form.get('username')
    pw = request.form.get('password')
    q = request.form.get('hint_question')
    a = request.form.get('hint_answer')

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # 1. Check if user already exists
            check_query = "SELECT * FROM myusers WHERE username = %s"
            cursor.execute(check_query, (user,))
            existing_user = cursor.fetchone()

            if existing_user:
                flash(f"Error: The username '{user}' is already taken!", "danger")
                return redirect(url_for('home'))

            # 2. If not exists, Insert new user
            insert_query = "INSERT INTO myusers (username, password, hint_question, hint_answer) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (user, pw, q, a))
            connection.commit()
            
            flash("Registration successful! Welcome aboard.", "success")
            
    except Exception as e:
        flash(f"An error occurred: {str(e)}", "danger")
    finally:
        connection.close()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)