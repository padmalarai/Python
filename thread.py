from threading import *
import time

def hello():
    print("hello")

t= Timer(10,hello)
t.start()


def test1():
    while True:
        print("test1")
        time.sleep(5)
    
def test2():
    while True:
        print("test2")
        time.sleep(5)

t1=Timer(10, test1)
t2=Timer(5, test2)

t1.start()
t2.start()
