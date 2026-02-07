from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/admin')
def admin():
   return render_template("admin.html")

@app.route('/course.html')
def course():
   return render_template("course.html")

@app.route('/contact.html')
def contact():
   return render_template("contact.html")

@app.route('/alumni.html')
def alumni():
   return render_template("alumni.html")



if __name__ == "__main__":
    # use_reloader=True is the key for automatic detection
    app.run(debug=True, port=5000, use_reloader=True)