#include <stdio.h>
# include <complex.h>
# include <math.h>
typedef double complex cd;

void fft(complex *X, int n)
{
	if(n == 1) return;
	
	cd X_odd[n/2], X_even[n/2];
	
	for(int i = 0; i < n/2; i++) 
	{
		X_even[i] = X[2*i];
		X_odd[i] = X[2*i+1];
	}
	
	fft(X_even, n/2);	 	
	fft(X_odd, n/2);		
	
	cd exp;
    for (int i = 0;i < n/2;i++) 
    {
		exp = CMPLX(cos(2*M_PI*i/n),-sin(2*M_PI*i/n));
	    X[i] = X_even[i] + exp * X_odd[i];
        X[i+n/2] = X_even[i] - exp * X_odd[i];
       
    }
}

int main()
{	
	int n = 8;  
	double x[] = {1,2,3,4,1,2,3,4};
	
	cd X[n];
	
	for(int i = 0; i < n; i++) 
	{
		X[i] = x[i];
	}
	fft(X, n);
	
	for(int i = 0; i < n; i++) 
		printf("(%.5lf, %.5lf)\n", creal(X[i]), cimag(X[i]));
}

