from typing import List




def merge_sort(a: List[int]):
    _merge_sort_between(a, 0, len(a)-1)

def _merge_sort_between(a:List[int], low:int, high:int):
    if low >= high: return
    mid = low + (high - low)//2
    _merge_sort_between(a, low, mid)
    _merge_sort_between(a, mid+1, high)

    _merge(a, low, mid, high)

def _merge(a:List[int], low:int, mid:int, high:int):
    i, j = low, mid+1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end+1])
    a[low:high+1] = tmp

    


if __name__ == '__main__':
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)