li = []
for _ in range(10):
    li.append(int(input())%42)
li = list(set(li))
print(len(li))