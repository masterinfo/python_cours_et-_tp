from sys import stdout
from sys import stdin
liste_felix =['chat','noir et blanc',5,3,"croquette"]
dict_felix ={ "race":'chat' ,"couleur" :'noir et blanc', "poids":5 ,"age":3 ,"food":"croquette"}
#--------------
liste_titi=['canari','jaune',0.5,4,"graines"]
dict_titi ={ "race":'canari' ,"couleur" :'jaune', "poids":0.5 ,"age":4 ,"food":"graines"}

print("************liste **********************")
for champs in liste_titi:
	print( champs     )

print("**********************************")

print("************dictionnaire **********************")
for nomchamps in dict_titi.keys() :
	print( nomchamps     )

for nomvalue in dict_titi.values() :
	print( nomvalue     )


for nomchamps,nomvalue in dict_titi.items():
	print(nomchamps," => "  ,nomvalue)

print("**********************************")





#------------------------------------------
class Animal:

	def __init__(self, nom, age):
		 self.nom = nom



#****************instanciation ******************/
chat1_felix = Animal("felix")



print(chat1_felix.nom)
chat1_felix.nom= "toto"
print(chat1_felix.nom)
chat2=Animal("gros minet")
print(chat2.nom)
#**Vous pouvez à tout moment créer un attribut pour votre objet ****
chat1_felix.couleur ="rouge"
print(chat1_felix.couleur)
##print(chat2.couleur)

help(Animal)