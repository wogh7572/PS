n, m = map(int, input().split())
graph = [input() for i in range(n)]
re_m = 2500
for i in range(n-7):
    for j in range(m-7):
        cnt=0
        for y in range(8):  
            for x in range(8):
                b, a = i+y, j+x
                if (b+a)%2==0:
                    if graph[b][a]=='W':
                        cnt+=1
                else:
                    if graph[b][a]=='B':
                        cnt+=1
        re_m = min(re_m, cnt, 64-cnt)
print(re_m)