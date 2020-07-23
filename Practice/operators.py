x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("x =", x)
print("y =", y)

print()

print("Arithmetic operations")
print("x + y = ", x + y)
print("x - y = ", x - y)
print("x * y = ", x * y)
print("x ** y = ", x ** y)
print("x / y = ", x / y if y != 0 else "I can't divide by 0")
print("x // y = ", x // y if y != 0 else "I can't divide by 0")
print("x % y = ", x % y if y != 0 else "I can't divide by 0")

print()

print("Bitwise operations")
print(
    "x & y = {2} & {3} = {4}  ({0} & {1}) = ({5}) AND".format(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8), x, y,
                                                              x & y,
                                                              bin(x & y)[2:].zfill(8)))
print(
    "x | y = {2} | {3} = {4}  ({0} | {1}) = ({5}) OR".format(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8), x, y,
                                                             x | y,
                                                             bin(x | y)[2:].zfill(8)))
print(
    "x ^ y = {2} ^ {3} = {4}  ({0} ^ {1}) = ({5}) XOR".format(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8), x, y,
                                                              x ^ y,
                                                              bin(x ^ y)[2:].zfill(8)))

print(
    "x << y = {2} << {3} = {4}  ({0} << {1}) = ({5})  Left Shift".format(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8), x,
                                                                         y, x << y,
                                                                         bin(x << y)[2:].zfill(8)))

print(
    "x >> y = {2} >> {3} = {4}  ({0} >> {1}) = ({5}) Right Shift".format(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8), x,
                                                                         y, x >> y,
                                                                         bin(x >> y)[2:].zfill(8)))
print(x, "bitwise not is ", ~x, bin(~x)[2:])
print(y, "bitwise not is ", ~y, bin(~y)[2:])
