class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  

# Example usage
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_node = middle_node(head)

# Print the linked list from the middle node
output_list = []
current = middle_node
while current:
    output_list.append(str(current.val))
    current = current.next

output_str = " -> ".join(output_list)
print(output_str)  # Output: 3 -> 4 -> 5
