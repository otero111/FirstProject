print("   Cuadre semanal \n DISEÑADO POR ROCKER")

### El objetivo de este proyecto es derminar la cantidad de dinero realizado en un pequeño negocio en el que trabajo.


l=float(input("Cantidad de dinero hecho el lunes: "))
m=float(input("Cantidad de dinero hecho el martes: "))
mi=float(input("Cantidad de dinero hecho el miercoles: "))
j=float(input("Cantidad de dinero hecho el jueves: "))
v=float(input("Cantidad de dinero hecho el viernes: "))
s=float(input("Cantidad de dinero hecho el sabado: "))

#Lo anterior me permite obtener el valor para cada dia de la semana para mas adelante trabajar con estos.


total = l + m + mi + j + v + s #para saber la cantidad de dinero total en la semana
promedio = int(total) / 6 #para saber el promedio de ventas




respuesta = "El total de la semana es {} y el promedio {}.".format(total, promedio) #me gusta trabajar de esta forma, noto una apariencia mas limpia

print(respuesta)




conclusion = "Objetivo alcanzado :)" if promedio >= 62 else "Objetivo NO alcanzado :("
print(conclusion) #esto es porque el promedio de ventas semanales tiene que ser mayor o igual a 62


if promedio > 85: #esto es una jarana para mi jefe
    print("Adilson no te quejes!!!!")


if promedio > 100: #Otra jarana
    print("WTF")

print("GRACIAS POR USAR MI PROGRAMA")


#Gracias por leer este proyecto ggg, es uno de mis primeros proyectos pero me es muy necesario para mi cierre de semana, A poco tiene mucho codigo pero ya trabajare en eso a medida que pase el tiempo. Saludos, ROCKER.