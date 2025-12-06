import matplotlib.pyplot as plt
import sys

sys.path.append('../src')  
from solver_1d import *



# #Convection lineaire

# x_linconv, u_linconv_final = linear_convection(nx=101, c=1.0, nt=50, sigma=0.5, xtot = 10)

# plt.plot(x_linconv, u_linconv_final)
# plt.title('Convection Lineaire 1D')
# plt.legend()
# plt.xlabel('Distance (x)')
# plt.ylabel('Vitesse (u)')
# plt.grid()
# plt.show()


# #Convection non-lineaire

# x_nonlinconv, u_nonlinconv_final = nonlinear_convection(nx=101, nt=50, sigma=0.5, xtot = 10)

# plt.plot(x_nonlinconv, u_nonlinconv_final)
# plt.title('Convection Non Lineaire 1D')
# plt.legend()
# plt.xlabel('Distance (x)')
# plt.ylabel('Vitesse (u)')
# plt.grid()
# plt.show()

# #Diffusion
# x_diff, u_diff_init = diffusion_1d(nx=51, nt=0, nu=0.3, sigma=0.2, xtot = 10)
# x_diff_final, u_diff_final = diffusion_1d(nx=51, nt=50, nu=0.3, sigma=0.2, xtot = 10)

# plt.figure(figsize=(10, 6))

# plt.plot(x_diff, u_diff_init, 'b--', label='Initial (Carre)')
# plt.plot(x_diff_final, u_diff_final, 'r-', linewidth=2, label='Apres diffusion (Viscosite)')

# plt.title('etape 3 : Diffusion 1D (equation de la Chaleur)')
# plt.xlabel('Distance (m)')
# plt.ylabel('Vitesse (m/s)')
# plt.legend()
# plt.grid(True)
# plt.show()

#Equation de Burgers

# --- Parametres communs ---
nx = 101 
nt = 100
xtot = 2 * np.pi 

# --- Definition des viscosites ---
nu_haute = 1
nu_basse = 0.05

# --- Experience A : Haute Viscosite ---
# On utilise la variable 'nu_haute'
x_visq, u_visq = burgers_equation(nx=nx, nt=nt, nu=nu_haute, xtot=xtot)

# --- Experience B : Basse Viscosite ---
# On utilise la variable 'nu_basse'
x_nonvisq, u_nonvisq = burgers_equation(nx=nx, nt=nt, nu=nu_basse, xtot=xtot)

# --- Graphique ---
plt.figure(figsize=(10, 6))

# On recree l'initiale pour comparer
dx = xtot / (nx - 1)
u_init = np.full(nx, 2.0)
u_init[int(0.5 / dx) : int(1 / dx + 1)] = 5
plt.plot(x_visq, u_init, 'k--', alpha=0.5, label='Initial')

# Resultats avec les legendes dynamiques (f-strings)
plt.plot(x_visq, u_visq, 'b-', label=f"Haute Viscosite (nu={nu_haute})")
plt.plot(x_nonvisq, u_nonvisq, 'r-', label=f"Faible Viscosite (nu={nu_basse})")

plt.title('etape 4 : equation de Burgers\n(Competition Convection vs Diffusion)')
plt.xlabel('Distance (m)')
plt.ylabel('Vitesse (m/s)')
plt.legend(loc='best') # 'best' demande à matplotlib de placer la legende là où ça gêne le moins
plt.grid(True)
plt.show()