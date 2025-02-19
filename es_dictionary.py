bici = {
    "nome": "BMX 200",
    "marca": "bianchi",
    "prezzo": 1400,
    "inVendita": True,
    "taglie": [39, 67, 89, 41, 56],
    "colori": ["rosso", "giallo", "blu"],
    "categoria": {"codice": "BDC", "nome": "bici da corsa"},
    "disp": [
        {
            "magazzino": "magazzino 1",
            "qta": 2,
            "indirizzo": {"via": "pippo", "civico": "4", "citta": "ROMA (RM)"},
        },
        {
            "magazzino": "magazzino 2",
            "qta": 3,
            "indirizzo": {"via": "paperino", "civico": "445", "citta": "ROMA (RM)"},
        },
    ],
}

# stampare
# 1 nome del prodotto
# 2 taglia più grande (hint: ciclo for)
# 3 l'indirizzo del magazzino 2 nel formato seguente: Via paperino, 445 - Roma (RM)
# 4 stampare il totale delle biciclette in tutti i magazzini

print(bici["nome"])

taglie_base = 0
taglia_maggiore = bici["taglie"]
for taglie in taglia_maggiore:
    if taglie > taglie_base:
        taglie_base = taglie

print(taglie_base)

via = bici["disp"][1]["indirizzo"]["via"]
civico = bici["disp"][1]["indirizzo"]["civico"]
citta = bici["disp"][1]["indirizzo"]["citta"]

print(f"Via {via}, {civico} - {citta}")

qta = bici["disp"][1]["qta"] + bici["disp"][0]["qta"]

print(qta)
