class tagSUBS:


    def __init__(self,donnees):
        self.__donnees = donnees

    def hexa(self):
        try :
            binaire = "00111"
            Rdn, imm8str = self.__donnees[1].split(", #")
            Rdn = Rdn[1:]
            binaire += imm3(int(Rdn))
            binaire += imm8(int(imm8str))
            return binaire
        except :
            print ("ERREUR SUBS 1")
        try :
            Rd, Rn, Rm = self.__donnees[1].split(", ")
            Rd = Rd[1:]
            Rn = Rn[1:]
            Rm = Rm[1:]

            if Rm[:1] == "#":
                binaire = "0001111"
            else :
                binaire = "0001101"
                
            binaire += imm3(int(Rm))
            binaire += imm3(int(Rn))
            binaire += imm3(int(Rd))
            return binaire
        except :
            print ("ERREUR SUBS 2")
        print("-------------------------------------")

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
