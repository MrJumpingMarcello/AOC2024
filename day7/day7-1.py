def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def evaluate_expression(nums, operators):
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i + 1]
        elif operators[i] == '*':
            result *= nums[i + 1]
    return result

def find_operators(nums, target):
    from itertools import product
    for operators in product(['+', '*'], repeat=len(nums) - 1):
        if evaluate_expression(nums, operators) == target:
            return True
    return False

def calculate_total_sum(file_path):
    lines = read_input(file_path)
    total_sum = 0

    for line in lines:
        target, expr = line.split(':')
        target = int(target.strip())
        nums = list(map(int, expr.split()))

        if find_operators(nums, target):
            total_sum += target

    return total_sum

# Define the path to the input file
input_file = 'input/day7.txt'

# Calculate the total sum of all true tests
total_sum = calculate_total_sum(input_file)

# Print the total sum
print(f"Total sum of all true tests: {total_sum}")
