import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex
#end if


N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])

X = np.fft.fft(x,N)
H = np.fft.fft(h,N)
Y = X*H
y = np.fft.ifft(Y)
y = np.real(y)

plt.figure(1)
plt.stem(range(0,N),y)
plt.title('Filter Output using FFT and IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('../figs/y_(n).pdf')
plt.savefig('../figs/y_(n).eps')
plt.show()
#subprocess.run(shlex.split("termux-open ../figs/y_n.pdf"))  #if using termex

plt.figure(2)
plt.stem(range(0,6),x)
plt.title('input signal')
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()# minor
#plt.savefig('../figs/x_n.pdf')
#plt.savefig('../figs/x_n.eps')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/n_n.pdf"))  #if using termex

plt.figure(3)
plt.stem(range(0,N),X)
plt.title('FFT of input signal X(k)')
plt.xlabel('$k$')
plt.ylabel('$X(K)$')
plt.grid()
#plt.savefig('../figs/X_fft.pdf')
#plt.savefig('../figs/X_fft.eps')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/X_fft.pdf"))  #if using termex

plt.figure(4)
plt.stem(range(0,N),H)
plt.title('FFT of Impulse response')
plt.xlabel('$k$')
plt.ylabel('$H(K)$')
plt.grid()
#plt.savefig('../figs/H_fft.pdf')
#plt.savefig('../figs/H_fft.eps')
#plt.show()
#subprocess.run(shlex.split("termux-open ../figs/H_fft.pdf"))  #if using termex


