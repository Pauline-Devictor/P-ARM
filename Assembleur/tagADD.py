class tagADD:


    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        binaire = "101100000"

        inutile, imm7str = self.__donnees[1].split(", sp, #")

        binaire += imm7(int(int(imm7str)/4))

        return binaire


def imm7(nb):
    if nb < 0:
        print ("BIZZAR")
        return bin(nb & 0b1111111)[2:]
    if nb == 0:
        return "0000000"
    else :
        a = bin(nb)[2:]
        while len(a) != 7 :
            a = "0" + a
        return a
