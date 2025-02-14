a = "Ciao mondo"

#trattare una stringa come una lista di caratteri

iniziale = a[0]
print(iniziale)

finale = a[-1]
print(finale)

print(a[:4])

numero_caratteri = len(a) # len = lenght
print(numero_caratteri)

txt = "ciao sono mario e ho 56 anni" # è case sensitive
esiste_mario = "mario" in txt
print(esiste_mario)

# trasformazione
print(a.upper()) #maiuscolo
print(a.lower()) #minuscolo

c = "    Ciao gente       "
print(c.strip()) #toglie gli spazi iniziali e finali

print(a.replace("o", "J")) #converti tutte le o in j nella stringa contenuta nella variabile a

c = "Via Indipendenza, 3, 12345, Roma (RM)"

stringa_divisa = c.split(",")
print(stringa_divisa)