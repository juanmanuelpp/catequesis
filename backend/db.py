# -*- coding: utf-8 -*-
"""
Persistencia del progreso del niño — separada de la base de conocimiento
(content.py), tal como define el modelo: "El conocimiento se mantendrá
separado de las actividades y de los datos personales del niño."

Se usa SQLite para este piloto (cero configuración). El documento maestro ya
prevé migrar a PostgreSQL cuando el proyecto pase a producción; el código de
la API no tendría que cambiar mucho porque las consultas son simples.

No se guarda ningún dato personal del niño: solo un "código" que asigna el
catequista (por ejemplo, un nombre corto o un código de grupo), sin correo,
sin apellido, sin datos identificables.

DB_PATH = os.path.join("DB_PATH",os.path.dirname(__file__), "catequesis.db")

"""
import sqlite3
import datetime
import os

DB_PATH = os.getenv("DB_PATH", os.path.join(os.path.dirname(__file__), "catequesis.db"))



def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS ninos (
        codigo TEXT PRIMARY KEY,
        creado_en TEXT
    );

    CREATE TABLE IF NOT EXISTS intentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_nino TEXT,
        encuentro_id TEXT,
        contenido_id TEXT,
        actividad_id TEXT,
        intento INTEGER,
        aciertos INTEGER,
        total INTEGER,
        estado_actividad TEXT,
        pistas_usadas INTEGER,
        fecha_hora TEXT
    );

    CREATE TABLE IF NOT EXISTS estado_actividad (
        codigo_nino TEXT,
        actividad_id TEXT,
        contenido_id TEXT,
        estado TEXT,
        intentos INTEGER,
        pistas_usadas INTEGER,
        PRIMARY KEY (codigo_nino, actividad_id)
    );
    """)
    conn.commit()
    conn.close()


def asegurar_nino(codigo):
    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO ninos (codigo, creado_en) VALUES (?, ?)",
        (codigo, datetime.datetime.utcnow().isoformat()),
    )
    conn.commit()
    conn.close()


def obtener_estado_actividad(codigo_nino, actividad_id):
    conn = get_conn()
    row = conn.execute(
        "SELECT * FROM estado_actividad WHERE codigo_nino=? AND actividad_id=?",
        (codigo_nino, actividad_id),
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def registrar_intento(codigo_nino, encuentro_id, contenido_id, actividad_id,
                       intento, aciertos, total, estado_actividad, pistas_usadas):
    conn = get_conn()
    conn.execute(
        """INSERT INTO intentos
           (codigo_nino, encuentro_id, contenido_id, actividad_id, intento,
            aciertos, total, estado_actividad, pistas_usadas, fecha_hora)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (codigo_nino, encuentro_id, contenido_id, actividad_id, intento,
         aciertos, total, estado_actividad, pistas_usadas,
         datetime.datetime.utcnow().isoformat()),
    )
    conn.execute(
        """INSERT INTO estado_actividad (codigo_nino, actividad_id, contenido_id, estado, intentos, pistas_usadas)
           VALUES (?,?,?,?,?,?)
           ON CONFLICT(codigo_nino, actividad_id)
           DO UPDATE SET estado=excluded.estado, intentos=excluded.intentos,
                         pistas_usadas=excluded.pistas_usadas""",
        (codigo_nino, actividad_id, contenido_id, estado_actividad, intento, pistas_usadas),
    )
    conn.commit()
    conn.close()


def estados_de_contenido(codigo_nino, actividad_ids):
    conn = get_conn()
    estados = []
    for aid in actividad_ids:
        row = conn.execute(
            "SELECT estado FROM estado_actividad WHERE codigo_nino=? AND actividad_id=?",
            (codigo_nino, aid),
        ).fetchone()
        estados.append(row["estado"] if row else None)
    conn.close()
    return estados


def progreso_actividades(codigo_nino, actividad_ids):
    conn = get_conn()
    out = {}
    for aid in actividad_ids:
        row = conn.execute(
            "SELECT estado, intentos, pistas_usadas FROM estado_actividad WHERE codigo_nino=? AND actividad_id=?",
            (codigo_nino, aid),
        ).fetchone()
        out[aid] = dict(row) if row else {"estado": None, "intentos": 0, "pistas_usadas": 0}
    conn.close()
    return out
