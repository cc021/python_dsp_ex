#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
from matplotlib import pyplot

'the inverse discrete fourier transform'

XX_CNT = 511
XX = [0 for i in range(XX_CNT)]
REX_CNT = 256
REX = [0 for i in range(REX_CNT)]
IMX = [0 for i in range(REX_CNT)]

N = 512

def idft():
	for k in range(REX_CNT):
		REX[k] = REX[k] / (N / 2)
		IMX[k] = IMX[k] / (N / 2)
	REX[0] = REX[0] / 2
	REX[REX_CNT - 1] = REX[REX_CNT - 1] / 2

	for i in range(XX_CNT):
		XX[i] = 0
		for k in range(REX_CNT):
			XX[i] = XX[i] + REX[k]*math.cos(2*math.pi*k*i/N)
			XX[i] = XX[i] + IMX[k]*math.sin(2*math.pi*k*i/N)
	print('xx', XX)
	pyplot.plot(XX, 'b')
	pyplot.show()
if __name__ == '__main__':
	idft()
