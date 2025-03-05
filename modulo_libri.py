class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno 
        
    def descrizione(self):
        return f"{self.titolo} di {self.autore} del {self.anno}"

# libreria / librimanager
class Libreria:
    def __init__(self, nome):
        self.libri = []
        self.nome = nome
        
    def aggiungi_libro(self, libro):
        if libro.titolo == "":
            print("attenzione specifica titolo")
        else:
            self.libri.append(libro)
            print(f"{libro.titolo} aggiunto con successo")
        
    def mostra_libri(self):
        print(f"Elenco libri di {self.nome}: ")
        if len(self.libri) == 0:
            print("la libreria è vuota")
        else:
            for l in self.libri:
                print("-", l.titolo)
        print("---------------") 
        