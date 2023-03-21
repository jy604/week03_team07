# 최소 스패닝 트리
# 1. find 2. union 3. 정렬 후 비교
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    # 부모 노드가 아니면, 부모 노드 찾을 때까지 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선 리스트, 최종 가중치
edges = []
result = 0

v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# # 부모 테이블 상에서, 부모를 자기 자신으로 초기화 ##
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split()) # c는 cost
    edges.append((c, a, b)) # 가중치 기준 정렬

# 간선 비용순으로 정렬
edges.sort()

# 간선 하나씩 확인
for edge in edges:
    c, a, b = edge
    # 사이클이 아닐 경우
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(a, b) # 합집합
        result += c

print(result)


