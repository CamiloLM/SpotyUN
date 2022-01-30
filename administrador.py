from usuario import Usuario
from prettytable import PrettyTable
from sqlite3 import OperationalError


class Administrador(Usuario):
    def __init__(self):
        super().__init__()


    def __str__(self) -> str:
        return ("Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}".format(self._cedula, self._nombre, self._apellido, self._correo))


    @property
    def cedula(self) -> int:
        return self._cedula


    @cedula.setter
    def cedula(self, cedula) -> None:
        self._cedula = cedula


    @property
    def datos_usuario(self) -> tuple:
        return self._nombre, self._apellido, self._correo


    @datos_usuario.setter
    def datos_usuario(self, datos_usuario) -> None:
        self._nombre, self._apellido, self._correo = datos_usuario


    def ingresar_usuario(self, con, cur) -> int:
        """
        Ingresa datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        datos (list): cedula, nombre, apellido, correo.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self._cedula, self._nombre, self._apellido, self._correo
        # Inserta los valores de datos en la tabla administrador si no se generan conflictos
        cur.execute("INSERT OR IGNORE INTO administrador VALUES (?, ?, ?, ?)", datos)
        con.commit()
        return cur.rowcount

    
    def consulta_usuario_especifica(self, cur) -> tuple:
        """
        Consulta los datos de un administrador por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_administrador (tuple): Si encuentra un administrador con esa cedula-
        None: Si no encuentra ninguna coincidencia.
        """
        # Trae toda la información de la tabla administrador donde la cedula coincida con el parametro
        cur.execute("SELECT * FROM administrador WHERE cedula = ?", [self._cedula])
        return cur.fetchone()
    

    def consulta_usuario_general(self, cur, campo="cedula") -> tuple:
        """
        Consulta todos los datos de la tabla administrador ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.

        Regresa:
        datos_administradores (tuple): Tupla con todos los administradores ordenados por el campo
        None: Si no encuentra ninguna coincidencia.
        """
        cur.execute("SELECT * FROM administrador ORDER BY {}".format(campo))
        return cur.fetchall()
    

    def actualizar_usuario(self, con, cur) -> int:
        """
        Actualiza datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self._nombre, self._apellido, self._correo, self._cedula
        cur.execute('''
            UPDATE OR IGNORE administrador
            SET nombre = ?,
            apellido = ?,
            correo = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount
    

    def borrar_usuario_especifico(self, con, cur) -> int:
        """
        Borra un registro la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM administrador WHERE cedula = ?", [self._cedula])
        con.commit()
        return cur.rowcount
    

    def borrar_usuario_general(self, con, cur) -> int:
        """
        Borra todos los registros en la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM administrador")
        con.commit()
        return cur.rowcount


def menu_administrador(con, cur):
    admin = Administrador()

    while True:
        print("\nSeleccione que opciones desea realizar:")
        print("1. Añadir administrador nuevo.")
        print("2. Consulta general administrador.")
        print("3. Consulta especifica administrador.")
        print("4. Actualizar administrador.")
        print("5. Eliminar administrador especifico.")
        print("6. Eliminar administrador general.")
        print("0. Salir del programa.")
        case = input()


        if case == "1":
            # Ingresando un nuevo administrador
            cedula = input("\nIngrese número de cedula: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            correo = input("Ingrese correo electronico: ")
            
            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and nombre.isalpha() and apellido.isalpha():
                admin.cedula = int(cedula)  # Actualiza la cedula del objeto admin
                admin.datos_usuario = [nombre, apellido, correo]  # Actualiza los datos usuario del objeto admin

                # Se borran las variables que ya no se utilizan
                del cedula, nombre, apellido, correo

                # Llama al metodo para ingresar el usuario en la base de datos
                cambios = admin.ingresar_usuario(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nAministrador ingresado con exito.")
                else:
                    print("\nLa cedula ya esta registrada, no se han realizado cambios.")
            else:
                print("\nAlguno de los datos que ingreso no son correctos")

        elif case == "2":
            # Consulta general de administradores por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]  # Asgina los nombres de los campos en la tabla
            campo = "cedula"  # Campo por el que se va a ordenar

            # Bucle para poder ordenar las busquedas por campos
            while True:
                # Excepcion por si se ingresan campos que no esten en la tabla
                try:
                    # Busqueda en la tabla usuario general pasando el campo por el que ordena
                    datos_admin = admin.consulta_usuario_general(cur, campo)
                    
                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_admin:
                        mi_tabla.add_rows(datos_admin)  # Añade datos las filas a la tabla
                        print("")
                        print(mi_tabla)
                        bandera = input("Desea ordenar la busqueda por un campo (S/n): ")

                        # Bandera logica por si se quiere ordenar un campo
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            campo = input("Ingrese el campo por el que quiere ordenar la busqueda: ").lower()  # Entrada en minisculas
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        break
                except OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha proporcionado.")
                    break

        elif case == "3":
            # Consulta especifica de administrador por cedula
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]  # Asgina los nombres de los campos en la tabla

            cedula = input("\nIngrese número de cedula: ")
            # Verficacion de los datos que son ingresados son correctos
            if cedula.isdigit():
                # Actualiza la cedula del objeto admin
                admin.cedula = int(cedula)
                # Almacena todos los datos del admin
                datos_admin = admin.consulta_usuario_especifica(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_admin:
                    mi_tabla.add_row(datos_admin)  # Añade datos las filas a la tabla
                    print("")
                    print(mi_tabla)
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor de la cedula ingresado no es valido")

        elif case == "4":
            # Actualizar los datos del administrador
            print("\nIngrese los datos nuevos del administrador")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo electronico: ")

            print("\nIngrese la cedula del administrador que va a modificar:")
            cedula = input()

            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and nombre.isalpha() and apellido.isalpha():
                admin.cedula = int(cedula)  # Actualiza la cedula del objeto admin
                admin.datos_usuario = [nombre, apellido, correo]  # Actualiza los datos usuario del objeto admin

                # Se borran las variables que ya no se utilizan
                del cedula, nombre, apellido, correo
                
                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = admin.actualizar_usuario(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nActualización realizada con exito.")
                else:
                    print("\nEsa cedula no esta registrada, no se han realizado cambios.")

        elif case == "5":
            # Eliminar datos especificos de la tabla administrador
            print("\nIngrese la cedula del administrador que va a eliminar:")
            cedula = input()

            if cedula.isdigit():
                admin.cedula = int(cedula)

                del cedula  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = admin.borrar_usuario_especifico(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nAdministrador eliminado con exito.")
                else:
                    print("\nEsa cedula no esta registrada, no se han realizado cambios.")

        elif case == "6":
            # Eliminar datos generales de la tabla administrador
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = admin.borrar_usuario_general(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nTodos los datos de la tabla administrador han sidos eliminados.")
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")

        elif case == "0":
            print("\nSaliendo del menu administrador.")
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")
