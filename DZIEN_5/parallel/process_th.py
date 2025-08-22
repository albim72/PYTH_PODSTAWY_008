from concurrent.futures import ProcessPoolExecutor
import math
from concurrent.futures.thread import ThreadPoolExecutor
import time


def intensive(n):
    return sum(math.sqrt(i) for i in range(10_000_000 * n))
if __name__ == '__main__':

    st1 = time.time()
    with ProcessPoolExecutor() as executor:
        results = executor.map(intensive, range(10))
        for result in results:
            print(result)
    tk1 = time.time()
    print(f"time Process: {tk1-st1}")
    print("____________________________")

    st2 = time.time()
    with ThreadPoolExecutor() as executor:
        results = executor.map(intensive, range(10))
        for result in results:
            print(result)
    tk2 = time.time()
    print(f"time Thread: {tk1 - st1}")
