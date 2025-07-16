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

    def registrar_usuario(self):
        print("\n--- Registro ---")
        rol = input("Rol (paciente / medico / admin): ").lower()
        id = input("ID: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        if rol == "paciente":
            telefono = input("Teléfono: ")
            usuario = Paciente(id, nombre, correo, telefono)
        elif rol == "medico":
            especialidad = input("Especialidad: ")
            usuario = Medico(id, nombre, correo, especialidad)
        elif rol == "admin":
            usuario = Administrador(id, nombre, correo)
        else:
            print("Rol inválido.")
            return

        self.__sistema.registrar_usuario(usuario)
        print(f"{rol.capitalize()} registrado exitosamente.")

    def login(self):
        print("\n--- Login ---")
        correo = input("Correo: ")
        for usuario in self.__sistema.get_usuarios():
            if usuario.get_correo() == correo:
                self.__usuario_actual = usuario
                print(f"Bienvenido/a, {usuario.get_nombre()}. Rol: {usuario.get_rol()}")
                self.menu_usuario()
                return
        print("Usuario no encontrado.")
