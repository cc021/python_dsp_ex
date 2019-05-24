#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import dft
from matplotlib import pyplot

__doc__ = 'rectangular to polar'

XX_CNT = 201
XX = [0 for i in range(XX_CNT)]
DFT_CNT = int(XX_CNT / 2) + 1 
print('XX_CNT', XX_CNT, 'DFT_CNT', DFT_CNT)
REX = [0 for i in range(DFT_CNT)]
IMX = [0 for i in range(DFT_CNT)]
MAG = [0 for i in range(DFT_CNT)]
PHASE = [0 for i in range(DFT_CNT)]

fs = 20 #khz
f1 = 1 #khz
f2 = 5 #khz
f3 = 6 #khz
ts = 1 / fs

sig1 = [0 for i in range(XX_CNT)]
sig2 = [0 for i in range(XX_CNT)]

def sin_gen():
	for i in range(XX_CNT):
		# sig1[i] = 10*math.sin(2 * math.pi * f1 * i * ts)
		sig2[i] = math.sin(2 * math.pi * f2 * i * ts)
		XX[i] = sig1[i] + sig2[i]

def rectangular_to_polar():
	for k in range(DFT_CNT):
		MAG[k] = math.sqrt(math.pow(REX[k], 2) + math.pow(IMX[k], 2))
		PHASE[k] = math.atan2(IMX[k], REX[k])
	
if __name__ == '__main__':
	sin_gen()
	dft.dft(XX, XX_CNT, REX, IMX)
	rectangular_to_polar()
	pyplot.subplot(231)
	pyplot.plot(XX)
	pyplot.subplot(232)
	pyplot.plot(REX)
	print(REX)
	pyplot.subplot(233)
	pyplot.plot(IMX)
	pyplot.subplot(234)
	pyplot.plot(MAG)
	pyplot.subplot(235)
	pyplot.plot(PHASE)
	pyplot.show()
