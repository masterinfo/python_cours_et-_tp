from sys import stdout
from sys import stdin

class Voiture:
    roues = 4
    moteur = 1

    def __init__(self):
        self.nom = "A déterminer"

class VoitureSport(Voiture):

    def __init__(self):
        self.nom = "Ferrari"


ma_voiture = Voiture()
print(ma_voiture.nom)
print(ma_voiture.roues)


ma_voiture_sport=VoitureSport()
print(ma_voiture_sport.nom)
print(ma_voiture_sport.roues)