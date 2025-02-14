

menu_principla =f"""
---------------------------------------------------
                CALCULADORA DE IMPUESTO
---------------------------------------------------
Seleccione una opción:
1. Calcular impuesto sobre un producto o servicio
2. Ver lista de tipos de impuestos
3. Salir
---------------------------------------------------
"""

menu_calculo_imp =f"""
---------------------------------------------------
             CÁLCULO DE IMPUESTO
---------------------------------------------------
Ingrese el precio base del producto o servicio:
> [Usuario ingresa valor]
---------------------------------------------------
Seleccione el tipo de impuesto:
1. IVA (10%)
2. Impuesto Especial (5%)
3. Impuesto local (8%)
4. Otro (permite ingresar una tasa personalizada)
---------------------------------------------------
Ingrese el valor del impuesto (en porcentaje) si seleccionó " Otro " :
 > [Usuario ingresa valor o selecciona uno predefinido]
---------------------------------------------------
¿Desea agregar otro impuesto ?
1. Sí
2. No
---------------------------------------------------

"""

menu_resultado_fin =f"""
---------------------------------------------------
                RESULTADO DEL CÁLCULO
---------------------------------------------------
Precio base: $[valor]
Impuesto(s):
- IVA (10%): $[valor del IVA]
- Impuesto Especial (5%): $[valor del impuesto especial]
Total con impuestos: $[total]

¿Desea hacer otro cálculo ?
1. Sí
2. No (Regresa al menú principal)
---------------------------------------------------
"""

menu_vista_impuestos =f"""
---------------------------------------------------
               TIPOS DE IMPUESTO
---------------------------------------------------
1. IVA (10%)
2. Impuesto Especial (5%)
3. Impuesto local (8%)
4. Otro (Personalizado)

¿Desea calcular un impuesto ahora ?
1. Sí (Regresa al cálculo)
2. No (Regresa al menú principal)
---------------------------------------------------

"""

salida =f"""
---------------------------------------------------
               ¡Gracias por usar la Calculadora ! 
---------------------------------------------------
"""