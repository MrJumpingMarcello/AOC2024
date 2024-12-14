def parse_robot_line(line):
    # Example line format: p=10,20 v=2,3
    parts = line.split()
    p = tuple(map(int, parts[0].split('=')[1].split(',')))
    v = tuple(map(int, parts[1].split('=')[1].split(',')))
    return p, v

def get_quadrant(x, y):
    # Map dimensions and middle lines
    center_x = 50
    center_y = 51
    
    if x > center_x and y < center_y:
        return 1  # top-right
    elif x > center_x and y > center_y:
        return 2  # bottom-right
    elif x < center_x and y < center_y:
        return 3  # top-left
    elif x < center_x and y > center_y:
        return 4  # bottom-left
    return None

def christmas_tree_pattern():
    # Define the pattern for the Christmas tree in coordinates (relative to the center)
    tree_coords = set()
    base_x = 50
    base_y = 51

    # Tree shape (like a triangle) with 7 levels and 9 base width
    for i in range(7):  # 7 levels (height)
        for j in range(-i, i+1):  # the width at each level
            tree_coords.add((base_x + j, base_y - i))
    
    return tree_coords

def simulate_robot(p, v, steps=100):
    x, y = p
    vx, vy = v
    
    # Simulate for each second
    positions = []
    for _ in range(steps):
        x = (x + vx) % 101  # Wrap around the width of the map
        y = (y + vy) % 103  # Wrap around the height of the map
        positions.append((x, y))
    
    return positions

def main():
    # Initialize tree pattern coordinates
    tree_coords = christmas_tree_pattern()
    
    # Initialize robots' initial positions and velocities
    robots = []
    with open('input/day14.txt', 'r') as file:
        lines = file.readlines()
    
    # Parse all robots
    for line in lines:
        p, v = parse_robot_line(line.strip())
        robots.append((p, v))
    
    # Try to find the number of seconds it takes for all robots to align to the tree pattern
    max_steps = 1000  # Maximum number of steps to simulate
    for t in range(max_steps):
        # Get all robot positions at time t
        all_positions = set()
        for p, v in robots:
            positions = simulate_robot(p, v, t+1)
            all_positions.add(positions[-1])
        
        # Check if the robots are aligned with the tree pattern
        if all_positions == tree_coords:
            print(f"All robots align in {t + 1} seconds!")
            break
    else:
        print("Could not align all robots within the given number of steps.")

if __name__ == "__main__":
    main()
