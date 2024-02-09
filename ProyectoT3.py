# Proyecto del Tema 3

nombre_completo = input("Tu nombre: ")
ventas_totales = input("Tus ventas totales: ")
resultado = (float(ventas_totales)) * 18 / 100
resultado_redondeado = round(resultado, 2)
print("Dadas sus ventas, a" + " " + nombre_completo + " " "le corresponde una comisión de" + " " + str(resultado_redondeado) + " " + "euros.")