from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Vijay in Azure!!"



@app.route("/users")
def users():
    return "Welcome Users to Task planner!!"