import sys
sys.setrecursionlimit(300000)

def solve():
    n, k = map(int, sys.stdin.readline().split())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    if k == 1:
        print(n * (n - 1) // 2)
        return
    
    total = 0
    size = [0] * n
    cnt = [[0] * k for _ in range(n)]
    
    def dfs(u, p):
        nonlocal total
        size[u] = 1
        cnt[u][0] = 1
        
        for v in g[u]:
            if v == p:
                continue
            dfs(v, u)
            
            for i in range(k):
                for j in range(k):
                    dist = (i + j + 1) % k
                    if dist == 0:
                        total += cnt[u][i] * cnt[v][j]
                    else:
                        total += cnt[u][i] * cnt[v][j]
            
            for i in range(k):
                cnt[u][(i + 1) % k] += cnt[v][i]
            size[u] += size[v]
    
    dfs(0, -1)
    print(total)

if __name__ == "__main__":
    solve()
