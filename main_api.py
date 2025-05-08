from flask import Flask, jsonify
from main import main
import logging

logging.basicConfig(
    filename='logs/app.log',             # Log file path
    filemode='w',                   # 'a' = append, 'w' = overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO              # Log level
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    logger.info("access predict, calculating...")
    res = main()
    logger.info("finish predict")
    return jsonify({"output": str(res)})

@app.route('/', methods=['GET'])
def home():
    logger.info("access home page")
    return "Hello World!"

if __name__ == '__main__':
    logger.info("starting the app...")
    app.run(host="0.0.0.0", port=8080)

