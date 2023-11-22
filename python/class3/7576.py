from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i, j])
while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[ny][nx]==0:
                graph[ny][nx]=1
                graph[ny][nx]=graph[y][x]+1
                queue.append([ny, nx])
flag=True
li=[]
for i in range(n):
    li.append(max(graph[i]))
    if 0 in graph[i]:
        flag=False
        break
if flag:
    print(max(li)-1)
else:
    print(-1)
