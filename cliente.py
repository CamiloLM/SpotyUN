from usuario import Usuario
from prettytable import PrettyTable
from datetime import date
from sqlite3 import OperationalError


class Cliente(Usuario):
    def __init__(self):
        super().__init__()
        self._pais = None
        self._ciudad = None
        self._telefono = None
        self._tarjeta_credito = None
        self._fecha_pago = None
        self._pago = None


    def __str__(self) -> str:
        return (
            "Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}\nPais: {}\nCiudad: {}\nTelefono: {}\nTarjeta credito: {}\nFecha pago: {}\nPago: {}".format(
            self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito, self._fecha_pago, self._pago)
        )


    @property
    def cedula(self) -> int:
        return self._cedula


    @cedula.setter
    def cedula(self, cedula) -> None:
        self._cedula = cedula


    @property
    def datos_usuario(self) -> tuple:
        return self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito


    @datos_usuario.setter
    def datos_usuario(self, datos) -> None:
        self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito = datos


    @property
    def datos_pago(self) -> tuple:
        return self._fecha_pago, self._pago


    @datos_pago.setter
    def datos_pago(self, datos) -> None:
        self._fecha_pago, self._pago = datos


    def ingresar_usuario(self, con, cur) -> int:
        """
        Ingresa los datos del objeto en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = (self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono,
            self._tarjeta_credito, self._fecha_pago, self._pago)
        cur.execute("INSERT OR IGNORE INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
        con.commit()
        return cur.rowcount


    def consulta_usuario_especifica(self, cur) -> tuple:
        """
        Consulta una cliente por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_cliente (tuple): Todos los datos del cliente.
        """
        cur.execute("SELECT * FROM cliente WHERE cedula = ?", [self._cedula])
        return cur.fetchone()


    def consulta_usuario_general(self, cur, campo="cedula") -> list:
        """
        Consulta todos los datos de la tabla cliente ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.
        
        Regresa:
        datos_clientes (list): Lista de tuplas con todos los datos de los clientes.
        """
        cur.execute("SELECT * FROM cliente ORDER BY {}".format(campo))
        return cur.fetchall()


    def actualizar_usuario(self, con, cur) -> int:
        """
        Actualiza datos en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = (self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito, self._cedula)
        cur.execute('''
            UPDATE OR IGNORE cliente
            SET nombre = ?,
            apellido = ?,
            correo = ?,
            pais = ?,
            ciudad = ?,
            telefono = ?,
            tarjetaCredito = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount
    

    def actualizar_datos_pago(self, con, cur) -> int:
        """
        Ingresa un pago en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = [self._fecha_pago, self._pago, self._cedula]
        cur.execute('''
            UPDATE OR IGNORE cliente
            SET fechaPago = ?,
            pago = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount


    def borrar_usuario_especifico(self, con, cur) -> int:
        """
        Borra un registro en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedula (int): Cedula del cliente.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM cliente WHERE cedula = ?", [self._cedula])
        con.commit()
        return cur.rowcount


    def borrar_usuario_general(self, con, cur) -> int:
        """
        Borra todos los registros en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM cliente")
        con.commit()
        return cur.rowcount


def menu_cliente(con, cur):
    cliente = Cliente()

    while True:
        print("\nSeleccione que opciones desea realizar:")
        print("1. Añadir cliente nuevo.")
        print("2. Consulta general cliente.")
        print("3. Consulta especifica cliente.")
        print("4. Actualizar datos cliente.")
        print("5. Actualizar pago cliente.")
        print("6. Eliminar cliente especifico.")
        print("7. Eliminar cliente general.")
        print("0. Salir del menu cliente.")
        case = input()

        if case == "1":
            # Ingresando un nuevo cliente
            cedula = input("\nIngrese número de cedula: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            correo = input("Ingrese correo electronico: ")
            pais = input("Ingrese el nombre del pais donde habita: ")
            ciudad = input("Ingrese el nombre de la ciudad donde habita: ")
            telefono = input("Ingrese su numero telefono: ")
            tarjeta_credito = input("Ingrese el numero de tarjeta de credito: ")
            
            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and nombre.isalpha() and apellido.isalpha() and correo and telefono.isdigit() and tarjeta_credito.isdigit():
                cliente.cedula = int(cedula)  # Actualiza la cedula del objeto cliente
                cliente.datos_usuario = [nombre, apellido, correo, pais, ciudad, int(telefono), int(tarjeta_credito)]  # Actualiza los datos usuario del objeto cliente

                # Se borran las variables que ya no se utilizan
                del cedula, nombre, apellido, correo, pais, ciudad, telefono, tarjeta_credito

                # Llama al metodo para ingresar el usuario en la base de datos
                cambios = cliente.ingresar_usuario(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nCliente ingresado con exito.")
                else:
                    print("\nLa cedula ya esta registrada, no se han realizado cambios.")
            else:
                print("\nAlguno de los datos que ingreso no son correctos")

        elif case == "2":
            # Consulta general de clientes por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono",
                "Tarjeta credito", "Fecha Pago", "Pago"]  # Asgina los nombres de los campos en la tabla
            campo = "cedula"  # Campo por el que se va a ordenar

            # Bucle para poder ordenar las busquedas por campos
            while True:
                # Excepcion por si se ingresan campos que no esten en la tabla
                try:
                    # Busqueda en la tabla usuario general pasando el campo por el que ordena
                    datos_cliente = cliente.consulta_usuario_general(cur, campo)
                    
                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_cliente:
                        mi_tabla.add_rows(datos_cliente)  # Añade datos las filas a la tabla
                        print("")
                        print(mi_tabla)
                        bandera = input("Desea ordenar la busqueda por un campo (S/n): ")

                        # Bandera logica por si se quiere ordenar un campo
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            entrada = input("Ingrese el campo por el que quiere ordenar la busqueda: ").lower()  # Entrada en minisculas
                            campo = entrada.replace(" ", "")  # Si se ingresan espacios estos se remueven
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        break
                except OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha proporcionado.")
                    break

        elif case == "3":
            # Consulta especifica de clientes por cedula
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono",
                "Tarjeta credito", "Fecha Pago", "Pago"]  # Asgina los nombres de los campos en la tabla

            cedula = input("\nIngrese número de cedula: ")
            # Verficacion de los datos que son ingresados son correctos
            if cedula.isdigit():
                # Actualiza la cedula del objeto cliente
                cliente.cedula = int(cedula)
                # Almacena todos los datos del cliente
                datos_cliente = cliente.consulta_usuario_especifica(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_cliente:
                    mi_tabla.add_row(datos_cliente)  # Añade datos las filas a la tabla
                    print("")
                    print(mi_tabla)
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor de la cedula ingresado no es valido")

        elif case == "4":
            # Actualizar los datos del cliente
            print("\nIngrese los datos nuevos del cliente")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo electronico: ")
            pais = input("Pais: ")
            ciudad = input("Ciudad: ")
            telefono = input("Numero de telefono: ")
            tarjeta_credito = input("Numero tarjeta de credito: ")

            print("\nIngrese la cedula del cliente que va a modificar:")
            cedula = input()

            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and nombre.isalpha() and apellido.isalpha() and telefono.isdigit() and tarjeta_credito.isdigit():                
                cliente.cedula = int(cedula)  # Actualiza la cedula del objeto cliente
                cliente.datos_usuario = [nombre, apellido, correo, pais, ciudad, int(telefono), int(tarjeta_credito)]  # Actualiza los datos usuario del objeto cliente

                # Se borran las variables que ya no se utilizan
                del cedula, nombre, apellido, correo, pais, ciudad, telefono, tarjeta_credito
                
                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = cliente.actualizar_usuario(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nActualización realizada con exito.")
                else:
                    print("\nEsa cedula no esta registrada, no se han realizado cambios.")

        elif case == "5":
            # Actualiza los datos del pago
            print("\nIngrese la cedula del cliente cuyo pago a actualizar:")
            cedula = input()

            if cedula.isdigit():
                fecha = date.today()  # Obtiene la fecha de hoy
                # Calculos que le añaden seis meses a la fecha actual
                mes = fecha.month + 5
                año = fecha.year + mes // 12
                mes = mes % 12 + 1
                dia = fecha.day
                nueva_fecha = date(año, mes, dia)  # Se crea la nueva fecha de pago
                cliente.cedula = int(cedula)
                cliente.datos_pago = [nueva_fecha, 1]

                # Se borran las variables que ya no se utilizan
                del cedula, fecha, mes, año, dia, nueva_fecha

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = cliente.actualizar_datos_pago(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nInformación de pago realizada con exito.")
                else:
                    print("\nEsa cedula no esta registrada, no se han realizado cambios.")

        elif case == "6":
            # Eliminar datos especificos de la tabla cliente
            print("\nIngrese la cedula del cliente que va a eliminar:")
            cedula = input()

            if cedula.isdigit():
                cliente.cedula = int(cedula)

                del cedula  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = cliente.borrar_usuario_especifico(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nCliente eliminado con exito.")
                else:
                    print("\nEsa cedula no esta registrada, no se han realizado cambios.")

        elif case == "7":
            # Eliminar datos generales de la tabla cliente
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = cliente.borrar_usuario_general(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nTodos los datos de la tabla cliente han sidos eliminados.")
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")

        elif case == "0":
            print("\nSaliendo del menu cliente.")
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")
