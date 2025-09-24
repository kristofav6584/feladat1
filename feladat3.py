class Szamelemzo:
    def __init__(self,lista):
        self.lista = lista
    
    def szamol(self):
        pozitiv=0
        negativ=0
        nullErtek=0

        for i in self.lista:
            if i > 0:
                pozitiv +=1
            elif i < 0:
                negativ+=1
            else:
                nullErtek+=1
        print(f"Pozitív számok {pozitiv}")
        print(f"Negatív számok {negativ}")
        print(f"Nulla számok {nullErtek}")
    
    def osszegez(self):
        ossz = sum(self.lista)
        return ossz

    def atlag(self):
        return self.osszegez()/len(self.lista)
    


szamok = []
for i in range(5):
    szam = int(input(f"Kérem az {i}. számot"))
    szamok.append(szam)

o1 = Szamelemzo(szamok)

o1.szamol()
print(f"A számok összeg: {o1.osszegez()}")
print(f"A számok átlaga: {o1.atlag()}")
print(o1.lista)