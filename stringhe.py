a = "Ciao mondo"

# trattare una stringa come una lista di caratteri

iniziale = a[0]
print(iniziale)

finale = a[-1]
print(finale)

print(a[:4])

numero_caratteri = len(a)  # len = lenght
print(numero_caratteri)

txt = "ciao sono mario e ho 56 anni"  # è case sensitive
esiste_mario = "mario" in txt
print(esiste_mario)

# trasformazione
print(a.upper())  # maiuscolo
print(a.lower())  # minuscolo

c = "    Ciao gente       "
print(c.strip())  # toglie gli spazi iniziali e finali

print(
    a.replace("o", "J")
)  # converti tutte le o in j nella stringa contenuta nella variabile a

c = "Via Indipendenza, 3, 12345, Roma (RM)"

stringa_divisa = c.split(",")
print(stringa_divisa)

# concatenazione di stringhe
a = "ciao"
b = "mondo"

# ciao mondo!
c = a + " " + b + "!"
print(c)

qta = 9
codice = "XYUS4"
prezzo = 9.99

# "voglio 9 pezzi del prodotto con codice XYUS4 per 9.99 euro"

ordine = "voglio {} pezzi del prodotto con codice {} per {} euro"
print(ordine.format(qta, codice, prezzo))

# f string

ordine_completo = (
    f"voglio {qta} pezzi del prodotto con codice {codice} per {prezzo} euro"
)
print(ordine_completo)

# escape
txt = "Siamo \"quelli bravi\" "
txt = 'Siamo "quelli bravi" '
txt = """
Ciao
e
arrivederci
"""