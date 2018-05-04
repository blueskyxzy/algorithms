#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata
# 直接选择排序
# 遍历数组，依次找到最小的放在前面
# i从1到len，i到len找到最小的缩影，与i交换位置


def selectsortxzy(x):
    if x == None or len(x) < 2:
        return x
    for i in range(len(x)):
        index = i
        for j in range(i, len(x)):
            if x[j] < x[index]:
                index = j
        tmp = x[i]
        x[i] = x[index]
        x[index] = tmp
    return x


if __name__ == '__main__':
    arr = testdata.arr2
    time1 = datetime.now()
    selectsortxzy(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)
