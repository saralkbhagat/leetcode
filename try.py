class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# root = Node(1)
# root.left = Node(2)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(3)
# root.left.left.left = Node(4)
# root.left.left.right = Node(4)
root = Node(1)
root.left = Node(2)

root.left.left = Node(3)



flag=True

h=None

count=10


def height(root):
    global count
    global h
    
    
    global flag
    
    
    if root is None:
        
        # print("None root")
        return 0
    hleft= height(root.left)
    print("qqqqqqqqqqq",root.data,hleft)
    hright=height(root.right)
    count=count+(hleft+1*100)
    print("count",count)
   
    
    
    print("xxxxxxxxxxxxxxx",root.data, h)
    h = hleft + hright + 1
    print("oooooooooo",root.data, h)

    if root.left and root.right is None:
        print(root.left)
        
        h=0
        for i in range(3):
            print("saral",root.data,i,end="  ")
        
    print("here",root.data,h)    
        
    print(root.data, h,"  l r",hleft,hright)
    
    if abs(hleft-hright)>1:
        flag=False
    

    return h
height(root)
print(flag)

