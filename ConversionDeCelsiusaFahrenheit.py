# Solicita al usuario ingresar la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convierte la temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Imprime el resultado en pantalla
print(f"Temperatura en grados Fahrenheit: {fahrenheit:.2f}")
