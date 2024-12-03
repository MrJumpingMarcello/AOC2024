import re

def process_line(line, enabled):
    # Regex pattern to match 'do()', 'don't()', and 'mul(x,y)' where x and y are digits
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    mul_pattern = r"mul\((\d+),(\d+)\)"
    
    # Initialize sum for this line
    line_sum = 0
    
    # Find all 'do()', 'don't()', and 'mul(x,y)' matches in the line
    tokens = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", line)
    
    for token in tokens:
        if re.match(do_pattern, token):
            enabled = True
        elif re.match(dont_pattern, token):
            enabled = False
        else:
            if enabled:
                match = re.match(mul_pattern, token)
                if match:
                    x, y = int(match.group(1)), int(match.group(2))
                    line_sum += x * y
    return line_sum, enabled

# Define the input file path
input_file = 'input/day3.txt'

# Initialize the total sum
total_sum = 0

# Initially, calculation is enabled
enabled = True

# Read and process the input file
with open(input_file, 'r') as file:
    for line in file:
        line_sum, enabled = process_line(line, enabled)
        total_sum += line_sum

# Print the total sum of all valid occurrences
print(f"Total sum of all valid occurrences: {total_sum}")
