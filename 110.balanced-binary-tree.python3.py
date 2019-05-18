
class Solution:
    def isBalanced(self, root):
        h=0
        def height(root):

            if root.left and root.right is None:
                return -1
            h=height(root.left)+height(root.right)+1
            
        
    




        


        

