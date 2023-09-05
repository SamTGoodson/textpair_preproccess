import argparse
import lz4.frame
import csv
import json

def jsonl_lz4_to_csv(input_file, output_file):
    with open(input_file, 'rb') as lz4_file:
        compressed_data = lz4_file.read()

    decompressed_data = lz4.frame.decompress(compressed_data)
    decompressed_text = decompressed_data.decode('utf-8')
    lines = decompressed_text.strip().split('\n')

    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)

        first_json_object = json.loads(lines[0])
        header = first_json_object.keys()
        csv_writer.writerow(header)
        
        for line in lines:
            json_object = json.loads(line)
            csv_writer.writerow(json_object.values())

    print(f"CSV file '{output_file}' has been created successfully.")

def main():
    parser = argparse.ArgumentParser(description='Convert textpair results to CSV')
    parser.add_argument('input_file', help='Input results file path')
    parser.add_argument('output_file', help='Output CSV file path')

    args = parser.parse_args()
    jsonl_lz4_to_csv(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
