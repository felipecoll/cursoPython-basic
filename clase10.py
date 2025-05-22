numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}
print(numbers[2])

information = {"nombre": "Juan", "apellido": "cortez", "altura": 1.75, "edad": 25}
del information["edad"]
print(information)

claves = information.keys()
print(claves)

values = information.values()
print(values)
items = information.items()
print(items)

contacts = {}