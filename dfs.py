from collections import defaultdict;
class Graph:
    def __init__(self):
        self.graph=defaultdict(list);
        self.dfs="";
        self.found=False;
    def addEdge(self,u,v):
        self.graph[u].append(v);
    def DFS(self,root,search,visited):
        visited.add(root)
        self.dfs=self.dfs+root+" ";
        if(root==search):
            self.found=True;
            return False;
        for neighbour in self.graph[root]:
            if neighbour not in visited:
                if self.DFS(neighbour,search,visited):
                    return False;        
    def DFS1(self,root,search):
        visited=set();
        self.DFS(root,search,visited)
g=Graph();
n=int(input("enter the no.of nodes"));
root=input("enter root node")
search=input("enter search element")
print("enter the verices of tree")
for i in range(0,n-1):
    s=input();
    x=s.split(",")
    g.addEdge(x[0],x[1])
g.DFS1(root,search);
if(g.found):
    print("Following is the Depth-First Search")
    print(g.dfs);
else:
     print("given element not found in tree")