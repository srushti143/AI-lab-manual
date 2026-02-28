import numpy as np, random

n_states, n_actions, goal = 5, 2, 4
Q = np.zeros((n_states, n_actions))
alpha, gamma, epsilon, episodes = 0.1, 0.9, 0.2, 500

for _ in range(episodes):
    s = 0
    while s != goal:
        a = random.randint(0,1) if random.random() < epsilon else np.argmax(Q[s])
        ns = s+1 if a==1 else max(0, s-1)
        r = 10 if ns==goal else -1
        Q[s,a] += alpha * (r + gamma * np.max(Q[ns]) - Q[s,a])
        s = ns

print("Learned Q-table:")
print(np.round(Q, 2))