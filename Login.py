from flask import Flask, request, render_template, redirect, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/signup"
app.secret_key = "your-secret-key"
mongo = PyMongo(app)
db = mongo.db

@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = {"username": username, "password": password}
        
        
        if db.users.find_one(user):
            return "I love you"


    return render_template("Login.html")

if __name__ == '__main__':
    app.run(debug = True)