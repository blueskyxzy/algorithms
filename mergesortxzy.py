#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata
# 归并排序  该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。


def merge(arr, low, mid, high):

    arr1 = []
    arr2 = []
    m = mid - low + 1
    n = high - mid
    for i in range(m):
        arr1.append(arr[low + i])
    for j in range(n):
        arr2.append(arr[mid + j + 1])

    # 加入哨兵
    arr1.append(float('inf'))
    arr2.append(float('inf'))

    i, j = 0, 0
    for k in range(low, high + 1):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1


def mergesortxzy(arr, low, high):
    mid = (low + high)/2
    if low < high:
        mergesortxzy(arr, low, mid)
        mergesortxzy(arr, mid + 1, high)
        merge(arr, low, mid, high)


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    mergesortxzy(arr, 0, len(arr) - 1)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
