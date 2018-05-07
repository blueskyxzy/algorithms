#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata


# 堆排序是利用堆的性质进行的一种选择排序
# 堆实际上是一棵完全二叉树，其任何一非叶节点满足性质：
# Key[i]<=key[2i+1]&&Key[i]<=key[2i+2]或者Key[i]>=Key[2i+1]&&key>=key[2i+2]
# 即任何一非叶节点的关键字不大于或者不小于其左右孩子节点的关键字。
# 堆分为大顶堆和小顶堆，满足Key[i]>=Key[2i+1]&&key>=key[2i+2]称为大顶堆，满足 Key[i]<=key[2i+1]&&Key[i]<=key[2i+2]称为小顶堆。
# 由上述性质可知大顶堆的堆顶的关键字肯定是所有关键字中最大的，小顶堆的堆顶的关键字是所有关键字中最小的。

# 其基本思想为(大顶堆)：
#
#     1)将初始待排序关键字序列(R1,R2....Rn)构建成大顶堆，此堆为初始的无序区；
#
#     2)将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,......Rn-1)和新的有序区(Rn),且满足R[1,2...n-1]<=R[n];
#
#     3)由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,......Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2....Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。
#
#     操作过程如下：
#
#      1)初始化堆：将R[1..n]构造为堆；
#
#      2)将当前无序区的堆顶元素R[1]同该区间的最后一个记录交换，然后将新的无序区调整为新的堆。
#
#     因此对于堆排序，最重要的两个操作就是构造初始堆和调整堆，其实构造初始堆事实上也是调整堆的过程，只不过构造初始堆是对所有的非叶节点都进行调整。

#   1. 将无序序列构建成大顶堆
#   2. 将顶堆第一个最大元素与最后一个元素交换
#   3. 去掉后面交换的元素，重新构建大顶堆，直到最后元素个数为1

def heaplist(x, i, length):
    # 第i个节点构造成大顶堆
    l = 2 * i + 1  # 左节点
    r = 2 * i + 2  # 右节点

    largest = i
    if l < length and x[l] > x[largest]:
        largest = l
    if r < length and x[r] > x[largest]:
        largest = r
    if largest != i:
        x[i], x[largest] = x[largest], x[i]
        heaplist(x, largest, length)


def buildmaxhead(x, length):
    # 构造最大堆
    mid = (length - 1)/2
    for i in range(mid, -1, -1):
        heaplist(x, i, length)


def heapsortxzy(x):
    length = len(x)
    buildmaxhead(x, length)

    for i in range(length - 1, -1, -1):
        x[0], x[i] = x[i], x[0]
        heaplist(x, 0, i)


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    heapsortxzy(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
