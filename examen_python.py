# 1 En una llantera se ha establecido una promoción de las llantas marca
#   Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
#   de cinco llantas el precio es de $300 cada una, de $250 si se compran de
#   cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
#   que una persona tiene que pagar por cada una de las llantas que compra y la
#   que tiene que pagar por el total de la compra.

numeroLlantas = int(input("Digite el numero de llantas a comprar "))
valorLlanta = 0
totalPagar = 0

if (numeroLlantas < 5):
     valorLlanta = 300
     totalPagar = numeroLlantas * valorLlanta
elif (numeroLlantas >= 5 and numeroLlantas <= 10):
     valorLlanta = 250
     totalPagar = numeroLlantas * valorLlanta
else:
     valorLlanta = 200
     totalPagar = numeroLlantas * valorLlanta
     
print(f"El dinero que se debe pagar por cada llanta es ${valorLlanta:,} \n"
      f"El total de la compra es ${totalPagar:,}")


# 2 Hacer algoritmo que de el valor final por la compra de televisores. El
#   descuento lo hace basado en los dos numeros finales a la cédula, si
#   termina en 01 el descuento es del 10% y si termina en 25 el descuento es
#   del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%.

cedula = input("Digite el numero de llantas a comprar ")
valorTv = float(input("Digite el valor del televisor "))
numeroFinal = str(cedula[len(cedula) - 2 :])
descuento = 0
totalPagar = 0

if (numeroFinal == "01"):
     descuento = valorTv * 0.1
     totalPagar = valorTv - descuento
elif (numeroFinal == "25"):
     descuento = valorTv * 0.2
     totalPagar = valorTv - descuento
elif (numeroFinal == "44"):
     descuento = valorTv * 0.35
     totalPagar = valorTv - descuento
elif (numeroFinal == "57"):
     descuento = valorTv * 0.5
     totalPagar = valorTv - descuento
else:
     totalPagar = valorTv

print(f"Su dos ultimos digitos de su cedula son '{numeroFinal}', por lo tanto tiene un descuento de ${descuento:,} \n"
      f"El total a pagar por la compra del TV es ${totalPagar:,}")


# 3 Una empresa de colchones ofrece descuento según la siguiente tabla
#   Numero de colchones comprados - % Descuento
#   De 0 a menos de 3 0%
#   De 3 hasta menos de 6 20%
#   De 6 hasta menos de 8 25%
#   De 8 en adelante 30%
#   Determine cuanto pagará una persona que compre colchones.

numColchon = int(input("Digite el numero de colchones que va comprar "))
valorColchon = float(input("Digite el valor del colchon "))
descuento = 0
totalPagar = 0

if (numColchon >= 0 and numColchon < 3):
     descuento = 0
     totalPagar = numColchon * valorColchon
elif (numColchon >= 3 and numColchon < 6):
     descuento = (numColchon * valorColchon) * 0.2
     totalPagar = (numColchon * valorColchon) - descuento
elif (numColchon >= 6 and numColchon < 8):
     descuento = (numColchon * valorColchon) * 0.25
     totalPagar = (numColchon * valorColchon) - descuento
else:
     descuento = (numColchon * valorColchon) * 0.3
     totalPagar = (numColchon * valorColchon) - descuento
     
print(f"El dinero que se debe pagar por la compra de los colchones es ${totalPagar:,}")


# 4 Una universidad desea seleccionar una muestra de estudiantes para
#   realizar una encuesta. Si el número de estudiantes es menor que 20 se
#   tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
#   si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
#   serán seleccionados para la encuesta?.

numEstudiante = int(input("Digite el numero de estudiantes "))
porcentaje = 0
totalMuestra = 0

if (numEstudiante < 20):
     porcentaje = 0.5
     totalMuestra = int(numEstudiante * porcentaje)
     porcentaje = porcentaje * 100 
elif (numEstudiante >= 20 and numEstudiante <= 30):
     porcentaje = 0.6
     totalMuestra = int(numEstudiante * porcentaje)
     porcentaje = porcentaje * 100
else:
     porcentaje = 0.7
     totalMuestra = int(numEstudiante * porcentaje)
     porcentaje = porcentaje * 100
     
print(f"El numero de estudiantes del salon es {numEstudiante:,}, por lo tanto se tomara el {porcentaje:,}% para la encuesta \n" +
      f"Por lo que se seleccionaran {totalMuestra:,} estudiante(s) para la encuesta.")














