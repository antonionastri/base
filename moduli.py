# importare tutto il contenuto di un modulo
import mio_modulo
import datetime

mio_modulo.saluta("mario")

print(mio_modulo.somma(4,5))

gigi = mio_modulo.Utente("gigi", 54)

# importare tutto il contenuto di un modulo con alias
import mio_modulo as mm

mm.saluta("pino")

# importare selettivamente
from mio_modulo import Utente, somma
pippo = Utente("pippo", 23)

# importare tutto senza prefisso
from datetime import *

# pacchetti
import mio_pacchetto.modulo1 as m1
m1.Categoria()
