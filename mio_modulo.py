def saluta(nome):
    print("ciao", nome)

def somma(x,y):
    return x + y

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
        