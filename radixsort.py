#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata


def cntDigit(arr, radix):
    # 获取数组元素的最大位数
    maxnum = arr[0]
    for x in arr:
        if x > maxnum:
            maxnum = x

    cnt = 0
    while (maxnum != 0):
        maxnum //= radix
        cnt += 1
    print("max radix=" + str(cnt))
    return cnt


def radixSort(arr, radix=10):
    k = cntDigit(arr, radix)  # 获取最大位数
    bucket = [[] for i in range(radix)]  # 10个桶
    for i in range(1, k + 1):
        for j in arr:
            # bucket[x]存储从低到高第i位为x的数，如数组中的543，i=1时存在bucket[3]里
            bucket[j // (radix ** (i - 1)) % (radix)].append(j)
        del arr[:]  # 先初始化arr
        # print(bucket)
        for z in bucket:  # 当前位数的数组按顺序放入arr中
            arr += z
            del z[:]
            # print(arr)
    return arr


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    radixSort(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)