'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dummy = ListNode()

        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
                print('c1:', cur.val)
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                print('c2:', cur.val)
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            print('c3:', cur.next.val)

        current_node = dummy.next
        while current_node:
            print(current_node.val)
            current_node = current_node.next
        return dummy.next
    
    def create_linked_list_from_list(self, lst):
        # Initialize the head and tail pointers as None
        head = tail = None

        # Iterate through the list in reverse order to create the linked list
        for val in lst:
            # Create a new node with the current value
            new_node = ListNode(val)

            # If the linked list is empty, set the new node as the head and tail
            if not head:
                head = tail = new_node
            else:
                # Otherwise, set the next pointer of the current tail to the new node
                tail.next = new_node
                # Update the tail pointer to the new node
                tail = new_node

        return head


l1 = [1, 4, 6]
l2 = [1, 3, 5]

l1 = Solution().create_linked_list_from_list(l1)
l2 = Solution().create_linked_list_from_list(l2)

# current_node = head_node
# while current_node:
#     print(current_node.val)
#     current_node = current_node.next

print('Res:')
current_node = Solution().mergeTwoLists(l1, l2)

# while current_node:
#     print(current_node.val)
#     current_node = current_node.next