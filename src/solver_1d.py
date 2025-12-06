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




def diffusion_1d(nx=41, nt=25, nu=0.3, sigma=0.2, xtot= 2):
    """
    Resout l'equation de diffusion 1D.
    Args:
    nx (int): Nombre de points de grille.
    nt (int): Nombre de pas de temps.
    nu (float): Coefficient de diffusion.
    sigma (float): Nombre de Courant (CFL).
    Returns:
    x (array): Coordonnees x.
    u (array): Vitesse finale.
    """
    dx = xtot / (nx - 1)
    dt = sigma * dx**2 / nu  # stabilite CFL
    # Initialisation
    u = np.ones(nx)
    u[int(0.5 / dx):int(1 / dx + 1)] = 2  # condition initiale
    
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx - 1):
            u[i] = un[i] + nu * dt / dx**2 * (un[i + 1] - 2 * un[i] + un[i - 1])
    x = np.linspace(0, xtot, nx)
    return x, u




def burgers_equation(nx=101, nt=100, nu=0.3, sigma=0.2, xtot= 2):
    """
    Resout l'equation de Burgers 1D.
    Args:
    nx (int): Nombre de points de grille.
    nt (int): Nombre de pas de temps.
    nu (float): Coefficient de viscosite.
    sigma (float): Nombre de Courant (CFL).
    Returns:
    x (array): Coordonnees x.
    u (array): Vitesse finale.
    """
    dx = xtot / (nx - 1)

    limit_convection = dx / 2.5       # Base sur la vitesse max de la vague
    limit_diffusion = dx**2 / (2*nu)  # Base sur la viscosite
    
    # On prend le plus petit des deux (le plus prudent)
    dt = sigma * min(limit_convection, limit_diffusion)

    # Initialisation
    u = np.full(nx, 2.0)
    u[int(0.5 / dx) : int(1 / dx + 1)] = 5
    
    for n in range(nt):
        un = u.copy()
        for i in range(1, nx - 1):
            u[i] = (un[i] - un[i] * dt / dx * (un[i] - un[i - 1]) +
                     nu * dt / dx**2 * (un[i + 1] - 2 * un[i] + un[i - 1]))
    x = np.linspace(0, xtot, nx)
    return x, u