from collections import deque

class A: 
    def __init__(s,n,p,a,d=[]): s.n,p,s.a,s.d=n,set(p),set(a),set(d)
    def apply(s,state): return (state - s.d) | s.a

def plan(init,acts,goal):
    q,vis=deque([(init,[])]),{frozenset(init)}
    while q:
        s,p=q.popleft()
        if goal<=s: return p
        for a in acts:
            if a.n<=s:
                ns=frozenset(a.apply(s))
                if ns not in vis: vis.add(ns); q.append((ns,p+[list(a.a)]))
    return None

init=frozenset({"onA_table","clearA","onB_table","clearB"})
acts=[A(frozenset(["onA_table","clearA"]),["holdingA"],["onA_table","clearA"]),
      A(frozenset(["holdingA","clearB"]),["onA_B"],["holdingA","clearB"])]
goal=frozenset(["onA_B"])
print("Plan:", plan(init,acts,goal))