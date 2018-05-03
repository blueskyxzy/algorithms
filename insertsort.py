#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def insertsort(arr):
    # 插入排序，最坏为O(n^2)，最好为O(n)
    # 升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if arr == None or len(arr) < 2:
        return arr
    for j in range(1, len(arr)):
        key = arr[j]   # 待插入的数
        i = j-1
        while i >= 0 and arr[i] > key:
            # 从后往前比较待插入的数和当前数，将arr[j-1]、arr[j-2]...向右移动直到找到arr[j]的适当位置
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key   # 遍历完将arr[j]插入到该位置
    return arr


if __name__ == '__main__':
    arr = [17, 28, 3, 9, 53, 34, 66, 77, 55, 25, 99]
    insertsort(arr)
    print(arr)


