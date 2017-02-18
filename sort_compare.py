from Sorting import insertion_sort, selection_sort, shell_sort
import time
from utils import AlgoType
from random import randint

def sort(algo, input):
    timestart = time.time()

    if(algo == AlgoType.SELECTION_SORT):
        selection_sort.do_sort(input)
    elif(algo == AlgoType.INSERTION_SORT):
        insertion_sort.do_sort(input)
    elif(algo == AlgoType.SHELL_SHORT):
        shell_sort.do_sort(input)


    return (time.time()-timestart)

def randomInputs(algo1, algo2, num_inputs, vals_per_input):

    algo1Time = 0.0
    algo2Time = 0.0

    # build random inputs
    for i in range(num_inputs):

        input = [randint(-1000,1000) for _ in range(vals_per_input)]
        #input = sorted(input)

        algo2Time += sort(algo2, list(input))
        algo1Time += sort(algo1, list(input))



    # get the average sorting time
    algo1Time /= num_inputs
    algo2Time /= num_inputs

    print("Algo1 Avg Time: {0:.15f}".format(algo1Time))
    print("Algo2 Avg Time: {0:.15f}".format(algo2Time))

    print("Algo1 is {0:.2f} times faster than Algo2".format(algo2Time/algo1Time))

if __name__ == '__main__':

    randomInputs(AlgoType.INSERTION_SORT, AlgoType.SELECTION_SORT,10,3000)
    #randomInputs(AlgoType.SHELL_SHORT, AlgoType.INSERTION_SORT,10,3000)
    randomInputs(AlgoType.SHELL_SHORT, AlgoType.SELECTION_SORT,10,3000)