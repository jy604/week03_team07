import sys
sys.stdin=open("week03\input.txt", "rt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))  

min_num = 1e9
max_num = -1e9


def dfs(a, now):
    global min_num, max_num

    if a == n:
        min_num = min(min_num, now)
        max_num = max(max_num, now)
        return
    
    if cal[0] > 0:
        cal[0] -= 1
        dfs(a+1, now+nums[a])
        cal[0] += 1

    if cal[1] > 0:
        cal[1] -= 1
        dfs(a+1, now-nums[a])
        cal[1] += 1

    if cal[2] > 0:
        cal[2] -= 1
        dfs(a+1, now*nums[a])
        cal[2] += 1

    if cal[3] > 0:
        cal[3] -= 1
        if now < 0:
            dfs(a+1, -(-now//nums[a]))
        else:
            dfs(a+1, now//nums[a])
        cal[3] += 1

dfs(1, nums[0])
print(max_num)
print(min_num)
