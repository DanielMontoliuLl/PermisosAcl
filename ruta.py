import os
class Ruta:
    ruta = ""
    def pedir_ruta(self):
        while True:

            self.ruta = input("Ruta completa del directorio/fichero del que desea cambiar los permisos: ")
            try:
                os.chdir(self.ruta)
            except FileNotFoundError:
                print("Esta ruta no existe ")
                continue
            break
        print(os.getcwd())

    def getRuta(self):
        return self.ruta