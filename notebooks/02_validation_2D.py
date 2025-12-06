import matplotlib.pyplot as plt
from matplotlib import cm # Pour les couleurs (colormaps)
import sys
import numpy as np

# Importation du nouveau solver 2D
sys.path.append('../src')
from solver_2d import *

# --- Parametres ---
nx = 101
ny = 101
nt = 100
nu = 0.01
c = 1
sigma = 0.2
xtot = 5
ytot = 5

# --- Simulation ---
"""
Equation de convection lineaire en 2D.
"""
# # On lance le calcul
# X, Y, u = linear_convection_2d(nx=nx, ny=ny, nt=nt, c=c, sigma=sigma, xtot=xtot, ytot=ytot)

# # --- Visualisation 3D ---
# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.add_subplot(111, projection='3d')

# # Trace de la surface
# surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2, linewidth=0, antialiased=False)

# # Labels
# ax.set_title(f'Convection Lineaire 2D (t={nt})')
# ax.set_xlabel('Axe X')
# ax.set_ylabel('Axe Y')
# ax.set_zlabel('Vitesse U')

# # Barre de couleur sur le c�te
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

"""
Equation de convection non lineaire en 2D.
"""
# # On lance le calcul
# X, Y, u = nonlinear_convection_2d(nx=nx, ny=ny, nt=nt, sigma=sigma, xtot=xtot, ytot=ytot)

# # --- Visualisation 3D ---
# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.add_subplot(111, projection='3d')

# # Trace de la surface
# surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2, linewidth=0, antialiased=False)

# # Labels
# ax.set_title(f'Convection NonLineaire 2D (t={nt})')
# ax.set_xlabel('Axe X')
# ax.set_ylabel('Axe Y')
# ax.set_zlabel('Vitesse U')

# # Barre de couleur sur le c�te
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()


"""
Equation de diffusion non lineaire en 2D.
"""

# # On lance le calcul
# X, Y, u = diffusion_2d(nx=nx, ny=ny, nt=nt, nu=nu, sigma=sigma, xtot=xtot, ytot=ytot)

# # --- Visualisation 3D ---
# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.add_subplot(111, projection='3d')

# # Trace de la surface
# surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2, linewidth=0, antialiased=False)

# # Labels
# ax.set_title(f'Convection NonLineaire 2D (t={nt})')
# ax.set_xlabel('Axe X')
# ax.set_ylabel('Axe Y')
# ax.set_zlabel('Vitesse U')

# # Barre de couleur sur le c�te
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

"""
Equation de Burgers non lineaire en 2D.
"""

X, Y, u, v = burgers_2d(nx=nx, ny=ny, nt=nt, nu=nu, sigma=sigma, xtot=xtot, ytot=ytot)

# --- 3. Visualisation 3D ---
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.add_subplot(111, projection='3d')

# Trace de la surface
# rstride/cstride : Sauter des lignes pour alléger le rendu graphique
surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2, linewidth=0, antialiased=False)

# Labels et Titres
ax.set_title(f'Burgers 2D (t={nt}, nu={nu})\nConvection + Diffusion couplées')
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Vitesse U')


# Barre de couleur
fig.colorbar(surf, shrink=0.5, aspect=5, label='Vitesse (m/s)')

# Ajuster l'angle de vue pour mieux voir le "choc"
ax.view_init(elev=30, azim=240)

plt.show()