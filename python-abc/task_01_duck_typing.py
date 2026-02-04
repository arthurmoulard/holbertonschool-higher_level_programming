#!/usr/bin/python3


from abc import ABC, abstractmethod
# Importe le module pour créer des classes abstraites et des méthodes abstraites.

import math
# Importe le module math pour accéder à des constantes et fonctions mathématiques, comme pi.

# Définition d'une classe abstraite "Shape"
class Shape(ABC):
    @abstractmethod
    def area(self):
        # Méthode abstraite pour calculer l'aire d'une forme
        pass

    @abstractmethod
    def perimeter(self):
        # Méthode abstraite pour calculer le périmètre d'une forme
        pass


# Classe concrète "Circle" héritant de "Shape"
class Circle(Shape):
    def __init__(self, radius):
        # Constructeur qui initialise le rayon du cercle
        self.radius = radius

    def area(self):
        # Calcul de l'aire du cercle : π * r²
        return(math.pi * self.radius * self.radius)
    
    def perimeter(self):
        # Calcul du périmètre du cercle : 2 * π * r
        return(2 * math.pi * self.radius)
    

# Classe concrète "Rectangle" héritant de "Shape"
class Rectangle(Shape):
    def __init__(self, width, height):
        # Constructeur qui initialise la largeur et la hauteur du rectangle
        self.width = width
        self.height= height
        
    def area(self):
        # Calcul de l'aire du rectangle : largeur * hauteur
        return(self.height * self.width)

    def perimeter(self):
        # Calcul du périmètre du rectangle : 2 * (largeur + hauteur)
        return((2 * self.height) + (2 * self.width))
    


# Fonction utilitaire pour afficher les informations d'une forme
def shape_info(Shape):
    # Affiche l'aire et le périmètre de la forme passée en argument
    # ATTENTION : le paramètre doit être une instance d'une sous-classe de Shape
    print("area:", Shape.area())
    print("perimeter:", Shape.perimeter())
