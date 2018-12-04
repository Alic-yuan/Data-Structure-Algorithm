import random
from heap import MinHeap



def top_k(nums, k):

    if len(nums) <= k:
        return nums

    min_h = MinHeap(nums[:k], k)
    for i in range(k, len(nums)):
        tmp = min_h.get_top()
        if nums[i] > tmp:
            min_h.remove_top()
            min_h.insert(nums[i])

    return min_h.get_data()



if __name__ == '__main__':
    nums = []
    k = 3

    for i in range(20):
        nums.append(random.randint(1, 100))

    print('--- nums ---')
    print(nums)

    print('--- top {} ---'.format(k))
    print(top_k(nums, k))