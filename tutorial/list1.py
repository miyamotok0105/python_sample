
list = ["A", "B", "C", "D"]

print(list.pop(1))
print(list)

list.pop()
print(list)


from collections import deque
items = deque([1, 2])
items.append(3) # deque == [1, 2, 3]
items.rotate(1) # The deque is now: [3, 1, 2]
items.rotate(-1) # Returns deque to original state: [1, 2, 3]
item = items.popleft() # deque == [2, 3]

print(item)


items = deque([1, 2])
items.append(3)
print(items)
items.append(3)
print(items)
item = items.popleft()
print(items)
print(item)
item = items.pop()
print(items)
print(item)
