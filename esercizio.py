numero_voti = input("Quanti voti vuoi inserire? ")
nuova_lista = []


try:
    eta_int = int(numero_voti)

    for i in range(int(numero_voti)):
        try:
            voto = input("Inserisci un voto (0-10): ")
            nuova_lista.append(int(voto))
        except:
            print("Devi inserire un numero intero")
    print(
        """
                --- Risultati ---
            """
    )

    def somma_multipla(*numeri):
        totale = 0
        for n in numeri:
            totale += n
        return int(totale)

    print("Voti inseriti: ", nuova_lista)
    print("Somma dei voti: ", somma_multipla(*nuova_lista))

    def media_voti(lista):
        return somma_multipla(*lista) / len(lista)

    print("Media dei voti: ", media_voti(nuova_lista))
    print("Voto massimo: ", max(nuova_lista))
    print("Voto minimo: ", min(nuova_lista))

    voti_sopra_media = somma_multipla(
        *[1 for voto in nuova_lista if voto > media_voti(nuova_lista)]
    )

    print("Voti sopra la media: ", voti_sopra_media)

    voti_sotto_media = somma_multipla(
        *[1 for voto in nuova_lista if voto < media_voti(nuova_lista)]
    )

    print("Voti sotto la media: ", voti_sotto_media)

    voti_insuff = somma_multipla(*[1 for voto in nuova_lista if voto < 6])

    print("Voti insufficienti: ", voti_insuff)

    if media_voti(nuova_lista) >= 6:
        print("Risultato: Promosso")
    else:
        print("Risultato: Bocciato")

except:
    print("Devi inserire un numero intero")
