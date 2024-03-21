import heapq
import argparse
import time 

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

    for i in range(graph.size): 

        unvisited = set([j for j in range(0, graph.size) if j!=i]) 

        h_cost, shortest_return = calculate_mst_cost(unvisited, graph, i)

        heapq.heappush(pq, (h_cost+shortest_return, 0, [i], unvisited ))


    while pq:
        # Pop the node (state) with the lowest estimated total cost
        estimation, cost, path, unvisited = heapq.heappop(pq)

        # Check if all cities are visited and path is back to start
        if len(unvisited) == 0 and path[0] == path[-1]:
            return path, cost 
        
        current_city = path[-1]
        for next_city in range(graph.size):


            if next_city in unvisited or (len(unvisited) == 0 and next_city == path[0]):
                new_path = path + [next_city]
                new_cost = cost + graph.list[current_city * graph.size + next_city]
                new_unvisited = unvisited - {next_city}
                h_cost, shortest_return = calculate_mst_cost(new_unvisited, graph, path[0])
                new_estimation = new_cost + h_cost + shortest_return

                
                heapq.heappush(pq, (new_estimation, new_cost, new_path, new_unvisited))


#parser = argparse.ArgumentParser(description="Run A* Search on problem file")
#parser.add_argument("-f", "--f", help="F: file path", required=True, type=str)
#args = parser.parse_args()

#f = args.f

#g = Graph(f)
#path, cost = a_star_tsp(g)

#print(f"path={path}")
#print(f"cost={cost}")


