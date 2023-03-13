import sys
input = sys.stdin.readline

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
N = int(input())
M = list(map(int, input().split()))

allParent = []
for m in M:
    parent = [i for i in range(N+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if a > b: a, b = b, a

        if findParent(parent, a) != findParent(parent, b):
            unionParent(parent, a, b)
    allParent.append(parent)

allParent.sort()

# 처리
print(*allParent)

# if findParent(parent, n):

# 출력
'''
N^2 -> N

'''