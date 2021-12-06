import crud
from time import sleep

print("╔" + "═"*34 + "╗")
print("║ Bienvenido al Programa SpotyUN. ║")
print("╚" + "═"*34 + "╝\n")

while True:
    print("Seleccione la opcion que desea realizar:")
    print("\t1. Ingresar como Administrador.")
    print("\t2. Ingresar como Cliente.")
    print("\t3. Salir del programa.")
    case = input()

    if case == "1":
        print("Ingrese el documento del administrador")
        

    elif case == "2":
        print("Ingrese el documento del cliente")

    elif case == "3":
        print("Hasta Luego.")
        sleep(1)
        break

    else:
        print("Entrada incorrecta. Intente otra vez.")


# def leer_info_cancion():
#     id=input("Código identificador: ")
#     cmax=12
#     fc='0'
#     fc1=' '
#     id=id.ljust(cmax,fc)
#     nombre=input("Nombre: ")
#     nombre=nombre.ljust(cmax,fc1)
#     genero=input("Género: ")
#     genero=genero.ljust(cmax,fc1)
#     album=input("Álbum: ")
#     album=album.ljust(cmax,fc1)
#     interprete=input("Intérprete: ")
#     interprete=interprete.ljust(cmax,fc1)
#     cancion=(id,nombre,genero,album,interprete)
#     return cancion


# def leer_info_usuario():
#     id=input("Documento de Identificación: ")
#     cmax1=10
#     cmax2=16
#     cmax=12
#     fc=' '
#     id=id.ljust(cmax1)
#     nombre=input("Nombre: ")
#     nombre=nombre.ljust(cmax,fc)
#     apellido=input("Apellido: ")
#     apellido=apellido.ljust(cmax,fc)
#     pais=input("Pais: ")
#     pais=pais.ljust(cmax,fc)
#     ciudad=input("Ciudad: ")
#     ciudad=ciudad.ljust(cmax,fc)
#     telefono=input("Teléfono: ")
#     telefono=telefono.ljust(cmax1)
#     fechapago=date.today()
#     fechapago = fechapago + timedelta(days=30)
#     tarjeta=input("Tarjeta de Crédito: ")
#     tarjeta=tarjeta.ljust(cmax2)
#     pago=input("Pagó (Yes/No): ")
#     usuario=(id,nombre,apellido,pais,ciudad,telefono,fechapago,tarjeta,pago)
#     return usuario


# Este bloque solo se ejecuta cuando se corre este archivo, si es importado no corre
# if __name__ == "__main__":
#     miCon = crud.conexion()
#     ObjCur= miCon.cursor()
#     usuario = leer_info_usuario()
#     cancion = leer_info_cancion

#     crud.insertar_tabla_cancion(miCon, ObjCur, cancion)
#     crud.insertar_tabla_usuario(miCon, ObjCur, usuario)
