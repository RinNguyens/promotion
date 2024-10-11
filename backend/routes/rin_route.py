from flask import Blueprint, jsonify

rin_route = Blueprint('rin_route', __name__)

@rin_route.route("/rin", methods=["GET"])
def hello():
    try:
        response = {
            "data": {"message": "Hello from Rin!", "history": [1, 2, 3, 4]},
            "status": 200,
        }
        return jsonify(response), 200
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500