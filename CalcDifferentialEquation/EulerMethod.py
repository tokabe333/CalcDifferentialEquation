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


#オイラー法で計算してplot
def EulerMethod(h, N):
	global figNo
	#計算結果格納用
	x = [0] * N
	y = [0] * N
	x[0] = 20
	y[0] = 20

	#次の時間について計算していく
	for i in range(0, N - 1):
		xt = x[i]
		yt = y[i]
		x[i + 1] = xt + h * F(xt, yt)
		y[i + 1] = yt + h * G(xt, yt)
	#End_For
	
	#Plot
	plt.figure(figsize=(10,10), dpi=300)
	plt.plot(np.arange(0, tFin, h)[0:len(x)], x, label="Prey h=" + str(h))
	plt.plot(np.arange(0, tFin, h)[0:len(y)], y, label="Predator h=" + str(h))
	plt.xlabel("Time", fontsize=16)
	plt.ylabel("Num of Individual", fontsize=16)
	plt.legend(bbox_to_anchor=(1.03, 1.13), loc="upper right", borderaxespad=1, fontsize=16)
	os.makedirs("Result_Euler", exist_ok=True)
	plt.savefig("Result_Euler/"+str(figNo)+"_Figure_" + str(h) + ".png")
	figNo += 1
#End_Def

####
def Main():
    # 刻みを変えながらやってみる
    hList = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    for i in hList:
        print("計算 h=" + str(i))
        N = int(tFin / i)  # 計算回数
        EulerMethod(i, N)  # オイラー法で計算してplot
	# End_For
# End_Method


if __name__ == "__main__":
    Main()
