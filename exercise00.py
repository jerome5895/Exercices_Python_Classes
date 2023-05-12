import sys


class Rectangle:
    def __init__(self, largeur, longueur, couleur):
        self.largeur, self.longueur, self.couleur = largeur, longueur, couleur
        self.surface()

    def __call__(self, largeur, longueur, couleur):
        self.largeur, self.longeur, self.couleur = largeur, longueur, couleur

    def __str__(self):
        return (f"Ce rectangle a {self.largeur} cm de largeur, {self.longueur} cm de longueur, et est de couleur {self.couleur}. Sa surface est de {self.surface()} metres carres.")

    def surface(self):
        self.calculate_surface = self.largeur * self.longueur
        return self.calculate_surface

# Main program
if __name__ == '__main__':
    largeur = int(sys.argv[1])
    longueur = int(sys.argv[2])
    rectangle1 = Rectangle(largeur, longueur, "vert")
    print(rectangle1)