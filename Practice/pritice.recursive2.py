def recursion(s):
    out = []
    
    if len(s) == 1:
        out = [s]
    else:
        for i, val in enumerate(s):
            for rec in recursion(s[:i] + s[i + 1:]):
                out += [val + rec]
    return out

a = 'abcd'

print(recursion(a))