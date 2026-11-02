import csv
import re
from collections import Counter

INPUT_LOG_FILE = "access.log"
OUTPUT_CSV_FILE = "post_request_summary.csv"

LINE_RE = re.compile(
    r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s.*?"(?P<method>[A-Z]+)\s'
)

def analyze_log_file():
    post_counts = Counter()

    try:
        with open(INPUT_LOG_FILE, "r", encoding="utf-8") as log_file:
            for line in log_file:
                match = LINE_RE.search(line)
                if match and match.group("method") == "POST":
                    post_counts[match.group("ip")] += 1
    except FileNotFoundError:
        print("Error: Input log file not found.")
        return None

    with open(OUTPUT_CSV_FILE, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["IP Address", "POST Request Count"])
        writer.writerows(post_counts.items())

    return post_counts


def main():
    post_counts = analyze_log_file()

    if post_counts is not None:
        print("POST Request Summary:")
        for ip_address, count in post_counts.items():
            print(ip_address, ":", count)
        print("CSV report generated successfully.")


if __name__ == "__main__":
    main()
