class tagSTR:


    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        binaire = "10010"

        try :
            Rt, imm8str = self.__donnees[1].split(", [sp, #")
            Rt = Rt[1:]
            imm8str = imm8str[:-1]
            binaire += imm3(int(Rt))
            binaire += imm8(int(int(imm8str)/4))

        except :
            Rt = self.__donnees[1].split(", [sp]")[0]
            Rt = Rt[1:]
            binaire += imm3(int(Rt))
            binaire += imm8(0)

        return binaire


def imm8(nb):
    if nb < 0:
        print ("BIZZAR")
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
