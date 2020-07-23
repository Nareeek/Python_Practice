def func1(name):
    return f"Hello {name}"


def func2(name):
    return f"{name} how you doing?"


def func3(func4):
    return func4("Dear learner")


print(func3(func1))
print(func3(func2))
print("-" * 15)


def func(n):
    print("first function")

    def func1():
        return "first child function"

    def func2():
        return "second child function"

    if n == 1:
        return func1()
    else:
        return func2()


a = func(1)
b = func(2)

print("-" * 15)
print(a)
print(b)
print("-" * 15)
