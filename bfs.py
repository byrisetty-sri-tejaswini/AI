from collections import defaultdict;
class Graph:
    def __init__(self):
        self.graph=defaultdict(list);
        self.bfs="";
        self.found=False;
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,root,search):
        visited=[];
        queue=[];
        self.bfs="";
        visited.append(root)
        queue.append(root)
        while queue:          
            m = queue.pop(0) 
            self.bfs=self.bfs+m+" ";
            if(m==search):
                self.found=True;
                return;
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
g=Graph();
n=int(input("enter the no.of nodes"));
root=input("enter root node")
search=input("enter search element")
print("enter the verices of tree")
for i in range(0,n-1):
    s=input();
    x=s.split(",")
    g.addEdge(x[0],x[1])
g.BFS(root,search);
if(g.found):
    print("Following is the Breadth-First Search")
    print(g.bfs);
else:
     print("Given search element is not found in tree")