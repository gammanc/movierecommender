from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['ENV'] = "development"

CORS(app)

@app.route("/")
def home():
    return jsonify({ "hello": "world"})

if __name__ == "__main__":
    app.run(debug=True)