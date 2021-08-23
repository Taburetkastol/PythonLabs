from threading import Thread, BoundedSemaphore
from time import sleep, time

# Вариант 25%5+1 = 1


semaphore = BoundedSemaphore(3)
semaphore.acquire()


def list_of(number):
    start = time()
    with semaphore:
        sleep(1)
        print(f"\nguy {number}, his time: {time() - start}")


guy = [Thread(target=list_of, args=(i,)) for i in range(5)]

for g in guy:
    g.start()
