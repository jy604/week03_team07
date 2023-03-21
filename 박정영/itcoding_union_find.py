# 기본적인 서로소 집합 알고리즘
# input
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# output
# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 2 1 5 5

# 특정 원소가 속한 집합 찾기 - find
# 경로 단축 기법(부모 찾기를 재귀적으로 호출하는 것)
# 거쳐거쳐서 가지 않고 바로 부모 노드를 찾아줌 >> 시간복잡도 개선됨
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 모든 루트를 확인하기때문에 최악의 경우 O(vm)만큼 동작함 >> 경로 압축 기법 사용
# def find_parent(parent, x):
#     # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# 두 원소가 속한 집합을 합치기 - union
def union_parent(parent, a, b):
    a = find_parent(parent, a) # 부모 찾음
    b = find_parent(parent, b)
    # 부모가 더 작은 노드를 가르키도록 연결
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

