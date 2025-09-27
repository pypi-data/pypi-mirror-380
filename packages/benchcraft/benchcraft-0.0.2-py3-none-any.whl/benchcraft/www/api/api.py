import os
import json
import re
from flask import Blueprint, request, jsonify


api_blueprint = Blueprint("api", __name__)


# Initial Setup
BENCHMARKS_DIR = "benchmarks"
RESULTS_FILE = "benchmarks/results.json"

if not os.path.exists(BENCHMARKS_DIR):
    os.makedirs(BENCHMARKS_DIR)

if not os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "w") as f:
        json.dump([], f)


# Helper: Sanitize filenames
def sanitize_filename(name):
    """Sanitizes a string to be used as a filename."""
    name = re.sub(r"[^\w\s-]", "", name).strip().lower()
    name = re.sub(r"[-\s]+", "-", name)
    return name


@api_blueprint.route("/benchmarks", methods=["GET"])
def get_benchmarks():
    """Lists all available benchmark files."""
    try:
        files = [f for f in os.listdir(BENCHMARKS_DIR) if f.endswith(".json")]
        benchmarks = []
        for filename in files:
            if "results.json" in filename:
                continue  # Skip results file
            try:
                with open(os.path.join(BENCHMARKS_DIR, filename), "r") as f:
                    data = json.load(f)
                    benchmarks.append(
                        {
                            "filename": filename,
                            "name": data.get("name", "Untitled Benchmark"),
                        }
                    )
            except (IOError, json.JSONDecodeError):
                # Skip corrupted or unreadable files
                continue
        return jsonify(benchmarks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route("/benchmarks", methods=["POST"])
def save_benchmark():
    """Saves a new or existing benchmark in Sample-compatible format."""
    try:
        data = request.get_json()
        if not data or "name" not in data or not data["name"]:
            return jsonify({"error": "Benchmark name is required."}), 400

        # Required benchmark-level metadata
        benchmark_name = data["name"]
        author_name = data.get("author", "Unknown Author")
        benchmark_revision = data.get("revision", "1.0")
        benchmark_description = data.get("description", "")
        evaluation_type = data.get("evaluationType", "multiple_choice")
        benchmark_system_prompt = data.get("systemPrompt", "")
        samples = data.get("samples", [])

        # Normalize samples to fit the Sample model schema
        formatted_samples = []
        for i, s in enumerate(samples, start=1):
            formatted_samples.append(
                {
                    "id": s.get("id", i),  # fallback to index
                    "input": s.get("input", ""),  # string or list of ChatMessage dicts
                    "target": s.get("target", ""),
                    "metadata": s.get("metadata", None),
                }
            )

        # Full benchmark JSON
        benchmark_payload = {
            "name": benchmark_name,
            "author": author_name,
            "revision": benchmark_revision,
            "description": benchmark_description,
            "evaluationType": evaluation_type,
            # TODO: Move the below into an "evaluation:" field in future:
            "systemPrompt": benchmark_system_prompt,
            "samples": formatted_samples,
        }

        # Save to disk
        filename = sanitize_filename(benchmark_name) + ".json"
        filepath = os.path.join(BENCHMARKS_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(benchmark_payload, f, indent=4)

        return (
            jsonify({"message": "Benchmark saved successfully.", "filename": filename}),
            201,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route("/benchmarks/<filename>", methods=["GET"])
def get_benchmark(filename):
    """Loads a specific benchmark file."""
    try:
        # Security: Ensure filename is safe
        if not re.match(r"^[\w-]+\.json$", filename):
            return jsonify({"error": "Invalid filename"}), 400

        filepath = os.path.join(BENCHMARKS_DIR, filename)
        if not os.path.exists(filepath):
            return jsonify({"error": "Benchmark not found."}), 404

        with open(filepath, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route("/benchmarks/<filename>", methods=["DELETE"])
def delete_benchmark(filename):
    """Deletes a specific benchmark file."""
    try:
        # Security: Ensure filename is safe
        if not re.match(r"^[\w-]+\.json$", filename):
            return jsonify({"error": "Invalid filename"}), 400

        filepath = os.path.join(BENCHMARKS_DIR, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({"message": "Benchmark deleted successfully."})
        else:
            return jsonify({"error": "Benchmark not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
