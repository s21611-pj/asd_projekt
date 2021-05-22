import timeit
import sys
sys.setrecursionlimit(10**6)

# bubblesort
def bubble_sort(array):
    time = []
    start = timeit.default_timer()
    size = len(array)
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("BUBBLE SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(array)

# #quicksort
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for i in range(p, r):
        if A[i] <= pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller

def run_quick_sort(A):
    time = []
    start = timeit.default_timer()
    quick_sort(A, 0, len(A) - 1)
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("QUICK SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(A)

#heapsort
def heapify(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and array[largest] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, size, largest)

def heap_sort(array):
    size = len(array)
    time = []
    start = timeit.default_timer()
    for i in range(size // 2 - 1, -1, -1):
        heapify(array, size, i)
    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("HEAP SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(array)