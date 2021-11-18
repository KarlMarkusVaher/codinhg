lause = str(input("Sisestage lause "))

def smt(lause):
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(" kuid ", ", kuid ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" vaid ", ", vaid ")
    print(lause)
    
smt(lause)