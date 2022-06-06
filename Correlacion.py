from Fourierft import *

class Correlacion():
	def trabaja(self, parte, senal02, ex):


		fourier=Fourierft()
		f0=fourier.transformada(parte, ex)
		f1=fourier.transformada(senal02, ex)

		c=[]

		
		for i in range(len(f0)):
			c.append(f1[i].conjugate()*f0[i])

		#====================== se realiza la transformada inversa para localizar el punto maximo de correlacion================
		R_xy = fourier.inversa(c, ex)

		R_xy=np.asarray(R_xy)
		R_xy=abs(R_xy)


		#====================== se calcula la energia de cada senal================
		L2 = [n2**2 for n2 in senal02]
		n=sum(L2)
	
		L1 = [n1**2 for n1 in parte]
		m=sum(L1)
		#====================== se normaliza la correlacion, valores de 0 a 1 ================
		for i in range(len(R_xy)):
		
			R_xy[i]=R_xy[i]/n
		
		R_xy=R_xy.tolist()

		return R_xy