# 1
def insert(value: list, dic: dict):
    dic[value[0]] = value[1]
    return


def addToValue(value: list, dic: dict):
    digit = value[0]
    return {k: v + digit for (k, v) in dic.items()}


def addToKey(value: list, dic: dict):
    digit = value[0]
    return {k + digit: v for (k, v) in dic.items()}


def get(value: list, dic: dict):
    digit = value[0]
    return dic[digit]


def hashMap(queryType, query):
    d = {}
    get_sum = 0
    for i in range(len(queryType)):
        if queryType[i] == "insert":
            insert(query[i], d)
        elif queryType[i] == "addToValue":
            d = addToValue(query[i], d)
        elif queryType[i] == "addToKey":
            d = addToKey(query[i], d)
        elif queryType[i] == "get":
            get_sum += get(query[i], d)

    return get_sum


# 2
def hashMap(queryType, query):
    a = []
    get = 0

    for (i, j) in zip(queryType, query):

        if i == "insert":
            if j[0] < 0 and abs(j[0]) > len(a):
                a = [0] * ((-j[0]) - len(a)) + a
                a[j[0]] = j[1]

            elif j[0] <= len(a):
                a.insert(j[0], j[1])
            elif j[0] >= 0:
                a = [0] * j[0] + a
                a[j[0]] = j[1]

        elif i == "addToKey":
            if j[0] >= 0:
                a = [0] * j[0] + a
            else:
                a = a[-j[0]:] + a[:-j[0]]

        elif i == "addToValue":
            a = list(map(lambda x: x + j[0], a))

        elif i == "get":
            if j[0] < 0:
                if abs(j[0]) < len(a):
                    get += a[j[0]]
            elif j[0] <= len(a):
                get += a[j[0]]

    return get


print(hashMap(["insert",
               "insert",
               "addToValue",
               "addToKey",
               "get"], [[1, 2],
                        [2, 3],
                        [2],
                        [1],
                        [3]]))
print()
