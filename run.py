from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Go to /time to see the current time."

@app.route('/time')
def get_time():
    now = datetime.datetime.now().isoformat()
    return jsonify({"current_time": now})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
