# find Node in Linked list
# 基于ListNode 实现一个Linked List
# create：add(location, val)
# read: get(location)
# update: set(location,val)
# remove: remove(location)

class ListNode:
    def __init__(self, val):
        self.val = val

        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None

    # add a new node to a given location
    def add(self, location, val):
        new_node = ListNode(val)
        if location > 0:
            pre = self.head
            for i in range(location - 1):
                pre = pre.next
            new_node.next = pre.next
            pre.next = new_node
        elif location == 0:
            new_node.next = self.head
            self.head = new_node

    def get(self, location):
        cur = self.head
        for i in range(location):
            cur = cur.next
        return cur.val

    def set(self, location, val):
        cur = self.head
        for i in range(location):
            cur = cur.next
        cur.val = val

    def remove(self, location):
        if location > 0:
            pre = self.head
            for i in range(location - 1):
                pre = pre.next

            pre.next = pre.next.next

        elif location == 0:
            self.head = self.head.next

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end=" ")
            cur = cur.next
    def is_empty(self):
        return self.head is None

if __name__ == '__main__':
    linked_list = MyLinkedList()
    linked_list.add(0,2) # 2-> None
    linked_list.add(0,3) # 3->2-> None
    linked_list.add(1,7) # 3->7->2->None
    linked_list.add(1,9) # e->9->7->2->None
    linked_list.traverse()
    print()
    linked_list.set(0,3)
    linked_list.traverse()
    linked_list.remove(1)
    linked_list.traverse()