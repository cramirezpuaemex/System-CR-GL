
import math
import numpy as np


class Fourierft():
	def transformada(self, senal, ex):
		expo=int(ex)
		resp=np.fft.fft(senal, 2**expo)
		return resp



	def inversa(self, vector, ex):
		expo=int(ex)
		resp=np.fft.ifft(vector, 2**expo)
		return resp