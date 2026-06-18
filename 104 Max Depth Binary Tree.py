#Mauricio Garcia

# Mauricio Garcia
# Initial recursive solution using DFS.
# I understood the recursive approach conceptually, but I wanted to challenge myself
# by implementing an iterative BFS solution to strengthen my understanding of tree
# traversal and level-order processing.
#Both works perfectly


#class Solution:
#    def maxDepth(self, root: Optional[TreeNode]) -> int:
#        if root is None:
#            return 0
#        else:
#            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
###################################################### End of this             
            
# Mauricio Garcia
# Implemented an iterative BFS solution for learning purposes.
# Although the recursive DFS approach is more concise, I chose BFS to better
# understand level-order traversal, queue operations, and how tree depth can be
# computed one level at a time. This implementation was significantly more
# challenging, but working through it helped reinforce the underlying concepts.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     




        if root is None:
            return 0
        else:
            level = 0 #initializing the level
            q = deque([root])       #we call deque and put root in it

            while q:                #while q exists,  We take a "picture" of the Q at this moment with this loop     
                for i in range(len(q)): # everytime we finish this loop, we know we have traveled 1 level, out goal is to remove
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1
            return level

