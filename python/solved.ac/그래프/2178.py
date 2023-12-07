from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]
visited = [[0]*m for i in range(n)]
queue = deque()
queue.append((0, 0))
visited[0][0]=1
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue
        if graph[ny][nx]==1 and visited[ny][nx]==0:
            graph[ny][nx] = graph[y][x]+1
            visited[ny][nx]=1
            queue.append((ny, nx))
print(graph[n-1][m-1])