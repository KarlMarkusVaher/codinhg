import requests
from bs4 import BeautifulSoup
import random
import re

URL = "https://tavast.ee/1000-sagedamat-sona-mida-qsis-pole/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

sõnad = []

for a in soup.findAll('a', {'target': '_blank'}):
    sõnad.append(a['href'].split('/')[-1])
    
# print(sõnad)

val_sõna = random.choice(sõnad)

# print(val_sõna)


tähed = list(val_sõna)
peidus = list(val_sõna)

for i in range(len(peidus)):
    peidus[i] = 0
    
#print(tähed)
# print(peidus)

elud = 10

öeldud = []

while True:
    i = 0
    for t in tähed:
        if peidus[i] == 1:
            print(t, end="")
        else:
            print("-", end="")
        i += 1
    print("\n")
            
    taht = input("Pange täht kurat: ")
    if len(taht) != 1:
        print("ei")
        print(öeldud)
        
    elif re.search("[0-9]", taht):
        print("ei numbreid")
        print(öeldud)
        
    elif taht in öeldud:
        print("Täht juba kasutatud")
        print(öeldud)
        
    elif taht in val_sõna: 
        print("Täht oli olemas")
        i = 0
        öeldud.append(taht)
        print("sul on " + str(elud) + " elusi")
        print(öeldud)
        for t in tähed:
            if t == taht:
                peidus[i] = 1
            i += 1
        
    else:
        print("Täht ei olnud")
        öeldud.append(taht)
        print(öeldud)
        elud -= 1
        print("sul on " + str(elud) + " elusi jäänud.")
    
    if elud == 0:
        print("Elud said otsa :(")
        break
          
    x = all(peidus)
    if x == True:
        print("Sa võitsid!")
        break
    
print(peidus)