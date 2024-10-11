from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import pandas as pd

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")

CORS(app, resources={r"/*": {"origins": "*"}})

# Import routes from the routes module
from routes.rin_route import rin_route
from routes.detail_scheme_route import detail_scheme_route
# Register Blueprints
app.register_blueprint(rin_route, url_prefix="/api")
app.register_blueprint(detail_scheme_route, url_prefix="/api")

# @app.route("/api/get-scheme-detail", methods=["GET"])
# def get_scheme_detail():
#     channel = request.args.get("channel")
#     scheme = request.args.get("scheme")

#     if not channel or not scheme:
#         return jsonify({"error": "Missing channel or scheme", "statusCode": 400}), 400

#     # Filter data based on channel and scheme
#     filtered_data = df[(df["CHANNEL"] == channel) & (df["SCHEME"] == scheme)]
#     # Check if no records are found for the given channel and scheme
#     if filtered_data.empty:
#         return (
#             jsonify(
#                 {"error": "No matching records found", "data": [], "statusCode": 404}
#             ),
#             404,
#         )

#     # Convert unique schemes to the desired format
#     scheme_detail = []

#     # Push DETAIL_SCHEME to scheme_detail for matching records
#     if not filtered_data.empty:
#         detail_schemes = filtered_data["DETAIL_SCHEME"].unique()
#         for detail_scheme in detail_schemes:
#             scheme_detail.append({"value": detail_scheme, "label": detail_scheme})

#     # Add 'other' option to scheme_detail
#     scheme_detail.append({"value": "other", "label": "Other"})

#     return jsonify({"data": scheme_detail, "statusCode": 200}), 200


# Serve React frontend
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(port=4000, debug=True)  # Specify port 4000 here
