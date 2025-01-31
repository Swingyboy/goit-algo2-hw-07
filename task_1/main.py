import random
import time
import threading
from functools import lru_cache

N = 100_000
CACHE_SIZE = 1000
Q = 50_000
QUERIES = []

# Generate an array of 100,000 random integers
ARRAY = [random.randint(1, 1000) for _ in range(N)]

# Generate 50,000 queries
for _ in range(Q):
    if random.choice([True, False]):
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        QUERIES.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 1000)
        QUERIES.append(('Update', index, value))


# --- Functions without caching ---
def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])


def update_no_cache(array, index, value):
    array[index] = value


# --- Functions with LRU cache ---
@lru_cache(maxsize=CACHE_SIZE)
def cached_range_sum(L, R):
    return sum(ARRAY[L:R + 1])


def range_sum_with_cache(L, R):
    return cached_range_sum(L, R)


def update_with_cache(array, index, value):
    array[index] = value
    cached_range_sum.cache_clear()  # Clear the cache after updating


# --- Testing and timing in threads ---
def test_no_cache():
    start_time = time.time()
    for query in QUERIES:
        if query[0] == 'Range':
            range_sum_no_cache(ARRAY, query[1], query[2])
        elif query[0] == 'Update':
            update_no_cache(ARRAY, query[1], query[2])
    no_cache_time = time.time() - start_time
    print(f'Time taken without caching: {no_cache_time:.2f} seconds\n')


def test_with_cache():
    start_time = time.time()
    for query in QUERIES:
        if query[0] == 'Range':
            range_sum_with_cache(query[1], query[2])
        elif query[0] == 'Update':
            update_with_cache(ARRAY, query[1], query[2])
    cache_time = time.time() - start_time
    print(f'Time taken with LRU cache: {cache_time:.2f} seconds\n')

# --- Run tests in threads ---
thread_no_cache = threading.Thread(target=test_no_cache)
thread_with_cache = threading.Thread(target=test_with_cache)

thread_no_cache.start()
thread_with_cache.start()

thread_no_cache.join()
thread_with_cache.join()
