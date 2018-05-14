#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import math
import random


def prime_array():             # 生成素数数组
    arraya = []
    for i in range(2, 100):    # 生成前100中的素数，从2开始因为2是最小的素数
        x = prime(i, 2)        # i为素数时返回True，则将x加入arraya数组中;2为测试值
        if x:
            arraya.append(i)
    return arraya


def prime(n, test_divisor):     # 判断是否为素数
    if math.sqrt(n) < test_divisor:
        return True   # 为素数时返回True
    if n % test_divisor == 0:
        return False  # 不为素数时返回False
    else:
        return prime(n, test_divisor+1)


def co_prime(s):       # 找出与（p-1）*(q-1)互质的数e
    while True:
        e = random.choice(range(100))
        x = gcd(e, s)
        if x == 1:    # 如果最大公约数为1，则退出循环返回e
            break
    return e


def gcd(a, b):     # 求两个数的最大公约数
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def find_d(e, s):
    # 根据e*d mod s = 1,找出d
    for d in range(100000000):   # 随机太难找，就按顺序找到d,range里的数字随意
        x = (e*d) % s
        if x == 1:
            return d


def test():         # 生成公钥和私钥
    a = prime_array()
    print("前100个素数:",a)
    p = random.choice(a)
    q = random.choice(a)
    print("随机生成两个素数p和q. p=", p, " q=", q)
    n = p * q
    s = (p-1)*(q-1)
    e = co_prime(s)
    print("根据e和(p-1)*(q-1))互质得到: e=", e)
    d = find_d(e, s)
    print("根据(e*d) 模 ((p-1)*(q-1)) 等于 1 得到 d=", d)
    print("公钥: n=", n, " e=", e)
    print("私钥: n=", n, " d=", d)
    pbvk = (n, e, d)
    return pbvk


def generate_pbk_pvk(a, zx):      # 生成public key公钥或private key私钥
    # zx==0 公钥 zx==1 私钥
    # a为元组(n,e,d)
    pbk = (a[0], a[1])  # public key公钥 元组类型，不能被修改
    pvk = (a[0], a[2])  # private key私钥
    if zx == 0:
        return pbk
    if zx == 1:
        return pvk


def encryption(mw, ned):     # 加密
    # 密文B = 明文A的e次方 模 n， ned为公钥
    # mw就是明文A，ned【1】是e， ned【0】是n
    B = pow(mw, ned[1]) % ned[0]
    return B


def decode(mw, ned):     # 解密
    # 明文C = 密文B的d次方 模 n， ned为私钥匙
    # mw就是密文B， ned【1】是e，ned【1】是d
    C = pow(mw, ned[1]) % ned[0]
    return C


if __name__=='__main__':
    pbvk = test()
    pbk = generate_pbk_pvk(pbvk, 0)  # 公钥 if 0 return pbk if 1 return pvk
    A = int(input("请输入明文: "))
    print("加密中....")
    B = encryption(A,pbk)      # 加密
    print("生成的密文是: ", B)
    pvk = generate_pbk_pvk(pbvk, 1)  # 私钥
    print("解密中....")
    C = decode(B,pvk)          # 解密
    print("解密后的明文是: ", C)
    if A == C:
        print("加密前的明文和解密后的明文一样，成功!!!")