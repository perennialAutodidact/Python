from random import randint

def merge(left, right):
    pass

def merge_sort(arr):
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f'left: {left}')
    print(f'right: {right}')

    merge_sort(left)
    merge_sort(right)
nums = [randint(0,100) for i in range(0,10)]
merge_sort(nums)