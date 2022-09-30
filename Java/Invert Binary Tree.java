public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            TreeNode tmp = root.left;
            root.left = invertTree(root.right);
            root.right = invertTree(tmp);
        }
        return root;
    }
}
