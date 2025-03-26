from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_coordinates():
    response_data = {
        "status": "success",
        "count": 1,
        "coordinates": [
            {"id": 1, "latitude": 0.0, "longitude": 0.0},
        ]
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
