# sisol

Este código Python implementa un Sistema Interactivo para la Gestión de Citas en una Clínica. Su objetivo principal es simular la interacción de diferentes tipos de usuarios (Pacientes, Médicos, Administradores) con un sistema centralizado para agendar, visualizar y gestionar citas médicas, así como registrar historiales clínicos y ver estadísticas.

El corazón del sistema es la clase SistemaInteractivo, que actúa como la interfaz de usuario principal. Esta clase permite a los usuarios:

Registrarse: Crear nuevas cuentas como Paciente, Médico o Administrador, solicitando información relevante para cada rol (teléfono para pacientes, especialidad para médicos).

Iniciar Sesión (Login): Acceder al sistema utilizando su correo electrónico.

Interactuar según su Rol: Una vez que un usuario inicia sesión, el sistema presenta un menú personalizado:

Pacientes: Pueden agendar nuevas citas con médicos específicos y visualizar sus citas programadas.

Médicos: Pueden ver su agenda de citas y registrar observaciones en el historial clínico de los pacientes.

Administradores: Tienen la capacidad de ver estadísticas generales del sistema, como el total de usuarios y citas.

Cerrar Sesión: Volver al menú principal de registro/login.

El sistema utiliza varias clases auxiliares (SistemaCitas, Usuario, Paciente, Medico, Administrador, Cita, HistorialClinico, Estadistica, AgendaMedica, Recordatorio, Notificacion) para organizar los datos y la lógica de negocio. Además, incluye una función cargarDatosDesdeJson para precargar usuarios y citas desde un archivo JSON, lo que facilita la prueba y el uso del sistema con datos iniciales.

En esencia, es una aplicación de consola que simula las operaciones básicas de una clínica en cuanto a la gestión de citas y la interacción con diferentes perfiles de usuario.
