from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
            
        visited.add(start)
        print(start, end=" ")
        
        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i, visited)

                
    def bfs(self, start):
        visited = set()
        
        queue = [start]
        visited.add(start)
        
        while(queue):
            content = queue.pop(0)
            print(content, end=" ")
            
            for i in self.graph[content]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        
g = Graph()

n = int(input("Enter the number of edges: "))  

for i in range(0, n):
    u, v = map(int, input().split()) 
    g.add_edge(u, v)

start = int(input("Enter the starting node: "))  

g.dfs(start)  
print()  

g.bfs(start)  
