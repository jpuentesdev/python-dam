'''
6.- Tabla de descuentos
-----------------------
Un minorista en particular tiene un 60 por ciento de descuento en una variedad de productos descontinuados.

Al minorista le gustaría ayudar a sus clientes a determinar el precio reducido de la mercancía al tener una tabla de descuentos impresa en el estante que muestre los precios originales y los precios después de que se haya aplicado el descuento. 

Escriba un programa que use un bucle para generar esta tabla, que muestre el precio original, el monto del descuento y el nuevo precio para compras de $4.95, $9.95, $14.95, $19.95 y $24.95. 

Asegúrese de que los montos de descuento y los nuevos precios se redondeen a 2 decimales cuando se muestren.
'''

print("Precio | Descuento | Precio Final")
print("------------------------")
def tabla_descuento():
    Precio_Original = 4.95
    while Precio_Original <= 24.95:
        Descuento = Precio_Original * 0.60
        PrecioFinal = Precio_Original - Descuento
        print(f"{Precio_Original}€   | {Descuento:.2f}€ | {PrecioFinal:.2f}€")
        Precio_Original += 5

tabla_descuento()











