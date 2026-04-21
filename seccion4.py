#lab1
john = 3
mary = 5
adam = 6


print(john, mary, adam, sep=", ")


total_apples = john + mary + adam


print(total_apples)

print("Número total de manzanas:", total_apples)

# ¿Cuántas manzanas tiene Adán que Juan?
diferencia = adam - john
print("Adán tiene", diferencia, "manzanas más que Juan")

# ¿Cuánto es el doble del total?
doble = total_apples * 2
print("El doble del total es:", doble)

# ¿Cuántas manzanas le tocan a cada uno si se reparten igual?
reparto = total_apples // 3
print("A cada uno le tocan:", reparto, "manzanas")

# ¿Sobran manzanas al repartir?
sobrante = total_apples % 3
print("Sobran:", sobrante, "manzanas")

#lab2

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, "millas son", round(millas_a_kilometros, 2), "kilómetros")
print(kilometros, "kilómetros son", round(kilometros_a_millas, 2), "millas")

#lab3
x = -1         # Cambia este valor para probar: 0, 1, -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)

#lab4
# 1. Calcular el puntaje total de un jugador

print("1. PUNTAJE TOTAL DEL JUGADOR")
puntos_nivel1 = int(input("Puntos obtenidos en el nivel 1: "))
puntos_nivel2 = int(input("Puntos obtenidos en el nivel 2: "))
puntos_nivel3 = int(input("Puntos obtenidos en el nivel 3: "))
puntaje_total = puntos_nivel1 + puntos_nivel2 + puntos_nivel3
print("Puntaje total del jugador:", puntaje_total)
print()
 
# 2. Calcular el tiempo total de juego en segundos

print("2. TIEMPO TOTAL DE JUEGO EN SEGUNDOS")
horas = int(input("Horas jugadas: "))
minutos = int(input("Minutos jugados: "))
segundos = int(input("Segundos jugados: "))
tiempo_total = (horas * 3600) + (minutos * 60) + segundos
print("Tiempo total jugado en segundos:", tiempo_total, "segundos")
print()
 
# 3. Calcular el daño total causado por un personaje

print("3. DAÑO TOTAL DEL PERSONAJE")
dano_ataque1 = float(input("Daño del ataque 1: "))
dano_ataque2 = float(input("Daño del ataque 2: "))
dano_ataque3 = float(input("Daño del ataque 3: "))
dano_total = dano_ataque1 + dano_ataque2 + dano_ataque3
print("Daño total causado:", round(dano_total, 2))
print()
 
# 4. Calcular la experiencia total ganada

print("4. EXPERIENCIA TOTAL GANADA")
exp_mision1 = int(input("Experiencia ganada en misión 1: "))
exp_mision2 = int(input("Experiencia ganada en misión 2: "))
exp_mision3 = int(input("Experiencia ganada en misión 3: "))
exp_total = exp_mision1 + exp_mision2 + exp_mision3
print("Experiencia total acumulada:", exp_total, "XP")
print()
 
# 5. Calcular el porcentaje de vida restante

