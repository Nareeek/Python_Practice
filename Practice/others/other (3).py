spelled =["zero"
        , "one"
        , "two"
        , "three"
        , "four"
        , "five"
        , "six"
        , "seven"
        , "eight"
        , "nine"
        , "ten"]

x = input().replace("10", spelled[10])
for i in range(10):
    x = x.replace(str(i), spelled[i])
print(x)