# ASSIGNMENT-3 

import random
import time
import copy
import sys

sys.setrecursionlimit(50000)

# ___________________  SORTING ALGORITHMS _________________________________________

# Insertion Sort | Stable | In-place 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort | Stable | Out-of-place 
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Quick Sort | Unstable | In-place
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high] = arr[high], arr[mid]

def partition(arr, low, high):
    median_of_three(arr, low, high)
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr


# ______________________ TIMING UTILITY  ___________________________________________

def measure_time(sort_func, arr):
    # Always sort a copy so the original data stays unchanged for other algorithms
    arr_copy = copy.deepcopy(arr)
    start = time.time()
    if sort_func == quick_sort:
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)
    end = time.time()
    return round((end - start) * 1000, 3)  # milliseconds


# ______________  DATASET GENERATOR _______________________________________

def generate_datasets(sizes):
    datasets = {}
    for n in sizes:
        random.seed(42)  # fixed seed for reproducibility
        rand_list    = random.sample(range(1, 100001), n)
        sorted_list  = sorted(rand_list)
        reverse_list = sorted(rand_list, reverse=True)
        datasets[n] = {
            'random' : rand_list,
            'sorted' : sorted_list,
            'reverse': reverse_list
        }
    return datasets


# ____________________   RUN EXPERIMENTS   ___________________________─

def run_experiments(datasets, sizes):
    input_types = ['random', 'sorted', 'reverse']

    print("\n" + "=" * 65)
    print("  Timing Results (milliseconds)")
    print("=" * 65)

    for n in sizes:
        print(f"\n  Size: {n}")
        print(f"  {'Input':<10} {'Insertion Sort':>16} {'Merge Sort':>12} {'Quick Sort':>12}")
        print("  " + "-" * 54)

        for itype in input_types:
            t_ins = measure_time(insertion_sort, datasets[n][itype])
            t_mrg = measure_time(merge_sort,     datasets[n][itype])
            t_qck = measure_time(quick_sort,     datasets[n][itype])
            print(f"  {itype:<10} {t_ins:>14} ms  {t_mrg:>8} ms  {t_qck:>8} ms")

    print("\n" + "=" * 65)


# _________________     CORRECTNESS CHECK _______________________________

def correctness_check():
    test   = [5, 2, 9, 1, 5, 6]
    expect = [1, 2, 5, 5, 6, 9]

    print("\n" + "=" * 65)
    print("  Correctness Check | Input: [5, 2, 9, 1, 5, 6]")
    print("  Expected         : [1, 2, 5, 5, 6, 9]")
    print("=" * 65)

    r1 = insertion_sort(test[:])
    print(f"  Insertion Sort : {r1}  {'PASS' if r1 == expect else 'FAIL'}")

    r2 = merge_sort(test[:])
    print(f"  Merge Sort     : {r2}  {'PASS' if r2 == expect else 'FAIL'}")

    r3 = test[:]
    quick_sort(r3, 0, len(r3) - 1)
    print(f"  Quick Sort     : {r3}  {'PASS' if r3 == expect else 'FAIL'}")

    print("=" * 65)


if __name__ == "__main__":
    print("\n  Sorting Performance Analyzer (SPA)")
    print(" Unit 3 Assignment")

    correctness_check()

    sizes = [1000, 5000, 10000]
    datasets = generate_datasets(sizes)
    run_experiments(datasets, sizes)

    print("\n  Algorithm Properties:")
    print("  Insertion Sort : Stable   | In-place     | O(n^2) avg | O(n) best")
    print("  Merge Sort     : Stable   | Out-of-place | O(n log n) always")
    print("  Quick Sort     : Unstable | In-place     | O(n log n) avg | O(n^2) worst")
    print()