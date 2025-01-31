import timeit
import matplotlib.pyplot as plt
import pandas as pd

from task_2.lru_calculation import fibonacci_lru
from task_2.splay_tree_calculation import SplayTree, fibonacci_splay


# Measure execution times
def measure_execution_times():
    splay_tree = SplayTree()
    results = []

    for n in range(0, 1001, 50):
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=10) / 10
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, splay_tree), number=10) / 10
        results.append((n, lru_time, splay_time))

    return results


if __name__ == "__main__":
    # Collect and display results
    results = measure_execution_times()
    df = pd.DataFrame(results, columns=["n", "LRU Cache Time (s)", "Splay Tree Time (s)"])
    print(df.to_string(index=False))

    # Plot the results
    plt.plot(df["n"], df["LRU Cache Time (s)"], label="LRU Cache")
    plt.plot(df["n"], df["Splay Tree Time (s)"], label="Splay Tree")
    plt.xlabel("n (Fibonacci number index)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Fibonacci Calculation Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()
