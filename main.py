
import Metodos
from ruta import Ruta
r = Ruta()
r.pedir_ruta()
while True:
    print("Asistente de Permisos en Linux")
    print("1. Añadir o modificar permisos")
    print("2. Eliminar Permisos")
    print("3. Cambiar ruta")
    print("4. Cambiar Mascara")
    print("5. Permisos Default")
    print("0. Salir")
    num = input("Opcion: ")

    if num == "1":
        Metodos.add_modificar(r.getRuta())
    elif num == "2":
        Metodos.delete(r.getRuta())
    elif num == "3":
        r.pedir_ruta()
    elif num == "4":
        Metodos.cambiarMascara(r.getRuta())
    elif num == "5":
        Metodos.defaults(r.getRuta())
    elif num == "0":
        break
