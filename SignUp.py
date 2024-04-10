from flask import Flask, url_for, redirect,Response, url_for,request,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/SignUp"
Mongo = PyMongo(app)
db  = Mongo.db

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]

        user = {"name":name, "email": email, "password": password }
        

        if  db.user.insert_one(user):
            return redirect(url_for("login"))
        else:
            return render_template("SignUp.html" )
        

    return render_template("SignUp.html"  )

@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        user = {"name": name, "password": password}
        
        
        if db.user.find_one(user):
            return "I love you"


    return render_template("Login.html")
if __name__ == '__main__':
    app.run(debug = True)