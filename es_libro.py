class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno 
        
    def descrizione(self):
        return f"{self.titolo} di {self.autore} del {self.anno}"
    
libro1 = Libro("pinocchio", "collodi", 1940)
print(libro1.descrizione())