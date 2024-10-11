from flask import Blueprint, jsonify, request
import os
import pandas as pd

detail_scheme_route = Blueprint("detail_scheme_route", __name__)

# Get the absolute path to the CSV file
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "../data/data_step1.csv")
# Load the CSV file
df = pd.read_csv(csv_file_path)

@detail_scheme_route.route("/detail_scheme", methods=["GET"])
def get_scheme_detail():
    channel = request.args.get("channel")
    scheme = request.args.get("scheme")

    if not channel or not scheme:
        return jsonify({"error": "Missing channel or scheme", "statusCode": 400}), 400

    # Filter data based on channel and scheme
    filtered_data = df[(df["CHANNEL"] == channel) & (df["SCHEME"] == scheme)]
    # Check if no records are found for the given channel and scheme
    if filtered_data.empty:
        return (
            jsonify(
                {"error": "No matching records found", "data": [], "statusCode": 404}
            ),
            404,
        )

    # Convert unique schemes to the desired format
    scheme_detail = []

    # Push DETAIL_SCHEME to scheme_detail for matching records
    if not filtered_data.empty:
        detail_schemes = filtered_data["DETAIL_SCHEME"].unique()
        for detail_scheme in detail_schemes:
            scheme_detail.append({"value": detail_scheme, "label": detail_scheme})

    # Add 'other' option to scheme_detail
    scheme_detail.append({"value": "other", "label": "Other"})

    return jsonify({"data": scheme_detail, "statusCode": 200}), 200
