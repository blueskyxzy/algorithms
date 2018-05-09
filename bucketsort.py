#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import testdata
from datetime import datetime
# 桶排序


def bucketsort(a):
    n = len(a)
    b = [[] for i in range(n)]  # 产生n个链表
    for i in range(n):
        # 第i个链表存放的是半开区间[i/10,(i+1)/10]的值
        buc = int(n * a[i])
        b[buc].append(a[i])
    res = []
    for list in b:
        insertsort(list)  # 插入排序
        res += list
    return res


def insertsort(arr):
    # 对每一个链表进行插入排序
    if (arr == None or len(arr) < 2):
        return arr
    for j in range(1, len(arr)):
        key = arr[j]  # 待插入的数
        i = j - 1
        while (i >= 0 and arr[i] > key):
            # 从后往前比较待插入的数和当前数，将arr[j-1]、arr[j-2]...向右移动直到找到arr[j]的适当位置
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key  # 遍历完将arr[j]插入到该位置
    return arr


# 测试用例：
# 产生一个[0,1)区间均匀分布的数组
# ranArr = [random.random() for i in range(10)]
# print(ranArr)
# res = bucketSort(ranArr)
# print(res)

if __name__ == '__main__':
    arr = testdata.arr3
    time1 = datetime.now()
    ranArr = [random.random() for i in range(10)]
    res = bucketsort(ranArr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(res)
