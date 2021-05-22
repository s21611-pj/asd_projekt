import random
import sys
sys.setrecursionlimit(100000000)

from sorting_algorithms import bubble_sort, run_quick_sort, heap_sort

def run():

    # random-numbers-list
    random_list1 = []
    random_list2 = []
    random_list3 = []

    for i in range(0, 2400):
        n = random.randint(1, 10)
        random_list1.append(n)
        random_list2.append(n)
        random_list3.append(n)

    # sorted-list
    sorted_list1 = random_list1
    sorted_list2 = random_list2
    sorted_list3 = random_list3

    # reversed-sorted-list
    reversed_sorted_list1 = list(reversed(sorted_list1))
    reversed_sorted_list2 = list(reversed(sorted_list2))
    reversed_sorted_list3 = list(reversed(sorted_list3))

    print("\nRANDOM NUMBERS LIST")
    bubble_sort(random_list1)
    heap_sort(random_list3)
    run_quick_sort(random_list2)

    print("\nREVERSED SORTED LIST")
    bubble_sort(reversed_sorted_list1)
    heap_sort(reversed_sorted_list3)
    run_quick_sort(reversed_sorted_list2)

    print("\nSORTED LIST")
    bubble_sort(sorted_list1)
    heap_sort(sorted_list3)
    run_quick_sort(sorted_list2)

if __name__ == '__main__':
    run()
