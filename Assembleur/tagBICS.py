class tagBICS:

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        binaire = "0100001110"

        Rdn, Rm = self.__donnees[1].split(", ")
        Rdn = Rdn[1:]
        Rm = Rm[1:]

        binaire += imm3(int(Rm))
        binaire += imm3(int(Rdn))

        return binaire


def imm3(nb):
    if nb == 0:
        return "000"
    else :
        a = bin(nb)[2:]
        while len(a) != 3 :
            a = "0" + a
        return a
