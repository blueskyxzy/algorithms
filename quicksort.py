#!/usr/bin/env python
# -*- coding: UTF-8 -*
import random
from datetime import datetime
import testdata


def quickSort(arr, low, high):
    # 随机选择基准元素的快速排序，达到期望时间复杂度O(nlgn)
    # 注意high是最大下标
    if low < high:
        mid = getPartition(arr, low, high)
        # 对基准元素两边的数组快排
        quickSort(arr, low, mid - 1)
        quickSort(arr, mid + 1, high)


def getPartition(arr, low, high):
    # 随机选择一个数并与arr[high]交换，防止最坏情况
    # 将arr[high]作为基准进行排序
    rand = random.randint(low, high)
    arr[high], arr[rand] = arr[rand], arr[high]

    index = low - 1
    for i in range(low, high):
        if arr[i] <= arr[high]:  # 保证index前面的数都比key小
            index += 1
            arr[index], arr[i] = arr[i], arr[index]
    arr[index + 1], arr[high] = arr[high], arr[index + 1]

    return index + 1


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    high = len(arr)
    quickSort(arr, 0, high - 1)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)