import matplotlib.pyplot as plt
import sys
sys.path.append('../src')  
from solver_1d import linear_convection, nonlinear_convection

#Convection lineaire

x_linconv, u_linconv_final = linear_convection(nx=101, c=1.0, nt=50, sigma=0.5, xtot = 10)

plt.plot(x_linconv, u_linconv_final)
plt.title('Convection Lineaire 1D')
plt.legend()
plt.xlabel('Distance (x)')
plt.ylabel('Vitesse (u)')
plt.grid()
plt.show()


#Convection non-lineaire

x_nonlinconv, u_nonlinconv_final = nonlinear_convection(nx=101, nt=50, sigma=0.5, xtot = 10)

plt.plot(x_nonlinconv, u_nonlinconv_final)
plt.title('Convection Non Lineaire 1D')
plt.legend()
plt.xlabel('Distance (x)')
plt.ylabel('Vitesse (u)')
plt.grid()
plt.show()

