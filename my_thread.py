import time
import threading
import datetime

def task1():
    time.sleep(1)
    print("task one completed\n")


def task2():
    time.sleep(1)
    print("task one completed\n")


def task3():
    time.sleep(1)
    print("task one completed\n")


current_time = time.perf_counter()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()



end_time = time.perf_counter()

elapsed_time =  end_time - current_time
print(f"Elapsed time: {elapsed_time} seconds")





