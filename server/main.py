from flask import Flask, jsonify

app = Flask(__name__)
app.config['ENV'] = "development"

@app.route("/")
def home():
    return jsonify({ "hello": "world"})

if __name__ == "__main__":
    app.run(debug=True)