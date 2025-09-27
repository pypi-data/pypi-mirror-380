import os
import re
import json
import time
import asyncio
from flask import Blueprint, jsonify, request, render_template
from openai import APIError, AsyncOpenAI
from typing import Any, Dict, List
from datetime import datetime, timezone
from collections import defaultdict


run_blueprint = Blueprint("run", __name__, template_folder="templates")


# Initial Setup
BENCHMARKS_DIR = "benchmarks"
RESULTS_FILE = "benchmarks/results.json"

if not os.path.exists(BENCHMARKS_DIR):
    os.makedirs(BENCHMARKS_DIR)

if not os.path.exists(RESULTS_FILE):
    with open(RESULTS_FILE, "w") as f:
        json.dump([], f)


# Helper: Load results file
def load_results():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


# Helper: Save results file
def save_results(results):
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, indent=4)


@run_blueprint.route("/", methods=["GET"])
def run_page():
    """Renders the run page."""
    return render_template("run.html")


@run_blueprint.route("/models", methods=["GET"])
def get_models():
    """Returns a list of available models."""
    models = [
        {"id": "moonshotai/kimi-k2", "name": "Kimi K2"},
        {"id": "openai/gpt-5", "name": "GPT-5"},
        {"id": "deepseek/deepseek-chat-v3-0324", "name": "DeepSeek"},
        {"id": "anthropic/claude-sonnet-4", "name": "Claude Sonnet 4"},
        {"id": "google/gemini-2.5-flash", "name": "Gemini 2.5 Flash"},
        {"id": "mistralai/mistral-7b-instruct:free", "name": "Mistral 7B Instruct"},
    ]

    return jsonify(models)


###### HELPER FUNCTIONS FOR EVALUATION ######


def extract_choice(response_text: str) -> str:
    """Extracts the first valid choice (A, B, C, or D) from a response string."""
    if not response_text:
        return "N/A"
    match = re.search(r"\b([A-D])\b", response_text.strip())
    return match.group(1) if match else "N/A"


async def evaluate_sample(
    client: AsyncOpenAI, sample: Dict[str, Any], system_prompt: str, model_name: str
) -> Dict[str, Any]:
    """Sends a single sample to the LLM and evaluates the response."""
    try:
        completion = await client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": sample["input"]},
            ],
            max_tokens=10,
            temperature=0.0,
        )
        response_text = completion.choices[0].message.content
        model_choice = extract_choice(response_text)
        is_correct = model_choice == sample["target"]

    except APIError as e:
        model_choice = f"API_ERROR: {e.status_code}"
        is_correct = False

    return {
        "id": sample.get("id", "N/A"),
        "topic": sample.get("metadata", {}).get("topic", "uncategorized"),
        "target": sample.get("target"),
        "response": model_choice,
        "is_correct": is_correct,
    }


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculates overall and per-topic accuracy from evaluation results."""
    total_questions = len(results)
    total_correct = sum(r["is_correct"] for r in results)

    topic_results = defaultdict(lambda: {"correct": 0, "total": 0})
    for r in results:
        topic = r["topic"]
        topic_results[topic]["total"] += 1
        if r["is_correct"]:
            topic_results[topic]["correct"] += 1

    topic_accuracy = {
        topic: (data["correct"] / data["total"]) * 100
        for topic, data in topic_results.items()
    }

    return {
        "overall_accuracy": (
            (total_correct / total_questions) * 100 if total_questions > 0 else 0
        ),
        "total_correct": total_correct,
        "total_questions": total_questions,
        "topic_accuracy": topic_accuracy,
    }


###### END HELPER FUNCTIONS #####


@run_blueprint.route("/benchmark", methods=["POST"])
def run_benchmark():
    """Runs an evaluation for a given benchmark + model."""
    data = request.get_json()
    benchmark_file = data.get("benchmark_file")
    model_name = data.get("model_name")

    if not benchmark_file or not model_name:
        return jsonify({"error": "benchmark_file and model_name are required"}), 400

    filepath = os.path.join(BENCHMARKS_DIR, benchmark_file)
    if not os.path.exists(filepath):
        return jsonify({"error": "Benchmark file not found."}), 404

    # Run evaluation asynchronously
    async def run_eval():
        client = AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ.get("OPENROUTER_API_KEY"),
        )
        with open(filepath, "r") as f:
            benchmark_data = json.load(f)

        tasks = [
            evaluate_sample(
                client, s, benchmark_data.get("systemPrompt", ""), model_name
            )
            for s in benchmark_data.get("samples", [])
        ]

        start_time = time.time()
        results = await asyncio.gather(*tasks)
        duration = time.time() - start_time

        metrics = calculate_metrics(results)

        # Record run summary
        all_results = load_results()
        timestamp = datetime.now(timezone.utc).isoformat()
        run_record = {
            "timestamp": timestamp,
            "benchmark_name": benchmark_data.get("name", benchmark_file),
            "model": model_name,
            "accuracy": metrics["overall_accuracy"],
            "details": results,
            "duration": duration,
        }
        all_results.append(run_record)

        save_results(all_results)

        return run_record

    try:
        run_record = asyncio.run(run_eval())
        return jsonify({"message": "Eval completed.", "result": run_record})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@run_blueprint.route("/results", methods=["GET"])
def get_results():
    """
    Returns all past evaluation results.
    """
    try:
        return jsonify(load_results())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
