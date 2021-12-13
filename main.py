data = [0, 2, 1, 4, 5, 0, 9, 4, 3, 2, 1, 6]
res = []
check = {
    0: 1,
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7: 0,
    8: 2,
    9: 1
}

for i in data:
    if i == 8:
        res.append(i)
        data.remove(i)
        
for i in data:
    if i == 9:
        res.append(i)
        data.remove(i)

for i in data:
    if i == 6:
        res.append(i)
        data.remove(i)

for i in data:
    if i == 4:
        res.append(i)
        data.remove(i)
        
for i in data:
    if i == 0:
        res.append(i)
        data.remove(i)
        
data.sort()

print(res[::-1] + data)