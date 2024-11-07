import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    
    def best_first_search(self, start, goal, heuristic):
        
        open_list = []
        heapq.heappush(open_list, (heuristic[start], start)) 
        
        visited = set()
        path = []
        
        while open_list:
            current = heapq.heappop(open_list)[1]
            
            if current == goal:
                print("Goal reached using Best-First Search.")
                return path
            
            visited.add(current)
            path.append(current)
            
            for neighbor, cost in self.graph[current]:
                if neighbor not in visited:
                    heapq.heappush(open_list, (heuristic[neighbor], neighbor))
        
        print("Goal not reachable using Best-First Search.")
        return path
    
    
    def a_star_search(self, start, goal, heuristic):
        open_list = []
        heapq.heappush(open_list, (heuristic[start], start))  
        
        g_cost = {start: 0}  
        came_from = {}
        path = []
        
        while open_list:
            current = heapq.heappop(open_list)[1]
            
            if current == goal:
                print("Goal reached using A* Search.")
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            
            for neighbor, cost in self.graph[current]:
                tentative_g = g_cost[current] + cost
                
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + heuristic[neighbor]
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current
        
        print("Goal not reachable using A* Search.")
        return path

g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 1)

heuristic = {
    1: 4,
    2: 2,
    3: 1,
    4: 0
}

start_node = 1
goal_node = 4

algorithm_choice = input("Choose algorithm (1 for Best-First, 2 for A*): ")

if algorithm_choice == '1':
    result = g.best_first_search(start_node, goal_node, heuristic)
elif algorithm_choice == '2':
    result = g.a_star_search(start_node, goal_node, heuristic)
else:
    print("Invalid choice.")

print("Path:", result)