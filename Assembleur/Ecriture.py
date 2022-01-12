class Ecriture:

        def __init__(self,ligneAEcrire,emplacement):
            self.__ligneAEcrire = ligneAEcrire
            self.__emplacement = emplacement[:-2] + "2.bin"
            #print(self.__ligneAEcrire)

        def ecrire(self):
            f = open(self.__emplacement, "w")
            f.write("v2.0 raw\n")
            ligneTotal = ""
            for ligne in self.__ligneAEcrire:
                ligneTotal += ligne + " "
            f.write(ligneTotal[:-1] + "\n")
            f.close()
