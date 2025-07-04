


s = ["words","python","java","c++","javascript","ruby","php","swift","kotlin","typescript"]


def func(s):
    new = []
    for i in s:
        if len(i) == len(set(i)):
            new.append(i)
    return new

print(func(s))