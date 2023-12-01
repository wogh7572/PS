from collections import deque
def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v]=1
    for i in range(1, n+1):
        if graph[v][i]==1 and visited[i]==0:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v]=0
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i]==1 and visited[i]==1:
                queue.append(i)
                visited[i]=0


n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(graph, v, visited)
print()
bfs(graph, v, visited)