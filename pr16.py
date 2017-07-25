a = str(2 ** 1000)
s = 0

for x in range(0, len(a)):
    s += int(a[x])

print(s)