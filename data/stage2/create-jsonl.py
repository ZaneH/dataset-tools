import csv
import json
import structlog
from pathlib import Path
import argparse

INJECT_SYSTEM_PROMPT = """
This would be your system prompt. Something that applies to all
tasks performed by your model.
""".strip()

USER_INPUT = """
Sometimes I'll keep the same USER_INPUT for a bunch
of examples, othertimes I need to update it per example. It depends.
""".strip()

log = structlog.get_logger()

def process_csv_file(input_file_path, output_dir, file_name):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file_path = output_dir / file_name

    with open(input_file_path, newline='') as csvfile, open(output_file_path, 'w') as jsonlfile:
        reader = csv.DictReader(csvfile, fieldnames=['text'])
        next(reader)  # Skip header if present
        json_lines = []

        for row in reader:
            text = row["text"]

            json_obj = {
                "conversations": [
                    {"from": "system", "value": INJECT_SYSTEM_PROMPT},
                    {"from": "user", "value": USER_INPUT},
                    {"from": "gpt", "value": text}
                ]
            }
            json_lines.append(json_obj)
            jsonlfile.write(json.dumps(json_obj) + '\n')

    log.info("CSV processing complete", output_file=str(output_file_path))

def main():
    parser = argparse.ArgumentParser(description='Process CSV to JSONL.')
    parser.add_argument('input_file', type=str, help='Input CSV file path')
    parser.add_argument('output_dir', type=str, help='Output directory for JSONL file')
    parser.add_argument('output_file', type=str, help='Output file name')

    args = parser.parse_args()
    process_csv_file(args.input_file, args.output_dir, args.output_file)

if __name__ == '__main__':
    main()