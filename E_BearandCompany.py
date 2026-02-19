def solve():
    n = int(input())
    s = input().strip()
    
    INF = 10**9
    v_pos = []
    k_pos = []
    o_pos = []
    
    for i, ch in enumerate(s):
        if ch == 'V':
            v_pos.append(i)
        elif ch == 'K':
            k_pos.append(i)
        else:
            o_pos.append(i)
    
    v_cnt = len(v_pos)
    k_cnt = len(k_pos)
    o_cnt = len(o_pos)
    
    dp = {}
    
    def go(i, j, l, last):
        if i == v_cnt and j == k_cnt and l == o_cnt:
            return 0
        
        key = (i, j, l, last)
        if key in dp:
            return dp[key]
        
        pos = i + j + l
        res = INF
        
        if i < v_cnt:
            cost = v_pos[i]
            for x in range(i):
                if v_pos[x] > v_pos[i]:
                    cost -= 1
            for x in range(j):
                if k_pos[x] > v_pos[i]:
                    cost -= 1
            for x in range(l):
                if o_pos[x] > v_pos[i]:
                    cost -= 1
            res = min(res, go(i + 1, j, l, 'V') + cost)
        
        if j < k_cnt and last != 'V':
            cost = k_pos[j]
            for x in range(i):
                if v_pos[x] > k_pos[j]:
                    cost -= 1
            for x in range(j):
                if k_pos[x] > k_pos[j]:
                    cost -= 1
            for x in range(l):
                if o_pos[x] > k_pos[j]:
                    cost -= 1
            res = min(res, go(i, j + 1, l, 'K') + cost)
        
        if l < o_cnt:
            cost = o_pos[l]
            for x in range(i):
                if v_pos[x] > o_pos[l]:
                    cost -= 1
            for x in range(j):
                if k_pos[x] > o_pos[l]:
                    cost -= 1
            for x in range(l):
                if o_pos[x] > o_pos[l]:
                    cost -= 1
            res = min(res, go(i, j, l + 1, 'O') + cost)
        
        dp[key] = res
        return res
    
    ans = go(0, 0, 0, '')
    print(ans)

if __name__ == "__main__":
    solve()
