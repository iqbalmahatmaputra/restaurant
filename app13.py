import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for
)
import certifi
from pymongo import MongoClient


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)

db = client[DB_NAME]

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index13.html")


@app.route('/restaurants', methods=["GET"])
def get_restaurants():
    # This api endpoint should fetch a list of restaurants
    restaurants = list(db.restaurants.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'restaurants': restaurants})


@app.route('/restaurants/delete', methods=["POST"])
def delete_restaurants():
    name = request.form.get('name')
    # This api endpoint should fetch a list of restaurants
    db.restaurants.delete_one({'name': name})
    return jsonify({'result': 'success', 'msg': 'Kamu berhasil menghapus data restaurants!'})


@app.route('/restaurants/create_restaurant', methods=["POST"])
def create_restaurant():
    name = request.form.get('name')
    categories = request.form.get('categories')
    location = request.form.get('location')
    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')
    # This api endpoint should fetch a list of restaurants
    doc = {
        'name': name,
        'categories': categories,
        'location': location,
        'coordinates': [longitude, latitude]
    }
    db.restaurants.insert_one(doc)
    return jsonify({'result': 'success', 'msg': 'Kamu berhasil menambahkan data restaurants!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5003, debug=True)
