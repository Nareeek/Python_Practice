# wrapper function
def function1(function):
    def wrapper():
        print("this is")
        function()
        print("decorator")

    return wrapper()


# without decorator
def main_function1():
    print("without")


function1(main_function1)

print("-" * 15)


# with decorator
@function1
def main_function2():
    print("with")
