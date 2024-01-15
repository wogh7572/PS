from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
pos = []
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)
cnt = 0

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    queue = deque([[x,y]])
    cand = []
    visited[x][y] = 1
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            nx, ny = i + dx[idx] , j + dy[idx]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and visited[nx][ny] == 0:
                if space[x][y] > space[nx][ny] and space[nx][ny] != 0:
                    visited[nx][ny] =  visited[i][j] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif space[x][y] == space[nx][ny]:
                    visited[nx][ny] =  visited[i][j] + 1
                    queue.append([nx,ny])
                elif space[nx][ny] == 0:
                    visited[nx][ny] =  visited[i][j] + 1
                    queue.append([nx,ny])                    
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))

i, j = pos
size = [2, 0]
while True:
    space[i][j] = size[0]
    cand = deque(bfs(i,j))   
    if not cand:
        break    
    step, nx, ny = cand.popleft()
    cnt += step
    size[1] += 1  
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    space[i][j] = 0
    i, j = nx, ny       
print(cnt)
