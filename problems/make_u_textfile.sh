#!/bin/sh

# n_vals = [3,4,6,8,10, 12, 14, 16, 18, 20]
python3 generate_tsp.py -n 3 -k 3 -u 1 -v 1 


#for n in $(seq 5 5 50); 
#for n in $(seq 2 2 10);
#for n in $(seq 10 10 100); 
for n in $(seq 4 2 20 ); 
do
    x=$(( n * (n - 1) / 2 ))
    python3 generate_TSP.py -n $n -k $x -u 1 -v 1
done 
