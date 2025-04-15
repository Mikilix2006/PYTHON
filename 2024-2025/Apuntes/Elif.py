ingresos_mensuales = 4000

#Si esto se cumple, no se ejecuta el resto
if ingresos_mensuales > 2000:
    print("Estás bien en España")

#Si lo anterior no se cumple y esto si, el resto no se ejecuta
elif ingresos_mensuales > 1000:
    print("Estás bien en Latinoamérica")

#Si las cosas anteriores no se cumplen y esto si, el resto no se ejecuta
elif ingresos_mensuales > 500:
    print("Estás bien en Argentina")

#...
elif ingresos_mensuales > 200:
    print("Estás bien en Venezuela")

#Si nada se cumple, ejecuta esto
else:
    print("Eres pobre")
