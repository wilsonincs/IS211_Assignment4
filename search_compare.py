import random
import time

"""Variable names in this exercise are inspired from chapter 2 and 5
of Problem_Solving_with_Algorithms_and_DataStructures"""

#lets define the sequential_search function that will take 2 parameters (theList,thing)


def sequential_search(the_list, thing):
    start_time = time.time()    #declaring the start time so we can return performance execution later on.
    position = 0                # declaring a position variable and initialize it to 0 it will be used to check against
                                # the loop and the condition.
    the_list.sort()
    found = False

    while position < len(the_list) and not found:
        if the_list[position] == thing:
            found = True
        else:
            position = position + 1

    end_time = time.time()

    return found,end_time - start_time

#------------------------------------------------------

def ordered_sequential_search(the_list, thing):

    start_time = time.time()
    position = 0
    the_list.sort()
    found = False
    stop = False

    while position < len(the_list) and not found and not stop:
        if the_list[position] == thing:
            found = True

        elif the_list[position] > thing:
            stop = True

        else:
            position = position + 1

    end_time = time.time()

    return found, end_time - start_time


#-------------------------------------------------------------

def binary_search_iterative(the_list, thing):
    first = 0
    the_list.sort()
    last = len(the_list) - 1
    found = False
    start_time = time.time()

    while first <= last and not found:
        midpoint = (first + last) // 2

        if the_list[midpoint] == thing:
            found = True

        elif thing < the_list[midpoint]:
            last = midpoint - 1

        else:
            first = midpoint + 1

    end_time = time.time()

    return found, end_time - start_time


#-------------------------------------------------------------------

def binary_search_recursive(the_list, thing):
    the_list.sort()
    start_time = time.time()

    if len(the_list) == 0:
        return False

    else:
        midpoint = len(the_list) // 2
        if the_list[midpoint] == thing:
            return True
        else:
            if thing < the_list[midpoint]:
                return binary_search_iterative(the_list[:midpoint], thing)
            else:
                return binary_search_iterative(the_list[midpoint + 1:], thing)

    end_time = time.time()

    return end_time - start_time


#-------------------------------------------------------------------------

def populate(top_values):

    example_list = random.sample(xrange(1, (top_values + 1)), 100)
    return example_list


def main():

    lists_size = [500, 1000, 10000]
    searches = {'Sequential Search': 0,
             'Ordered Sequential': 0,
             'Binary Iterative': 0,
             'Binary Recursive': 0}

    for size in lists_size:
        num = 0
        while num < 100:
            searches_list = populate(size)
            searches['Sequential Search'] += sequential_search(searches_list, -1)[0]
            searches['Ordered Sequential'] += ordered_sequential_search(searches_list, -1)[0]
            searches['Binary Iterative'] += binary_search_iterative(searches_list, -1)[0]
            searches['Binary Recursive'] += binary_search_recursive(searches_list, -1)[0]
            num = num + 1

        print 'For sample size %s:' % (size)

        for tries in searches:
            print ("%s Search took %10.7f seconds to run, on average.") % (tries, searches[tries] / num)


if __name__ == "__main__":
    main()