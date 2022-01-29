from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self):
        self._cedula = None
        self._nombre = None
        self._apellido = None
        self._correo = None

    @property
    @abstractmethod
    def cedula(self): pass

    @property
    @abstractmethod
    def datos_usuario(self): pass

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
