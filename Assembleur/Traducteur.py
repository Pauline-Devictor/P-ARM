from tagADCS import *
from tagADD import *
from tagADDS import *
from tagANDS import *
from tagASRS import *  #pas tester
from tagB import *
from tagBICS import *  #pas tester
from tagCMN import *  #pas tester
from tagCMP import *
from tagEORS import *  #pas tester
from tagLDR import *
from tagLSLS import *
from tagLSRS import *
from tagMOVS import *
from tagMULS import *
from tagMVNS import *  #pas tester
from tagORRS import *
from tagRORS import *
from tagRSBS import *
from tagSBCS import *
from tagSTR import *
from tagSUB import *
from tagSUBS import *
from tagTST import *  #pas tester



class Traducteur :

    def __init__(self,ligneATraduire):
        self.__ligneATraduire=ligneATraduire
        self.__ligneTraduitBIN=[]
        self.__ligneTraduitHEXA=[]

    def traductionbin(self,branches):
        i = 0
        print("\n  Voici lea traduction de Unified Assembler Language en codage Thumb:  \n")
        for ligne in self.__ligneATraduire:
            i += 1
            self.__ligneTraduitBIN.append(traduire(ligne.split("\t"),branches,i))

    def traductionhex(self):
        for ligneBIN in self.__ligneTraduitBIN:
            self.__ligneTraduitHEXA.append(BinToHexa(ligneBIN))
        return self.__ligneTraduitHEXA



def traduire(listTrad,branches,i):
    listTrad.pop(0)
    listTrad[-1] = listTrad[-1][:-1]
    print ("DONNEE: " + str(listTrad))
    tag = listTrad[0]
    if tag == "lsls":
        binaire = tagLSLS(listTrad).hexa()
        #print("FAUX ?")
        print(binaire)
    elif tag == "lsrs":
        binaire = tagLSRS(listTrad).hexa()
        #print("FAUX ?")
        print(binaire)
    elif tag == "asrs":
        binaire = tagASRS(listTrad).hexa()
        #rint("FAUX ?")
        print(binaire)
    elif tag == "adds":
        binaire = tagADDS(listTrad).hexa()
        #print("FAUX ?")
        print(binaire)
    elif tag == "subs":
        binaire = tagSUBS(listTrad).hexa()
        #print("FAUX ?")
        print(binaire)
    elif tag == "movs":
        binaire = tagMOVS(listTrad).hexa()
        print(binaire)
    elif tag == "cmp":
        binaire = tagCMP(listTrad).hexa()
        #print("FAUX ?")
        print(binaire)
    elif tag == "ands":
        binaire = tagANDS(listTrad).hexa()
        print(binaire)
    elif tag == "eors":
        binaire = tagEORS(listTrad).hexa()
        print(binaire)
    elif tag == "adcs":
        binaire = tagADCS(listTrad).hexa()
        print(binaire)
    elif tag == "sbcs":
        binaire = tagSBCS(listTrad).hexa()
        print(binaire)
    elif tag == "rors":
        binaire = tagRORS(listTrad).hexa()
        print(binaire)
    elif tag == "tst":
        binaire = tagTST(listTrad).hexa()
        print(binaire)
    elif tag == "rsbs":
        binaire = tagRSBS(listTrad).hexa()
        print(binaire)
    elif tag == "cmn":
        binaire = tagCMN(listTrad).hexa()
        print(binaire)
    elif tag == "orrs":
        binaire = tagORRS(listTrad).hexa()
        print(binaire)
    elif tag == "muls":
        binaire = tagMULS(listTrad).hexa()
        print(binaire)
    elif tag == "bics":
        binaire = tagBICS(listTrad).hexa()
        print(binaire)
    elif tag == "mvns":
        binaire = tagMVNS(listTrad).hexa()
        print(binaire)
    elif tag == "str":
        binaire = tagSTR(listTrad).hexa()
        print(binaire)
    elif tag == "ldr":
        binaire = tagLDR(listTrad).hexa()
        print(binaire)
    elif tag == "add":
        binaire = tagADD(listTrad).hexa()
        print(binaire)
    elif tag == "sub":
        binaire = tagSUB(listTrad).hexa()
        print(binaire)
    elif tag[:1] == "b":
        binaire = tagB(listTrad,branches,i).hexa()
        print(binaire)
    else :
        print("EREUR")
    print("")
    return binaire

def BinToHexa(binStr):
    nb1, nb2, nb3, nb4 = binStr[:4], binStr[4:8], binStr[8:12], binStr[12:]
    a = [nb1,nb2,nb3,nb4]
    nbHexa = ""
    for nb in a:
        if nb == "0000":
            nbHexa += "0"
        elif nb == "0001":
            nbHexa += "1"
        elif nb == "0010":
            nbHexa += "2"
        elif nb == "0011":
            nbHexa += "3"
        elif nb == "0100":
            nbHexa += "4"
        elif nb == "0101":
            nbHexa += "5"
        elif nb == "0110":
            nbHexa += "6"
        elif nb == "0111":
            nbHexa += "7"
        elif nb == "1000":
            nbHexa += "8"
        elif nb == "1001":
            nbHexa += "9"
        elif nb == "1010":
            nbHexa += "a"
        elif nb == "1011":
            nbHexa += "b"
        elif nb == "1100":
            nbHexa += "c"
        elif nb == "1101":
            nbHexa += "d"
        elif nb == "1110":
            nbHexa += "e"
        elif nb == "1111":
            nbHexa += "f"

    return nbHexa
