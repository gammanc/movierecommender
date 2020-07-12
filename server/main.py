from flask import Flask, jsonify, request
from flask_cors import CORS
from data_utils import retrieve_popular_movies

app = Flask(__name__)
app.config['ENV'] = "development"

CORS(app)

@app.route("/api/movies/popular")
def retrieve_popular():
    list_size = int(request.args.get("max", "10"))
    list_size = 5 if list_size < 5 else list_size
    return jsonify(retrieve_popular_movies(list_size))

if __name__ == "__main__":
    app.run(debug=True)