print("5. PORCENTAJE DE VIDA RESTANTE")
vida_maxima = float(input("Vida máxima del personaje: "))
vida_actual = float(input("Vida actual del personaje: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Porcentaje de vida restante:", round(porcentaje_vida, 2), "%")
print()
 
# 6. Calcular el oro total recolectado

print("6. ORO TOTAL RECOLECTADO")
oro_mision1 = int(input("Oro recolectado en misión 1: "))
oro_mision2 = int(input("Oro recolectado en misión 2: "))
oro_mision3 = int(input("Oro recolectado en misión 3: "))
oro_total = oro_mision1 + oro_mision2 + oro_mision3
print("Oro total acumulado:", oro_total)
print()
 
# 7. Calcular la velocidad promedio de un vehículo

print("7. VELOCIDAD PROMEDIO DEL VEHÍCULO")
distancia = float(input("Distancia recorrida (km): "))
tiempo = float(input("Tiempo tomado (horas): "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio del vehículo:", round(velocidad_promedio, 2), "km/h")
print()
 
# 8. Calcular el costo total de mejoras

print("8. COSTO TOTAL DE MEJORAS")
costo_mejora1 = int(input("Costo de la mejora 1: "))
costo_mejora2 = int(input("Costo de la mejora 2: "))
costo_mejora3 = int(input("Costo de la mejora 3: "))
costo_total_mejoras = costo_mejora1 + costo_mejora2 + costo_mejora3
print("Costo total de las mejoras:", costo_total_mejoras)
print()
 
# 9. Calcular el tiempo restante para completar una misión

print("9. TIEMPO RESTANTE DE LA MISIÓN")
tiempo_total_mision = int(input("Tiempo total de la misión (segundos): "))
tiempo_transcurrido = int(input("Tiempo transcurrido (segundos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante para completar la misión:", tiempo_restante, "segundos")
print()
 
# 10. Calcular el nivel promedio de un equipo

print("10. NIVEL PROMEDIO DEL EQUIPO")
nivel_jugador1 = int(input("Nivel del jugador 1: "))
nivel_jugador2 = int(input("Nivel del jugador 2: "))
nivel_jugador3 = int(input("Nivel del jugador 3: "))
nivel_promedio = (nivel_jugador1 + nivel_jugador2 + nivel_jugador3) / 3
print("Nivel promedio del equipo:", round(nivel_promedio, 2))
print()
 
# 11. Calcular el daño crítico en un ataque

print("11. DAÑO CRÍTICO")
dano_base = float(input("Daño base del ataque: "))
multiplicador_critico = float(input("Multiplicador crítico (ej: 1.5 para 150%): "))
dano_critico = dano_base * multiplicador_critico
print("Daño crítico causado:", round(dano_critico, 2))
print()
 
# 12. Convertir tiempo total de juego a horas y minutos

print("12. TIEMPO DE JUEGO EN HORAS Y MINUTOS")
tiempo_minutos = int(input("Tiempo total jugado (en minutos): "))
horas_convertidas = tiempo_minutos // 60
minutos_restantes = tiempo_minutos % 60
print("Tiempo total de juego:", horas_convertidas, "hora(s) y", minutos_restantes, "minuto(s)")
print()
 
# 13. Calcular el porcentaje de misiones completadas

print("13. PORCENTAJE DE MISIONES COMPLETADAS")
total_misiones = int(input("Número total de misiones: "))
misiones_completadas = int(input("Número de misiones completadas: "))
porcentaje_completado = (misiones_completadas / total_misiones) * 100
print("Porcentaje de misiones completadas:", round(porcentaje_completado, 2), "%")
print()
 
# 14. Calcular el costo total de objetos en una tienda

print("14. COSTO TOTAL DE OBJETOS EN TIENDA")
costo_objeto1 = int(input("Costo del objeto 1: "))
costo_objeto2 = int(input("Costo del objeto 2: "))
costo_objeto3 = int(input("Costo del objeto 3: "))
costo_total_objetos = costo_objeto1 + costo_objeto2 + costo_objeto3
print("Costo total de los objetos comprados:", costo_total_objetos)
print()
 
# 15. Calcular el tiempo promedio de una partida

print("15. TIEMPO PROMEDIO POR PARTIDA")
tiempo_partida1 = float(input("Tiempo de la partida 1 (minutos): "))
tiempo_partida2 = float(input("Tiempo de la partida 2 (minutos): "))
tiempo_partida3 = float(input("Tiempo de la partida 3 (minutos): "))
tiempo_promedio = (tiempo_partida1 + tiempo_partida2 + tiempo_partida3) / 3
print("Tiempo promedio por partida:", round(tiempo_promedio, 2), "minutos")
print()
 
# 16. Calcular el porcentaje de enemigos derrotados

print("16. PORCENTAJE DE ENEMIGOS DERROTADOS")
total_enemigos = int(input("Número total de enemigos: "))
enemigos_derrotados = int(input("Número de enemigos derrotados: "))
porcentaje_derrotados = (enemigos_derrotados / total_enemigos) * 100
print("Porcentaje de enemigos derrotados:", round(porcentaje_derrotados, 2), "%")
print()