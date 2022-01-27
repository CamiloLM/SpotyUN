from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, cedula, nombre, apellido, correo):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    @property
    @abstractmethod
    def cedula(self): pass

    @property
    @abstractmethod
    def datos(self): pass

    @abstractmethod
    def ingresar_usuario(self): pass

    @abstractmethod
    def consulta_usuario_especifica(self): pass

    @abstractmethod
    def consulta_usuario_general(self): pass

    @abstractmethod
    def actualizar_usuario(self): pass

    @abstractmethod
    def borrar_usuario_especifico(self): pass

    @abstractmethod
    def borrar_usuario_general(self): pass
