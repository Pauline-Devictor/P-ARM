class tagCMP:


    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):

        try :
            binaire = "00101"

            Rd, imm8str = self.__donnees[1].split(", #")
            Rd = Rd[1:]

            binaire += imm3(int(Rd))
            binaire += imm8(int(imm8str))

            return binaire
        except :
            print ("ERREUR CMP 1")

        try :
            binaire = "0100001010"

            Rd, Rn = self.__donnees[1].split(", ")
            Rd = Rd[1:]
            Rn = Rn[1:]

            binaire += imm3(int(Rn))
            binaire += imm3(int(Rd))

            return binaire
        except :
            print ("ERREUR CMP 2")


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
