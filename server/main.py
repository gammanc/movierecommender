from flask import Flask, jsonify, request
from flask_cors import CORS
from data_utils import retrieve_popular_movies, retrieve_names, get_recommendations

app = Flask(__name__)
app.config['ENV'] = "development"

CORS(app)

@app.route("/api/movies/popular")
def retrieve_popular():
    list_size = int(request.args.get("max", "10"))
    list_size = 5 if list_size < 5 else list_size
    return jsonify(retrieve_popular_movies(list_size))

@app.route("/api/movies/names")
def get_movies_titles():
    list_size = int(request.args.get("max", "1"))
    list_size = None if list_size < 5 else list_size
    return jsonify(retrieve_names(list_size))

@app.route("/api/movies/recommend")
def get_movie_recommendations():
    title = request.args.get("title", None)
    if title is None:
        return jsonify({ "error": "Query param 'title' not provided"}), 400
    list_size = int(request.args.get("max", "5"))
    list_size = 5 if list_size < 5 else list_size
    return jsonify(get_recommendations(title, list_size))

if __name__ == "__main__":
    app.run(debug=True)
