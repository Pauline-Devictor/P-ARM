from InformationUtile import *
from TouteLesBranches import *
from Traducteur import *
from Ecriture import *

emplacement = "s/simple_add.s"
fichier = open(emplacement , "r")
contenu = fichier.readlines()
fichier.close()

informationUtile = InformationUtile(contenu)
informationUtile.clear()
informationUtile.detail()

branches = TouteLesBranches(informationUtile.get())
branches.creationLien()
branches.detail()

trad = Traducteur(branches.getLigneSansLien())
trad.traductionbin(branches)
listeValHexa = trad.traductionhex()

Ecriture(listeValHexa, emplacement).ecrire()
