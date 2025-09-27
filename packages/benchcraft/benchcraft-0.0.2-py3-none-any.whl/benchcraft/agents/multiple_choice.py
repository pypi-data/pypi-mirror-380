import os
import json
import asyncio
import re
import time
import argparse
from openai import AsyncOpenAI, APIError
from collections import defaultdict
from tqdm.asyncio import tqdm_asyncio
from typing import List, Dict, Any

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


def load_benchmark_data(file_path: str) -> Dict[str, Any]:
    """Loads and validates the benchmark data from the specified JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Basic validation for required top-level keys
        for key in ["name", "systemPrompt", "samples"]:
            if key not in data:
                raise KeyError(f"Benchmark file is missing required key: '{key}'")
        return data
    except FileNotFoundError:
        print(f"Error: Benchmark file not found at '{file_path}'")
        exit(1)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error processing benchmark file: {e}")
        exit(1)


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


def print_report(
    metrics: Dict[str, Any], model_name: str, duration: float, benchmark_name: str
):
    """Prints a formatted report of the evaluation metrics."""
    header = f" {benchmark_name} Report "
    print(f"\n{header:=^60}")
    print(f"{'Model Tested:':<20} {model_name}")
    print(f"{'Total Time:':<20} {duration:.2f} seconds")
    print("-" * 60)
    print(
        f"{'Overall Accuracy:':<20} {metrics['overall_accuracy']:.2f}% ({metrics['total_correct']}/{metrics['total_questions']})"
    )
    print("-" * 60)
    print("Accuracy by Topic:")
    sorted_topics = sorted(metrics["topic_accuracy"].items())
    for topic, acc in sorted_topics:
        print(f"  - {topic.ljust(20)}: {acc:.2f}%")
    print("=" * 60)


async def main(args: argparse.Namespace):
    """Main function to orchestrate the benchmark evaluation."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set.")

    client = AsyncOpenAI(base_url=OPENROUTER_BASE_URL, api_key=api_key)

    benchmark_data = load_benchmark_data(args.file)
    benchmark_name = benchmark_data.get("name", "Generic Benchmark")

    print(f"Starting {benchmark_name} for model: {args.model}")

    tasks = [
        evaluate_sample(client, sample, benchmark_data["systemPrompt"], args.model)
        for sample in benchmark_data["samples"]
    ]

    start_time = time.time()
    results = await tqdm_asyncio.gather(*tasks, desc="Evaluating Samples")
    duration = time.time() - start_time

    metrics = calculate_metrics(results)
    print_report(metrics, args.model, duration, benchmark_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run a generic, multiple-choice benchmark on a specified model."
    )
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="mistralai/mistral-7b-instruct:free",
        help="The model identifier from OpenRouter to be evaluated.",
    )
    parser.add_argument(
        "-f", "--file", type=str, required=True, help="Path to the benchmark JSON file."
    )

    parsed_args = parser.parse_args()
    asyncio.run(main(parsed_args))
