'''
multiprocessing : better for CPU bound tasks (Heavy CPU Usage)
multithreading : better for IO bound tasks (Waiting around)
'''

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    start_time = time.perf_counter()
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    
    a.join()
    b.join
    c.join()
    d.join()
    
    end_time = time.perf_counter()
    print(f'Finished in {end_time-start_time} seconds')

if __name__ == '__main__':
    main()