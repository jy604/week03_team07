import sys
sys.setrecursionlimit(10**6)

n = int(input())

a = input().rstrip()

graph = [[] for _ in range(n + 1)]
place = [0] * (n + 1)
visited = [0] * (n + 1)

for i in range(len(a)):
    if a[i] == '1':
        place[i + 1] = 1

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    result = 0
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                result += dfs(next_node)
        else:
            result += 1
    return result


ans = 0

for i in range(1, n + 1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            result = dfs(i)
            ans += result * (result - 1)
    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1

print(ans)