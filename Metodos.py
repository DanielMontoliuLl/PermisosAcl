import os
import subprocess
import pwd
import grp
from pwd import getpwuid
from pathlib import Path

def add_modificar(ruta):
    while True:
        print("Añadir o Modificar")
        print("1. Usuario")
        print("2. Grupo")
        print("0. Salir")
        num = input("Opcion: ")

        if num == "1":
            user = input("Usuario: ")
            try:
                pwd.getpwnam(user)
            except KeyError:
                print("Este usuario no existe")
                continue
            permisos = preguntarPermisos()

            if find_owner(ruta) == user:
                subprocess.run(["setfacl", "-m", f"u::{permisos}", f"{ruta}"])
            else:
                subprocess.run(["setfacl", "-m", f"u:{user}:{permisos}", f"{ruta}"])

        elif num == "2":
            group = input("Grupo: ")
            try:
                grp.getgrnam(group)
            except KeyError:
                print("Este grupo no existe")
                continue
            permisos = preguntarPermisos()
            if find_ownerg(ruta) == group:
                subprocess.run(["setfacl", "-m", f"g::{permisos}", f"{ruta}"])
            else:
                subprocess.run(["setfacl", "-m", f"g:{group}:{permisos}", f"{ruta}"])

        elif num == "0":
            break
def delete(ruta):
    while True:
        print("Eliminar")
        print("1. Usuario")
        print("2. Grupo")
        print("0. Salir")
        num = input("Opcion: ")

        if num == "1":
            user = input("Usuario: ")
            try:
                pwd.getpwnam(user)
            except KeyError:
                print("Este usuario no existe")
                continue
            if find_owner(ruta) == user:
                print("No se pueden eliminar los permisos del usuario owner, si modificarlos")
            else:
                subprocess.run(["setfacl", "-x", f"u:{user}:", f"{ruta}"])

        elif num == "2":
            group = input("Grupo: ")
            try:
                grp.getgrnam(group)
            except KeyError:
                print("Este grupo no existe")
                continue
            subprocess.run(["setfacl", "-x", f"g:{group}:", f"{ruta}"])

        elif num == "0":
            break



def preguntarPermisos():
    permisos=0
    lectura=input("Deseas que tenga permiso de lectura (S/n) ")
    if lectura == "S" or lectura == "s":
        permisos += 4

    escritura = input("Deseas que tenga permiso de escritura (S/n) ")
    if escritura == "S" or escritura == "s":
        permisos += 2

    ejecucion = input("Deseas que tenga permiso de ejecucion (S/n) ")
    if ejecucion == "S" or ejecucion == "s":
        permisos += 1

    if permisos == 7:
        permisosStr = "rwx"
    elif permisos == 6:
        permisosStr = "rw"
    elif permisos == 5:
        permisosStr = "rx"
    elif permisos == 4:
        permisosStr = "r"
    elif permisos == 3:
        permisosStr = "wx"
    elif permisos == 2:
        permisosStr = "w"
    elif permisos == 1:
        permisosStr = "x"
    elif permisos == 0:
        permisosStr = "0"
    print(permisosStr)
    return permisosStr




def find_owner(filename):
    return getpwuid(os.stat(filename).st_uid).pw_name

def find_ownerg(filename):
    l=Path(filename)
    return l.group()

def cambiarMascara(ruta):
    while True:
        print("Máscara")
        print("1. Modificar máscara")
        print("2. Que es la máscara?")
        print("0. Salir")
        num = input("Opcion: ")

        if num == "1":
            permisos = preguntarPermisos()
            subprocess.run(["setfacl", "-m", f"m::{permisos}", f"{ruta}"])
        elif num == "2":
            print("La máscara en los permisos ACl, indica los permisos máximos que pueden tener los usuarios, sin contar el usuario owner")
        elif num == "0":
            break

def defaults(ruta):
    while True:
        print("Permisos Default")
        print("1. Usuario")
        print("2. Grupo")
        print("3. Que es el campo default?")
        print("0. Salir")
        num = input("Opcion: ")

        if num == "1":
            user = input("Usuario: ")
            try:
                pwd.getpwnam(user)
            except KeyError:
                print("Este usuario no existe")
                continue
            permisos = preguntarPermisos()

            if find_owner(ruta) == user:
                subprocess.run(["setfacl", "-m", f"d:u::{permisos}", f"{ruta}"])
            else:
                subprocess.run(["setfacl", "-m", f"d:u:{user}:{permisos}", f"{ruta}"])

        elif num == "2":
            group = input("Grupo: ")
            try:
                grp.getgrnam(group)
            except KeyError:
                print("Este grupo no existe")
                continue
            permisos = preguntarPermisos()
            if find_ownerg(ruta) == group:
                subprocess.run(["setfacl", "-m", f"d:g::{permisos}", f"{ruta}"])
            else:
                subprocess.run(["setfacl", "-m", f"d:g:{group}:{permisos}", f"{ruta}"])
        elif num == "3":
            print("El campo default indica los permisos que tendrá el usuario por defecto en los hijos del directorio donde se aplica")
        elif num == "0":
            break