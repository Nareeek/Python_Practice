def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')
list4 = extendList('b')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)
print("list4 = %s" % list4)

print()
print()

letter = "hai sethuraman"
for i in letter:
    if i == "a":
        pass
        print("pass statement is execute ..............")
    else:
        print(i)

print()
print()

list = ['a', 'b', 'c', 'd', 'e']
print(list[7:])

print()
print()


def fn(*argList):
    for argx in argList:
        print(argx)


fn('I', 'am', 'Learning', 'Python')
print()
print()

for i in range(5):
    print(i)

print()
print()


def fn(**kwargs):
    for emp, age in kwargs.items():
        print("%s's age is %s." % (emp, age))


fn(John=25, Kalley=22, Tom=32)
print()
print()

weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
listAsString = ' _'.join(weekdays)
print(listAsString)

print()
print()


class PC:
    processor = "Xeon"

    def set_processor(self, new_processor):
        processor = new_processor


class Desktop(PC):
    os = "Mac OS High Sierra"
    ram = "32 GB"


class Laptop(PC):
    os = "Windows 10 Pro 64"
    ram = "16 GB"


desk = Desktop()

print(desk.processor, desk.os, desk.ram)

lap = Laptop()

print(lap.processor, lap.os, lap.ram)
