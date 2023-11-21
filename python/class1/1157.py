s = input().upper()
li = [0 for i in range(26)]
for i in s:
    x = ord(i)
    li[x-65]+=1
max_n = max(li)
flag = 0
for i in range(26):
    if max_n==li[i]:
        flag+=1
        idx=i
if flag==1:
    print(chr(idx+65))
else:
    print("?")

