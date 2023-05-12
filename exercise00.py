
class Rectangle:
    def __init__(self, largeur, longueur, couleur):
        self.largeur, self.longueur, self.couleur = largeur, longueur, couleur

    def __call__(self, largeur, longueur, couleur):
        self.largeur, self.longeur, self.couleur = largeur, longueur, couleur

    def __str__(self):
        return (f"Ce rectangle a {self.largeur} de largeur, {self.longueur} de longueur, et est de couleur {self.couleur}.")


if __name__ == '__main__':
    rectangle1 = Rectangle()
    print(rectangle1)