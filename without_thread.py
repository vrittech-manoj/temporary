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

task1()
task2()
task3()

end_time = time.perf_counter()
elapsed_time =  end_time - current_time
print(f"Elapsed time: {elapsed_time} seconds")
