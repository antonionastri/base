anni = input("Quanti anni hai? ")

try:
    eta_int = int(anni)
    
    if eta_int >= 18:
        try:
            patente =  input("hai la patente? (solo si o no): ")

        except:
            print("inserisci un dato valido")
    else:
        bici = input("hai una bicicletta?")
    
    
    
    
    
    
    
except ValueError:
    print("inserisci un numero intero")
    