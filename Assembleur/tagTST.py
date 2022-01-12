class tagTST:

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        binaire = "0100001000"

        Rn, Rm = self.__donnees[1].split(", ")
        Rn = Rn[1:]
        Rm = Rm[1:]

        binaire += imm3(int(Rm))
        binaire += imm3(int(Rn))

        return binaire


def imm3(nb):
    if nb == 0:
        return "000"
    else :
        a = bin(nb)[2:]
        while len(a) != 3 :
            a = "0" + a
        return a
