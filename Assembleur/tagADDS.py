class tagADDS:

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):

        try :

            Rd, Rn, imm3str = self.__donnees[1].split(", ")
            Rd = Rd[1:]
            Rn = Rn[1:]

            if imm3str[:1] == "#":
                binaire = "0001110"
            else :
                binaire = "0001100"

            imm3str = imm3str[1:]

            binaire += imm3(int(imm3str))
            binaire += imm3(int(Rn))
            binaire += imm3(int(Rd))

            return binaire
        except :
            print ("ERREUR ADDS 1")

        try :
            binaire = "00110"

            Rd, imm8str = self.__donnees[1].split(", #")
            Rd = Rd[1:]

            binaire += imm3(int(Rd))
            binaire += imm8(int(imm8str))

            return binaire
        except :
            print ("ERREUR ADDS 2")


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
