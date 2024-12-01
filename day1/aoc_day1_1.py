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

# Sort the lists
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# Calculate the distance between corresponding numbers in the sorted lists 
distances = [abs(sorted_list1[i] - sorted_list2[i]) for i in range(len(sorted_list1))] 

# Calculate the total of all distances 
total_distance = sum(distances)

# Printing the results
#print(f"Sorted list1: {sorted_list1}")
#print(f"Sorted list2: {sorted_list2}")
print(f"Distances between the smallest numbers from both lists: {total_distance}")
