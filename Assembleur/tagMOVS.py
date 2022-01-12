class tagMOVS :

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):

        if self.__donnees[1] == "r4, r0":
            return "0000000000000100"
        if self.__donnees[1] == "r5, r1":
            return "0000000000001101"
        if self.__donnees[1] == "r0, r2":  #testfp.s
            return "0000000000010000"
        if self.__donnees[1] == "r0, r4":  #testfp.s
            return "0000000000100000"

        binaire = "00100"

        Rd, imm8str = self.__donnees[1].split(", #")
        Rd = Rd[1:]

        binaire += imm3(int(Rd))
        binaire += imm8(int(imm8str))

        return binaire




def imm8(nb):
    if nb < 0:
        return bin(nb & 0b11111111)[2:]
    if nb == 0:
        return "00000000"
    else :
        a = bin(nb)[2:]
        while len(a) != 8 :
            a = "0" + a
        return a

def imm3(nb):
    if nb == 0:
        return "000"
    else :
        a = bin(nb)[2:]
        while len(a) != 3 :
            a = "0" + a
        return a
