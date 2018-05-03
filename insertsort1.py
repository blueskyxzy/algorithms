#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 直接插入排序
# 1. i从1到length以此顺序排列
# 2. 第i个数按顺序插入1中已经排列好前i-1的数组中
# for + while(插入改变索引值，用while节省很多代码,i>0注意Python索引可以是负号)


def insertsort1(x):
    if x == None or len(x) == 1:
        return x
    for i in range(1, len(x)):
        k = x[i]
        while x[i-1] > k and i > 0:
            x[i] = x[i-1]
            i -= 1
        x[i] = k
    return x


if __name__ == '__main__':
    arr = [17, 28, 3, 9, 53, 34, 66, 77, 55, 25, 99]
    insertsort1(arr)
    print(arr)




