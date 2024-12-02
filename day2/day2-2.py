def check_increasing_or_decreasing(nums):
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    increasing = all(1 <= diff <= 3 for diff in diffs)
    decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return increasing or decreasing

def check_with_removal(nums):
    for i in range(len(nums)):
        modified_nums = nums[:i] + nums[i + 1:]
        if check_increasing_or_decreasing(modified_nums):
            return True
    return False

# Define the input file path
input_file = 'input/day2.txt'

# Initialize the counter for lines that meet the criteria
true_count = 0

# Read and process the input file
with open(input_file, 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if check_increasing_or_decreasing(numbers):
            true_count += 1
            print(True)
        elif check_with_removal(numbers):
            true_count += 1
            print(True)
        else:
            print(False)

# Print the total number of "true" lines
print(f"Total number of true lines: {true_count}")
