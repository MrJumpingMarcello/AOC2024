# Define the input file path
input_file = 'input/day1.txt'

# Initialize lists
list1 = []
list2 = []

# Read the input file
with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split()
        if len(numbers) >= 2:
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

# Function to count occurrences of each item in list2
def count_occurrences(list_to_count):
    occurrences = {}
    for item in list_to_count:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

# Count occurrences of each item in list2
occurrences_list2 = count_occurrences(list2)

# Calculate the sum of multiplications
total_sum = 0
for num in list1:
    if num in occurrences_list2:
        total_sum += num * occurrences_list2[num]

print(f"Sum of all calculations: {total_sum}")
