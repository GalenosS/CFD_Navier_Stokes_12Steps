import numpy as np

def linear_convection_2d(nx=81, ny=81, nt=100, c=1, sigma=0.2, xtot=2, ytot=2):
    """
    Resout l'equation de convection lineaire en 2D.
    Args:
        nx, ny (int): Nombre de points de grille en x et y.
        c (float): Vitesse de propagation.
        nt (int): Nombre de pas de temps.
        sigma (float): Nombre de Courant (CFL).
    Returns:
        X, Y (meshgrid): Les coordonnees pour le trace 3D.
        u (array 2D): Le champ de vitesse final.
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    # Calcul du pas de temps stable pour la 2D

    dt = sigma / (c/dx + c/dy)

    # Coordonnees (Meshgrid est essentiel pour la 3D)
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    #Initialisation "pave" carre au milieu
    u = np.ones((ny, nx))
    u[int(0.5 / dy):int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2
    # # Initialisation plus fine
    # u = np.full((ny, nx), 1.0) 
    # u[:, int(0.5 / dx):int(1 / dx + 1)] = 2
    

    # Boucle Temporelle
    for n in range(nt + 1): # +1 pour faire exactement nt pas
        un = u.copy()
        
        # Discretisation 2D :
        # u[j, i] depend de son voisin de gauche (i-1) ET de son voisin du bas (j-1)
        # On utilise le slicing numpy pour eviter une double boucle 'for' (tres lent en Python)
        
        # u[1:, 1:] represente tous les points sauf la premiere ligne et premiere colonne
        # C'est l'equivalent de for j in range(1, ny): for i in range(1, nx):
        
        u[1:, 1:] = (un[1:, 1:] - 
                     (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) - 
                     (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
                     
        # Conditions aux limites (Boundary Conditions)
        # On force les bords a rester a 1
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

    return X, Y, u

def nonlinear_convection_2d(nx=81, ny=81, nt=100, sigma=0.2, xtot=2, ytot=2):
    """
    Resout l'equation de convection non lineaire en 2D.
    Args:
        nx, ny (int): Nombre de points de grille en x et y.
        nt (int): Nombre de pas de temps.
        sigma (float): Nombre de Courant (CFL).
    Returns:
        X, Y (meshgrid): Les coordonnees pour le trace 3D.
        u (array 2D): Le champ de vitesse final.
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    # Calcul du pas de temps stable pour la 2D

    dt = sigma / (2/dx + 2/dy)

    # Coordonnees (Meshgrid est essentiel pour la 3D)
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    #Initialisation "pave" carre au milieu
    u = np.ones((ny, nx))
    u[int(0.5 / dy):int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2
    # # Initialisation plus fine
    # u = np.full((ny, nx), 1.0) 
    # u[:, int(0.5 / dx):int(1 / dx + 1)] = 2
    

    # Boucle Temporelle
    for n in range(nt + 1): # +1 pour faire exactement nt pas
        un = u.copy()
        
        # Discretisation 2D :
        # u[j, i] depend de son voisin de gauche (i-1) ET de son voisin du bas (j-1)
        # On utilise le slicing numpy pour eviter une double boucle 'for' (tres lent en Python)
        
        # u[1:, 1:] represente tous les points sauf la premiere ligne et premiere colonne
        # C'est l'equivalent de for j in range(1, ny): for i in range(1, nx):
        
        u[1:, 1:] = (un[1:, 1:] - 
                     (un[1:, 1:] * dt / dx * (un[1:, 1:] - un[1:, :-1])) - 
                     (un[1:, 1:] * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
                     
        # Conditions aux limites (Boundary Conditions)
        # On force les bords a rester a 1
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

    return X, Y, u

def diffusion_2d(nx=31, ny=31, nt=17, nu=0.05, sigma=0.25, xtot=2, ytot=2):
    """
    Resout l'equation de diffusion pure en 2D (Chaleur).
    ?u/?t = ?(?�u/?x� + ?�u/?y�)
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    # Calcul de stabilite pour la diffusion (CFL visqueux)
    dt = sigma * dx * dy / nu # Simplifie, ou votre formule plus precise :
    dt = sigma / (nu / dx**2 + nu / dy**2)

    # Grille
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    # Initialisation (Fonction Chapeau)
    u = np.ones((ny, nx))
    u[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dx+1)] = 2
    
    # Boucle Temporelle
    for n in range(nt):
        un = u.copy()
        
        # --- ReSOLUTION VECTORIELLE (Slicing) ---
        # Schema : u_ij = un_ij + (nu*dt/dx^2 * (voisin_droite - 2*centre + voisin_gauche))
        
        u[1:-1, 1:-1] = (un[1:-1, 1:-1] + 
                        nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) + 
                        nu * dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]))
        
        # Conditions aux limites (Murs a 1)
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

    return X, Y, u

def burgers_2d(nx=41, ny=41, nt=120, nu=0.01, sigma=0.0009, xtot=2, ytot=2):
    """
    Résout l'équation de Burgers couplée en 2D.
    Système de 2 équations pour u et v.
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    # --- SECURITÉ STABILITÉ (CFL) ---
    # On calcule la limite imposée par la viscosité
    limit_viscosite = (dx * dy) / nu * sigma
    # On calcule la limite imposée par la vitesse (Convection)
    # On suppose une vitesse max d'environ 2.0 m/s (valeur de la bosse)
    vitesse_max = 2.0
    limit_convection = (dx / vitesse_max) * 0.2  # 0.2 est un facteur de sécurité
    
    # On prend LE PLUS PETIT des deux pour être sûr de ne pas exploser
    dt = min(limit_viscosite, limit_convection)

    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    # --- Initialisation (u et v) ---
    u = np.ones((ny, nx))
    v = np.ones((ny, nx))
    
    # On place le "pavé" de vitesse initiale
    u[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dx+1)] = 2
    v[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dx+1)] = 2
    
    # --- Boucle Temporelle ---
    for n in range(nt):
        un = u.copy()
        vn = v.copy()
        
        # C'est ici que ça se corse !
        # On calcule u (en utilisant un et vn)
        # Terme 1 : Convection u*du/dx
        # Terme 2 : Convection v*du/dy
        # Terme 3 : Diffusion Laplacien(u)
        
        u[1:-1, 1:-1] = (un[1:-1, 1:-1] -
                     dt / dx * un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, :-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[:-2, 1:-1]) +
                     nu * dt / dx**2 * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) +
                     nu * dt / dy**2 * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]))

        # On fait exactement pareil pour v (en remplaçant u par v dans les dérivées)
        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                     dt / dx * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, :-2]) -
                     dt / dy * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[:-2, 1:-1]) +
                     nu * dt / dx**2 * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) +
                     nu * dt / dy**2 * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1]))
                     
        # Conditions aux limites (Murs à 1)
        u[0, :] = 1; u[-1, :] = 1; u[:, 0] = 1; u[:, -1] = 1
        v[0, :] = 1; v[-1, :] = 1; v[:, 0] = 1; v[:, -1] = 1
        
    return X, Y, u, v

