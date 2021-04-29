from datetime import datetime
import clases


def mandar():
    dia = datetime.now().weekday()
    hora = datetime.now().strftime("%H:%M")
    for materia in clases.info:
        if materia.get("dia") == dia:
            if hora == materia.get("hora"):
                return materia
