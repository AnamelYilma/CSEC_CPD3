def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            component = [i]
            
            while queue:
                current = queue.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        component.append(neighbor)
            
            edges = 0
            for node in component:
                edges += len(graph[node])
            edges //= 2
            
            k = len(component)
            if edges != k * (k - 1) // 2:
                print("NO")
                return
    
    print("YES")

if __name__ == "__main__":
    solve()
