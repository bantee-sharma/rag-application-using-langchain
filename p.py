




n = [1,2,3,4,1,2,5,6,3,8,3,6]

def func(n):
    seen = []
    s = set()
    for i in n:
        if i not in seen:
            seen.append(i)
        else:    
            s.add(i)
    return list(s)

print(func(n))