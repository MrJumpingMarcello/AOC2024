import re

def extract_and_multiply(line):
    # Regex pattern to match 'mul(x,y)' where x and y are digits
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches in the line
    matches = re.findall(pattern, line)
    
    # Calculate the product of the numbers in each match
    results = [int(match[0]) * int(match[1]) for match in matches]
    
    return results

# Define the input file path
input_file = 'input/day3.txt'

# Initialize the total sum
total_sum = 0

# Read and process the input file
with open(input_file, 'r') as file:
    for line in file:
        products = extract_and_multiply(line)
        total_sum += sum(products)

# Print the total sum of all occurrences
print(f"Total sum of all occurrences: {total_sum}")
