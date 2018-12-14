# -*- coding: utf-8 -*-
class MaxHeap(object):
    def __init__(self,array = None):
        self.last = 0
        self.heap = []
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _max_heapify(self, array):
        for i in array:
            self.push(i)

    def push(self, item):
        i = self.last
        while i > 0:
            p = (i-1)/2
            if self.heap[p] >= item:
                break
            self.heap[i] = self.heap[p]
            i = p
        self.last += 1
        self.heap[i] = item

    def pop(self):
        self.last -= 1
        result = self.heap[0]
        x = self.heap[self.last]
        self.heap[self.last] = result
        i = 0
        while 2*i+1 < self.last:
            left = 2*i+1
            right = 2*i+2
            swap = left
            if right < self.last and self.heap[left] < self.heap[right]:
                swap = right
            if self.heap[swap] <= x:
                break
            self.heap[i] = self.heap[swap]
            i = swap
        self.heap[i] = x
        return result


if __name__ == '__main__':
    testList = [2,4,3,1,8,7,5,6]
    a = MaxHeap(testList)
