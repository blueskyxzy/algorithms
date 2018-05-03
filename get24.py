#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from datetime import datetime

# 求24，输入4个数字输出所有最终结果为24的表达式 （曾经的面试上机题，当时没做出来）
# 1.遍历4个数，随机排序 4*3*2*1
# 2. 1到4依次遍历所有运算算出值和拼接表达式
# 3. 每步运算拼接的表达式都加()
# 4. 最终值为24的输出表达式
# 一共有4*3*2*1*4*4*4种可能性

# operator 0代表+，1代表-，2代表*，3代表/


def createexpession(y1, y2, exp, operator):
    y = 0.0
    if operator == 0:
        y = y1 + y2
        if len(exp) >= 4:
            exp = "(" + exp + "+" + str(y2) +")"
        else:
            exp = "(" + str(y1) + "+" + str(y2) +")"
    if operator == 1:
        y = y1 - y2
        if len(exp) >= 4:
            exp = "(" + exp + "-" + str(y2) +")"
        else:
            exp = "(" + str(y1) + "+" + str(y2) + ")"
    if operator == 2:
        y = y1 * y2
        if len(exp) >= 4:
            exp = "(" + exp + "*" + str(y2) +")"
        else:
            exp = "(" + str(y1) + "+" + str(y2) + ")"
    if operator == 3:
        y = y1 / y2
        if len(exp) >= 4:
            exp = "(" + exp + "/" + str(y2) +")"
        else:
            exp = "(" + str(y1) + "+" + str(y2) + ")"
    return y, exp


def get24expression(x):
    exp = ""
    for i in range(4):
        j1 = [z for z in range(4) if z != i]
        for j in j1:
            k1 = [z for z in range(4) if z != i and z != j]
            for k in k1:
                l1 = [z for z in range(4) if z != i and z != j]
                for l in l1:
                    for operator1 in range(4):
                        x1, exp1 = createexpession(x[i], x[j], "", operator1)
                        for operator2 in range(4):
                            x2, exp2 = createexpession(x1, x[k], exp1, operator2)
                            for operator3 in range(4):
                                x3, exp3 = createexpession(x2, x[l], exp2, operator3)
                                y = x3
                                exp = exp3
                                if y == 24:
                                    print("表达式有：" + exp)

    print("end")


if __name__ == '__main__':
    x1 = input("Please intput number1 :")
    x2 = input("Please intput number2 :")
    x3 = input("Please intput number3 :")
    x4 = input("Please intput number4 :")
    x = [x1, x2, x3, x4]
    time1 = datetime.now()
    get24expression(x)
    time2 = datetime.now()
    timeDef = (time2 - time1).microseconds  # 单位微秒
    print("用时：" + str(timeDef) + "微妙")
    print("x:" + str(x))


