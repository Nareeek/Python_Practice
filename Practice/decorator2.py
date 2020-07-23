import functools


def function1(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("welcome home")

    return wrapper


@function1
def function2(name):
    print(f"{name}")


function2("python")

print("-" * 15)


class Square:
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            print("error")

    @property
    def area(self):
        return self._side ** 2

    @classmethod
    def unit_square(cls):
        return cls(1)


s = Square(5)
print(s.side)
print(s.area)

print("-" * 15)


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class One:
    pass


first = One()
second = One()

print(first is second)

print("-" * 15)


def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator_repeat


@repeat(num=5)
def function(name):
    print(f"{name}")


function("python")
