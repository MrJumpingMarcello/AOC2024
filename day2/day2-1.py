def check_increasing_or_decreasing(nums):
    if len(nums) < 2:
        return True

    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    increasing = all(1 <= diff <= 3 for diff in diffs)
    decreasing = all(-3 <= diff <= -1 for diff in diffs)
    
    return increasing or decreasing

# Define the input file path
input_file = 'input/day2.txt'

# Initialize the counter for lines that meet the criteria
true_count = 0

# Read and process the input file
with open(input_file, 'r') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        result = check_increasing_or_decreasing(numbers)
        if result:
            true_count += 1
        print(result)

# Print the total number of "true" lines
print(f"Total number of true lines: {true_count}")
