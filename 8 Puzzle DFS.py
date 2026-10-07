#Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

#Function to print the puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

#Generate possible moves
# Order: Up -> Down -> Left -> Right
def get_neighbours(state):
    neighbours = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]       #up, down, left, right

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3 :
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]

            neighbours.append(tuple(new_state))

    return neighbours

#DFS Algorithm

def dfs(start):
    stack = [(start, [ ])]   # simple stack
    visited = {start}

    while stack:
        state, path = stack.pop()  # Remove first item

        if state == goal :
            return path + [state]

        neighbours = get_neighbours(state)
        
        #Reverse push so DFS explores:
        #Up -> Down -> Left -> Right
        for neighbour in reversed(neighbours) :
            if neighbour not in visited :
                visited.add(neighbour)
                stack.append((neighbour, path + [state]))

    return None

#Example start state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

#Solve puzzle
solution = dfs(start)

if solution :
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print_board(step)

else:
    print("No Solution Found.")
    
            
        

