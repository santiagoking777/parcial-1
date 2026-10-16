def ejercicio1():
    print("--- Registro de Calificaciones ---")
    
    nombres = []
    promedios = []
    
    cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
    
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
        nombres.append(nombre)
        
        print("Ingrese las 3 calificaciones (de 0.0 a 5.0):")
        n1 = float(input("Calificación 1: "))
        n2 = float(input("Calificación 2: "))
        n3 = float(input("Calificación 3: "))
        
        prom = round((n1 + n2 + n3) / 3, 2)
        promedios.append(prom)
    
    print("\n--- Resultados del Grupo querido ---")
    suma_total = 0
    
    for i in range(len(nombres)):
        if promedios[i] >= 3.0:
            estado = "aprobado y postre"
        else:
            estado = "reprobad@ y repita el año"
            
        print("Estudiante:", nombres[i], "| Promedio:", promedios[i], "| Estado:", estado)
        suma_total = suma_total + promedios[i]
    
    promedio_general = suma_total / len(nombres)
    print("\nPromedio general del grupo querido:", promedio_general)
    
    mayor = promedios[0]
    for p in promedios:
        if p > mayor:
            mayor = p
            
    print("El mayor promedio es:", mayor)
    print("Estudiantes con el mayor promedio:")
    
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            print("-", nombres[i])

ejercicio1()

def ejercicio2():
    inventario = [
    ["TT1", "Teclado GAMER", 54000, 10],
    ["TR2", "Raton OFICINA", 30000, 30],
    ["TP3", "Pantalla de monitor", 167000, 20],
    ["TM4", "Memoria USB de un 1T", 480000, 17]
]
    total_vendido = 0
    
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Consultar inventario")
        print("2. Vender producto")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("\n--- Inventario Actual ---")
            for prod in inventario:
                print("Código:", prod[0], "| Nombre:", prod[1], "| Precio: $", prod[2], "| Existencias:", prod[3])
                
        elif opcion == "2":
            codigo = input("Ingrese el código del producto (ej. TT1): ")
            
            pos = -1
            for i in range(len(inventario)):
                if inventario[i][0] == codigo:
                    pos = i
                    break
            
            if pos == -1:
                print("Error: El código del producto no existe busque alguien que se sepa los codigos de memoria.")
            else:
                cantidad = int(input("Ingrese la cantidad a vender: "))
                
                if cantidad <= 0:
                    print("Error: La cantidad debe ser mayor a cero tampoco abuse del sistema.")
                elif cantidad > inventario[pos][3]:
                    print("Error: No hay suficiente disponibilidad ya se vendieron vuelve pronto. Existencias actuales:", inventario[pos][3])
                else:
                    inventario[pos][3] = inventario[pos][3] - cantidad
                    
                    valor_venta = inventario[pos][2] * cantidad
                    print("¡Venta exitosa yupi! Total de la venta: $", valor_venta)
                    
                    total_vendido = total_vendido + valor_venta
                    
        elif opcion == "3":
            print("\n--- Resumen Final ---")
            print("Total vendido: $", total_vendido)
            print("Productos con menos de cinco unidades:")
            
            encontrados = False
            for prod in inventario:
                if prod[3] < 5:
                    print("-", prod[1], "(Código:", prod[0] + "):", prod[3], "unidades")
                    encontrados = True
                    
            if not encontrados:
                print("Ningún producto tiene menos de 5 unidades deberiamos vender mas.")
            break
            
        else:
            print("Opción inválida. Intente de nuevo minimo te equivocaste.")

ejercicio2()