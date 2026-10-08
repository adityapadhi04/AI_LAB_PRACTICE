from collections import deque  # 1. Fixed module name

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()

    # Queue stores: (jug1_water, jug2_water, path_history)
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()  # 2. Kept consistent names (jug1, jug2)

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        current_path = path + [(jug1, jug2)]

        # Check if target state is reached
        if (jug1, jug2) == target_state:  # 3. Fixed spelling typo
            return current_path

        # Generate all possible next moves
        next_moves = [
            (cap1, jug2),  # Fill Jug 1
            (jug1, cap2),  # Fill Jug 2
            (0, jug2),     # Empty Jug 1
            (jug1, 0),     # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (jug1 - min(jug1, cap2 - jug2), jug2 + min(jug1, cap2 - jug2)),
            # Pour Jug 2 -> Jug 1
            (jug1 + min(jug2, cap1 - jug1), jug2 - min(jug2, cap1 - jug1))
        ]

        for move in next_moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))

    return None  # 4. Fixed block indentation

# Solve for jug1 capacity = 4L, jug2 capacity = 3L, Goal state = (4,2)
target_goal = (4, 2)
solution = water_jug(4, 3, target_goal)

if solution:
    print("Solution found:")
    for state in solution:
        print(f"Step: {state}")  # 5. Fixed print syntax error
else:
    print("No solution exists.")
