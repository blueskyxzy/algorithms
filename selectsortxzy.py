#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime
import testdata


def selectsortxzy(x):




if __name__ == '__main__':
    arr = testdata.arr1
    time1 = datetime.now()
    selectsortxzy(arr)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds   # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print(arr)