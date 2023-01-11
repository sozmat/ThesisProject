import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_insert(self):
        """Required TestCase #2: Check that an IndexError is raised when inserting into a full heap"""
        print("\n")
        print("Checking if IndexError is raised when inserting into full heap")
        mh = mheap.max_heap(2)
        mh.insert(3)
        mh.insert(4)
        with self.assertRaises(IndexError):
            mh.insert(5)
        print("\n")

    def test_3_pq_insert(self):
        """Additional TestCase #1: Checks to see if None is retained when not all spots in heap are filled"""
        print("\n")
        pq = pqueue.pqueue(4)
        pq.insert(2)
        pq.insert(5)
        pq.insert(3)
        pq_list = [element for element in pq]
        self.assertEqual(pq.get_pqueue(), [5, 2, 3, None])

    def test_4_pq_insert(self):
        """Additional TestCase #2: Checks if heap properties still hold after insertion of ints in random order"""
        print("\n")
        pq = pqueue.pqueue(9)
        pq.insert(4)
        pq.insert(10)
        pq.insert(3)
        pq.insert(37)
        pq.insert(7)
        pq.insert(57)
        pq.insert(24)
        pq.insert(67)
        pq.insert(87)
        pq_list = [element for element in pq]
        self.assertEqual(pq.get_pqueue(), [87, 67, 37, 57, 7, 3, 24, 4, 10])

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

    def test_t2_pq_peek(self):
        """Additional TestCase #5: Checks if peeking on an empty heap is None"""
        print("\n")
        pq = pqueue.pqueue(3)
        self.assertEqual(pq.peek(), None)

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max(self):
        """Required TestCase #3: Check that a KeyError is raised when extract_max() is called on an empty heap"""
        print("\n")
        mh = mheap.max_heap()
        with self.assertRaises(KeyError):
            mh.extract_max()
        print("\n")

    def test_3_pq_extract_max(self):
        """Required TestCase #4: Check that an object of pqueue is still a valid maximum heap after calling insert()
        and extract_max() on the same pqueue object"""
        print("\n")
        pq = pqueue.pqueue(4)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.extract_max()
        pq.extract_max()
        self.assertEqual(pq.get_pqueue(), [2, 1, None, None])
        print("\n")

class T4_test_build_heap(unittest.TestCase):

    def test_build_heap_1(self):
        """Required TestCase #1: Check that build_heap() properly builds a max heap"""
        print("\n")
        list_to_heap = [18, 20, 30, 17, 50]
        mh = mheap.max_heap(len(list_to_heap), list_to_heap)
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [50, 20, 30, 17, 18])

    def test_build_heap_2(self):
        """Additional TestCase #3: Tests to see that build heap properly applies heap properties, more swaps required than above example"""
        print("\n")
        list_to_heap = [5, 15, 3, 20, 6, 17, 2]
        mh = mheap.max_heap(len(list_to_heap), list_to_heap)
        mh.build_heap()
        self.assertEqual(mh.get_heap(), [20, 15, 17, 5, 6, 3, 2])

class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

    def test_heap_sort_2(self):
        """Additional TestCase #4: Tests to check that heap sort works"""
        print("\n")
        list_to_sort = [4, 99, 34, 57, 1, 7, 20]
        sorted = mheap.heap_sort(list_to_sort)
        self.assertEqual(sorted, [1, 4, 7, 20, 34, 57, 99])

class T7_put_it_all_together(unittest.TestCase):

    def test_everything(self):
        """Additional TestCase #6: Using insert(), extract_max(), and heap_sort() on list"""
        print("\n")
        pq = pqueue.pqueue(4)
        pq.insert(3)
        pq.insert(18)
        pq.insert(7)
        pq.extract_max()
        pq.insert(1)
        pq.insert(5)
        list = [element for element in pq]
        sorted = mheap.heap_sort(list)
        self.assertEqual(sorted, [1, 3, 5, 7])
    
if __name__ == '__main__':
    unittest.main()