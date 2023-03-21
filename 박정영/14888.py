# 연산자 끼워넣기
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = - int(1e9)
min_result = int(1e9)
res = 0


def dfs(res, cnt):
    global max_result, min_result, add, sub, mul, div
    if cnt == n:
        max_result = max(res, max_result)
        min_result = min(res, min_result)
    if add > 0:
        add -= 1
        dfs(res + data[cnt], cnt+1)
        add += 1
    if sub > 0:
        sub -= 1
        dfs(res - data[cnt], cnt+1)
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(res * data[cnt], cnt+1)
        mul += 1
    if div > 0:
        div -= 1
        dfs(int(res / data[cnt]), cnt+1)
        div += 1


dfs(data[0], 1)
print(max_result)
print(min_result)