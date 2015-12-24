__author__ = 'lixianpeng'


import treeutils


"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        vals = []
        self.level_traversal(root, vals, 1)
        return vals


    def level_traversal(self, node, vals, height):
        if not node:
            return
        if (height > len(vals)):
            vals.append([])
        vals[height - 1].append(node.val)
        height += 1
        self.level_traversal(node.left, vals, height)
        self.level_traversal(node.right, vals, height)


node1 = treeutils.TreeNode(3)
node2 = treeutils.TreeNode(9)
node3 = treeutils.TreeNode(20)
node4 = treeutils.TreeNode(15)
node5 = treeutils.TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

solution = Solution()
print(solution.levelOrder(node1))

