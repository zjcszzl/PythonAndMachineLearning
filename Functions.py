def greet(first="", last=""):
    print("Hello " + first + " " + last)
    # If no return, the function returns None


def increment(number, by=10):
    return number + by


def multiply(*numbers):
    res = 1
    for number in numbers:
        res *= number
    return res


# Key - Value pairs
def save_user(**user):
    print(user["name"])


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return str(input)
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return str(input)


if __name__ == "__main__":
    greet("Jue")
    res = increment(number=2, by=5)
    print(res)
    other = increment(10)
    print(other)
    print(multiply(2, 3, 4, 5))
    save_user(name="Jue", id=12, age=24)
    message = "a"

    def g(name):
        message = "b"

    g("Mosh")
    print(message)
    print(fizz_buzz(12))
