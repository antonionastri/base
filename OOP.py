from datetime import datetime
# OOP - object oriented programming (programmazione orientata ad oggetti)

# classe => è un progetto (o uno stampo con il quale creare gli oggetti)
# oggetto => è un qualcosa creato a partire da una classe
# creare un oggetto da una classe => istanziare

class Utente:
    # costruttore
    def __init__(self, n, eta):
        self.nome = n
        self.eta = eta
        print("istanziato")
    
    def corri(self):
        if self.eta > 42:
            print(f"sono {self.nome} ho {self.eta} e non corro")
        else:
            print(f"sono {self.nome} ho {self.eta} e posso correre")
        
mario = Utente("mario", 56) # istanzio l'oggetto mario dalla classe utente
gigi = Utente("gigi", 41)

print(mario.nome)


print(gigi.nome)

mario.corri()
gigi.corri()

print(gigi.eta)

anna = Utente("anna", 21)
anna.corri()

nascita = datetime(1976, 1, 20)
# timestamp è un metodo di oggetto
nascita.timestamp()

# now è unn metodo di classe
adesso = datetime.now()