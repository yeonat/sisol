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
class Medico(Usuario):
    def __init__(self, id, nombre, correo, especialidad):
        super().__init__(id, nombre, correo)
        self.__especialidad = especialidad
        self.__agenda = AgendaMedica()

    def get_rol(self):
        return "Medico"
    
    def get_especialidad(self):
        return self.__especialidad
    
    def get_agenda(self):
        return self.__agenda
    
# Clase Administrador
class Administrador(Usuario):
    def get_rol(self):
        return "Administrador"
    
# Clase Recepcionista
class Recepcionista(Usuario):
    def get_rol(self):
        return "Recepcionista"

# Cita médica
class Cita:
    def __init__(self, id: str, paciente: Paciente, medico: Medico, fecha: datetime):
        self.__id = id
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha = fecha
        self.__estado = "Programada"

    def get_id(self):
        return self.__id

    def get_paciente(self):
        return self.__paciente

    def get_medico(self):
        return self.__medico

    def get_fecha(self):
        return self.__fecha

    def get_estado(self):
        return self.__estado

# Agenda médica del médico
class AgendaMedica:
    def __init__(self):
        self.__citas: List[Cita] = []

    def agregar_cita(self, cita: Cita):
        self.__citas.append(cita)

    def get_citas(self):
        return self.__citas

# Recordatorio
class Recordatorio:
    def __init__(self, id: str, mensaje: str):
        self.__id = id
        self.__mensaje = mensaje

    def get_id(self):
        return self.__id

    def get_mensaje(self):
        return self.__mensaje

    @staticmethod
    def enviar(paciente: Paciente, cita: Cita):
        print(f"Recordatorio: {paciente.get_nombre()}, tienes una cita el {cita.get_fecha()}.")

# Notificación general
class Notificacion:
    def __init__(self, id: str, contenido: str):
        self.__id = id
        self.__contenido = contenido

    def get_id(self):
        return self.__id
    
    def get_contenido(self):
        return self.__contenido

# Historial clínico
class HistorialClinico:
    def __init__(self, id: str, paciente: Paciente):
        self.__id = id
        self.__paciente = paciente
        self.__notas: List[str] = []

    def agregar_nota(self, texto: str):
        self.__notas.append(texto)

    def get_notas(self):
        return self.__notas   
     
    def get_paciente(self):
        return self.__paciente
    
    def get_id(self):
        return self.__id

# Estadística
class Estadistica:
    def __init__(self, id: str, datos: dict):
        self.__id = id
        self.__datos = datos

    def get_id(self):
        return self.__id

    def mostrar_reporte(self):
        print(f"Reporte: {self.__datos}")

# Sistema central de citas
class SistemaCitas:
    def __init__(self):
        self.__usuarios: List[Usuario] = []
        self.__citas: List[Cita] = []
        self.__historiales_clinicos = {} # Add this line to store medical histories.

    def get_usuarios(self):
        return self.__usuarios
    
    def get_citas(self):
        return self.__citas
    
      # Add these lines to get and add medical histories.
    def get_historial_clinico(self, paciente_id: str):
        return self.__historiales_clinicos.get(paciente_id)

    def agregar_historial_clinico(self, historial: HistorialClinico):
            self.__historiales_clinicos[historial.get_paciente().get_id()] = historial

    def registrar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    def agendar_cita(self, cita: Cita):
        self.__citas.append(cita)
        cita.get_paciente().agregar_cita(cita)
        cita.get_medico().get_agenda().agregar_cita(cita)
        Recordatorio.enviar(cita.get_paciente(), cita)
        