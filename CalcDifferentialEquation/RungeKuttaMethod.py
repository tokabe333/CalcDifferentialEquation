# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os

# 定数
a = 1
b = 0.01
c = 1
d = 0.02

# 終了時刻
tFin = 30

# 画像保存用
figNo = 0


# 微分したい数(ロトカ・ヴォルテラ方程式 xについて)
def F(x, y):
    return a * x - b * x * y
# End_Def

# 微分したい数(ロトカ・ヴォルテラ方程式 yについて)
def G(x, y):
    return -c * y + d * x * y
# End_Def

# ルンゲクッタ法で計算してplot
def RungeKuttaMethod(h, N):
    global figNo
    # 計算結果格納用
    x = [0] * N
    y = [0] * N
    x[0] = 20
    y[0] = 20

    # 次の時間について計算していく
    for i in range(0, N - 1):
        xt = x[i]
        yt = y[i]

        # xについて
        k1 = h * F(xt, yt)
        k2 = h * F(xt + k1 / 2, yt + k1 / 2)
        k3 = h * F(xt + k2 / 2, yt + k2 / 2)
        k4 = h * F(xt + k3, yt + k3)
        # if i == 23:
        # print("xt:" + str(xt) + "  yt:" + str(yt) + "  k1:" + str(k1) + "  k2:" + str(k2) + "  k3:" + str(k3) + "  k4:" + str(k4))
        x[i + 1] = xt + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        # print("i:"+str(i)+" x[i+1]:"+str(x[i+1]))

        # yについて
        k1 = h * G(xt, yt)
        k2 = h * G(xt + k1 / 2, yt + k1 / 2)
        k3 = h * G(xt + k2 / 2, yt + k2 / 2)
        k4 = h * G(xt + k3, yt + k3)
        y[i + 1] = yt + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        # print("xt:" + str(xt) + "  yt:" + str(yt) + "  k1:" + str(k1) + "  k2:" + str(k2) + "  k3:" + str(k3) + "  k4:" + str(k4))
    # End_For

    # Plot
    plt.figure(figsize=(10, 10), dpi=300)
    plt.plot(np.arange(0, tFin, h)[0:len(x)], x, label="Prey h=" + str(h))
    plt.plot(np.arange(0, tFin, h)[0:len(y)], y, label="Predator h=" + str(h))
    plt.xlabel("Time", fontsize=16)
    plt.ylabel("Num of Individual", fontsize=16)
    plt.legend(bbox_to_anchor=(1.03, 1.13), loc="upper right",
               borderaxespad=1, fontsize=16)
    os.makedirs("Result_RungeKutta", exist_ok=True)
    plt.savefig("Result_RungeKutta/" + str(figNo) +
                "Figure_" + str(h) + ".png")
    figNo += 1
# End_Def

####
def Main():
    # 刻みを変えながらやってみる
    hList = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    for i in hList:
        print("計算 h=" + str(i))
        N = int(tFin / i)  # 計算回数
        RungeKuttaMethod(i, N)  # オイラー法で計算してplot
	# End_For
# End_Method


if __name__ == "__main__":
    Main()
