import core


def init():
    inter = True
    while inter:
        try:
            print("--------Menu--------")
            print("1. Agregar producto")
            print("2. Mostrar producto")
            print("3. Calcular estadisticas")
            print("4. Salir")
            print("--------------------")
            op = int(input("Opcion -> "))
            if op == 1:
                core.agregar()
            elif op == 2: 
                core.mostrar()
            elif op == 3:
                core.estadisticas()
            elif op == 4:
                inter = False
            else:
                print("[x] Opcion invalida")
        except:
            print("[x] Debe ser un dato numerico (int)")

init()