import sys
sys.stdin=open("week03\input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(k, count) :
    visited[k] = 1
 
    for i in tree[k] :
        if A[i] == 1 :
            count += 1
 
        elif A[i] == 0 and not visited[i] :
            count = dfs(i, count)           # 재귀 함수의 return 값을 변수에 저장
                                            # if 문에서 update된 count 변수가 인수로 들어감
    return count
 
 
N = int(input())
 
A = [0] + list(map(int, input().strip()))
 
tree = [[] for _ in range(N + 1)]
 
 
case1 = 0
 
for _ in range(N - 1) :
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
 
    if A[u] == 1 and A[v] == 1:
        case1 += 2
 
visited = [0] * (N + 1)
 
 
case2 = 0
 
for j in range(1, N + 1) :
    if A[j] == 0 and not visited[j] :
        res = dfs(j, 0)                     # 다른 실외 노드의 인접한 실내 노드를 찾는 것이므로 0부터 다시 시작
        case2 += res * (res - 1)            # 인접한 실내 노드를 모두 찾았을 때마다 계산해주어야 함
 
path = case1 + case2
 
print(path)