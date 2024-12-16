from collections import deque

# Direction mappings: N, E, S, W
DIRECTIONS = {
    'N': (-1, 0),  # Up
    'E': (0, 1),   # Right
    'S': (1, 0),   # Down
    'W': (0, -1)   # Left
}

# Possible 90-degree rotations
ROTATIONS = {
    'N': ['E', 'S', 'W'],
    'E': ['S', 'W', 'N'],
    'S': ['W', 'N', 'E'],
    'W': ['N', 'E', 'S']
}

def parse_map(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def find_start_and_end(maze):
    start = None
    end = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                start = (y, x)
            elif maze[y][x] == 'E':
                end = (y, x)
    return start, end

def find_all_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    # Queue of states: (y, x, direction, cost, steps, turns, path)
    queue = deque()
    all_paths = []  # To store all paths and their costs, steps, and turns
    visited = set()  # (y, x, direction) to prevent revisiting the same state
    
    # Start BFS from 'S' in all four directions
    for direction in ['N', 'E', 'S', 'W']:
        queue.append((start[0], start[1], direction, 0, 0, 0, [(start[0], start[1])]))  # (y, x, direction, cost, steps, turns, path)
        visited.add((start[0], start[1], direction))
    
    while queue:
        y, x, direction, cost, steps, turns, path = queue.popleft()
        
        # If we reached the end, save the path details
        if (y, x) == end:
            all_paths.append((cost, steps, turns, path))
        
        # Try moving in all four directions
        for new_direction in ['N', 'E', 'S', 'W']:
            dy, dx = DIRECTIONS[new_direction]
            new_y, new_x = y + dy, x + dx
            
            # Check if the move is within bounds and not a wall
            if 0 <= new_y < rows and 0 <= new_x < cols and maze[new_y][new_x] != '#':
                # If direction changes, add 1000 to cost and increment turns
                new_cost = cost + 1  # Move cost
                new_steps = steps + 1  # One more step taken
                new_turns = turns + (1 if new_direction != direction else 0)  # Rotation cost
                new_path = path + [(new_y, new_x)]  # Add the new position to the path
                
                # Add to queue if not visited in the same direction
                if (new_y, new_x, new_direction) not in visited:
                    visited.add((new_y, new_x, new_direction))
                    queue.append((new_y, new_x, new_direction, new_cost, new_steps, new_turns, new_path))
    
    return all_paths

def create_projection(maze, path):
    # Create a copy of the maze to mark the path
    projection = [row[:] for row in maze]
    
    # Mark each step on the path with 'X'
    for (y, x) in path:
        if projection[y][x] not in ['S', 'E']:  # Don't overwrite the start and end
            projection[y][x] = 'X'
    
    return projection

def save_projection(projection, filename):
    with open(filename, 'w') as file:
        for row in projection:
            file.write(''.join(row) + '\n')

def main():
    # Step 1: Parse the input maze
    maze = parse_map('input/day16.txt')
    
    # Step 2: Find start and end positions
    start, end = find_start_and_end(maze)
    
    # Step 3: Run BFS to find all paths from 'S' to 'E' and their costs
    all_paths = find_all_paths(maze, start, end)
    
    # Step 4: Output the result
    if not all_paths:
        print("No path found.")
    else:
        print(f"Found {len(all_paths)} paths.")
        
        # For each path, create and save a projection
        for index, (_, _, _, path) in enumerate(all_paths):
            print(f"Creating projection for path {index + 1}")
            projection = create_projection(maze, path)
            save_projection(projection, f'input/day16-path-{index + 1}.txt')

if __name__ == "__main__":
    main()
