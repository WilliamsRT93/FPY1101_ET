import csv
import random
import os,time

def limpiar_pantalla():
    time.sleep(2)
    os.system("cls")

trabajadores = ['Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez']

def asignar_sueldos():
    return [random.randint(300000, 2500000) for x in range(len(trabajadores))]

def clasificar_sueldos(sueldos, trabajadores):
    menores_800k = []
    entre_800k_2000k = []
    mayores_2000k = []

    for i in range(len(trabajadores)):
        empleado = trabajadores[i]
        sueldo = sueldos[i]
        if sueldo < 800000:
            menores_800k.append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2000k.append((empleado, sueldo))
        else:
            mayores_2000k.append((empleado, sueldo))

    print("Sueldos menores a $800.000 TOTAL: ", len(menores_800k))
    for empleado, sueldo in menores_800k:
        print(f"{empleado}: ${sueldo}")

    print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: ", len(entre_800k_2000k))
    for empleado, sueldo in entre_800k_2000k:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos superiores a $2.000.000 TOTAL: ", len(mayores_2000k))
    for empleado, sueldo in mayores_2000k:
        print(f"{empleado}: ${sueldo}")

    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: $ {total_sueldos}")
    
def media_geometrica_manual(data):
    producto = 1
    for valor in data:
        producto *= valor
    return producto ** (1 / len(data))

def ver_estadisticas(sueldos):
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio = round(sum(sueldos) / len(sueldos))
    media_geometrica = round(media_geometrica_manual(sueldos))
    
    print(f"Sueldo más alto: $ {max_sueldo}")
    print(f"Sueldo más bajo: $ {min_sueldo}")
    print(f"Promedio de sueldos: $ {promedio}")
    print(f"Media geométrica: $ {media_geometrica}")

def reporte_sueldos(sueldos, trabajadores):
    try:
        reporte = []
        for i in range(len(trabajadores)):
            trabajador = trabajadores[i]
            sueldo_base = sueldos[i]
            descuento_salud = round(sueldo_base * 0.07)
            descuento_afp = round(sueldo_base * 0.12)
            sueldo_liquido = round(sueldo_base * 0.81)
            reporte.append((trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido))

        with open('reporte_sueldos.csv', mode='a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
            writer.writerows(reporte)

        print("Reporte generado: reporte_sueldos.csv")
    except Exception as x:
        print(f"Se a generado un error de tipo \n{x} \nal crear el archivo")

def menu():
    sueldos = []
    while True:
        print("\nMenú:\n")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa\n")
        try:
            opcion = int(input("Seleccione una opción: "))
            limpiar_pantalla()            
            if opcion == 1:
                sueldos = asignar_sueldos()
                print("Sueldos asignados:", sueldos)

            elif opcion == 2:
                if sueldos:
                    clasificar_sueldos(sueldos, trabajadores)
                else:
                    print("Primero asigne los sueldos.")
                    limpiar_pantalla()

            elif opcion == 3:
                if sueldos:
                    ver_estadisticas(sueldos)
                else:
                    print("Primero asigne los sueldos.")
                    limpiar_pantalla()

            elif opcion == 4:
                if sueldos:
                    reporte_sueldos(sueldos, trabajadores)
                else:
                    print("Primero asigne los sueldos.")
                    limpiar_pantalla()

            elif opcion == 5:
                print("Finalizando Programa...")
                print("Desarrollado por Williams Rivas")
                print("18.596.728-K")
                limpiar_pantalla()
                break

            else:
                print("Opción no válida. Intente nuevamente.")
                limpiar_pantalla()

        except Exception as x:
            print(f"Se produjo un error de tipo: \n{x}")
            limpiar_pantalla()

limpiar_pantalla()
menu()