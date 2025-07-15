import json
from datetime import datetime
from clinica import SistemaCitas, Paciente, Medico, Administrador, Recepcionista, Cita, HistorialClinico

def cargarDatosDesdeJson(ruta_json: str, sistema: SistemaCitas):
    with open(ruta_json, "r") as f:
        datos = json.load(f)

    usuarios_map = {}

    for u in datos["usuarios"]:
        tipo = u["tipo"]
        if tipo == "Paciente":
            usuario = Paciente(u["id"], u["nombre"], u["correo"], u["telefono"])
        elif tipo == "Medico":
            usuario = Medico(u["id"], u["nombre"], u["correo"], u["especialidad"])
        elif tipo == "Administrador":
            usuario = Administrador(u["id"], u["nombre"], u["correo"])
        elif tipo == "Recepcionista":
            usuario = Recepcionista(u["id"], u["nombre"], u["correo"])
        else:
            continue
        sistema.registrar_usuario(usuario)
        usuarios_map[u["id"]] = usuario
