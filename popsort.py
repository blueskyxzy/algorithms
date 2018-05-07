#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from datetime import datetime
import testdata


def popSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    popSort(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)