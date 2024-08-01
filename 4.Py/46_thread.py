import threading
import time

def eat_breakfast():
    time.sleep(3)
    print('You ate breakfast!')

def drink_coffee():
    time.sleep(4)
    print("You drank coffee!")

def study():
    time.sleep(5)
    print("You finished studying!")

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

# eat_breakfast()
# drink_coffee()
# study()

x.join()
y.join()
z.join()

print(threading.enumerate(), threading.active_count())
print(time.perf_counter())