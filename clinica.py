from datetime import datetime
from typing import List

# Módulo base para gestión de citas en la clínica - Versión Python
# Clase base Usuario
class Usuario:
    def __init__(self, id: str, nombre: str, correo: str):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo

    def get_rol(self):
        pass

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo