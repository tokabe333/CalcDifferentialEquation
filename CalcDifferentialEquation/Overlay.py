# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os

# 定数
a = 1
b = 0.01
c = 1
d = 0.02

# 名前保存用
figNo = 0


# 微分したい数(ロトカ・ヴォルテラ方程式 xについて)
def F(x, y):
    return a * x - b * x * y
# End_Def

# 微分したい数(ロトカ・ヴォルテラ方程式 yについて)
def G(x, y):
    return -c * y + d * x * y
# End_Def


# オイラー法で計算する
def EulerMethod(tFin, h, N):
    # 計算結果格納用
    x = [0] * N
    y = [0] * N
    x[0] = 20
    y[0] = 20

    # 次の時間について計算していく
    for i in range(0, N - 1):
        xt = x[i]
        yt = y[i]
        x[i + 1] = xt + h * F(xt, yt)
        y[i + 1] = yt + h * G(xt, yt)
    # End_For

    return x, y
# End_Def

# オイラー法で計算する
def RungeKuttaMethod(tFin, h, N):
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

    return x, y
# End_Def

# オイラーとルンゲクッタを重ねて表示
def PlotOverlay(xe, ye, xr, yr, tFin, h):
    global figNo
    # 画像サイズ
    plt.figure(figsize=(10, 10), dpi=300)
    plt.rcParams['font.family'] = 'Times new Roman'

    # 誤差で配列サイズが変わる時がある
    length = min(len(xe), len(ye), len(xr), len(yr))

    # 色分けしてPlot 緑→Euler オレンジ→RungeKutta
    plt.plot(np.arange(0, tFin, h)[
             0:length], xr, label="Prey     Runge-Kutta h=" + str(h), color="#ff7f00")
    plt.plot(np.arange(0, tFin, h)[
             0:length], yr, label="Predator Runge-Kutta h=" + str(h), color="#ff7f00")
    plt.plot(np.arange(0, tFin, h)[
             0:length], xe, label="Prey     Euler       h=" + str(h), color="#377eb8")
    plt.plot(np.arange(0, tFin, h)[
             0:length], ye, label="Predator Euler       h=" + str(h), color="#377eb8")

    # 整形
    plt.xlabel("Time", fontsize=20)
    plt.ylabel("Num of Individual", fontsize=20)
    plt.legend(bbox_to_anchor=(1.03, 1.13), loc="upper right",
               borderaxespad=1, fontsize=13)
    os.makedirs("Result_Overlay", exist_ok=True)
    plt.savefig("Result_Overlay/" + str(figNo) + "_Figure_" + str(h) + ".png")
    figNo += 1
# End_Def

####
def Main():
    tFin = 30  # 終了時刻
    h = 0.1  # 刻み

    # 刻みを変えながら
    #hList = [0.1, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.001]
    hList = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    #hList = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    for i in hList:
        h = i
        print("計算 h = " + str(h))
        N = int(tFin / h)
        # 計算
        xe, ye = EulerMethod(tFin, h, N)
        xr, yr = RungeKuttaMethod(tFin, h, N)
        # plot
        PlotOverlay(xe, ye, xr, yr, tFin, h)
        h /= 10
    # End_For
# End_Method


if __name__ == "__main__":
    Main()
