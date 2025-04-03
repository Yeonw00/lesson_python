d = {'x': 100, 'y': 200}

# key만 나옴
for v in d:
    print(v)

# dict_items([('x', 100), ('y', 200)])
print(d.items())

for k, v in d.items():
    print(k, ':' ,v)