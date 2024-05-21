import argparse
from pathlib import Path
import structlog

log = structlog.get_logger()

def merge_jsonl_files(directory_path, output_file):
    directory_path = Path(directory_path)
    with open(output_file, 'w') as outfile:
        for jsonl_file in directory_path.glob('*.jsonl'):
            with open(jsonl_file, 'r') as infile:
                for line in infile:
                    outfile.write(line)
    log.info("Merged JSONL files", output_file=str(output_file))

def main():
    parser = argparse.ArgumentParser(description='Merge JSONL files from a directory into a single file.')
    parser.add_argument('directory_path', type=str, help='Directory containing JSONL files to merge')
    parser.add_argument('output_file', type=str, help='Output file path for the merged JSONL file')

    args = parser.parse_args()
    merge_jsonl_files(args.directory_path, args.output_file)

if __name__ == '__main__':
    main()
