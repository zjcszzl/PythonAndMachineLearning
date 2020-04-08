# Class: blueprint of creating new project
# Object: instance of a class
# Class: Human:
# Object: John, Mary, Jack


from abc import ABC, abstractmethod


class Point:
    # Class attributes, shared across all the instance of class
    default_color = "red"

    # Constructor, self refer to the current project
    def __init__(self, x=0, y=0):
        # Instance attributes, belong to the point object, every object can have different
        self.x = x
        self.y = y

    # Instance method
    def draw(self):
        print(self.x, self.y)

    # Class Method
    @classmethod
    def zero(cls):
        return cls(1, 2)

    # Magic method
    def __str__(self):
        return (str(self.x) + " " + str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x or self.y > other.y

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


class TagCloud:
    def __init__(self):
        self.__tags = dict()
        # __ would make the attribute become private

    def add(self, tag):
        if tag.lower() not in self.__tags:
            self.__tags[tag.lower()] = 1
        else:
            self.__tags[tag.lower()] += 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price should be positive")
        self.price = value

    price = property(get_price, set_price)


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal is parent, Mammal is child
class Mammal(Animal):
    def __init__(self):  # would override the constructor in the base class
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


class Employee:
    def greet(self):
        print("Employee")


class Person:
    def greet(self):
        print("Person")


class Manager(Employee, Person):  # Order matters
    pass


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# A child class has to implement the abstract method in the parent class
class MemoryStream(Stream):
    pass


if __name__ == "__main__":
    p = Point(1, 5)
    p.z = 10
    p.draw()
    print(type(p))
    P = Point.zero()
    P.draw()
    print(Point.default_color)
    print(isinstance(p, Point))
    print(str(P))
    print(P == p)
    print(P > p)
    print(P < p)
    Z = P + p
    Z.draw()

    cloud = TagCloud()
    cloud.add("python")
    cloud.add("python")
    cloud.add("Python")
    print(cloud["python"])
    # print(cloud.__tags)
    print(len(cloud))
    for val in cloud:
        print(cloud[val])
    print(cloud.__dict__)

    #pro = Product(10)
    # pro.set_price(65)

    m = Mammal()
    m.eat()
    print(m.weight)

    M = Manager()
    M.greet()

    stream = NetworkStream()
    stream.read()
