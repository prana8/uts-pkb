object_names = ['cabbage', 'farmer', 'goat', 'wolf']


def is_valid_state(state):
    farmer, goat, wolf, cabbage = state
    # Check if the goat and cabbage are left alone on one side of the river
    if goat == cabbage and farmer != goat:
        return False
    # Check if the goat and wolf are left alone on one side of the river
    if goat == wolf and farmer != goat:
        return False
    return True


def is_goal_state(state):
    # All objects have crossed to the other side
    return state == (1, 1, 1, 1)


def generate_next_states(state):
    next_states = []
    farmer, goat, wolf, cabbage = state

    # Farmer crosses alone
    next_states.append((1 - cabbage, 1 - farmer, 1 - goat, 1 - wolf))

    # Farmer crosses with the goat
    if farmer == goat:
        next_states.append((1 - cabbage, 1 - farmer, 1 - wolf, goat))

    # Farmer crosses with the wolf
    if farmer == wolf:
        next_states.append((1 - cabbage, 1 - farmer, goat, 1 - wolf))

    # Farmer crosses with the cabbage
    if farmer == cabbage:
        next_states.append((farmer, 1 - goat, 1 - wolf, 1 - cabbage))

    return next_states


def solve(state, path):
    if not is_valid_state(state):
        return False

    if is_goal_state(state):
        return True

    for next_state in generate_next_states(state):
        if next_state not in path:
            path.append(next_state)
            if solve(next_state, path):
                return True
            path.pop()

    return False


# Find the solution
# Initially, all objects are on the starting side of the river
initial_state = (0, 0, 0, 0)
path = [(initial_state, ())]
solve(initial_state, path)

# Display the solution
for state, transported in path:
    left_side = [object_names[i] for i in range(4) if state[i] == 0]
    right_side = [object_names[i] for i in range(4) if state[i] == 1]
    print("{{{" + ", ".join(left_side) + "}, {" + ", ".join(right_side) + "}}},")


# # Display the solution
# for state in path:
#     left_side = [str(item) for item in state if item == 0]
#     right_side = [str(item) for item in state if item == 1]
#     print("{{{" + ", ".join(left_side) + "}, {" + ", ".join(right_side) + "}}},")
