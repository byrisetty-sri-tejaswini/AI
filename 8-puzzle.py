arrlist = []

def count_inversions(board):
    inversions = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] > board[j] and board[i] != 0 and board[j] != 0:
                inversions += 1
    return inversions

def is_solvable(initial, goal):
    initial_inversions = count_inversions(initial)
    goal_inversions = count_inversions(goal)
    return (initial_inversions % 2 == goal_inversions % 2)

def move(board, goal, v):
    a = board.index(0)
    moves = {}
    if (a - 3 > -1):
        l1= board[:]
        temp = l1[a - 3]
        l1[a - 3] = 0
        l1[a] = temp
        if l1 not in arrlist:
            moves["top"] = l1
            arrlist.append(l1)
    if a not in [2, 5, 8]:
        l4 = board[:]
        temp = l4[a + 1]
        l4[a + 1] = 0
        l4[a] = temp
        if l4 not in arrlist:
            moves["right"] = l4
            arrlist.append(l4)
            

    if (a + 3 < 9):
        l2 = board[:]
        temp = l2[a + 3]
        l2[a + 3] = 0
        l2[a] = temp
        if l2 not in arrlist:
            moves["bottom"] = l2
            arrlist.append(l2)

        l3 = board[:]
        temp = l3[a - 1]
        l3[a - 1] = 0
        l3[a] = temp
        if l3 not in arrlist:
            moves["left"] = l3
            arrlist.append(l3)

    solve(moves, goal, v)

def solve(moves, goal, v):
    c = []
    value = list(moves.values())
    side = list(moves.keys())
    for i in value:
        if i != goal:
            count = v
            for j in range(9):
                if i[j] != goal[j]:
                    count += 1
            c.append(count - 1)
        else:
            print(side[value.index(i)], "==>g(x)=", v, "+h(x)=0")
            for k in range(0, 9, 3):
                print(i[k], i[k + 1], i[k + 2], sep=" ", end="\n")
            print("Goal state found")
            print("No. of states", v)
            return 
    print(side[c.index(min(c))], "==>g(x)=", v, "+h(x)", min(c) - v)
    for i in range(0, 9, 3):
        print(value[c.index(min(c))][i], value[c.index(min(c))][i + 1], value[c.index(min(c))][i + 2], sep=" ", end="\n")
    v += 1
    move(value[c.index(min(c))], goal, v)

def input_state(prompt):
    state = []
    i = 0
    while i < 3:
        try:
            row = input(prompt).split(' ')
            if len(row) != 3:
                raise ValueError("Invalid input. Please enter 3 values separated by spaces.")
            state.append([int(val) for val in row])
            i += 1
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
    return [val for sublist in state for val in sublist]

print("Initial state:")
initial = input_state("Enter 3 values for each row, separated by spaces: ")

print("Goal state:")
goal = input_state("Enter 3 values for each row, separated by spaces: ")

if not is_solvable(initial, goal):
    print("No solution exists for this puzzle configuration.")
else:
    move(initial, goal, 1)
