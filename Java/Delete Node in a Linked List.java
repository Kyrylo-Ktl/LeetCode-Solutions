public class Solution {

    /**
     * Time:   O(1)
     * Memory: O(1)
     */
    public void deleteNode(ListNode node) {
        node.val  = node.next.val;
        node.next  = node.next.next;
    }
}
