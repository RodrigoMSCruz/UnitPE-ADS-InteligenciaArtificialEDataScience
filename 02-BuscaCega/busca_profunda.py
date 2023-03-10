# Depth First-Search Algorithm

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node, finalNode):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        if(node != finalNode):
          for neighbour in graph[node]:
              dfs(visited, graph, neighbour, finalNode)

# Driver Code
print("Following is the Depth-First Search")
finalNode = input("Enter the node to find: ")
dfs(visited, graph, '5', finalNode)