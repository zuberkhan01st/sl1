def selection_sort(arr):
    n = len(arr)
    
    for i in range(0,n):
        
        min= i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        
        temp= arr[min]
        arr[min]=arr[i]
        arr[i]=temp
    
    for k in range(0,n):
        print(arr[k],end=" ")
        
arr=[2,3,1]

selection_sort(arr)


#Prims
import heapq

def prim_mst(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]  # (cost, vertex)
    total_cost = 0

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
    return total_cost


#Kruskals Algorithm
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def kruskal_mst(graph, vertices):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    while e < vertices - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    return result

#Dijkrits Algo
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    min_heap = [(0, start)]  # (distance, vertex)

    while min_heap:
        dist, u = heapq.heappop(min_heap)
        if dist > distances[u]:
            continue

        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(min_heap, (distances[v], v))
    return distances


            