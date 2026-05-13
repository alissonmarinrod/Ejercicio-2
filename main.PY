saldo_inicial = 1000
lista_de_operaciones_realizadas = []
opcion = "" # Esta variable vacía permite que el while empiece"

# PASO 2: Agregamos el bucle al WHILE manteniendo el menú activo
# El menú se repite mientras la opcion no sea "4"
while opcion != "4":
    print("MENU DEL CAJERO")
    print("1. Consultar saldo actual")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa")
    
    opcion = input("Elija una opcion (1-4): ")
    # PASO 3: Agregar deposito, retiro y consulta con IF/ELIF/ELSE
    if opcion == "1":
        print("Su saldo actual es: $", saldo_inicial)
        
    # PASO 4: Mostrar historial con ciclo FOR 
        print("Historial de movimientos:")
        for movimiento in lista_de_operaciones_realizadas:
            print("-", movimiento)
