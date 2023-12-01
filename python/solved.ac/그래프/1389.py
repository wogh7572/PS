# 구현은 bfs로 다른 사람과의 거리를 각각 구한 후 합한 값을 출력하게하면 된다.
def func(v):
    print()


n, m = map(int , input().split())
graph = [[0]*(n+1) for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b]=1
    graph[b][a]=1
li = []
for i in range(1, n+1):
    func(i) #케빈베이컨의 수를 구하는 함수