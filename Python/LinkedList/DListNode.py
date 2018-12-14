# -*- coding: utf-8 -*-
class DListNode:
    def __init__(self,val):
        self.val = val
        self.prev = self.next = None

    def reverse(self,head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt


