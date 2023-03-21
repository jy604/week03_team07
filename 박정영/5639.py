# 재귀 이해 못함....
# import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break


def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end) #오른쪽 트리
    print(pre[start]) #루트 노드


# post(0, len(pre) - 1)

# 왼쪽 오른쪽 나눠서 새로운 배열 만들어서 돌리는 방법
# 메모리, 시간 더 걸리지만 직관적임 >> 백준에서 시간초과 남
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# num = []
#
# # 입력을 언제까지 받는지 모르기 때문에 try ~ except문 사용
# # 입력이 없으면 while문 탈출함
# while True:
#     try:
#         n = int(input())
#         num.append(n)
#     except:
#         break
#
#
# def postorder(num):
#     if len(num) == 0: # 받은 배열 길이가 0이면 return
#         return
#     root = num[0] # 전위는 가장 처음이 루트
#     left = []
#     right = []
#
#     # 루트를 제외한 배열에서 루트보다 커지는 부분을 기록해서 left, right를 나눔
#     for i in range(1, len(num)):
#         if num[i] > root:
#             left = num[1:i]
#             right = num[i:]
#             break
#         else: # 왼쪽으로 쭉 뻗는 트리 > 모두 왼쪽 노드
#             left = num[1:]
#
#     postorder(left)
#     postorder(right)
#     print(root)
#
#
# postorder(num)
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
# node = []
# while True:
#     try:
#         node.append(int(input()))
#     except:
#         break
#
#
# def postorder(start, end):


