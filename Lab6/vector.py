import multiprocessing
from time import time
import sharedmem


def f(M, start, stop):
    N = 5000
    P = []
    Q = []
    for i in range(N):
        P.append(0)
    for i in range(N):
        Q.append(1)
    for i in range(start, stop):
        for j in range(N):
            r = 1 / (1 + abs(Q[j] - P[i]))
            M.append(r)


if __name__ == '__main__':
    N = int(5000)
    M1 = []
    M2 = []
    M3 = []
    for i in range(N):
        M1.append(sharedmem.empty(N))
    for i in range(N):
        M2.append(sharedmem.empty(N))
    for i in range(N):
        M3.append(sharedmem.empty(N))
    start_time1 = time()
    f(M1, 0, N)
    print(f"Time without multiprocessing: {time() - start_time1}")
    n = N // 4
    start_time2 = time()
    p1 = multiprocessing.Process(target=f, args=(M2, 0, n))
    p2 = multiprocessing.Process(target=f, args=(M2, n, 2 * n))
    p3 = multiprocessing.Process(target=f, args=(M2, 2 * n, 3 * n))
    p4 = multiprocessing.Process(target=f, args=(M2, 3 * n, 4 * n))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print(f"Time with multiprocessing: {time() - start_time2}")
    f(M3, 0, N)
    flag = False
    for i in range(N // 12):
        for j in range(N // 12):
            if M1[i][j] != M3[i][j]:
                flag = True
    if not flag:
        print("Equal")
    else:
        print("Not Equal")