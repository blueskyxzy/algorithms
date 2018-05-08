#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata


def mergesort(arr, p, r):
    # p17,归并排序，O(nlgn).注意r是数组的最大下标
    if p < r:
        q = int((p + r) / 2)
        mergesort(arr, p, q)
        mergesort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    # 合并两个有序数组,arr1[p...q]和arr2[q+1...r]
    n1 = q - p + 1  # 左边数组的长度(因为q中位数是向下取整，所以q-p+1)
    n2 = r - q  # 右边数组的长度
    arr1 = []
    arr2 = []
    for i in range(n1):
        arr1.append(arr[p + i])
    for j in range(n2):
        # 注意j的范围
        arr2.append(arr[q + 1 + j])
    arr1.append(float('inf'))  # 放置一个无穷大的数作为“哨兵值”
    arr2.append(float('inf'))
    # print(arr1,arr2)
    i, j = 0, 0
    for k in range(p, r + 1):  # 注意k的范围
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    mergesort(arr, 0, len(arr) - 1)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
