from Branche import *

class TouteLesBranches :

    def __init__(self,ligneImportante):
        self.__lignesImportante = ligneImportante
        self.__lienBranche = []

    def creationLien(self):
        lenLignesImportante = len(self.__lignesImportante)
        k=0
        for i in range (lenLignesImportante):
            if self.__lignesImportante[k][:6] == ".LBB0_" :
                self.__lienBranche.append(Branche(self.__lignesImportante[k][:-2],k+1))
                self.__lignesImportante.pop(k)
            else :
                k+=1

    def detail(self):
        print ("\n  Voici le lien de toutes les branches: \n")
        for i in self.__lienBranche:
            i.detail()

    def detail2(self):
        print ("\n  Voici tout les lignes retenues comme importante sans branche: \n")
        for i in self.__lignesImportante:
            print (i)

    def getLigneSansLien(self):
        return self.__lignesImportante

    def getNcible(self,name):
        for i in self.__lienBranche:
            if i.name == name :
                return i.numeroLigne
        print("BUG !!!")
