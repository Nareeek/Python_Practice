from collections import namedtuple
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import UserDict, UserList, UserString

a = namedtuple("courses", "name, technology, quality")
s = a("data science", "python", "easy")
print(s)

b = ["e", "d", "u", "r", "e", "k", "a"]
c = deque(b)
print(c)
c.append("python")
print(c)
c.appendleft("python")
print(c)
c.pop()
print(c)
c.popleft()
print(c)

a = {1: "edureka", 2: "python"}
b = {3: "ML", 4: "AI"}
a1 = ChainMap(a, b)
print(a1)

a = [2, 4, 2, 2, 1, 3, 123, 4, 2, 3, 4, 5, 3, 4, 4, 5, 4]
c = Counter(a)

print(c)
# print(list(c.elements()))
print(c.most_common())
sub = {5: 1, 123: 1}
print(c.subtract(sub))
print(c.most_common())

d = OrderedDict()
d[1] = "e"
d[2] = "d"
d[3] = "u"
d[4] = "r"
d[5] = "e"
d[6] = "k"
d[7] = "a"
print(d)
print(d.keys())
print(d.values())
d[1] = "p"
print(d)

d = defaultdict(int)
d[1] = 123
d[2] = 456
print(d)
print(d[3])
a = {1: 123, 2: 456}
print(a[3])
