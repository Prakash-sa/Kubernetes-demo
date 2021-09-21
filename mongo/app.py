from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='localhost',
                         port=30081, 
                         username='username', 
                         password='password',
                        authSource="admin")
    print(client["animal_db"])
    db = client["animal_db"]["animals"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of animals."

@app.route("/add_one")
def add_one():
    db=""
    try:
        db = get_db()
        db.insert_one({'id': "4", 'name': "Crow",'type':"bird"})
        return jsonify(message="success")
    except:
        print("Cannot access")
        pass
    finally:
        if type(db)==MongoClient:
            db.close()
    

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        print("Cannot access")
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)