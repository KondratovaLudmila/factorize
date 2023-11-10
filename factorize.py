from time import time
from math import sqrt
from multiprocessing import cpu_count, Pool

def operate_number(number: int):
    result = []
    max_div = int(sqrt(number))
    for div in range(1, max_div + 1):
        if number % div == 0:
            result.append(div)
            result.append(number // div)
    result.sort()
    return result

def factorize(*numbers):
    with Pool(processes=cpu_count()) as pool:
        total_result = pool.map(operate_number, numbers)

    return total_result

if __name__=="__main__":
    start = time()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print(f"Total time: {time()-start}")



