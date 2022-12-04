# Unsolved

import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self, data):
        self.head = Node(None)
        self.start = Node(data)
        self.head.next = self.start
        self.start.prev = self.head
        self.cursor = self.start

    def append(self, data):
        new_node = Node(data)
        if self.cursor == self.head:
            new_node.prev = self.head
            new_node.next = self.cursor.next
            self.start = new_node
            self.head.next = self.start
        else:
            new_node.prev = self.cursor
            new_node.next = self.cursor.next
            self.cursor.next = new_node
            self.cursor = new_node

    def get_node(self, idx):
        if idx == 0:
            return self.start

        cur_idx = 0
        cur_node = self.start

        while cur_idx < idx:
            cur_idx += 1
            cur_node = cur_node.next

        return cur_node

    def print(self):
        cur = self.start

        while cur is not None:
            print(cur.data, end='')
            cur = cur.next
        print()

    def cursor_move_left(self):
        if self.cursor == self.head:
            return
        self.cursor = self.cursor.prev

    def cursor_move_right(self):
        if self.cursor.next is None:
            return
        self.cursor = self.cursor.next

    # def delete(self):
    #     if self.cursor == self.head:
    #         return

    #     self.cursor.prev


s = list(input().rstrip())
my_list = LinkedList(s[0])

for data in s[1:]:
    my_list.append(data)

my_list.print()
my_list.cursor_move_left()
my_list.append('1')
my_list.cursor_move_left()
my_list.append('2')
my_list.cursor_move_left()
my_list.cursor_move_left()
my_list.append('3')
my_list.cursor_move_left()
my_list.cursor_move_left()
my_list.append('4')
my_list.print()
my_list.cursor_move_left()
my_list.cursor_move_left()
my_list.cursor_move_left()
my_list.append('5')
my_list.print()

# for _ in range(int(input().rstrip())):
#     commands = list(input().rstrip().split())

#     command = commands[0]

#     if command == 'L':
#         my_list.cursor_move_left
#     elif command == 'D':
#         my_list.cursor_move_right
#     elif command == 'B':
#         pass
#     elif command == 'P':
#         my_list.append(commands[1])