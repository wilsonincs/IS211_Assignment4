import time
import random

def insertion_sort(the_list):
    start_time = time.time()
    for index in range(1, len(the_list)):
        current_value = the_list[index]
        position = index

        while position > 0 and the_list[position - 1] > current_value:
            the_list[position] = the_list[position - 1]
            position -= 1

        the_list[position] = current_value
    time_end = time.time()
    time_difference = time_end - start_time
    return { "the list": the_list, "difference": time_difference}

def shell_sort(the_list):
    start_time = time.time()
    sublist_count = len(the_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(the_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    time_end = time.time()
    time_difference = time_end - start_time
    return { "the list": the_list, "difference": time_difference}

def gap_insertion_sort(the_list, start, gap):
    for i in range(start + gap, len(the_list), gap):
        current_value = the_list[i]
        position = i
        while position >= gap and the_list[position - gap] > current_value:
            the_list[position] = the_list[position - gap]
            position = position - gap
        the_list[position] = current_value

def python_sort(the_list):
    start_time = time.time()
    the_list = the_list.sort()
    time_end = time.time()
    time_difference = time_end - start_time
    return { "the list": the_list, "difference": time_difference}

def populate(top_values):
    sorting_list = random.sample(xrange(1, (top_values+1)), 100)
    return sorting_list

def main():
    lists_size = [500,1000,10000]

    for size in lists_size:
        sort_types = {
            'Insertion sort':0.0,
            'Shell sort': 0.0,
            'Python sort': 0.0
        }

        i = 0
        while i < 100:
            sorting_list = populate(size)
            sort_types['Insertion sort'] += insertion_sort(sorting_list)["difference"]
            sort_types['Shell sort'] += shell_sort(sorting_list)["difference"]
            sort_types['Python sort'] += python_sort(sorting_list)["difference"]
            i += 1

        for sort in sort_types:
            print "%s  took %10.7f seconds to run, on average %s" % (sort, sort_types[sort] / i, size)


if __name__ == "__main__":
    main()