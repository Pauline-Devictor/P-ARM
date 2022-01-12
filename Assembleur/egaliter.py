
emplacement = "C:/Users/emile/Documents/Programmation/Python/assenbleur/s/calckeyb2.bin"
fichier = open(emplacement , "r")
contenu1 = fichier.readlines()
fichier.close()
contenu1bis = contenu1[1].split(" ")

emplacement = "C:/Users/emile/Documents/Ecole/Architecture/P-ARM/code_c/calckeyb.bin"
fichier = open(emplacement , "r")
contenu2 = fichier.readlines()
fichier.close()
contenu2bis = contenu2[1].split(" ")

if contenu1bis[0] != contenu2bis[0]:
    contenu1bis.pop(0)

k=0

for i in range(len(contenu1bis)):
    k+=1
    if (contenu1bis[i][:4] != contenu2bis[i][:4]):
        print(str(i )+" "+ contenu1bis[i] + " != != != " + contenu2bis[i])
        break
    else:
        print(str(i )+ " " +contenu1bis[i][:4] + " == " + contenu2bis[i][:4])

print (k)
