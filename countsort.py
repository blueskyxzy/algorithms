#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import testdata
from datetime import datetime
# 计数排序


def countSort(a):
    k = a[0]
    # 得到最大值k
    for x in a:
        if x > k:
            k = x
    b = [0 for i in range(len(a))]  # b存放排序的输出
    c = [0 for i in range(k + 1)]  # c是计数数组

    for x in a:
        # c[x]记录了数组a中x出现的次数
        c[x] += 1
    for i in range(1, k + 1):
        # [i]记录了小于等于i的元素的数量
        c[i] = c[i] + c[i - 1]
    for x in a:
        # 小于等于x的元素有c[x]个，将x放在第c[x]的位置
        # 注意下标从0开始
        b[c[x] - 1] = x
        c[x] -= 1
    return b


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    countSort(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)