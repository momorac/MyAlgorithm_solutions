def dfs(cur) :          # 현재위치(cur)에서 깊이우선 탐색
    visited[cur] = 1    # 현재 위치 방문표시 (중복방문 방지)

    # 첫 방문시 해야할 일

    # 연결된 노드 4방향
    for next in adj[cur]:
        # 범위 내, 미방문, 조건에 맞으면 dfs 호출
        if visited[next] == 0:
            dfs(next)

# N : 노드의 개수 / M: 간선의 개수 / V: 시작할 노드
n = int(input())
m = int(input())

# 인접리스트 생성
adj = [[] for _ in range(n+1)]

# M개의 링크 정보 입력받기
for i in range(m):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

# 노드의 방문 여부 저장할 리스트 선언
visited = [0] * (n+1)

count = 0
dfs(1)

print(sum(visited)-1)