# 트리 순회
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
import sys

n = int(sys.stdin.readline().strip())
tree = {} # 딕셔너리로 선언
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


# 전위 순회 중 왼 오
def preorder(root)->None:
    if root != '.':
        print(root, end='')
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right


# 중위 순회 왼 중 오
def inorder(root)->None:
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


# 후위 순회 왼 오 중
def postorder(root)->None:
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder('A')
print()

inorder('A')
print()

postorder('A')
print()