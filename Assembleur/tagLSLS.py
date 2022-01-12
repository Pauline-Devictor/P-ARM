class tagLSLS:

    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):

        try :
            binaire = "0100000010"

            Rdn, Rm = self.__donnees[1].split(", ")
            Rdn = Rdn[1:]
            Rm = Rm[1:]

            binaire += imm3(int(Rm))
            binaire += imm3(int(Rdn))

            return binaire
        except :
            print ("ERREUR LSLS 1")

        try :
            binaire = "00000"

            Rd, Rm, imm5str = self.__donnees[1].split(", ")
            Rd = Rd[1:]
            Rm = Rm[1:]
            imm5str = imm5str[1:]

            binaire += imm5(int(imm5str))
            binaire += imm3(int(Rm))
            binaire += imm3(int(Rd))

            return binaire
        except :
            print ("ERREUR LSLS 2")

        print ("----------------------------------")

def imm5(nb):
    if nb < 0:
        print ("BIZZAR")
        return bin(nb & 0b11111)[2:]
    if nb == 0:
        return "00000"
    else :
        a = bin(nb)[2:]
        while len(a) != 5 :
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
