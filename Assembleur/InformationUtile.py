from Tag import *

class InformationUtile :

    def __init__(self,lignes):
        self.__listeLignes=lignes
        self.__listeLignesImportante=[]
        self.__tagImportant = Tag()


    def clear(self):
        for i in range (len(self.__listeLignes)):
            ligne = self.__listeLignes[i]

            ligneSplit = ligne.split("\t")
            lenLigneSplit = len(ligneSplit)

            if lenLigneSplit == 1:
                if ligneSplit[0][:6] == ".LBB0_":
                    self.__listeLignesImportante.append(ligne)
            else :
                if self.__tagImportant.tagCorrect(ligneSplit[1]) :
                    self.__listeLignesImportante.append(ligne)

    def detail(self):
        print ("\n  Voici tout les lignes retenues comme importante: \n")
        for i in self.__listeLignesImportante:
            print (i[:-1])

    def get(self):
        return self.__listeLignesImportante
