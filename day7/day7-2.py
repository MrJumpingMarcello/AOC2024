from itertools import product

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def evaluate_expression(nums, operators):
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '||':
            result = int(str(result) + str(nums[i + 1]))
        else:
            if operators[i] == '+':
                result += nums[i + 1]
            elif operators[i] == '*':
                result *= nums[i + 1]
    return result

def find_operators(nums, target):
    for operators in product(['+', '*', '||'], repeat=len(nums) - 1):
        if evaluate_expression(nums, operators) == target:
            return True
    return False

def check_equations(file_path):
    lines = read_input(file_path)
    results = []
    total_sum_true = 0

    for line in lines:
        print(f"Evaluating line: {line}")
        target, expr = line.split(':')
        target = int(target.strip())
        nums = list(map(int, expr.split()))

        if find_operators(nums, target):
            results.append(f"{line} -> true")
            total_sum_true += target
        else:
            results.append(f"{line} -> false")

    return results, total_sum_true

def re_evaluate_false_results(results, file_path):
    lines = read_input(file_path)
    additional_sum_true = 0

    for idx, result in enumerate(results):
        if "-> false" in result:
            target, expr = lines[idx].split(':')
            target = int(target.strip())
            nums = list(map(int, expr.split()))

            print(f"Re-evaluating line {idx + 1}: {lines[idx]}")
            if find_operators(nums, target):
                print(f"Line {idx + 1}: Sum: {target}, Values: {nums} -> true (by concatenation ||)")
                additional_sum_true += target
            else:
                print(f"Line {idx + 1}: Sum: {target}, Values: {nums} -> false")

    return additional_sum_true

# Define the path to the input file
input_file = 'input/day7.txt'

# Check the equations and get results
results, total_sum_true_initial = check_equations(input_file)

# Print the results for each equation
for result in results:
    print(result)

# Print only the false results
print("False results:")
false_results = [result for result in results if "-> false" in result]
for result in false_results:
    print(result)

# Re-evaluate false results with concatenation and update total sum of true tests
total_sum_true_concatenation = re_evaluate_false_results(results, input_file)

# Total sum of all true tests
final_total_sum_true = total_sum_true_initial + total_sum_true_concatenation
print(f"Total sum of all true tests including concatenation: {final_total_sum_true}")
