# daemon thread - thread running in program, not important for programs

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()
print(x.isDaemon)

answer = input("Do you wish to exit? ")