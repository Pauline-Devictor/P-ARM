class tagRSBS:

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        binaire = "0100001001"

        Rd, Rn, inutile = self.__donnees[1].split(", ")
        Rd = Rd[1:]
        Rn = Rn[1:]

        binaire += imm3(int(Rn))
        binaire += imm3(int(Rd))

        return binaire


def imm3(nb):
    if nb == 0:
        return "000"
    else :
        a = bin(nb)[2:]
        while len(a) != 3 :
            a = "0" + a
        return a
