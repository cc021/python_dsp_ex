#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
from matplotlib import pyplot

'the discrete fourier transform'

XX_CNT = 511
XX = [0 for i in range(XX_CNT)]
REX_CNT = 256
REX = [0 for i in range(REX_CNT)]
IMX = [0 for i in range(REX_CNT)]
PWR = [0 for i in range(REX_CNT)]
N = 512

fs = 20 #khz
f1 = 1 #khz
f2 = 5 #khz
f3 = 6 #khz
ts = 1 / fs

sig1 = [0 for i in range(XX_CNT)]
sig2 = [0 for i in range(XX_CNT)]

def sin_gen():
	for i in range(XX_CNT):
		sig1[i] = 10*math.sin(2 * math.pi * f1 * i * ts)
		sig2[i] = 20*math.sin(2 * math.pi * f2 * i * ts)
		XX[i] = sig1[i] + sig2[i]

def dft():
	for k in range(REX_CNT):
		REX[k] = 0
		IMX[k] = 0
		for i in range(XX_CNT):
			REX[k] = REX[k] + XX[i] * math.cos(2*math.pi*k*i/N)
			IMX[k] = IMX[k] - XX[i] * math.sin(2*math.pi*k*i/N)
		PWR[k] = math.pow(REX[k], 2) + math.pow(IMX[k], 2)
		# PWR[k] = 10*math.log(PWR[k], 10)

	pyplot.subplot(221)
	pyplot.plot(XX)
	pyplot.subplot(222)
	pyplot.plot(REX)
	pyplot.subplot(223)
	pyplot.plot(IMX)
	pyplot.subplot(224)
	pyplot.plot(PWR)
	print(PWR)
	pyplot.show()
if __name__ == '__main__':
	sin_gen()
	dft()
