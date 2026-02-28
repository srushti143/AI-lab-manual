import numpy as np

def f(x): return -x**2 + 5
def neigh(x, s=0.1): return [x+s, x-s]

x = 2.0
for i in range(100):
    n = neigh(x)
    best = max(n, key=f)
    if f(best) > f(x):
        x = best
        print(f"Step {i+1}: x={x:.4f}, f(x)={f(x):.4f}")
    else:
        print("Converged"); break

print(f"\nBest x={x:.4f}, f(x)={f(x):.4f}")