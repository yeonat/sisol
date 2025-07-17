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

    def menu_usuario(self):
        while self.__usuario_actual:
            rol = self.__usuario_actual.get_rol()
            print(f"\n--- Menú ({rol}) ---")
            print("1. Gestión de Citas")
            print("2. Visualizar Agenda")
            if rol == "Medico":
                print("3. Registrar Observaciones")
            elif rol == "Administrador":
                print("3. Ver Estadísticas")
            print("0. Cerrar Sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_citas()
            elif opcion == "2":
                self.ver_agenda()
            elif opcion == "3" and rol == "Medico":
                self.registrar_observaciones()
            elif opcion == "3" and rol == "Administrador":
                self.ver_estadisticas()
            elif opcion == "0":
                print("Cerrando sesión...")
                self.__usuario_actual = None
                self.iniciar()
            else:
                print("Opción inválida.")

    def gestionar_citas(self):
        if isinstance(self.__usuario_actual, Paciente):
            medico_id = input("Ingrese ID del médico: ")
            fecha = input("Ingrese fecha de la cita (YYYY-MM-DD HH:MM): ")
            medico = next((u for u in self.__sistema.get_usuarios() if isinstance(u, Medico) and u.get_id() == medico_id), None)
            if medico:
                cita = Cita(f"cita{len(self.__sistema.get_citas())+1}", self.__usuario_actual, medico, datetime.strptime(fecha, "%Y-%m-%d %H:%M"))
                self.__sistema.agendar_cita(cita)
                print("Cita agendada.")
            else:
                print("Médico no encontrado.")
        else:
            print("Solo los pacientes pueden agendar citas.")

    def ver_agenda(self):
        if isinstance(self.__usuario_actual, Medico):
            for cita in self.__usuario_actual.get_agenda().get_citas():
                print(f"{cita.get_fecha()} - Paciente: {cita.get_paciente().get_nombre()}")
        elif isinstance(self.__usuario_actual, Paciente):
            for cita in self.__usuario_actual.get_citas():
                print(f"{cita.get_fecha()} - Médico: {cita.get_medico().get_nombre()} - Observaciones: {self.ver_observaciones(cita.get_paciente())}")
        else:
            print("Sin agenda asociada.")

    def registrar_observaciones(self):
        paciente_id = input("ID del paciente: ")
        nota = input("Ingrese observación: ")
        paciente = next((u for u in self.__sistema.get_usuarios() if isinstance(u, Paciente) and u.get_id() == paciente_id), None)
        if paciente:
            # Retrieve existing historial or create a new one
            historial = self.__sistema.get_historial_clinico(paciente.get_id())
            if not historial:
                historial = HistorialClinico(f"hist_{paciente.get_id()}", paciente)
                self.__sistema.agregar_historial_clinico(historial)
            historial.agregar_nota(nota)
            print("Observación registrada.")
        else:
            print("Paciente no encontrado.")

    def ver_observaciones(self, paciente: Paciente):
        if paciente:
            historial = self.__sistema.get_historial_clinico(paciente.get_id())
            if historial:
                # Join all notes with a newline for better readability
                return "\n".join(historial.get_notas()) 
            else:
                return "No hay observaciones registradas."
        else:
            return "Paciente no encontrado."

    def ver_estadisticas(self):
        stats = Estadistica("1", {"total_usuarios": len(self.__sistema.get_usuarios()), "total_citas": len(self.__sistema.get_citas())})
        stats.mostrar_reporte()

# Ejecución del sistema
if __name__ == "__main__":
    sistema_citas = SistemaCitas()
    cargarDatosDesdeJson("datos_clinica.json", sistema_citas)
    app = SistemaInteractivo(sistema_citas)
    app.iniciar()
    