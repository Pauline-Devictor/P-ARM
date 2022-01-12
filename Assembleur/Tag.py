class Tag :

    def __init__(self):
        fichier = open("info.txt" , "r")
        self.__toutTags = fichier.readlines()
        fichier.close()
        for i in range (len(self.__toutTags)):
            #print (str(self.__toutTags[i]))
            self.__toutTags[i] = self.__toutTags[i][:-1]
        #print ("Voici tout les tags pris en compte: ")
        #print (self.__toutTags)

    def tagCorrect(self,tagQuestion):
        for tag in self.__toutTags:
            if tagQuestion == tag :
                return True
        return False
