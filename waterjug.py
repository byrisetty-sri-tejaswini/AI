def water_jug_problem(a, b, target):
    def dfs(current_state, visited, path):
        if current_state[0] == target or current_state[1] == target:
            return True, path
        
        visited.add(current_state)
        
        next_states = []
        
        next_states.append(((a, current_state[1]), (a, current_state[1])))
        
        next_states.append(((current_state[0], b), (current_state[0], b)))
        
        next_states.append(((0, current_state[1]), (0, current_state[1])))
        
        next_states.append(((current_state[0], 0), (current_state[0], 0)))
        
        pour_amount = min(current_state[0], b - current_state[1])
        next_states.append(((current_state[0] - pour_amount, current_state[1] + pour_amount),
                            (current_state[0] - pour_amount, current_state[1] + pour_amount)))
        
        pour_amount = min(current_state[1], a - current_state[0])
        next_states.append(((current_state[0] + pour_amount, current_state[1] - pour_amount),
                            (current_state[0] + pour_amount, current_state[1] - pour_amount)))
        
        for next_state, action in next_states:
            if next_state not in visited:
                success, new_path = dfs(next_state, visited, path + [action])
                if success:
                    return True, new_path
        
        return False, []

    initial_state = (0, 0)
    initial_path = []
    visited = set()
    
    success, steps = dfs(initial_state, visited, initial_path)
    return success, steps

jug_a = int(input("Enter jug A capacity: "))
jug_b = int(input("Enter jug B capacity: "))
goal = int(input("Enter target amount: "))

result, steps = water_jug_problem(jug_a, jug_b, goal)
if result:
    print("Target amount can be measured.")
    print("Steps:")
    for step, state in enumerate(steps):
        print(f" {state}")
else:
    print("Target amount cannot be measured.")