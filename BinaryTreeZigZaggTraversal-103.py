# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        stack = []
        stack.append(root)
        flag = 1
        temp = []
        while len(stack) > 0:
            nodes = len(stack)
            for i in range(nodes):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ret.append(temp[::flag])
            flag *= -1
            temp.clear()
        return ret
                
            
        
        