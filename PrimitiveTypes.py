'''
Numbers, Boolean, String
'''
import math
student_count = 1000
rating = 4.99
is_published = True
course_name = "python programming"
# Strings
message = """
Hi, John, this is xxxx, from
"""
length = len(message)
message = message.strip()
print(message[0:3])
print(message[:3])
print(message)
# Escape sequences
# \"   \'    \\    \n
course = "python \'programming\'"
print(course)
# Formated Strings
first = "mosh"
last = "hamedani"
full = first + " " + last
print(full)
# String methods
course = "Python Programming"
print(len(course))
print(course.capitalize())
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course)
print(course.find("P"))
print(course.replace("P", "j"))
print("Pyt" in course)
print(not course)
# Numbers
a = 1
a = 1.1
a = 1 + 2j
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
# Working with numbers
print(round(2.9))
print(abs(-2.9))
print(math.sin(1.57))
print(math.sqrt(4))
print(math.pow(3, 2))
# Type conversion
x = input("X: ")
y = int(x) + 1
# int() float() bool() str()
y = bool(y)
print(y)
# Quiz
