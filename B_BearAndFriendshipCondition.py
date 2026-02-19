import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        g[a].append(b)
        g[b].append(a)

    dead = [False] * n
    size = [0] * n
    ans = 0

    f = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            f[i][j] = (i + j + k - 1) // k

    def calc_size(root):
        stack = [(root, -1)]
        order = []
        parent = {}
        while stack:
            u, p = stack.pop()
            parent[u] = p
            order.append(u)
            for v in g[u]:
                if v != p and not dead[v]:
                    stack.append((v, u))
        for u in reversed(order):
            sz = 1
            for v in g[u]:
                if v != parent[u] and not dead[v]:
                    sz += size[v]
            size[u] = sz
        return size[root]
    def find_centroid(root, total):
        u = root
        par = -1
        while True:
            candidate = None
            for v in g[u]:
                if v != par and not dead[v] and size[v] > total // 2:
                    candidate = v
                    break
            if candidate is None:
                return u
            par = u
            u = candidate

    def collect(root, parent, start_depth):
        nodes = []
        stack = [(root, parent, start_depth)]
        while stack:
            u, p, d = stack.pop()
            q = d // k
            r = d % k
            nodes.append((q, r))
            for v in g[u]:
                if v != p and not dead[v]:
                    stack.append((v, u, d + 1))
        return nodes

    def process(c):
        nonlocal ans
        cnt = [0] * k
        total_q = 0
        total_cnt = 0
        cnt[0] = 1
        total_cnt = 1
        for v in g[c]:
            if dead[v]:
                continue
            nodes = collect(v, c, 1)
            
            for q, r in nodes:
                contrib = total_q + total_cnt * q
                for rr in range(k):
                    if cnt[rr]:
                        contrib += cnt[rr] * f[rr][r]
                ans += contrib
            for q, r in nodes:
                cnt[r] += 1
                total_q += q
                total_cnt += 1

    def decompose(start):
        total = calc_size(start)
        c = find_centroid(start, total)
        process(c)
        dead[c] = True
        for v in g[c]:
            if not dead[v]:
                decompose(v)

    decompose(0)
    print(ans)

if __name__ == "__main__":
    solve()
