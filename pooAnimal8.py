


class Animal:
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur


# ****************instanciation ******************/
a1 = Animal("felix", 'noir et blanc')
print(a1.nom, "est", a1.couleur)

a2 = Animal("titi", 'jaune')
print(a2.nom, "est", a2.couleur)
