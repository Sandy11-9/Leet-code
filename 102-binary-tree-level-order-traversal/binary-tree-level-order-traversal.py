from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # 2. Iterate only through the nodes belonging to this level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # 3. Add existing children to the queue for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 4. Append the completed level list to the final result
            result.append(current_level)
            
        return result