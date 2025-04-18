from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_coordinates():
    response_data = {
        "status": "success",
        "count": 1,
        "coordinates": [
            {
                "id": 1,
                "name": "no parking zone 1",
                "start": [12.9373, 77.5449],
                "end": [12.9374, 77.5451]
            }
        ]
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(port=5555, debug=True)

