import heapq

li = [6, 2, 3, 1, 4, 5]

# initialize heapq with element object
heapq.heapify(li)

# push into heapq
heapq.heappush(li, 7)

# pop smallest element from heapq
print(heapq.heappop(li))

# push first and then remove
print(heapq.heappushpop(li, 0))

# first pop and then remove smallest element
print(heapq.heapreplace(li, 0))

# some advanced

task = []
heapq.heappush(task, ("write document", 10))
heapq.heappush(task, ("leetcode", 0))
heapq.heappush(task, ("leetcode new", 9))

print(task)

while task:
    print(heapq.heappop(task))
    
# customized with greater or smaller

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority > other.priority
        

tasks = []

heapq.heappush(tasks, Task("Write", 10))
heapq.heappush(tasks, Task("leetcode", 20))

while tasks:
    print(heapq.heappop(tasks).name)


import heapq

words = ["apple", "banana", "cherry", "date", "fig", "grape"]

print(heapq.nsmallest(3, words, key=len))

def compare(item):
    return item[1]
    
employees = [
    ("Alice", 80000),
    ("Bob", 50000),
    ("Charlie", 60000),
    ("David", 75000)
]

# print(heapq.nsmallest(3, employees, key=lambda x: x[1]))
print(heapq.nsmallest(3, employees, key=compare))


