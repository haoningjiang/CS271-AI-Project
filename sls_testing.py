from astar_v2 import a_star_tsp
from astar_v2 import calculate_mst_cost
from astar_v2 import Graph as Astar_Graph
from SLS import * 

import matplotlib.pyplot as plt 
import time 
import numpy as np 


def testing(vals, filenames, graphx1, graphy1, graphtitle1, graphx2, graphy2, graphtitle2): 

    num_iters = 20

    max_iterations = 20000
    
    mse = []
    correct_count = []


    for i in range(len(filenames)): 

        filename = filenames[i]
        g_star = Astar_Graph(filename)
        true_path, true_cost = a_star_tsp(g_star)

        square_error = []
        my_correct_count = 0 

        g = Graph(filename)

        for j in range(num_iters): 
            best_path, best_cost = stochastic_local_search(g, max_iterations)

            if round(best_cost, 4)==round(true_cost, 4): 
                my_correct_count+=1 
            
            square_error.append((best_cost-true_cost)**2)
        
        mse.append(round(np.average(square_error), 4))
        correct_count.append(my_correct_count / num_iters)

        print(f"{filename} done")



    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax_two = fig.add_subplot(111)
    fig, ax = plt.subplots(2)
    fig.tight_layout(pad=3)

    ax[0].plot(vals, mse, label='MSE')
        
    for xy in zip(vals, mse):                                       
        ax[0].annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 

    
    ax[1].plot(vals, correct_count, label='correct count')

    for xy in zip(vals, correct_count):                                       
        ax[1].annotate('(%s, %s)' % xy, xy=xy, textcoords='data') 


        
    #plt.xlabel(graphx)
    #plt.ylabel(graphy)
    #plt.title(graphtitle)
    ax[0].title.set_text(graphtitle1)
    ax[0].set_ylabel(graphy1)

    ax[1].title.set_text(graphtitle2)
    ax[1].set_xlabel(graphx2)
    ax[1].set_ylabel(graphy2)
    
    ax[0].grid()
    ax[1].grid()
    plt.show()


def n_test(): 

    n_vals = [3,4,6,8,10, 12, 14, 16, 18, 20]
    #n_vals = [3,4,6,8,10]

    n_files = ['problems/tsp-problem-{}-{}-1-1-1.txt'.format(i, i*(i-1)//2) for i in n_vals]

    testing(n_vals, n_files, 
            'number of cities', 'MSE', 'number of cities (n) vs MSE of path cost found by SLS', 
            'number of cities', 'percent SLS queries with correct answer', 'number of cities vs percent SLS queries with correct answer')


def iter_test(): 
    iter_vals = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    #iter_vals = [1, 10, 100, 1000, 10000, 100000, 1000000]
    filename = 'problems/tsp-problem-10-45-1-1-1.txt'
    #filename = 'problems/tsp-problem-20-190-1-1-1.txt'

    num_iters = 50 

    g_star = Astar_Graph(filename)
    true_path, true_cost = a_star_tsp(g_star)
    print(true_path, true_cost)

    g = Graph(filename)

    mse = []
    correct_count = []

    for max_iterations in iter_vals: 
        square_error = []
        my_correct_count = 0 

        for j in range(num_iters): 
            best_path, best_cost = stochastic_local_search_new(g, max_iterations)

            if round(best_cost, 4)==round(true_cost, 4): 
                my_correct_count+=1 
                
            square_error.append((best_cost-true_cost)**2)
            
        mse.append(round(np.average(square_error), 4))
        correct_count.append(my_correct_count / num_iters)
        
        print(max_iterations)


    fig, ax = plt.subplots(2)
    fig.tight_layout(pad=3)

    #ax[0].semilogx(iter_vals, mse, label='MSE')
    ax[0].plot(iter_vals, mse, label='MSE')

       
    for x, y in zip(iter_vals, mse): 
        ax[0].annotate('%s' % y, xy=(x,y), textcoords='data')

    
    #ax[1].semilogx(iter_vals, correct_count, label='correct count')
    ax[1].plot(iter_vals, correct_count, label='correct count')


    for x, y in zip(iter_vals, correct_count): 
        ax[1].annotate('%s' % y, xy=(x,y), textcoords='data')


    ax[0].title.set_text('number of iterations vs MSE of path cost found by SLS')
    ax[0].set_ylabel('MSE')

    ax[1].title.set_text('number of iterations vs percent SLS queries with correct answer')
    ax[1].set_xlabel('number of iterations')
    ax[1].set_ylabel('percent SLS queries with correct answer')
    
    ax[0].grid()
    ax[1].grid()
    plt.show()

iter_test()