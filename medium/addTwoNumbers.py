### Don't fully understand the solution – revisit when you have time

import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list with n nodes
def create_linked_list(n):
    head = None
    for i in range(n):
        val = random.randint(0, 9)  # Generate a random non-zero, positive integer
        # If it's the first node and the value is zero, regenerate the value until it's not zero
        while i == 0 and val == 0:
            val = random.randint(0, 9)
        if not head:  # If the linked list is empty (head is None)
            head = ListNode(val)  # Assign the value of the first node
            tail = head  # The tail and the head nodes are the same (as there is only one node)
        else:
            tail.next = ListNode(val)
            tail = tail.next
    return head

def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next

# Function to count the number of nodes in a linked list
def count_nodes(head):
    count = 0
    current_node = head
    while current_node is not None:
        count += 1
        current_node = current_node.next
    return count

''' The above functions were used to understand how linked lists work '''

def rev_num_array_from_ll(head):
    i = 0
    num_array = []
    current_node = head
    while current_node is not None:
        num_array.append(current_node.val)
        current_node = current_node.next
        i += 1
    rev_num_array = num_array[::-1]
    return rev_num_array

def rev_sum_of_arrays(a1, a2):
    sum = 0
    int1 = int(''.join(map(str, a1)))
    int2 = int(''.join(map(str, a2)))
    sum = int1 + int2
    array_sum = [int(digit) for digit in str(sum)]
    return array_sum[::-1]

# Function to create a linked list with n nodes
def create_ll_from_array(array):
    head = None
    for i in range(len(array)):
        val = array[i]
        if not head:  # If the linked list is empty (head is None)
            head = ListNode(val)  # Assign the value of the first node
            tail = head  # The tail and the head nodes are the same (as there is only one node)
        else:
            tail.next = ListNode(val)
            tail = tail.next
    return head

# Solving the problem:
# – Need a function that goes through each node of a linked list and stores the value in an array
# – Reverse the array
# – Perform addition
# – Need another function that converts values stored in an array and returns a linked list

# Create two linked lists with 3 and 2 nodes
l1 = create_linked_list(3)
l2 = create_linked_list(2)

print("Linked List 1:")
print_linked_list(l1)
print("\nLinked List 2:")
print_linked_list(l2)

a1 = rev_num_array_from_ll(l1)
a2 = rev_num_array_from_ll(l2)
rev_a1_plus_a2 = rev_sum_of_arrays(a1, a2)
print("\nSum of LL1 & LL2, Reversed:")
# print(rev_a1_plus_a2)
rev_sum_ll = create_ll_from_array(rev_a1_plus_a2)
print_linked_list(rev_sum_ll)