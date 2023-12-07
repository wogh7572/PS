from collections import deque

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
queue = deque()
cnt=0
visited = [[0]*(n) for i in range(n)]
#아기상어의 좌표
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            queue.append([i, j])

level = 2
level_point = 0

#bfs를 통해 가장 가까운 먹이를 향해 달려가고 queue를 초기화한다.
#
#bfs()
while queue:
    y, x = queue.popleft()
    for i in range(n):
        for j in range(n):
            if 0<graph[i][j]<level:
                cnt+=1
    if cnt==0:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[ny][nx]<=level:
            queue.append([ny, nx])
            visited[ny][nx] = visited[y][x]+1
            if 0<graph[ny][nx]<level:
                level_point+=1
                graph[ny][nx]=0
                if level_point==level:
                    level+=1
                    level_point=0
                queue = deque([[ny, nx]])


#bite_fish라는 함수를 정의해서 구현



for i in visited:
    print(i)