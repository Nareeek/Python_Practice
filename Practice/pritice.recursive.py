from pprint import pprint

a = [1, 2, 3, 4]

def rec(s):
   if len(s) == 1:
     return [s]

   r_l = [] # resulting list
   for x in s:
     rem_el = [y for y in s if y != x]
     z = rec(rem_el) # sublist

     for t in z:
       r_l.append([x] + t)

   return r_l


a = rec(a)
pprint(a)