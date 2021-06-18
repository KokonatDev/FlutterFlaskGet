from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({'message' : "Front-end connected Back-end"})

