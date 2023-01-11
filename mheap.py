class max_heap(object):
    """A Class to represent a Binary Max-Heap

    Attributes:
        size: total capacity of the heap
        data: list containing desired heap contents

    Methods:
        get_heap():
            returns the heap object
        insert():
            inserts an int into the end of the heap and ensures it
            maintains max heap properties
        peek():
            returns the value at node 0 of the heap, in our case the max value
        extract_max():
            returns and removes the max value in our binary heap, our heap is then
            rechecked/ swaps are made to ensure it maintains max heap properties
        __heapify(curr_index, list_length):
            ensures our heap still maintains heap properties within a subtree
        build_heap():
            uses heapify() function to create a heap from a given set of data
        __get_parent():
            gives us the parent of our node
        __get_left():
            returns the left child of node
        __get_right():
            returns right child of node
        __swap(a, b):
            exchanges values at location a and b in list
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap

    def insert(self, data):
        """Insert an element into the heap.
        Raises IndexError if the heap is full."""

        if self.length == self.max_size:
            raise IndexError
        else:
            self.length += 1
            # self.heap[self.max_size] = data # insert data into our last pos in list
            curr = self.length - 1
            self.heap[curr] = data
            while curr != 0 and self.heap[self.__get_parent(curr)] < self.heap[curr]:
                self.__swap(self.__get_parent(curr), curr)
                curr = self.__get_parent(curr)  # update curr variable

    def peek(self):
        """Return the maximum value in the heap."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.
        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length == 0:
            raise KeyError
        else:
            self.__swap(0, self.length - 1)
            max = self.heap[self.length - 1]
            self.heap[self.length - 1] = None
            self.length -= 1
            self.__heapify(0, self.length - 1)
        return max

    def __heapify(self, curr_index, list_length = None):
        """Ensures that our heap maintains the heap properties"""
        # Page 157 of CLRS book, following code is based off of pseudocode
        # given from this textbook
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)
        if left <= self.length-1 and self.heap[left] > self.heap[curr_index]:
            largest = left
        else:
            largest = curr_index
        if right <= self.length-1 and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, self.length)

    def build_heap(self):
        """Builds a max heap from the binary tree present in heap structure
        calls heapify in a bottom-up manner"""
        start_index = (self.length // 2) - 1
        for i in range(start_index, -1, -1):
            self.__heapify(i, self.length)

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)  #taking the floor of evaluation
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure
    mh = max_heap(len(l), l)
    mh.build_heap()
    sorted_list = [None] * len(l)
    for i in range(0, mh.length):
        sorted_list[len(l)-i -1] = mh.extract_max()
    return sorted_list



