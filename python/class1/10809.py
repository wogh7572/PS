s = input()
li = [-1 for i in range(26)]
for idx, chr in enumerate(s):
    c = ord(chr)-97
    if li[c]==-1:
        li[c]=idx
print(li)