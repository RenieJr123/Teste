lista_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_a = [1, 2, 3, 4, 5, 60, 7, 80, 9, 90, 100, 190]

# somar_as_listas_em_uma_so = [a + b for a, b in zip(lista_b, lista_a)]

# print (somar_as_listas_em_uma_so)
from itertools import zip_longest

nova_lista = [a + b for a, b in zip_longest(lista_b, lista_a, fillvalue=0)]

print(nova_lista)