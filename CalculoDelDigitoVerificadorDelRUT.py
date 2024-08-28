def calcular_digito_verificador(rut):
    rut = rut[::-1]  # Invierte el RUT para el cálculo
    suma = 0
    multiplo = 2

    for digito in rut:
        suma += int(digito) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador

# Solicita al usuario ingresar el RUT
rut = input("Ingrese el RUT (sin el dígito verificador): ")

# Calcula el dígito verificador
digito_verificador = calcular_digito_verificador(rut)

# Imprime el resultado en pantalla
print(f"El dígito verificador es: {digito_verificador}")
