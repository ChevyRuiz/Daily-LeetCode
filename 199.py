from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)
        
        rightSideValues = []
        while len(queue) > 0:
            stack = []
            for i in range(len(queue)):
                curr = queue.popleft()
                stack.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            rightSideValues.append(stack.pop())

        return rightSideValues
