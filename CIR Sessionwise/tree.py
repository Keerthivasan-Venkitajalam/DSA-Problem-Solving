from collections import defaultdict, deque

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        graph = defaultdict(list)
        
        for __ in range(n - 1):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            
        if n == 2:
            print(1)
            continue
        
        # Find the degrees of all nodes
        degrees = [0] * (n + 1)
        for node in graph:
            degrees[node] = len(graph[node])
        
        # Count the number of leaf nodes
        leaf_count = sum(1 for deg in degrees if deg == 1)
        
        # The answer is (leaf_count + 1) // 2 + 1
        result = (leaf_count + 1) // 2 + 1
        print(result)

# Sample input simulation
if __name__ == "__main__":
    solve()
