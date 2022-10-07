public class Solution {

    /**
     * Time:   O(n)
     * Memory: O(1)
     */
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast= head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next;

            if (slow == fast)
                return true;
        }

        return false;
    }
}
