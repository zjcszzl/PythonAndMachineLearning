from sys import getsizeof
from array import array
import collections
# List
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 7
combined = zeros + letters
print(combined)
arr = list(range(1, 10, 2))
print(arr)
str = list("areyouok")
print(str)
print(len(str))
# Use [index] to access items in list, negative index means from the back
letters[0] = "A"
print(letters[:-2])
# List unpacking
numbers = [1, 2, 3]
first, second, third = numbers
# other, *hhh = numbers
# print(other)
# print(hhh)
# Looping over lists
# Enumerate would give a tuple, (a,b)->a:index, b:element at index
for letter in enumerate(letters):
    print(letter)
    print(letter[0])
for loc, item in enumerate(letters):
    print(loc, item)
# Adding or removing items
l = ["a", "b", "c"]
# add: append add at end
l.append("d")
l.insert(0, "-")
l.pop()
l.remove("-")  # only remove the first occurrence
del l[0]    # pop only remove certain index, del remove certain range
print(l)
# Finding items
L = ["a", "b", "c"]
print(L.index("a"))  # If not exist, would give an error
if "d" in L:
    print(L.index("d"))
print(L.count("a"))
# Sorting lists
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
sorted(numbers)  # return a new list, would not affect the original one
print(numbers)
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 8),
    ("Product4", 15)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
# lambda expression
items.sort(key=lambda x: x[1])
print(items)
# Map & Filter functions
prices = []
for item in items:
    prices.append(item[1])
x = list(map(lambda x: x[1], items))
y = list(filter(lambda x: x[1] > 10, items))
print(y)
print(x)
print(prices)
# List comprehension
z = [item for item in items if item[1] > 10]
print(z)
# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
X = [(i, j) for i in list1 for j in list2]
Y = [zip(list1, list2)]
print(X)
print(Y)
# Stacks - LIFO, append to add to top, pop to remove the pop, [-1] to access the top
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
hist = stack.pop()
if not stack:
    print(hist)
# Queues: - FIFO,
queue = collections.deque()
queue.append(4)
queue.append(5)
queue.append(6)
queue.appendleft(7)
queue.popleft()
queue.pop()
if not queue:
    print("Empty")
print(queue)
# Tuples: read only list, immutable
point = ((1, 2) + (3, 4)) * 2
p = 1,
print(type(point), type(p))
print(point)
# Swapping variables
x, y = 10, 11
y, x = x, y
print(x, y)
# Arrays, less memory and time than list
arr = array("i", [1, 2, 3])
arr.append(4)
arr.insert(2, 7)
print(arr)
# Sets -- unordered
nums = [1, 1, 2, 3, 4]
unique = set(nums)
print(unique)
unique.add(5)
unique.remove(3)
print(len(unique))
first = set(nums)
second = {1, 4}
print(first | second)  # Union two sets that include in either
print(first & second)  # intersect of two sets
print(first - second)  # in first, not in second
print(first ^ second)  # only in one set, cannot in both
if 1 in first:
    print("yes")
# Dictionaries: key-value pair
point = dict()   # Or point = dict(x=1,y=2)
point["x"] = 1
point["y"] = 2
point["z"] = 3
if "x" in point:
    print(point["x"])
print(point.get("x"))
del point["z"]
print(point)
for key in point:
    print(key)
for key, value in point.items():
    print(key, value)
# Dictionary comprehension
values = [x**2 for x in range(5)]
print(values)
phone = {a: b for a in "abc" for b in range(3)}
print(phone)
# Generator expression
v = (x*2 for x in range(10000000))
print("Generator", getsizeof(v))
# Unpacking operator: *
n = [1, 2, 3]
print(n)
# Quiz
sentence = "This is a common interview question"
# Find most repeated character
count = collections.Counter(sentence)
print(count.most_common(1))
print(count)
print(sorted(count.items(), key=lambda kv: kv[1], reverse=True))
