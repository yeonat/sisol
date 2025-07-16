from datetime import datetime
from clinica import SistemaCitas, Usuario, Paciente, Medico, Administrador, Cita, HistorialClinico, Estadistica
from cargarDatosDesdeJson import cargarDatosDesdeJson

class SistemaInteractivo:
    def __init__(self, sistema: SistemaCitas):
        self.__sistema = sistema
        self.__usuario_actual: Usuario = None

    def iniciar(self):
        while True:
            print("\n--- Clínica Saludable ---")
            print("1. Registro de Usuario")
            print("2. Login")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.login()
            elif opcion == "3":
                print("Gracias por usar el sistema.")
                exit()
            else:
                print("Opción inválida.")
