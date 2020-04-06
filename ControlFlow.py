# Conditional Statements
temperature = 35
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's OK")
else:
    print("Done")

# Tenary Operator
age = 22
message = "Eligible" if age > 18 else "Not Eligible"
print(message)

# Logical Operator
high_income = False
good_credit = True
student = True
if not high_income and good_credit and student:
    print("Eligible")
else:
    print("Not Eligible")

# Short-circuit evaluation
# Chaining Comparison Operators
age = 22
if 18 < age < 25:
    print("Eligible")

# For loops
for num in range(3):
    print("Hello")

# For else loops
for num in range(3):
    print("Success")
    if num == 4:
        break
else:
    print("done")

# Nested loops
for x in range(5):
    for y in range(6):
        print("Area: " + str(x*y))

# Iterables
# While loops
number = 10
while number > 0:
    print("Hello")
    number -= 2

command = ""
while command.lower() != "quit":
    command = input("")
    print("command")

# Infinite loops
while True:
    command = input()
    if command.lower() == "quit":
        break
