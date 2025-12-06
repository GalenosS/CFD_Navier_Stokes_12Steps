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

# """
# Equation de Burgers non lineaire en 2D.
# """

# X, Y, u, v = burgers_2d(nx=nx, ny=ny, nt=nt, nu=nu, sigma=sigma, xtot=xtot, ytot=ytot)

# # --- 3. Visualisation 3D ---
# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.add_subplot(111, projection='3d')

# # Trace de la surface
# # rstride/cstride : Sauter des lignes pour alléger le rendu graphique
# surf = ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2, linewidth=0, antialiased=False)

# # Labels et Titres
# ax.set_title(f'Burgers 2D (t={nt}, nu={nu})\nConvection + Diffusion couplées')
# ax.set_xlabel('Axe X')
# ax.set_ylabel('Axe Y')
# ax.set_zlabel('Vitesse U')


# # Barre de couleur
# fig.colorbar(surf, shrink=0.5, aspect=5, label='Vitesse (m/s)')

# # Ajuster l'angle de vue pour mieux voir le "choc"
# ax.view_init(elev=30, azim=240)

# plt.show()

# """
# Equation de Laplace en 2D.
# """

# X, Y, p, iterations = laplace_2d(nx=31, ny=31, l1norm_target=1e-4)

# print(f"Équilibre atteint en {iterations} itérations.")

# # Visualisation 3D
# fig = plt.figure(figsize=(11, 7))
# ax = fig.add_subplot(111, projection='3d')

# surf = ax.plot_surface(X, Y, p, cmap=cm.viridis, rstride=1, cstride=1, linewidth=0, antialiased=False)

# ax.set_title(f'Équation de Laplace (Équilibre de Pression)\nConverge en {iterations} itérations')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Pression P')
# ax.view_init(elev=30, azim=220)

# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()


# """
# Equation de Poisson en 2D.
# """
# # On lance le calcul
# # On fait 100 itérations pour laisser la pression s'établir
# X, Y, p, b = poisson_2d(nx=50, ny=50, nt=100)

# # Visualisation 3D
# fig = plt.figure(figsize=(11, 7))
# ax = fig.add_subplot(111, projection='3d')

# surf = ax.plot_surface(X, Y, p, cmap=cm.coolwarm, rstride=1, cstride=1, linewidth=0, antialiased=False)

# ax.set_title('Équation de Poisson (Source + Puits)')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Pression P')
# ax.view_init(elev=30, azim=220)

# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()


"""
Equation de Navier-Stokes en 2D.
"""

# --- Simulation ---
print("Démarrage de Navier-Stokes (Cavity Flow)...")
# On lance 700 pas de temps pour que le tourbillon s'installe bien
# nit=50 assure que la pression est bien calculée à chaque étape
X, Y, u, v, p = cavity_flow(nx=41, ny=41, nt=700, nit=50, rho=1, nu=0.1, dt=0.001)
print("Calcul terminé.")

# --- Visualisation 2D (Coupe) ---
fig = plt.figure(figsize=(11, 7), dpi=100)

# 1. On affiche la pression en fond (Contourf)
# alpha=0.5 rend la couleur un peu transparente pour voir les flèches
contour = plt.contourf(X, Y, p, alpha=0.5, cmap=cm.viridis)
plt.colorbar(contour, label='Pression')

# 2. On affiche le champ de vitesse (Quiver / Flèches)
# On saute quelques points (skip) pour ne pas surcharger le graphique
skip = 2
plt.quiver(X[::skip, ::skip], Y[::skip, ::skip], 
           u[::skip, ::skip], v[::skip, ::skip])

plt.title('Navier-Stokes : Cavité Entraînée\n(Flèches = Vitesse, Couleurs = Pression)')
plt.xlabel('X')
plt.ylabel('Y')

# On force un aspect carré
plt.axis('scaled')

plt.show()