def laplace_2d(nx=31, ny=31, l1norm_target=1e-4, xtot=2, ytot=1):
    """
    Résout l'équation de Laplace (∇²p = 0) par méthode itérative.
    Args:
        l1norm_target (float): Critère d'arrêt (précision voulue).
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)

    # Initialisation : Pression nulle partout
    p = np.zeros((ny, nx))
    
    # Conditions aux limites initiales (Boundary Conditions)
    # x=0 : p=0 (Côté gauche)
    # x=2 : y (Linéaire, côté droit)
    # y=0 : p=0 (Bas)
    # y=1 : p=0 (Haut)
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)
    
    # On impose la condition complexe sur le bord droit (x=xtot)
    # p = y sur le bord droit
    p[:, -1] = y 

    # Boucle Itérative (On ne boucle pas sur le temps, mais sur la convergence)
    l1norm = 1
    it = 0
    
    while l1norm > l1norm_target:
        pn = p.copy()
        
        # Formule de la moyenne des 4 voisins
        p[1:-1, 1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, :-2]) +
                          dx**2 * (pn[2:, 1:-1] + pn[:-2, 1:-1])) /
                         (2 * (dx**2 + dy**2)))
        
        # Ré-imposition des conditions aux limites à chaque tour
        p[:, 0] = 0        # Gauche (p=0)
        p[:, -1] = y       # Droite (p=y)
        p[0, :] = p[1, :]  # Bas (Neumann: dp/dy = 0 -> p[0] = p[1])
        p[-1, :] = p[-2, :]# Haut (Neumann: dp/dy = 0)
        
        # Calcul de l'erreur (différence entre l'étape k et k+1)
        l1norm = (np.sum(np.abs(p[:]) - np.abs(pn[:])) / np.sum(np.abs(pn[:])))
        it += 1

    return X, Y, p, it


def poisson_2d(nx=50, ny=50, nt=100, xtot=2, ytot=2):
    """
    Résout l'équation de Poisson (∇²p = b).
    Nous allons créer deux 'spikes' dans le terme source b.
    """
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    # Initialisation
    p = np.zeros((ny, nx))
    b = np.zeros((ny, nx))
    
    # --- Création de la Source b ---
    # On place deux pics à des endroits précis (1/4 et 3/4 du domaine)
    b[int(ny / 4), int(nx / 4)]  = 100  # Source (Pousse fort)
    b[int(3 * ny / 4), int(3 * nx / 4)] = -100 # Puits (Aspire fort)

    # Boucle Itérative (Pseudo-temps pour relaxer la pression)
    for n in range(nt):
        pn = p.copy()
        
        # La formule magique de Poisson discrétisée :
        # p_new = (Moyenne_Voisins - b * dx^2)
        
        p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, :-2]) * dy**2 +
                          (pn[2:, 1:-1] + pn[:-2, 1:-1]) * dx**2 -
                          b[1:-1, 1:-1] * dx**2 * dy**2) / 
                         (2 * (dx**2 + dy**2)))

        # Conditions aux limites (Pression nulle aux bords)
        p[0, :] = 0
        p[nx-1, :] = 0
        p[:, 0] = 0
        p[:, ny-1] = 0

    return X, Y, p, b


def cavity_flow(nx=41, ny=41, nt=500, nit=50, rho=1, nu=0.1, dt=0.001):
    """
    Résout les équations de Navier-Stokes pour l'écoulement en cavité.
    Args:
        nit (int): Nombre d'itérations internes pour résoudre la pression (Poisson).
    """
    xtot, ytot = 2, 2
    dx = xtot / (nx - 1)
    dy = ytot / (ny - 1)
    
    x = np.linspace(0, xtot, nx)
    y = np.linspace(0, ytot, ny)
    X, Y = np.meshgrid(x, y)

    # Initialisation : Tout est à zéro au début
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))
    p = np.zeros((ny, nx)) 
    b = np.zeros((ny, nx))
    
    # BOUCLE TEMPORELLE (On avance dans le temps)
    for n in range(nt):
        un = u.copy()
        vn = v.copy()
        
        # --- ETAPE 1 : Calcul du terme Source 'b' pour Poisson ---
        # C'est la divergence de la vitesse qui crée la pression
        b[1:-1, 1:-1] = (rho * (1 / dt * ((un[1:-1, 2:] - un[1:-1, 0:-2]) / (2 * dx) + 
                         (vn[2:, 1:-1] - vn[0:-2, 1:-1]) / (2 * dy)) -
                        ((un[1:-1, 2:] - un[1:-1, 0:-2]) / (2 * dx))**2 -
                        2 * ((un[2:, 1:-1] - un[0:-2, 1:-1]) / (2 * dy) *
                             (vn[1:-1, 2:] - vn[1:-1, 0:-2]) / (2 * dx)) -
                        ((vn[2:, 1:-1] - vn[0:-2, 1:-1]) / (2 * dy))**2))

        # --- ETAPE 2 : Résolution de la Pression (Boucle interne Poisson) ---
        for q in range(nit):
            pn = p.copy()
            p[1:-1, 1:-1] = (((pn[1:-1, 2:] + pn[1:-1, 0:-2]) * dy**2 + 
                              (pn[2:, 1:-1] + pn[0:-2, 1:-1]) * dx**2) /
                             (2 * (dx**2 + dy**2)) -
                             dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * b[1:-1, 1:-1])

            # Conditions aux limites pour la Pression (dp/dn = 0 aux murs)
            p[:, -1] = p[:, -2] # dp/dx = 0 à x = 2
            p[0, :] = p[1, :]   # dp/dy = 0 à y = 0
            p[:, 0] = p[:, 1]   # dp/dx = 0 à x = 0
            p[-1, :] = 0        # p = 0 à y = 2 (Couvercle) -> Référence de pression

        # --- ETAPE 3 : Mise à jour des Vitesses (Navier-Stokes) ---
        # u = u_prev + Convection + Pression + Diffusion
        u[1:-1, 1:-1] = (un[1:-1, 1:-1]-
                         un[1:-1, 1:-1] * dt / dx *
                        (un[1:-1, 1:-1] - un[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                        (un[1:-1, 1:-1] - un[0:-2, 1:-1]) -
                         dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                         nu * (dt / dx**2 *
                        (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                         dt / dy**2 *
                        (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1])))

        v[1:-1, 1:-1] = (vn[1:-1, 1:-1] -
                         un[1:-1, 1:-1] * dt / dx *
                        (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) -
                         vn[1:-1, 1:-1] * dt / dy *
                        (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) -
                         dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                         nu * (dt / dx**2 *
                        (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) +
                         dt / dy**2 *
                        (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1])))

        # --- Conditions aux limites pour les Vitesses ---
        # Murs immobiles
        u[0, :]  = 0
        u[:, 0]  = 0
        u[:, -1] = 0
        v[0, :]  = 0
        v[-1, :] = 0
        v[:, 0]  = 0
        v[:, -1] = 0
        
        # LE COUVERCLE MOBILE (Lid)
        u[-1, :] = 1  # Vitesse u = 1 tout en haut (y=2)

    return X, Y, u, v, p