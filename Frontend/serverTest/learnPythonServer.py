from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/articles")
def get_articles():
    articles = [
        {"name": "Black Holes", "resume": "Regions of spacetime where gravity is so strong nothing can escape."},
        {"name": "Dark Matter", "resume": "A mysterious form of matter that makes up most of the universe’s mass."},
        {"name": "Exoplanets", "resume": "Planets that orbit stars outside our solar system."}
    ]
    return jsonify(articles)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
