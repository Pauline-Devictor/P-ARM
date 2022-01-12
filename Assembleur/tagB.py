class tagB:

    def __init__(self,donnees,branches,Nsource):
        self.__donnees = donnees
        self.__branches = branches
        self.__Nsource = Nsource

    def hexa(self):
        Ncible = self.__branches.getNcible(self.__donnees[1])
        #print("Ncible: " + str(Ncible))

        binaire = ""

        tag = self.__donnees[0]
        if tag == "b":
            binaire += "11100"
            binaire += imm11(Ncible-self.__Nsource-3)
        else :
            binaire += "1101"
            if tag == "beq":
                binaire += "0000"
            elif tag == "bne":
                binaire += "0001"
            elif tag == "bcs":
                binaire += "0010"
            elif tag == "bhs":
                binaire += "0010"
            elif tag == "bcc":
                binaire += "0011"
            elif tag == "blo":
                binaire += "0011"
            elif tag == "bmi":
                binaire += "0100"
            elif tag == "bpl":
                binaire += "0101"
            elif tag == "bvs":
                binaire += "0110"
            elif tag == "bvc":
                binaire += "0111"
            elif tag == "bhi":
                binaire += "1000"
            elif tag == "bls":
                binaire += "1001"
            elif tag == "bge":
                binaire += "1010"
            elif tag == "blt":
                binaire += "1011"
            elif tag == "bgt":
                binaire += "1100"
            elif tag == "ble":
                binaire += "1101"
            elif tag == "bal":
                binaire += "1110"

            binaire += imm8(Ncible-self.__Nsource-3)

        return binaire

def imm11(nb):
    if nb < 0:
        return bin(nb & 0b11111111111)[2:]
    if nb == 0:
        return "00000000000"
    else :
        a = bin(nb)[2:]
        while len(a) != 11 :
            a = "0" + a
        return a

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
