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
    
# Clase Paciente
class Paciente(Usuario):
    def __init__(self, id, nombre, correo, telefono):
        super().__init__(id, nombre, correo)
        self.__telefono = telefono
        self.__citas: List[Cita] = []

    def agregar_cita(self, cita):
        self.__citas.append(cita)

    def get_rol(self):
        return "Paciente"
    
    def get_telefono(self):
        return self.__telefono

    def get_citas(self):
        return self.__citas
    
# Clase Medico
# class Medico(Usuario):
#     def __init__(self, id, nombre, correo, especialidad):
#         super().__init__(id, nombre, correo)
#         self.__especialidad = especialidad
#         self.__agenda = AgendaMedica()

#     def get_rol(self):
#         return "Medico"
    
#     def get_especialidad(self):
#         return self.__especialidad
    
#     def get_agenda(self):
#         return self.__agenda

# Clase Administrador
class Administrador(Usuario):
    def get_rol(self):
        return "Administrador"

# Clase Recepcionista
class Recepcionista(Usuario):
    def get_rol(self):
        return "Recepcionista"
    
# Cita médica
# class Cita:
#     def __init__(self, id: str, paciente: Paciente, medico: Medico, fecha: datetime):
#         self.__id = id
#         self.__paciente = paciente
#         self.__medico = medico
#         self.__fecha = fecha
#         self.__estado = "Programada"

#     def get_id(self):
#         return self.__id

#     def get_paciente(self):
#         return self.__paciente

#     def get_medico(self):
#         return self.__medico

#     def get_fecha(self):
#         return self.__fecha

#     def get_estado(self):
#         return self.__estado