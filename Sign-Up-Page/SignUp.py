from flask import Flask, url_for, redirect,Response, url_for,request,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Signup"
Mongo = PyMongo(app)
db  = Mongo.db

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
        name=request.form["username"]
        email=request.form["email"]

        signup = { "username": name, "email": email }

        db.user.insert_one(signup)

    return render_template("SignUp.html")

if __name__ == '__main__':
    app.run(debug = True)