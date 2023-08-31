from flask import Flask
from bson import json_util
from pymongo import MongoClient
import os

app = Flask(__name__)

db_connection_string = os.environ.get('AZURE_COSMOS_CONNECTIONSTRING', 'mongodb://localhost:27017/taskplannerdb')
client = MongoClient(db_connection_string)


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