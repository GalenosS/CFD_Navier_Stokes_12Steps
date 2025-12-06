import numpy as np

def linear_convection(nx=41, c=1.0, nt=25, sigma=0.5, xtot= 3):
        """
        Resout l'equation de convection lineaire 1D.
        Args:
        nx (int): Nombre de points de grille.
        c (float): Vitesse de l'onde.
        nt (int): Nombre de pas de temps.
        sigma (float): Nombre de Courant (CFL).
        Returns:
        x (array): Coordonnees x.
        u (array): Vitesse finale.
        """

        dx = xtot / (nx - 1)
        dt = sigma * dx / c #stabilite CFL

        # Initialisation

        u = np.ones(nx)
        u[int(0.5 / dx):int(1 / dx + 1)] = 2  # condition initiale

        for n in range(nt):
            un = u.copy()
            for i in range(1, nx):
                u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

        x = np.linspace(0, xtot, nx)
        return x, u



def nonlinear_convection(nx=41, nt=25, sigma=0.5, xtot= 3):
        """
        Resout l'equation de convection non lineaire 1D.
        Args:
        nx (int): Nombre de points de grille.
        nt (int): Nombre de pas de temps.
        sigma (float): Nombre de Courant (CFL).
        Returns:
        x (array): Coordonnees x.
        u (array): Vitesse finale.
        """

        dx = xtot / (nx - 1)
        dt = sigma * dx / 2 #stabilite CFL

        # Initialisation

        u = np.ones(nx)
        u[int(0.5 / dx):int(1 / dx + 1)] = 2  # condition initiale

        for n in range(nt):
            un = u.copy()
            for i in range(1, nx):
                u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1])

        x = np.linspace(0, xtot, nx)

        return x, u