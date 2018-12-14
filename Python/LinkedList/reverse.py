# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

    def reverse(self,head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(4)
    a.next = b
    b.next = c
    d = a.reverse(a)
    while d:
        print d.val
        d = d.next
