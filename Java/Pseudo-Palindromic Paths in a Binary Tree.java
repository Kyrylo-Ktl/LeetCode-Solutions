class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int pseudoPalindromicPaths (TreeNode root) {
        return preorder(root, 0);
    }

    public int preorder(TreeNode node, int path) {
        if (node == null)
            return 0;

        path = path ^ (1 << node.val);
        if (node.left == null && node.right == null)
            if ((path & (path - 1)) == 0)
                return 1;

        return preorder(node.left, path) + preorder(node.right, path);
    }
}
