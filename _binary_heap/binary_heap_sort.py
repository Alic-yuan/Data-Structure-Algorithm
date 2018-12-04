from binary_heap import BinaryHeap



class BinaryHeapSort(BinaryHeap):

    def __init__(self):
        super(BinaryHeapSort, self).__init__()

    def sort(self, nums):

        assert type(nums) is list
        length = len(nums)

        if length <= 1:
            return

        self._type_assert(nums)

        self._heapify(nums, length-1)

        for i in range(length-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heap_down(nums, 0, i-1)

        return




if __name__ == '__main__':
    bhs = BinaryHeapSort()
    nums = [3, 5, 2, 6, 1, 7, 6]

    print('--- before sort ---')
    print(nums)

    bhs.sort(nums)
    print('--- after sort ---')
    print(nums)