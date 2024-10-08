


class Animal:
	def __init__(self, race, nom, couleur, poids , age , food = "croquette"):

		self.race = race
		self.nom = nom
		self.couleur = couleur
		self.poids = poids
		self.age = age
		self.food = food

	def __str__(self) :
		return "je suis daans un objet de la classe animal"
		#return super().__str__()


# ****************instanciation ******************/
a1 = Animal("chat","felix", 'noir et blanc',5,3)
print(a1.nom, "est", a1.couleur)

a2 = Animal("canari","titi", "jaune", 0.5,4,"graines")
print(a2.nom, "est", a2.couleur)

print(a2)