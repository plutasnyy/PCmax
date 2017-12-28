# Genethic Alghoritm to solve PC MAX problem

### Data structure

Example data.txt:
```
15 <- amount of processors
20 <- amount of exersies
1 <- exercise`s time
8
...
```

### Installation
```
git clone https://github.com/plutasnyy/PCmax
```
In main.py:
```
genetic = GeneticAlghoritm(
    data = data,
    population_size = i, # set your population size, recommend 20-40
    time_limit = j, # and execution time
)
```
In config.py:
```
#RANDOM GREEDY LAST_BEST
INITIAL_VECTOR = "LAST_BEST" # set how will look your initial population
# in case of empty last_bect vector program will use reverse sorted exercises
```
You can run using: `python3 main.py [optional 0-4 argument]`. Use argument to mark file:
```
0 - random vector
1 - m25
2 - m50
3 - m50n200
4 - m50n1000
```
Default is `0`. Using random vector you should set config:
```
OPTIMAL = True # You will know optimal value

RAND_PROC = False # False -> amount of proc = PROCESSORS, else random from MIN-MAX
PROCESSORS = 10
MAX_PROC = 10000
MIN_PROC = 3

RAND_EX = False
EXERCIESES = 80
MAX_EX = 50000
MIN_EX = 50

MIN_EX_TIME = 10 # interval exercise time
MAX_EX_TIME = 5000
```

### Description
The chromosome is represented by the input vector into the greedy algorithm. Mutation was implemented as swaping two elements in chromosome. Crossing, however, by crossover by order.  
In the fitness function, the absolute value of the distance from the expected optimum is evaluated.  
For optimized cases, the program was confused by 1-2 units of time :D
