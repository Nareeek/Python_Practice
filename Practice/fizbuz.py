def fizzbuzz(n):
    if n % 3 == 0:
        if n % 5:
            return "fizz"
        else:
            return "fizzbuzz"

    return "buzz" if n % 5 else n


print(fizzbuzz(15))
