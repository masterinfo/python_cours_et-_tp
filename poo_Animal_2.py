# liste_felix =['chat','noir et blanc',5,3,"croquette"]
# dict_felix ={ "race":'chat' ,"couleur" :'noir et blanc',
#               "poids":5 ,"age":3 ,"food":"croquette"}

# liste_titi=['canari','jaune',0.5,4,"graines"]
# dict_titi ={ "race":'canari' ,"couleur" :'jaune',
#              "poids":0.5 ,"age":4 ,"food":"graines"}


class Animal:
	"""  ceci est la classe Animal"""
	def __init__(self, nom, couleur):
		self.nom = nom
		self.couleur = couleur

	def __str__(self):
		return " nom " + self.nom + " couleur "  + self.couleur


# ****************instanciation ******************/
a1 = Animal("felix", 'noir et blanc')
print(a1.nom, "est", a1.couleur)

a2 = Animal("titi", 'jaune')
print(a2.nom, "est", a2.couleur)


print(a2)
print(a2.__dict__)
print(a2.__doc__)

