import os
import json
from flask import Blueprint, jsonify, render_template


review_blueprint = Blueprint("review", __name__, template_folder="templates")

RESULTS_FILE = "benchmarks/results.json"


def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


@review_blueprint.route("/")
def review_page():
    """Renders the review page."""
    return render_template("review.html")


@review_blueprint.route("/results")
def get_results():
    """Returns all past evaluation results."""
    try:
        return jsonify(load_results())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@review_blueprint.route("/results/<timestamp>")
def get_result(timestamp):
    """Returns a specific evaluation result."""
    try:
        results = load_results()
        result = next((r for r in results if r["timestamp"] == timestamp), None)
        if result:
            return jsonify(result)
        return jsonify({"error": "Result not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
