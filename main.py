import csv
from dataset import get_dataset
from model import mock_model
from metrics import calculate_asr
from utils import log

OUTPUT_FILE = "results.csv"

def run_benchmark():
    data = get_dataset()
    results = []

    log("Starting benchmark...")

    for item in data:
        response = mock_model(item["prompt"])
        success = item["expected"] in response

        results.append([item["prompt"], response, success])

    save_results(results)

    asr = calculate_asr([r[2] for r in results])
    log(f"Attack Success Rate: {asr}")

def save_results(results):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Prompt", "Response", "Attack Success"])
        writer.writerows(results)

if __name__ == "__main__":
    run_benchmark()