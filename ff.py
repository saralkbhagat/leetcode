class Node:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
d={}
v=0
count=0

def travel(root,v):
    global count
    print("loop count", count)
    count+=1
    if root is None:
        return
    travel(root.left,v-1)
    # print(root.val,v)
    try:
        d[v].append(root.val)
    except:
        d[v]=[root.val]
    travel(root.right,v+1)

travel(root,v)
print(d)


    


