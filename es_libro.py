from modulo_libri import *

libro1 = Libro("Pinocchio", "collodi", 1940)
libro2 = Libro("Dune", "frank harbert", 1980)

# print(libro1.descrizione())

libreria_salotto = Libreria("Libreria Salotto")
libreria_salotto.aggiungi_libro(libro1)
libreria_salotto.mostra_libri()

libreria_cucina = Libreria("Libreria cucina")
libreria_cucina.aggiungi_libro(libro2)
libreria_cucina.mostra_libri()