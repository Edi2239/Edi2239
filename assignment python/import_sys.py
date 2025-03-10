import sys
import csv

def process_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            reader = csv.reader(infile)
            outfile.write("Sum, Average\n")  # Writing header

            for row in reader:
                try:
                    numbers = list(map(int, row))  # Convert strings to integers
                    total = sum(numbers)
                    average = total / len(numbers)
                    outfile.write(f"{total}, {average:.2f}\n")
                except ValueError:
                    print(f"Skipping invalid row: {row}")

        print(f"Processing complete. Output saved to {output_file}")

    except FileNotFoundError:
        print("Error: Input file not found. Please check the file path.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python process_data.py <input_file> <output_file>")
    else:
        process_data(sys.argv[1], sys.argv[2])