import random

# Definimos los palos y colores
palos = {
    "♣": "negro",   # trébol
    "♠": "negro",   # picas
    "♥": "rojo",    # corazones
    "♦": "rojo"     # diamantes
}

# Generar una baraja completa (52 cartas)
baraja = [(palo, numero) for palo in palos for numero in range(1, 14)]

# Mezclamos las cartas
random.shuffle(baraja)

# Tomamos solo 13 cartas como dice el enunciado
cartas = baraja[:13]
print("Cartas recibidas:", cartas)

# Función de ordenamiento Insertion Sort
def insertion_sort(lista, key_func):
    for i in range(1, len(lista)):
        key_item = lista[i]
        j = i - 1
        while j >= 0 and key_func(lista[j]) > key_func(key_item):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key_item
    return lista

# Paso 1: ordenar por color
cartas = insertion_sort(cartas, key_func=lambda c: palos[c[0]])

# Paso 2: ordenar por palo
orden_pal = {"♣": 1, "♠": 2, "♥": 3, "♦": 4}
cartas = insertion_sort(cartas, key_func=lambda c: orden_pal[c[0]])

# Paso 3: ordenar por número dentro de cada palo
cartas = insertion_sort(cartas, key_func=lambda c: c[1])

print("\nCartas ordenadas:", cartas)
