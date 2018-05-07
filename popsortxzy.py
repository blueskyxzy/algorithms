#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import testdata

# 冒泡排序  交换排序的一种
# 一般用2次for循环 0到len-1,len -1到i
# 思路，每次遍历将最小的排在前面


def popsortxzy(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1, i - 1, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    popsortxzy(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
