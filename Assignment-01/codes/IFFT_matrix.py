import numpy as np 

Y = np.array([16.65625,-2.95312+1j*1.16372,-0.07813+1j*1.1096,-3.84375,-0.07813-1j*1.1096,-2.95312-1j*1.16372]) 
def ifft_matrix(n):
	fft_mat = np.zeros((n,n),dtype=np.complex128)
	for i in range(n):
		for j in range(n):
				fft_mat[i][j] = (1/n)*np.exp(2j*np.pi*i*j/n)
	return fft_mat

def ifft(x):
	n = len(x)
	F = ifft_matrix(n)
	return F@x


print(ifft(Y))
