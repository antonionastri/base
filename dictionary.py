auto = {"marca": "fiat", "modello": "panda", "anno": 1990}

print(auto)

# accesso alle caratteristiche
print(auto["modello"])

auto["anno"] = 1991

ford = {
    "marca": "ford",
    "anno": 1985,
    "elettrica": False,
    "colori": ["giallo", "nero", "bianco"],
}

colore = ford["colori"][1]
print(colore)

for colore in ford["colori"]:
    print(colore)

gianni = {"nome": "Gianni", "eta": 56, "moglie": {"nome": "luisa", "eta": 50}}

# quanti anni ha la moglie di gianni

print(gianni["moglie"]["eta"])

pino = {"nome": "pino", "anni": 34}

invitati_alla_festa = [{"nome": "luca", "eta": 23}, {"nome": "paolo", "eta": 67}, pino]
