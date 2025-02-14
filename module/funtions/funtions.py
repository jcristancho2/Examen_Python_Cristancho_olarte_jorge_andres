import module.menus as m , module.utils.controlScreen as cc , module.utils.decor as dec , module.utils.validate_data as  vd , module.json.json as js
from main import NAME_ARC

ERROR = ' 🚫option invalid 🚫'


def menu ():
    cc.XScreen()
    js.crearJson(NAME_ARC)
    print(m.menu_principla)
    option = int(vd.validateInt(dec.inn))
    match option:
        case 1:
            calcular_imp_pos()
        case 2:
            ver()
        case 3:
            cc.LLScreen()
            exit()
        case _:
            print (ERROR)



    
def inbase():
        print(f'{dec.lineas*51}')
        print(f'        CALCULO DE IMPUESTO     ')
        print(f'{dec.lineas*51}')
        print('Ingrese el precio base del producto o servicio')
        valor = int(input(dec.inn))
        return valor
        
def tipoimp(valor):
    
        print("""
          Seleccione el tipo de impuesto:
            1. IVA (10%)
            2. Impuesto Especial (5%)
            3. Impuesto local (8%)
            4. Otro (permite ingresar una tasa personalizada)""")  
        option = int(vd.validatefloat(dec.inn))

        impuesto ={
            1: 0.1,
            2: 0.05,
            3: 0.08
        }
        
        if option in impuesto:
            tasa = impuesto[option]
        elif option == 4:
            print('Ingrese el valor del impuesto (en porcentaje) si seleccionó " Otro " :')
            otro = int(vd.validateInt(dec.inn))/100
        else :
            print(ERROR)
            return tipoimp(valor)
        
        impuesto = valor*tasa
        total = valor + impuesto
        
        print (f'base: {valor}')
        print(f"Impuesto calculado: {impuesto}")
        print(f"Total con impuestos: {total}")
        
        return impuesto, total
        

def calcular_imp_pos():
    cc.XScreen()

    lector = js.leerJson(NAME_ARC)    
    if not isinstance(lector, list):
        lector = []

    valor = inbase() 
    impuesto, total = tipoimp(valor) 
    
    elemento = {
        'base': valor,
        'IVA': impuesto if impuesto / valor == 0.1 else 0,
        'impuesto_especial': impuesto if impuesto / valor == 0.05 else 0,
        'impuesto_local': impuesto if impuesto / valor == 0.08 else 0,
        'otros': impuesto if impuesto / valor not in [0.1, 0.05, 0.08] else 0,
        'total': total
    }

    lector.append(elemento)  
    js.actualizarJson(NAME_ARC, lector)  



    
    
def ver():
    print(f'{dec.lineas*51}')
    print(f'        TIPO DE IMPUESTO     ')
    print(f'{dec.lineas*51}')
    print("""
            1. IVA (10%)
            2. Impuesto Especial (5%)
            3. Impuesto local (8%)
            4. Otro (Personalizado)""")
    option = int(vd.validateInt(dec.inn))
    match option:
        case 1:
            
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print (ERROR)    

    op = vd.validateAlpha(f'¿Desea calcular un impuesto ahora ? [si/no] ').lower()
    if ( op in ['si','no']):
        if (op == 'si'):
            return calcular_imp_pos()            
        else:
            return menu()
