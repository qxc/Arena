import csv

def createCard(name, cardType, text, image):
    code = "\\begin{tikzpicture} \n\cardbackground{" +cardType+ "}"
    code += "\cardtitle{" + name+ "} \n"
    code += "\cardborder{} \n"
    code += "\cardcontent{" + text + "} \n"
    code += "\cardimage{" + image + "} \n"
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
            cardType = row['type'].capitalize()            
            image = row['Image']
            text = row['Description']
            if cardType == "":
                continue
            if row['Card Status'] == "":
                continue
            card = createCard(name, cardType, text, image)
            #f.write(card)
            number = row['Supply'] #this line and the next are the ones i changed
            f.write(card*int(number))
    return

processCards()
