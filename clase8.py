to_do = ["Despertarse para desayunar", "Cambiarse para salir",
         "Buscar una perra de pasajera", "Abandonarla por ahi"]

print(to_do)

numbers = [1, 2, 3, 4, 5, "cinco"]

print(type(numbers))

mix = [1, 2, 3, 4, 5, "cinco", True]
# print(type(mix))
# print(len(mix))
# print("primer elemento: " + str(mix[0]))
# print("segundo elemento: " + str(mix[1]))

# string = "Hola mundo baboso"

# print("Ultimo elemento: " + str(string[-1]))
# print(mix[2:-1])

# print(mix)
mix.append(False)
print(mix)

mix.append(['a', 'b', 'c'])
print(mix)