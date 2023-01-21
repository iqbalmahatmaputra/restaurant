from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify
)
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("prac_map.html")


@app.route("/tugas")
def main2():
    return render_template("prac_map_2.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
