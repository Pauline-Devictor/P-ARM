class Branche :

    def __init__(self,name,numeroLigne):
        self.name=name
        self.numeroLigne=numeroLigne

    def detail(self):
        print (self.name + " a la ligne: " + str(self.numeroLigne))
