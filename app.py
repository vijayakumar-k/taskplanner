from flask import Flask
from bson import json_util
# from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

#mongo db connection
# app.config["MONGO_URI"] = "mongodb://taskplanner-server:PKtgp7V16ytOOGyVim8nEkUyyBLE7P63HCJMOCKlyPIGQhYekYIklFpxzoYT07sbopWq9gX5Y45vACDbCcZesg==@taskplanner-server.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@taskplanner-server@/taskplanner-database"
# app.config["MONGO_URI"] = "mongodb://localhost:27017/taskplannerdb"
# mongo = PyMongo(app)
# if mongo.db is None:
    # print("Connection failed")

#pymongo connection
client = MongoClient("mongodb://taskplanner-server:PKtgp7V16ytOOGyVim8nEkUyyBLE7P63HCJMOCKlyPIGQhYekYIklFpxzoYT07sbopWq9gX5Y45vACDbCcZesg==@taskplanner-server.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@taskplanner-server@")
# client = MongoClient("mongodb://localhost:27017/taskplannerdb")
db = client["taskplanner-database"]
if db is None:
    print("Connect to db failed")
tasks = db["tasks"]
if tasks is None:
    print("Connect to tasks collection failed")

mydict = { "name": "ta1", "date": "today" }

@app.route("/")
def welcome():
    return "Welcome Vijay in Azure!!"

@app.route("/users")
def users():
    return "Welcome Users to Task planner!!"

@app.route('/tasks/<task_name>')
def add_task(task_name):
    mydict["name"]= task_name
    x = tasks.insert_one(mydict)
    return f"Inserted task: {x.inserted_id}!"


@app.route("/tasks")
def get_all_tasks():
    return json_util.dumps(tasks.find({}))