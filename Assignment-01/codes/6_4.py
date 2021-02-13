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

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

X = np.fft.fft(x,N)
H = np.fft.fft(h,N)
Y = X*H
y = np.fft.ifft(Y)
y = np.real(y)

plt.figure(1)
plt.stem(range(0,N),y,use_line_collection=True)
plt.title('Filter Output using FFT and IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('../figs/y_n.pdf')
plt.savefig('../figs/y_n.eps')
#subprocess.run(shlex.split("termux-open ../figs/y_n.pdf"))  #if using termex

plt.figure(2,figsize=(9,4))
plt.subplot(1,2,1)
plt.stem(np.abs(Y),use_line_collection=True)
plt.title(r'$|Y(k)|$')
plt.xlabel('$n$')
plt.ylabel(r'$|Y(k)|$')
plt.grid()

plt.subplot(1,2,2)
plt.stem(np.angle(Y),use_line_collection=True)
plt.title(r'$\angle{Y(k)}$')
plt.xlabel('$n$')
plt.ylabel(r'$\angle{Y(k)}$')
plt.grid()
plt.savefig('../figs/Y_1.pdf')
plt.savefig('../figs/Y_1.eps')

#subprocess.run(shlex.split("termux-open ../figs/Y_1.pdf"))  #if using termex


plt.figure(3,figsize=(9,7.5))
plt.subplot(2,2,1)
plt.stem(np.abs(x),use_line_collection=True)
plt.title(r'$|x(n)|$')
plt.grid()

plt.subplot(2,2,2)
plt.stem(np.angle(x),use_line_collection=True)
plt.title(r'$\angle{x(n)}$')
plt.grid()

plt.subplot(2,2,3)
plt.stem(np.abs(h),use_line_collection=True)
plt.title(r'$|h(n)|$')
plt.grid()

plt.subplot(2,2,4)
plt.stem(np.angle(h),use_line_collection=True)
plt.title(r'$\angle{h(n)}$')
plt.grid()
plt.savefig('../figs/xh_1.pdf')
plt.savefig('../figs/xh_1.eps')

#subprocess.run(shlex.split("termux-open ../figs/xh_1.pdf"))  #if using termex



plt.figure(4,figsize=(9,7.5))
plt.subplot(2,2,1)
plt.stem(np.abs(X),use_line_collection=True)
plt.title(r'$|X(k)|$')
plt.grid()

plt.subplot(2,2,2)
plt.stem(np.angle(X),use_line_collection=True)
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.subplot(2,2,3)
plt.stem(np.abs(H),use_line_collection=True)
plt.title(r'$|H(k)|$')
plt.grid()

plt.subplot(2,2,4)
plt.stem(np.angle(H),use_line_collection=True)
plt.title(r'$\angle{H(k)}$')
plt.grid()
plt.savefig('../figs/XH_fft.pdf')
plt.savefig('../figs/XH_fft.eps')
plt.show()
#subprocess.run(shlex.split("termux-open ../figs/XH_fft.pdf"))  #if using termex


