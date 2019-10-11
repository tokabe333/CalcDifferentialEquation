# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os

#定数
a = 1
b = 0.01
c = 1
d = 0.02


#微分したい数(ロトカ・ヴォルテラ方程式 xについて)
def F(x, y):
	return a * x - b * x * y
#End_Def

#微分したい数(ロトカ・ヴォルテラ方程式 yについて)
def G(x, y):
	return -c * y + d * x * y
#End_Def

#オイラー法で計算してplot
def EulerMethod(tFin, h, N):
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
	os.makedirs("Result", exist_ok=True)
	plt.savefig("Result/Figure_" + str(h) + ".png")
#End_Def

####
def Main():
	tFin = 30			#終了時刻
	h = 0.1				#刻み

	#刻みを変えながらやってみる
	for i in range(7):
		print("計算 h=" + str(h))
		N = int(tFin / h)			#計算回数
		EulerMethod(tFin, h , N)	#オイラー法で計算してplot
		h /= 10						#次の刻み
	#End_For
#End_Method

if __name__ == "__main__":
	Main()
