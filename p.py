




n = [1,2,3,4,1,2,5,6,3,8,3,6]

def func(n):
    s = set()
    for i in n:
        if i in s:
            s
    return list(s)

print(func(n))