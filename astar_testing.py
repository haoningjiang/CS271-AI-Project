from astar_v2 import *

import time
import matplotlib.pyplot as plt 

def testing(x_vals, filenames, xlabel, ylabel, graphtitle): 
        mytimes = []

        for i in range(len(filenames)): 

            start_time = time.time()
            filename = filenames[i]
            g = Graph(filename)
            result = a_star_tsp(g)
            mytime = time.time() - start_time
            mytimes.append(round(mytime, 4)) 
            
            print(result)
            print(mytime)
            print('.')

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(x_vals, mytimes)
        for xy in zip(x_vals, mytimes):                                       
            ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(graphtitle)

        ax.grid()
        plt.show()

def n_test(): 

    n_vals = [3,4,6,8,10, 12, 14, 16, 18, 20]

    n_files = ['problems/tsp-problem-{}-{}-1-1-1.txt'.format(i, i*(i-1)//2) for i in n_vals]

    testing(n_vals, n_files, 'number of cities', 'runtime', 'number of cities (n) vs A* runtime')



def u_test(): 

    #u_vals = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    u_vals = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    u_files = ['problems/tsp-problem-10-45-{}-1-1.txt'.format(i) for i in u_vals]

    testing(u_vals, u_files, 'average distance between cities', 'runtime', 'average distance (u) vs A* runtime')



def v_test(): 

    v_vals = [1, 5, 10, 15, 20, 25, 30]
    v_files = ['problems/tsp-problem-10-45-100-{}-1.txt'.format(i) for i in v_vals]

    testing(v_vals, v_files, 'variance of distances', 'runtime', 'variance (v) vs A* runtime')

def k_test(): 
    k_vals = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    k_files = ['problems/tsp-problem-10-{}-1-1-1.txt'.format(i) for i in k_vals]

    testing(k_vals, k_files, 'number of distinct distance values', 'runtime', 'number of distinct distance values (k) vs A* runtime')


def twenty_test(): 
    x_letters = ['a', 'b', 'c', 'd']
    x_files = ["problems/tsp-problem-20-20-1-1-1-{}.txt".format(i) for i in x_letters]

    mytimes = []

    starting_city = 1 

    for i in range(len(x_files)): 

        start_time = time.time()
        filename = x_files[i]
        g = Graph(filename)
        result = a_star_tsp(g, starting_city)
        mytime = time.time() - start_time
        mytimes.append(round(mytime, 4)) 
        print(result)
        print(mytime)
        print('.')
    
    plt.bar(x_files, mytimes)
    plt.xlabel('filename')
    plt.ylabel('runtime')
    plt.title('runtimes of different 20-city problems with A*')

    plt.show()
    
#filename = 'problems/tsp-problem-10-10-1-1-1.txt'
#g = Graph(filename)

#starting_city = 1 

#best_path, best_cost = a_star_tsp(g, starting_city)


#print(f"Best path: {best_path}")
#print(f"Best cost: {best_cost}")
#print('.')

k_test()