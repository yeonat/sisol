import json
from datetime import datetime
from clinica import SistemaCitas, Paciente, Medico, Administrador, Recepcionista, Cita, HistorialClinico

def cargarDatosDesdeJson(ruta_json: str, sistema: SistemaCitas):
    try:
        with open(ruta_json, "r") as f:
            datos = json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_json}' no se encontró.")
        return
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el archivo JSON '{ruta_json}'. Asegúrate de que sea un JSON válido.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return

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

    for c in datos["citas"]:
        paciente = usuarios_map.get(c["paciente_id"])
        medico = usuarios_map.get(c["medico_id"])
        fecha = datetime.strptime(c["fecha"], "%Y-%m-%d %H:%M")
        if paciente and medico:
            cita = Cita(c["id"], paciente, medico, fecha)
            sistema.agendar_cita(cita)

    for a in datos["atenciones"]:
        paciente = usuarios_map.get(a["paciente_id"])
        if paciente:
            historial = HistorialClinico(a["historial_id"], paciente)
            historial.agregar_nota(a["nota"])
            sistema.agregar_historial_clinico(historial)
            print(f"Historial creado para {paciente.get_nombre()} con nota: {a['nota']}")

        

# # Uso de la función:
# if __name__ == "__main__":
#     sistema = SistemaCitas()
#     cargarDatosDesdeJson("datos_clinica.json", sistema)
