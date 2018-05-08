#!/usr/bin/env python
# -*- coding: UTF-8 -*
import random
from datetime import datetime
import testdata


def quickone(arr, low, high):
    index = random.randint(low, high)  # 随机基准
    # key = arr[index]
    arr[index], arr[high] = arr[high], arr[index]  # 基准从high开始

    # 1.通过改变2个从两边到中间的左右索引和交换的方式：

    # while low < high:
    #     while arr[low] <= key and low < high:
    #         low += 1
    #     arr[low], arr[high] = arr[high], arr[low]
    #     while arr[high] > key:
    #         high -= 1
    #     arr[low], arr[high] = arr[high], arr[low]
    # mid = low

    # 2.通过2个从左到右的索引和交换的方式：(比low小1的索引)
    ind = low - 1
    for i in range(low, high):   # low到high -1
        if arr[i] < arr[high]:
            ind += 1
            arr[i], arr[ind] = arr[ind], arr[i]
    arr[ind + 1], arr[high] = arr[high], arr[ind + 1]
    return ind + 1


def quicksortxzy(arr, low, high):
    if low < high:
        mid = quickone(arr, low, high)
        quicksortxzy(arr, low, mid - 1)
        quicksortxzy(arr, mid + 1, high)


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    low = 0
    # high 是最大的索引，等于len - 1
    high = len(arr) - 1
    quicksortxzy(arr, low, high)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
