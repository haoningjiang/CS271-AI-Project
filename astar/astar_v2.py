import heapq


class Graph:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            size = int(file.readline().strip())
            matrix = []
            for line in file:
                row = list(map(float, line.strip().split()))
                matrix.append(row)
        self.list = []
        for i in range(size):
            for j in range(size):
                self.list.append(matrix[i][j])
        self.size = size


def calculate_mst_cost(unvisited, graph, origin):
    mst = set()
    if len(unvisited) == 0:
        return 0, 0
    start_vertex = next(iter(unvisited))
    mst.add(start_vertex)

    # Cost, start vertex, next vertex
    edges = [(graph.list[start_vertex * graph.size + v], start_vertex, v)
             for v in unvisited]
    heapq.heapify(edges)

    mst_cost = 0

    while len(mst) < len(unvisited):
        cost, _, next_vertex = heapq.heappop(edges)
        if next_vertex not in mst:
            mst.add(next_vertex)
            mst_cost += cost

            for new_adjacent in unvisited:
                if new_adjacent not in mst:
                    new_cost = graph.list[next_vertex * graph.size + new_adjacent]
                    heapq.heappush(edges, (new_cost, next_vertex, new_adjacent))
    shortest_return = min(graph.list[origin * graph.size + v] for v in unvisited)
    return mst_cost, shortest_return


def a_star_tsp(graph):
    # estimation cost, current cost, path, unvisited
    pq = []
    heapq.heappush(pq, (0, 0, [0], set(range(1, graph.size))))

    best_found = float('inf')
    best_path = []

    while pq:
        # Pop the node (state) with the lowest estimated total cost
        estimation, cost, path, unvisited = heapq.heappop(pq)

        # Check if all cities are visited and path is back to start
        if len(unvisited) == 0 and path[0] == path[-1]:
            if cost < best_found:
                best_found = cost
                best_path = path
            continue

        current_city = path[-1]
        for next_city in range(graph.size):
            if next_city in unvisited or (len(unvisited) == 0 and next_city == path[0]):
                new_path = path + [next_city]
                new_cost = cost + graph.list[current_city * graph.size + next_city]
                new_unvisited = unvisited - {next_city}
                h_cost, shortest_return = calculate_mst_cost(new_unvisited, graph, path[0])
                new_estimation = new_cost + h_cost + shortest_return

                if cost + h_cost >= best_found:
                    continue

                if new_estimation < best_found:
                    heapq.heappush(pq, (new_estimation, new_cost, new_path, new_unvisited))

    return best_path, best_found


import time

start_time = time.time()
filename = 'tsp-problem-20-20-20-2-1.txt'
g = Graph(filename)
result = a_star_tsp(g)
print(result)
print(time.time() - start_time)
