from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
app = Flask(__name__)

mongodb = MongoClient("localhost" , 27017)
db = mongodb.dbsparta

@app.route('/', methods=['GET'])
def home():
    print("flask_server_is_working")
    return render_template("index.html")

@app.route('/customer_info_process', methods=['POST'])
def process_customer_info():
 
    db.food_orders.insert_one({"name" : request.form["username"], "select_count" : request.form["select"], "address" : request.form["address"], "phone_number" : request.form["phone_number"]})
    food_orders_collection = list(db.food_orders.find({}, {'_id':False}))
    print(food_orders_collection)
    return jsonify(food_orders_collection)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)