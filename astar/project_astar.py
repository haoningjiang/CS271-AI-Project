import heapq 
import argparse
import sys 
import itertools as it
import gc 




#starting_city = 0



# Class to represent a graph 
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
  
    # Function to add an edge to graph 
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w]) 
  
    # A utility function to find set of an element i 
    # (truly uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 
  
            parent[i] = self.find(parent, parent[i]) 
        return parent[i] 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
  
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
  
        else: 
            parent[y] = x 
            rank[x] += 1
  
    # The main function to construct MST using Kruskal's algorithm 
    def KruskalMST(self): 
  
        result = [] 
  
        i = 0
  
        e = 0
  
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
  
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
  
        while e < self.V - 1: 
  
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
  
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 
  
        minimumCost = 0
        for u, v, weight in result: 
            minimumCost += weight 
        
        return minimumCost






class Node: 
    def __init__(self, visited_ordered, g, h, depth): 
        self.visited_ordered = visited_ordered
        self.g = g
        self.h = h 
        self.depth = depth

        self.unvisited = all_cities.difference(set(self.visited_ordered))

    def __lt__(self, other): #for < 
        return self.g+self.h < other.g+other.h

    def __le__(self, other): #for <=
        return self.g+self.h<=other.g+other.h


    

    def getChildren(self): 
        children = []

        #if set(self.visited_ordered)==all_cities: 
        if len(self.unvisited)==0: 
            child = Node(
                visited_ordered=self.visited_ordered+[starting_city], 
                g=self.g + distance[min(self.visited_ordered[-1], starting_city), max(self.visited_ordered[-1], starting_city)], 
                h=0, 
                depth=self.depth+1
            )
            children.append(child)
        else: 
            for city in self.unvisited: 
                #child = Node()

                child_visited_ordered = self.visited_ordered + [city]
                child_depth = self.depth+1 

                child_g = self.g + distance[min(self.visited_ordered[-1], city), max(self.visited_ordered[-1], city)]

                #calculate h: 
                #mst = (mst of unvisited cities) 

                collection = list(self.unvisited.difference(set([city]))) 

                graph = Graph(len(collection))

                #result = it.combinations(collection, 2)
                #for u,v in result: 
                #    g.addEdge(u,v,distance[(u,v)])

                for i in range(len(collection)): 
                    for j in range(i+1, len(collection)): 
                        key = (min(collection[i], collection[j]), max(collection[i], collection[j]))
                        graph.addEdge(i,j,distance[key])
                
                mincost = graph.KruskalMST()


                #to_nearest_unvisited = (distance from city to nearest unvisited city) 
                #closest_to_start = (min distance from an unvisited city to the starting city) 
                to_nearest_unvisited = sys.maxsize
                closest_to_start = sys.maxsize

                for c in self.unvisited: 
                    if c!=city: 
                        key1 = (min(c, city), max(c, city))
                        to_nearest_unvisited = min(to_nearest_unvisited, distance[key1])

                        key2 = (min(c, starting_city), max(c, starting_city))
                        closest_to_start = min(closest_to_start, distance[key2])
                
                child_h = to_nearest_unvisited + mincost + closest_to_start 
                
                child = Node(
                    visited_ordered=child_visited_ordered, 
                    g=child_g, 
                    h=child_h, 
                    depth=child_depth
                )
                
                children.append(child) 

                del graph 
                del collection 
                gc.collect()
        
        return children 

    def isGoal(self): 
	    return self.depth==n+1 and self.visited_ordered[0]==self.visited_ordered[-1]



def a_star(starting_city): 

    
    frontier = []#(minimum priority queue on g(x)+h(x)) 
    heapq.heapify(frontier)

    #create starting node 
    #mst = (mst on all cities in all_cities) 
    graph = Graph(len(all_cities))
    for i in range(n): 
        for j in range(i+1, n): 
            graph.addEdge(i, j, distance[(i,j)])
    mincost = graph.KruskalMST()

    #to_nearest_unvisited = (distance from starting_city to any other city) 
    to_nearest_unvisited = sys.maxsize
    for i in range(n): 
        if i!=starting_city: 
            key = (min(i, starting_city), max(i, starting_city))
            to_nearest_unvisited = min(to_nearest_unvisited, distance[key])

    #closest_to_start = (min distance from any other city to starting_city) 
    closest_to_start = to_nearest_unvisited

    starting_node = Node(
        visited_ordered = [starting_city],
        g = 0, 
        h = to_nearest_unvisited + mincost + closest_to_start, 
        depth = 1) 
    
    del graph 
    gc.collect()

    heapq.heappush(frontier, (starting_node.g+starting_node.h, starting_node))
    #frontier.push((starting_node, starting_node.g+starting_node.h)) 

    #print('starting node h = ' + str(starting_node.h))



    while True: 
        if frontier==[]: return -1 

        #node = frontier.pop() #pops node with smallest g(x)+h(x) 
        gh, node = heapq.heappop(frontier)

        if node.isGoal(): return node 

        children = node.getChildren()

        for child in children: 
            #print('path=' + str(child.visited_ordered) + ' unvisited=' + str(child.unvisited) + ' g='+str(child.g) + ' h='+str(child.h))

            heapq.heappush(frontier, (child.h+child.g, child))
    









parser = argparse.ArgumentParser(description="Run A* Search")
parser.add_argument("-f", "--f", help="F: filename", required=True, type=str)
args = parser.parse_args()

f = args.f

file = open(f, 'r')
n = int(file.readline()) 
all_cities = set([x for x in range(n)])

distance = {}

for i in range(n): 
    dists = file.readline().split()

    for j in range(i+1, n): 
        distance[(i,j)] = float(dists[j]) 

print(distance)

#starting_city = 0

bestg = sys.maxsize
best = None  

for i in range(n): 
    starting_city = i 

    result = a_star(starting_city)
    if result.g < bestg: 
        best = result 
        bestg = result.g 

print(best.visited_ordered)
print(best.g)