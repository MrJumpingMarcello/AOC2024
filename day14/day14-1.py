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

def simulate_robot(p, v, steps=100):
    x, y = p
    vx, vy = v
    
    for _ in range(steps):
        x = (x + vx) % 101  # Wrap around the width of the map
        y = (y + vy) % 103  # Wrap around the height of the map
    
    # After 100 steps, return the quadrant of the final position
    return get_quadrant(x, y)

def main():
    # Initialize quadrant counts
    quadrant_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    
    # Read input file
    with open('input/day14.txt', 'r') as file:
        lines = file.readlines()
    
    # Process each robot
    for line in lines:
        p, v = parse_robot_line(line.strip())
        
        # Simulate movement and get quadrant
        quadrant = simulate_robot(p, v, steps=100)
        
        # Update the count for the appropriate quadrant
        if quadrant:
            quadrant_counts[quadrant] += 1
    
    # Calculate the product of robot counts in all quadrants
    product = 1
    for quadrant in range(1, 5):
        product *= quadrant_counts[quadrant]
    
    # Print the results
    print(f"Product of robots in all quadrants: {product}")
    for quadrant in range(1, 5):
        print(f"Quadrant {quadrant}: {quadrant_counts[quadrant]} robots")

if __name__ == "__main__":
    main()
