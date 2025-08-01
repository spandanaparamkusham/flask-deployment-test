from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/status")
def status():
    return jsonify({"status": "Running", "success": True})

if __name__ == "__main__":
    app.run(debug=True)
