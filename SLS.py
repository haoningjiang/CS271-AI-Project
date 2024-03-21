import random
import time 


class Graph:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            size = int(file.readline().strip())
            matrix = []
            for line in file:
                row = list(map(float, line.strip().split()))
                matrix.append(row)
        self.size = size
        self.matrix = matrix


def calculate_cost(path, graph):
    return sum(graph.matrix[path[i - 1]][path[i]] for i in range(len(path)))


def get_neighbors(path):
    neighbors = []
    for i in range(len(path)-1):
        for j in range(i + 1, len(path)-1):
            neighbor = path[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            if i==0: 
                neighbor[-1] = neighbor[0]

            neighbors.append(neighbor)
    return neighbors


def stochastic_local_search(graph, max_iter, starting_city):
    current_path = [i for i in range(graph.size) if i!=starting_city]
    #current_path = list(range(graph.size))
    random.shuffle(current_path)

    current_path = [starting_city] + current_path + [starting_city]

    current_cost = calculate_cost(current_path, graph)
    best_path = current_path[:]
    best_cost = current_cost

    for _ in range(max_iter):
        
        neighbors = get_neighbors(current_path)

        new_path = random.choice(neighbors)
        new_cost = calculate_cost(new_path, graph)

        if new_cost < current_cost:
            current_path, current_cost = new_path, new_cost

            if new_cost < best_cost:
                best_path, best_cost = new_path, new_cost

    return best_path, best_cost




def stochastic_local_search_new(graph, max_iter, mytime):
    current_path = [i for i in range(graph.size)]
    random.shuffle(current_path)

    current_path = current_path + [current_path[0]]

    current_cost = calculate_cost(current_path, graph)

    for i in range(max_iter):

        if time.time()-mytime>=600: 
            return current_path, current_cost
        
        neighbors = get_neighbors(current_path)

        local_min = True 

        for neighbor in neighbors: 
            new_cost = calculate_cost(neighbor, graph)
            if new_cost <= current_cost: 
                local_min = False 
                current_path, current_cost = neighbor, new_cost 

        if local_min: 
            break 
    
    return current_path, current_cost






# import matplotlib.pyplot as plt 
# import numpy as np 

# real_best_path = [1, 4, 5, 7, 3, 9, 2, 6, 0, 8, 1]
# real_best_cost_rounded = round(1.7499257704549598, 4)
# real_best_cost = 1.7499257704549598

# old_count = 0 
# new_count = 0 

# filename = 'problems/tsp-problem-10-10-1-1-1.txt'
# g = Graph(filename)
# max_iterations = 20000
# starting_city = 1 

# for i in range(10): 


#     old_se = []
#     new_se = []

#     old_costs = []
#     new_costs = []

#     for _ in range(100): 

#         best_path, best_cost = stochastic_local_search(g, max_iterations, starting_city)
#         best_path_new, best_cost_new = stochastic_local_search_new(g, max_iterations, starting_city)

#         if round(best_cost, 4)==real_best_cost_rounded: 
#             old_count+=1 
        
#         if round(best_cost_new, 4)==real_best_cost_rounded: 
#             new_count+=1 
        
#         old_se.append((real_best_cost-best_cost)**2)
#         new_se.append((real_best_cost-best_cost_new)**2)

#         old_costs.append(best_cost)
#         new_costs.append(best_cost_new)


#         #print(f"Best path: {best_path}")
#         #print(f"Best cost: {best_cost}")
#         #print('.')


#     #plt.hist(results_new)
#     #plt.xlabel('path cost found')

#     #plt.show()
            
#     print(f"old count={old_count}")
#     print(f"new count={new_count}")

#     print(f"old mse={np.average(old_se)}")
#     print(f"new mse={np.average(new_se)}")

#     print(f'old avg cost={np.average(old_costs)}')
#     print(f'new avg cost={np.average(new_costs)}')
#     print('.')
