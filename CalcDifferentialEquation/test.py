# -*- Coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def Main():
    #傾きを出すときのΔx、刻み幅
    h = [1 / (2 ** n) for n in range(1,51)]
    #微分する地点
    x = 0.3 * np.pi
    #真値         
    trueValue = np.cos(x)

    #刻み幅ごとのyを計算するよ
    y = [np.abs(trueValue - Defferential(F, x, hh)) for hh in h]

    #プロット
    plt.semilogy(range(1,len(h) + 1), y)
    plt.xlabel('$1/2^N$', fontsize=16)
    plt.ylabel('Error', fontsize=16)
    plt.show()
#End_Func

#微分したい関数
def F(x):
    return np.sin(x)
#End_Func

#微分を行う
def Defferential(func, x, h):
    return (func(x + h) - func(x)) / h
#End_Func


if __name__ == "__main__":
    Main()