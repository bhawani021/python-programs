#!/usr/bin/env python
"""
Threads
- A thread is a smallest unit that can be scheduled by an operating system.
- Threads are generally contained in processes.
- Threads share common memory and state of process.
- Threads share code or instructions and value of variables

Type of Threads
- Kernel threads
- User threads

Every process has at least one thread(i.e. process itself).
A process can start multiple threads.
OS executes these threads like parallel processes.
On a single processor machine this parallelism is achieved by thread scheduling or timeslicing.

In multithreaded application, there are several points of execution within the same memory space.
 - Each point of execution is called a thread
 - Threads share access to memory

A program that can have two or more parts that can run concurrently.
Each independent part of program is called a thread.
Each thread defines a separate path of execution.
Multithreading is a special form of multitasking

"""
import threading


# Example 1
def worker():
    print('Worker')
    return


for i in range(5):
    t = threading.Thread(target=worker)
    t.start()


# Example 2
# Spawn a tread and pass it arguments
def worker1(counter):
    print('Worker {}'.format(counter))
    return

for i in range(5):
    t = threading.Thread(target=worker1, args=(i,))
    t.start()
