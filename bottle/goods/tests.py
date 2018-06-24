a = [1, 3, 4, 5, 0, 0, 6, 6, 0, 5, 4, 7, 6, 7, 0, 5]
b = []
c = []
for item in a:
    if item not in b:
        b.append(item)
    else:
        c.append(item)
print(c)
for item in a:
    if item not in c:
        print(item)
