nodes=int(input("enter no.of nodes in graph")) 
g=[]
d={}
va={}
for i in range(nodes):
    node=[]
    valu=[]
    n=int(input("enter the particular node"))
    a=int(input("enter the no.of adjacents for given node"))
    for j in range(a):
        b=int(input("enter the adjacent node"))
        v=int(input("enter the adjacent value"))
        node.append(b)
        valu.append(v)
    d[n]=node
    va[n]=valu
start=int(input("enter the start node"))
final=[]
finalvalue=[]
g.append(start)
def find(start,final,g):
    flag=False
    for j in d[start]:
        if j not in g:
                g.append(j)
                flag=True
        if(flag):
            flag=False
            final,g=find(j,final,g)
    if(flag==False):
        if len(g)==nodes:
            h=g[:]
            h.append(1)
            final.append(h)
        g=g[:-1]
        return final,g
    return final,g
final,g=find(start,final,g)
for i in final:
    sum=0
    for j in range(0,nodes):
        k=d[i[j]].index(i[j+1])
        sum+=va[i[j]][k]
    
    finalvalue.append(sum)
#print(finalvalue)
m=min(finalvalue)
print("optimum path")
for i in range(0,len(finalvalue)):
    
    if finalvalue[i]==m:
       print(final[i],'Total path cost',m)
print("Total paths",len(final))
for i in range(0,len(final)):
    print(i+1,'.',final[i],'Total path cost',finalvalue[i])