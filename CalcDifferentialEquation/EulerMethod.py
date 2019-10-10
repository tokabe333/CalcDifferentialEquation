# -*- Coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#定数
a = 1
b = 0.01
c = 1
d = 0.02

tFin = 30			#終了時刻
h = 0.001				#刻み
N = int(tFin / h)	#計算回数

#計算結果格納用
x = [0] * N
y = [0] * N
x[0] = 20
y[0] = 20

#微分したい数(ロトカ・ヴォルテラ方程式 xについて)
def F(x, y):
	return a * x - b * x * y
#End_Def

#微分したい数(ロトカ・ヴォルテラ方程式 yについて)
def G(x, y):
	return -c * y + d * x * y
#End_Def

#
def Main():
	#EulerMethod
	for i in range(0, N - 1):
		xt = x[i]
		yt = y[i]
		x[i + 1] = xt + h * F(xt, yt)
		y[i + 1] = yt + h * G(xt, yt)
	#End_For

	#Plot
	plt.plot(np.arange(0, tFin, h), x, label="Prey")
	plt.plot(np.arange(0, tFin, h), y, label="Predator")
	plt.xlabel("Time", fontsize=16)
	plt.ylabel("Num of Individual", fontsize=16)
	plt.legend()
	plt.show()
#End_Method

if __name__ == "__main__":
	Main()
