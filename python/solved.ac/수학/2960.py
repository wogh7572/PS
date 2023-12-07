def is_prime(n):
    if n<2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n, k = map(int, input().split())
visited = [0 for i in range(n+1)]
flag = False
while True:
    for i in range(2, n+1):
        if is_prime(i):
            for j in range(i, n+1, i):
                if visited[j]==0:
                    k-=1
                    visited[j]=1
                    if k==0:
                        print(j)
                        flag=True
                        break
    if flag:
        break
    visited = [0 for i in range(n+1)]
