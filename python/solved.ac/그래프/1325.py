#나중에 답 보고 학습하자

from collections import deque
n, m = map(int, input().split())
graph = [[0] for i in range(n+1)]
# graph[a][b] : a -> b (a가 b를 신뢰한다 -> b를 해킹하면 a가 공짜)
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
cnt_m=0
li=[]
for i in range(1, n+1):
	if graph[i]:
		queue=deque([i])
		visited=[0]*(n+1)
		visited[i]=1
		while queue:
			v = queue.popleft()
			for j in range(1, n+1):
				if j in graph[v] and visited[j]==0:
					visited[j]=1
					queue.append(j)
		cnt = sum(visited)
		if cnt > cnt_m:
			cnt_m = cnt
			li = [i]
		if cnt == cnt_m:
			li.append(i)
print(li)
    