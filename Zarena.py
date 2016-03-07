import csv

def createCard(name, cardType, text, image, mini,player):
    code = "\\begin{tikzpicture} \n\cardbackground{" +cardType+ "}\n"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "}{" +mini + "} \n"
    code += "\player{" + player + "} \n"
    #if version != "":
     #   code += "\sync{" + version + "} \n"
    
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code

def createModCard(name, cardType, text, image, mini,player):
    code = "\\begin{tikzpicture} \n\modcardbackground{" +cardType+ "}\n"
    code += "\modifier{} \n \modcardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\modcardcontent{" + text + "} \n"
    code += "\modcardimage{" + image +  "}{" +mini + "} \n"
    code += "\player{" + player + "} \n"
    #if version != "":
     #   code += "\sync{" + version + "} \n"
    
    code += "\end{tikzpicture}\n\hspace{-4mm}\n"
    return code


def processCards(fileName = "cardList.csv"):
    f = open("cards.txt", "w")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            mod = row['Modifier']
            cardType = row['type'].capitalize()            
            image = row['Image']
            mini = row['MiniImage']
            text = row['Description']
            player = row['Player']
            if cardType == "":
                continue
            if row['Card Status'] == "":
                continue
            if mod == "":
                card = createCard(name, cardType, text, image, mini,player)
            else:
                card = createModCard(name, cardType, text, image, mini,player)
            #f.write(card)
            number = row['Supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
    return

processCards()
