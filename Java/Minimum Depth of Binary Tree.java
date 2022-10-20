public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(n)
     */
    public int minDepth(TreeNode root) {
        if (root == null)
            return 0;

        int leftDepth = minDepth(root.left), rightDepth = minDepth(root.right);
        int min = Math.min(leftDepth, rightDepth);

        return 1 + (min > 0 ? min : Math.max(leftDepth, rightDepth));
    }
}
