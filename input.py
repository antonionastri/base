eta = input(
    "Quanti anni hai? "
)  # il valore ritornato da input è sempre di tipo stringa

# gestione errore
try:
    eta_int = int(eta)
    if eta_int >= 18:
        print("maggiorenne")
    else:
        print("minorenne")
except: # intercetto ogni tipi di errore
    print("Devi inserire un numero intero")

try:
    x = 10 / 0
except ZeroDivisionError as e: # intercetto un tipo di errore specifico
    print(e)
    print("non puoi dividere per zero")
    

try:
    file = open("filette.txt", "r")
    
    lista = [1, 2, 3]
    n = lista[10]
except FileNotFoundError :
    print("Errore file non trovato")
except IndexError:
    print("Errore indice lista non trovato")