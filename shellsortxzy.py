#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime


# 希尔排序  又称“缩小增量排序”
# 1.直接插入排序步长是1，希尔排序的步长依次按照一半逐渐递减到1的插入排序
# 2.按照步长分组，每组进行插入排序

# 希尔排序是基于插入排序的以下两点性质而提出改进方法的：
# 1.插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率。
# 2.但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

def shellsortxzy(x):
    d = len(x)/2
    while d >= 1:
        for i in range(d, len(x)):
            k = x[i]
            while x[i-d] > k and i >= d:
                x[i] = x[i-d]
                i -= d
            x[i] = k
        d /= 2

    return x


if __name__ == '__main__':
    arr = [17, 28, 3, 9, 53, 34, 66, 77, 55, 25, 99]
    time1 = datetime.now()
    shellsortxzy(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds  # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)

