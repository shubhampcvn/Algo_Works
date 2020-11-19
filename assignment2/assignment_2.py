import threading
import datetime
from threading import Thread

class myThread (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    
    def run(self):
        print("\nStarting " + self.name)
        self.run_in_parallel()


    def run_in_parallel(self):
        t1 = Thread(target=self.A)
        t2 = Thread(target=self.B)
        t3 = Thread(target=self.C)
        t4 = Thread(target=self.D)
        t1.start()
        t2.start()
        t3.start()
        t4.start()

    def A(self):
        for i in range(1, 101):
            print(f"A{i}")

    def B(self):
        for i in range(1, 101):
            print(f"B{i}")
    
    def C(self):
        for i in range(1, 101):
            print(f"C{i}")

    def D(self):
        for i in range(1, 101):
            print(f"D{i}")

thread1 = myThread("Thread1")
thread2 = myThread("Thread2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
