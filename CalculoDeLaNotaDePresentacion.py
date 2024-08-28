# Solicita al usuario ingresar las notas
lab1 = float(input("Ingrese la nota de Lab 1: "))
lab2 = float(input("Ingrese la nota de Lab 2: "))
lab3 = float(input("Ingrese la nota de Lab 3: "))
tarea1 = float(input("Ingrese la nota de Tarea 1: "))
tarea2 = float(input("Ingrese la nota de Tarea 2: "))
tarea3 = float(input("Ingrese la nota de Tarea 3: "))
solemne1 = float(input("Ingrese la nota de Solemne 1: "))
solemne2 = float(input("Ingrese la nota de Solemne 2: "))

# Calcula los promedios de laboratorio y tareas
prom_lab = (lab1 + lab2 + lab3) / 3
prom_tareas = (tarea1 + tarea2 + tarea3) / 3

# Calcula la nota de presentación
nota_presentacion = (prom_lab * 0.15) + (prom_tareas * 0.15) + (solemne1 * 0.35) + (solemne2 * 0.35)

# Imprime el resultado en pantalla
print(f"La nota de presentación es: {nota_presentacion:.2f}")
