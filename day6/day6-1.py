def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def find_start_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                return r, c
    return None, None

def count_steps_and_unique_fields(grid):
    rows, cols = len(grid), len(grid[0])
    unique_steps = set()
    directions = ['up', 'right', 'down', 'left']
    current_direction = 0
    r, c = find_start_position(grid)

    if r is None or c is None:
        return -1, -1  # No starting position found

    direction_vectors = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }

    while 0 <= r < rows and 0 <= c < cols:
        dr, dc = direction_vectors[directions[current_direction]]
        steps = 0
        while 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] != '#':
            r += dr
            c += dc
            unique_steps.add((r, c))
            steps += 1
        
        # Print steps until facing #
        print(f"Steps until facing '#': {steps}")

        # Turn right before the #
        current_direction = (current_direction + 1) % 4
        dr, dc = direction_vectors[directions[current_direction]]

        # Continue until facing the next #
        unique_segment_steps = set()
        steps = 0
        while 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] != '#':
            r += dr
            c += dc
            unique_segment_steps.add((r, c))
            steps += 1
        
        # Print unique steps after turning right
        print(f"Steps after turning right: {steps}")
        print(f"Unique steps after turning right: {len(unique_segment_steps)}")

        # Add unique steps from this segment to the total
        unique_steps.update(unique_segment_steps)

        # Check for leaving the map
        if not (0 <= r + dr < rows and 0 <= c + dc < cols):
            break

    return len(unique_steps)

# Define the path to the input file
input_file = 'input/day6.txt'

# Read and process the input file
grid = read_input(input_file)
total_unique_fields = count_steps_and_unique_fields(grid)

# Print the total number of unique fields (steps) taken
print(f"Total number of unique fields (steps) taken: {total_unique_fields}")
