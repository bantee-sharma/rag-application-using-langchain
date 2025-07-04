

d = [
    {"fruits": ["apple", "banana", "cherry"],
    "price":[100, 200, 300]}
]

s = 0
for i in d:
    s = s + i["price"]
    print(s)