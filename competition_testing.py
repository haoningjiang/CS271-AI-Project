from astar_v2 import a_star_tsp
from astar_v2 import calculate_mst_cost
from astar_v2 import Graph as Astar_Graph

from SLS import stochastic_local_search_new
from SLS import Graph as SLS_Graph 

import time 
import csv 

# import required module
import os
# assign directory
directory = 'Competion'
 
notproblems = set(['Competion/genTSP.py', 'Competion/TSP-competition-notes.txt'])

filenames = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if f not in notproblems: 
            filenames.append(f)


filenames.sort()
print(filenames)
#filenames = filenames[:3]


with open('competition_result.csv', mode='w') as competition_file:
    filewriter = csv.writer(competition_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    for f in filenames: 
        g_star = Astar_Graph(f)
        mytime = time.time()
        path, cost, timeout = a_star_tsp(g_star, mytime)
        endtime = time.time()

        if timeout: 
            timeres = "TIMEOUT"
        else: 
            timeres = str(endtime-mytime)
        
        filewriter.writerow([f, path, cost, timeres])
        print(f, timeres)

print('.')
print('done')


#filename = filenames[i]
#g_star = Astar_Graph(filename)
#true_path, true_cost = a_star_tsp(g_star, starting_city)
