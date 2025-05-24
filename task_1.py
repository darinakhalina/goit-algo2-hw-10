import random
import time
import numpy as np
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure(sort_func, arr: list[int]):
    results = []
    for _ in range(5):
        start = time.time()
        sort_func(arr.copy())
        end = time.time()
        results.append(end - start)
    return np.mean(results), sum(results) / 5


def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times, deterministic_times = [], []

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        rand_avarage, randomized_time = measure(randomized_quick_sort, arr)
        randomized_times.append(rand_avarage)
        det_avarage, deterministic_time = measure(deterministic_quick_sort, arr)
        deterministic_times.append(det_avarage)

        print(f"\nРозмір масиву: {size}")
        print(f"\tРандомізований QuickSort: {randomized_time:.4f} секунд")
        print(f"\tДетермінований QuickSort: {deterministic_time:.4f} секунд")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, "b", label="Рандомізований QuickSort")
    plt.plot(
        sizes,
        deterministic_times,
        "r",
        label="Детермінований QuickSort",
    )
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
