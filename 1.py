from collections import deque

g = {1:[2,3], 2:[4], 3:[4], 4:[5]}

def dfs(u, goal, v=[], p=[]):
    v.append(u); p.append(u)
    if u==goal: return p
    for x in g.get(u,[]):
        if x not in v:
            r=dfs(x,goal,v,p)
            if r: return r
    p.pop(); return None

def bfs(s, goal):
    q=deque([(s,[s])]); v={s}
    while q:
        n,p=q.popleft()
        if n==goal: return p
        for x in g.get(n,[]):
            if x not in v: v.add(x); q.append((x,p+[x]))

print("DFS:", dfs(1,5))
print("BFS:", bfs(1,5))
