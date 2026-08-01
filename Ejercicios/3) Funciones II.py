def calcular_ventas(precio, cantidad):
    total=precio*cantidad
    return total
Total=calcular_ventas(50, 4)
print("El total de ventas es:", Total)

def aplicar_descuento(precio,descuento):
    total=precio-(precio*descuento)
    return total
Total=aplicar_descuento(200, 0.25)
print("El total con descuento es:", Total)

def ganancia(ingreso,costo):
    ganancia=ingreso-costo
    return ganancia
ganancia=ganancia(500, 300)
print("la ganancia es:",ganancia)