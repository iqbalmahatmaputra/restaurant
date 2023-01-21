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

app = Flask(__name__)

password = 'iqbalmp'
cxn_str = f'mongodb+srv://iqbalmp:{password}@cluster0.ligsrx6.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cxn_str, tlsCAFile=certifi.where())
db = client.dbsparta_plus_week3


@app.route('/')
def main():
    return render_template("index13.html")


@app.route('/restaurants', methods=["GET"])
def get_restaurants():
    # This api endpoint should fetch a list of restaurants
    return jsonify({'result': 'success', 'restaurants': []})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
