from flask import Flask, jsonify
from main import main


app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    res = main()
    return jsonify({"output": str(res)})

@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

