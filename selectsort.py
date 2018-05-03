#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime


def selectsort(arr):
    # 选择排序，最坏为O(n^2)
    # 升序排列一个数组，降序排列将while语句中改为arr[i]<key即可
    if (arr == None or len(arr) < 2):
        return arr
    for j in range(len(arr)):

        index = j
        for i in range(j, len(arr)):
            if arr[i] < arr[index]:
                index = i  # 找出剩余的最小元素

        # 未排序中最小的元素跟arr[j]交换
        tmp = arr[j]
        arr[j] = arr[index]
        arr[index] = tmp

    return arr


if __name__ == '__main__':
    arr = [17, 28, 3, 9, 53, 34, 66, 77, 55, 25, 99]
    time1 = datetime.now()
    selectsort(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)