# Ejemplo de iteradores en Python

# Crear una lista

# my_list = [1, 2, 3, 4, 5]
# # Crear un iterador a partir de la lista
# my_iterator = iter(my_list)
# # Usar el iterador para recorrer la lista
# for item in my_iterator:
#     print(item)

# print(next(my_iterator))  # Esto lanzará StopIteration porque ya se ha recorrido el iterador
# # Reiniciar el iterador creando uno nuevo
# my_iterator = iter(my_list) 

# text = "Hola mundo!"

# iter_text = iter(text)
# # Usar el iterador para recorrer el texto
# for char in iter_text:
#     print(char)

# Crear un iterador para numeros impares 

# limite

limite = 10

odd_itter = iter(range(1, limite + 1, 2))

for num in odd_itter:
    print(num)