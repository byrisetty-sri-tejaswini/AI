def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return

    tower_of_hanoi(n-1, source, target, auxiliary)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, source, target)

n = int(input("Enter the number of disks: "))
print("Start state:")
A=[]
for i in range(1,n+1): 
    A.append(i)
print("A:",A,"B:0 C:0")
tower_of_hanoi(n, 'A', 'B', 'C')
print("Goal state reached")
C=[]
for i in range(1,n+1):
    C.append(i)
print("A:0 B:0 C:",C)

