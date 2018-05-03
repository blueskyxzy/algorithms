#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime

def shellsort(arr):
    # 改进版的插入排序-希尔排序，最坏为O(n^2)，最好为O(n)，平均为O(n^1.3)
    gap = len(arr) / 2
    while gap > 0:
        for i in range(gap, len(arr)):
            if arr[i] < arr[i - gap]:  # 后面的元素比前面的小，以gap为步长进行插入排序
                key = arr[i]
                j = i - gap
                while j >= 0 and arr[j] > key:
                    arr[j + gap] = arr[j]
                    j -= gap
                arr[j + gap] = key
                # 步长减一半
        gap /= 2

    return arr


if __name__ == '__main__':
    arr = [17, 28, 3, 9, 53, 34, 66, 77, 55, 25, 99]
    time1 = datetime.now()
    shellsort(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
