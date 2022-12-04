class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# 단방향 연결리스트
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def get_node(self, idx):
        cur_idx = 0
        cur_node = self.head

        while cur_idx < idx:
            cur_idx += 1
            cur_node = cur_node.next
        return cur_node

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = Node(data)

    def insert(self, idx, data):
        node = Node(data)
        if idx == 0:
            node.next = self.head
            self.head = node
            return

        cur_idx = 0
        cur_node = self.get_node(idx)
        node.next = cur_node
        self.get_node(cur_idx - 1).next = node

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def size(self):
        cur = self.head
        size = 0
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next
            return

        node = self.get_node(idx - 1)
        node.next = node.next.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print()  # 1 2 3
print(linked_list.size())  # 3
linked_list.insert(1, 5)
linked_list.print()  # 1 5 2 3
print(linked_list.size())  # 4
linked_list.insert(0, 9)
linked_list.print()  # 9 1 5 2 3
linked_list.append(7)
linked_list.print()  # 9 1 5 2 3 7
linked_list.insert(0, 10)
linked_list.print()  # 10 9 1 5 2 3 7
linked_list.delete(0)  # 9 1 5 2 3 7
linked_list.print()
linked_list.delete(3)
linked_list.print()  # 9 1 5 3 7
print(linked_list.size())  # 5
