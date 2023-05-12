import sys


class Rectangle:
    def __init__(self, largeur, longueur, couleur):
        self.largeur, self.longueur, self.couleur = largeur, longueur, couleur
        self.surface()


    def __call__(self, largeur, longueur, couleur):
        self.largeur, self.longeur, self.couleur = largeur, longueur, couleur


    def __str__(self):
        return (f"Ce rectangle a {self.largeur} cm de largeur, {self.longueur} cm de longueur, et est de couleur {self.couleur}. Sa surface est de {self.surface()} mètres carrés.")


    def surface(self):
        self.calculate_surface = self.largeur * self.longueur
        return self.calculate_surface





class Carre:
    def __init__(self, cote):
        self.cote = cote
        self.surface()


    def __call__(self, cote):
        self.cote = cote


    def __str__(self):
        return (f"Ce carré a {self.cote} de côté et a une surface de {self.calculate_surface} centimètres carré.")


    def surface(self):
        self.calculate_surface = self.cote * self.cote
        return self.calculate_surface
    


# Main program
if __name__ == '__main__':
    rectangle1 = Rectangle(5, 10, "vert")
    print(rectangle1)
    print("\n")
    carre1 = Carre(10)
    print(carre1)