# -*- coding: utf-8 -*-
"""
Base de conocimiento — Camino a la Primera Comunión
Contenido REAL de dieciséis encuentros, cada uno con sus 6 contenidos y 60
actividades (10 por contenido) — 96 contenidos y 960 actividades en total:

  PC01 — "Dios nos creó por amor" (PC01-C01 a PC01-C06), tomado del
         documento maestro v4.0 (PC01-C01) y del documento
         "PC02PC06_A01-10" que completó los contenidos C02 a C06. La
         familia "aplicación" (A10) se había retirado del modelo tras
         probar el piloto, y se reintegró luego como una tarea de la
         vida real (situación + varias respuestas válidas).
  PC02 — "Jesús es nuestro amigo" (PC02-C01 a PC02-C06, Marcos 10,13-16),
         tomado del documento maestro de este segundo encuentro. Algunas
         actividades de tipo "reto" y "aplicación" que el documento
         describe como tarea abierta (escribir una oración propia,
         realizar una acción y contarla) se adaptaron al mismo mecanismo
         de opciones con varias respuestas válidas que ya usan el resto
         de actividades, para reutilizar el motor ya probado en vez de
         crear un tipo de actividad nuevo.
  PC03 — "Dios nos habla en la Biblia" (PC03-C01 a PC03-C06,
         2 Timoteo 3,14-17 / Lucas 24,13-35), alineado con el documento
         maestro de este tercer encuentro (Emaús y la Palabra de Dios
         como guía de vida).
  PC04 — "La familia de Jesús: la Iglesia" (PC04-C01 a PC04-C06,
         Hechos 2,42-47), alineado con el documento maestro de este
         cuarto encuentro (la primera comunidad cristiana y la Iglesia
         como familia).
  PC05 — "El Bautismo: somos hijos de Dios" (PC05-C01 a PC05-C06,
         Mateo 28,18-20 / Juan 3,5), alineado con el documento maestro
         de este quinto encuentro (el mandato de Jesús, la Trinidad, el
         agua como signo y la filiación divina).
  PC06 — "La Eucaristía: Jesús se queda con nosotros" (PC06-C01 a
         PC06-C06, Lucas 22,19-20 / Juan 6,51), alineado con el documento
         maestro de este sexto encuentro (la Última Cena, la entrega de
         Jesús en el pan y el vino, y la participación en la Misa).
  PC07 — "El Espíritu Santo nos da fuerza" (PC07-C01 a PC07-C06,
         Hechos 2,1-4), alineado con el documento maestro de este séptimo
         encuentro (Pentecostés, los dones del Espíritu y el testimonio
         alegre de la fe).
  PC08 — "Jesús nos enseña a amar a todos" (PC08-C01 a PC08-C06,
         Lucas 10,25-37), alineado con el documento maestro de este
         octavo encuentro (la parábola del Buen Samaritano y el amor sin
         distinción de personas).
  PC09 — "Aprendemos a rezar con Jesús" (PC09-C01 a PC09-C06,
         Mateo 6,5-13), alineado con el documento maestro de este noveno
         encuentro (la enseñanza de Jesús sobre la oración sincera y el
         Padre Nuestro).
  PC10 — "María, la Madre de Jesús y Madre nuestra" (PC10-C01 a
         PC10-C06, Lucas 1,26-38 / Juan 19,25-27), alineado con el
         documento maestro de este décimo encuentro (la Anunciación, el
         "sí" de María y su maternidad espiritual sobre la Iglesia).
  PC11 — "Somos amigos y misioneros de Jesús" (PC11-C01 a PC11-C06,
         Juan 15,15-17 / Mateo 28,19-20), sobre la amistad con Jesús que
         se vuelve misión: ser enviados a anunciar con la vida lo que se
         ha recibido.
  PC12 — "Dios nos promete la vida eterna" (PC12-C01 a PC12-C06,
         Juan 11,25-26 / Juan 14,1-3), sobre la resurrección, la
         esperanza cristiana y la promesa de una casa preparada junto al
         Padre.
  PC13 — "El Espíritu Santo nos envía" (PC13-C01 a PC13-C06,
         Hechos 1,8 / Juan 20,21-22), sobre la fuerza y los dones del
         Espíritu Santo que capacitan y envían a dar testimonio.
  PC14 — "Iglesia sinodal: caminamos juntos" (PC14-C01 a PC14-C06,
         Hechos 15,6-7.22 / Hechos 2,42), sobre la Iglesia como
         comunidad que escucha, discierne y camina unida.
  PC15 — "Ser luz en el mundo" (PC15-C01 a PC15-C06,
         Mateo 5,14-16 / Juan 8,12), sobre el testimonio cristiano en la
         vida diaria, a partir de la imagen de la luz y la sal.
  PC16 — "Celebración final: envío misionero" (PC16-C01 a PC16-C06,
         Hechos 1,8-11 / Lucas 24,50-53), el cierre del itinerario: un
         recorrido de memoria agradecida por todo el camino recorrido,
         la Ascensión como escena bíblica central, el envío misionero y
         una vuelta final a María como Madre de la Iglesia (haciendo eco
         intencional de PC10), terminando en una "Celebración final"
         cuya última actividad dispara la animación de cierre descrita
         más abajo.

  Nota sobre PC06 a PC16: el documento maestro entregado por la
  formadora solo llegaba hasta especificar, encuentro por encuentro, el
  título y (para PC06-PC10) la cita bíblica y la pregunta guía de la
  actividad A03 ("Práctica con la Biblia"); para PC11-PC16 solo se
  recibieron los seis títulos de encuentro. En todos los casos el resto
  de la plantilla (A01-A02, A04-A10, y para PC11-PC16 también las citas
  bíblicas de cada contenido) se redactó siguiendo el mismo estilo,
  nivel catequético y estructura pedagógica que los encuentros
  anteriores, cuidando no repetir una misma cita bíblica de A03 entre
  encuentros distintos. Por tratarse de contenido redactado sin un
  documento maestro detallado para PC11-PC16, conviene que la formadora
  lo revise y lo compare con su propio material antes de usarlo con los
  niños. Por convención (igual que en PC01-PC05), las respuestas del
  crucigrama se escriben sin tildes ni Ñ, ya que generar_layout_crucigrama
  (en app.py) normaliza los acentos automáticamente.

Bloqueo de avance ("gating"): un niño no puede abrir el contenido
siguiente de un encuentro (ni el primer contenido del encuentro
siguiente) si no ha aprobado (logrado) todas las actividades del
contenido actual. Si intenta saltarse contenido sin haber aprobado sus
actividades, la API responde con una advertencia explícita indicando
que debe completar las actividades del contenido actual antes de
avanzar, en vez de permitir el salto.

Animación final del camino (al terminar PC16-C06-A10): como
CONTENIDOS es una sola lista continua que recorre los 16 encuentros en
orden, siguiente_contenido_de(...) devuelve None únicamente para el
último contenido de todo el itinerario (PC16-C06). Cuando ese contenido
se completa, la respuesta de /api/actividad/<id>/responder incluye
"camino_completo": true, y el frontend usa esa señal (en vez del aviso
genérico de "encuentro completado") para mostrar una animación de
cierre: un camino ilustrado en el que va apareciendo, encuentro por
encuentro, la figura de un niño que recorre y supera los 16 encuentros,
hasta llegar a un altar con Jesús, que los recibe con los brazos
abiertos y una frase de felicitación por haber completado el camino
hacia la Primera Comunión.

Las familias de actividad por contenido, en orden pedagógico (iguales en
los dieciséis encuentros):
  A01 crucigrama          A06 seleccion_multiple
  A02 sopa_letras         A07 unir_parejas
  A03 práctica c/Biblia*  A08 reto
  A04 completar           A09 recuperacion
  A05 verdadero_falso     A10 aplicacion

  * A03 es la actividad "Práctica con la Biblia" en los 96 contenidos de
    los 16 encuentros (alineada con el documento maestro, donde sustituyó
    a la antigua "Palabra por número" en toda la formación). Reutiliza el
    tipo "completar" ya probado: un primer ítem cerrado en el que el niño
    busca la cita indicada en su Biblia y completa la palabra que falta
    en el versículo (con banco de palabras distractoras), y un segundo
    ítem abierto ("abierta": True) de reflexión personal sobre lo leído,
    evaluado solo por participación. Cada contenido tiene su propia cita
    bíblica distinta, relacionada con su contenido específico, para que
    la práctica y la experiencia sean más enriquecedoras (antes de esta
    unificación, PC01 y PC02 usaban aquí una segunda sopa de letras).

Varios tipos reutilizan el mismo "motor de interacción" que otro tipo ya
probado, porque su mecánica pedagógica es equivalente:
  - crucigrama    -> se arma como una cuadrícula real, con las palabras
                      cruzándose entre sí (generar_layout_crucigrama, en
                      app.py); la evaluación reutiliza la misma mecánica
                      que completar (definición -> palabra)
  - recuperacion  -> misma mecánica que completar (admite ítems "abiertos",
                      sin respuesta única, evaluados solo por participación)
  - reto          -> dos modos: "preguntas" (igual a seleccion_multiple,
                      con cronómetro) o "elegir_libres" (marcar varias
                      palabras/ideas de un banco, con un mínimo requerido)
  - aplicacion    -> misma mecánica que seleccion_multiple (una "situación"
                      de contexto + una pregunta con varias opciones), pero
                      admitiendo más de una respuesta igualmente válida
                      ("correctas": [índices]) porque en la vida real hay
                      más de una buena acción posible ante la misma situación
"""

ENCUENTROS = [
    {
        "id": "PC01",
        "titulo": "Dios nos creó por amor",
        "texto_biblico": "Génesis 1,26-31",
        "objetivo": "Reconocer que somos creación de Dios y obra de su amor.",
    },
    {
        "id": "PC02",
        "titulo": "Jesús es nuestro amigo",
        "texto_biblico": "Marcos 10,13-16",
        "objetivo": "Descubrir a Jesús como amigo cercano que nos ama y nos bendice.",
    },
    {
        "id": "PC03",
        "titulo": "Dios nos habla en la Biblia",
        "texto_biblico": "2 Timoteo 3,14-17 / Lucas 24,13-35",
        "objetivo": "Descubrir la Palabra de Dios como guía para nuestra vida.",
    },
    {
        "id": "PC04",
        "titulo": "La familia de Jesús: la Iglesia",
        "texto_biblico": "Hechos 2,42-47",
        "objetivo": "Comprender que la Iglesia es una familia unida en el amor y la fe.",
    },
    {
        "id": "PC05",
        "titulo": "El Bautismo: somos hijos de Dios",
        "texto_biblico": "Mateo 28,18-20 / Juan 3,5",
        "objetivo": "Valorar el Bautismo como comienzo de nuestra vida cristiana.",
    },
    {
        "id": "PC06",
        "titulo": "La Eucaristía: Jesús se queda con nosotros",
        "texto_biblico": "Lucas 22,19-20 / Juan 6,51",
        "objetivo": "Reconocer la Eucaristía como presencia viva de Jesús.",
    },
    {
        "id": "PC07",
        "titulo": "El Espíritu Santo nos da fuerza",
        "texto_biblico": "Hechos 2,1-4",
        "objetivo": "Reconocer al Espíritu Santo como fuerza y guía de nuestra fe.",
    },
    {
        "id": "PC08",
        "titulo": "Jesús nos enseña a amar a todos",
        "texto_biblico": "Lucas 10,25-37",
        "objetivo": "Aprender a amar sin distinción siguiendo al Buen Samaritano.",
    },
    {
        "id": "PC09",
        "titulo": "Aprendemos a rezar con Jesús",
        "texto_biblico": "Mateo 6,5-13",
        "objetivo": "Aprender a orar con confianza como hijos de Dios.",
    },
    {
        "id": "PC10",
        "titulo": "María, la Madre de Jesús y Madre nuestra",
        "texto_biblico": "Lucas 1,26-38 / Juan 19,25-27",
        "objetivo": "Imitar la fe y obediencia de María.",
    },
    {
        "id": "PC11",
        "titulo": "Somos amigos y misioneros de Jesús",
        "texto_biblico": "Juan 15,15-17 / Mateo 28,19-20",
        "objetivo": "Descubrir que ser amigos de Jesús nos llama a ser también sus misioneros.",
    },
    {
        "id": "PC12",
        "titulo": "Dios nos promete la vida eterna",
        "texto_biblico": "Juan 11,25-26 / Juan 14,1-3",
        "objetivo": "Descubrir la esperanza de la vida eterna que Jesús nos promete.",
    },
    {
        "id": "PC13",
        "titulo": "El Espíritu Santo nos envía",
        "texto_biblico": "Hechos 1,8 / Juan 20,21-22",
        "objetivo": "Reconocer que el Espíritu Santo nos envía a continuar la misión de Jesús.",
    },
    {
        "id": "PC14",
        "titulo": "Iglesia sinodal: caminamos juntos",
        "texto_biblico": "Hechos 15,6-7.22 / Hechos 2,42",
        "objetivo": "Descubrir que la Iglesia camina junta, escuchando y decidiendo en comunidad, como el Pueblo de Dios.",
    },
    {
        "id": "PC15",
        "titulo": "Ser luz en el mundo",
        "texto_biblico": "Mateo 5,14-16 / Juan 8,12",
        "objetivo": "Descubrir que estamos llamados a ser luz del mundo, siguiendo el ejemplo de Jesús.",
    },
    {
        "id": "PC16",
        "titulo": "Celebración final: envío misionero",
        "texto_biblico": "Hechos 1,8-11 / Lucas 24,50-53",
        "objetivo": "Celebrar el camino recorrido y recibir el envío misionero como discípulos de Jesús.",
    },
]

CONTENIDOS = [
    {"id": "PC01-C01", "titulo": "Dios es Creador"},
    {"id": "PC01-C02", "titulo": "Dios nos creó por amor"},
    {"id": "PC01-C03", "titulo": "Somos creados a imagen de Dios"},
    {"id": "PC01-C04", "titulo": "Soy único y valioso para Dios"},
    {"id": "PC01-C05", "titulo": "Dios nos confió el cuidado de su creación"},
    {"id": "PC01-C06", "titulo": "Cuidamos juntos la creación"},
    {"id": "PC02-C01", "titulo": "Jesús acoge a los niños"},
    {"id": "PC02-C02", "titulo": "Jesús ama y bendice"},
    {"id": "PC02-C03", "titulo": "Los discípulos aprenden a acoger"},
    {"id": "PC02-C04", "titulo": "Jesús es amigo cercano"},
    {"id": "PC02-C05", "titulo": "La amistad con Jesús se vive en oración"},
    {"id": "PC02-C06", "titulo": "Mostramos la amistad de Jesús"},
    {"id": "PC03-C01", "titulo": "La Biblia es Palabra de Dios"},
    {"id": "PC03-C02", "titulo": "La Palabra guía la vida"},
    {"id": "PC03-C03", "titulo": "Jesús se revela en la Escritura"},
    {"id": "PC03-C04", "titulo": "Los discípulos de Emaús reconocen a Jesús"},
    {"id": "PC03-C05", "titulo": "Escuchar y meditar la Palabra"},
    {"id": "PC03-C06", "titulo": "Compartir la Palabra en familia y comunidad"},
    {"id": "PC04-C01", "titulo": "La primera comunidad cristiana"},
    {"id": "PC04-C02", "titulo": "Los cristianos viven como hermanos"},
    {"id": "PC04-C03", "titulo": "Compartir es parte de la comunidad"},
    {"id": "PC04-C04", "titulo": "La Iglesia es familia"},
    {"id": "PC04-C05", "titulo": "Pertenecer a la comunidad"},
    {"id": "PC04-C06", "titulo": "Construir fraternidad"},
    {"id": "PC05-C01", "titulo": "Jesús manda bautizar"},
    {"id": "PC05-C02", "titulo": "Bautismo en el nombre de la Trinidad"},
    {"id": "PC05-C03", "titulo": "El agua como signo bautismal"},
    {"id": "PC05-C04", "titulo": "Somos hijos de Dios"},
    {"id": "PC05-C05", "titulo": "Somos miembros de la Iglesia"},
    {"id": "PC05-C06", "titulo": "Recordamos y vivimos el Bautismo"},
    {"id": "PC06-C01", "titulo": "La Última Cena"},
    {"id": "PC06-C02", "titulo": "Pan y vino en la entrega de Jesús"},
    {"id": "PC06-C03", "titulo": "Jesús se entrega por amor"},
    {"id": "PC06-C04", "titulo": "La Eucaristía es presencia viva de Jesús"},
    {"id": "PC06-C05", "titulo": "La Misa y la comunión"},
    {"id": "PC06-C06", "titulo": "Participar con respeto y alegría"},
    {"id": "PC07-C01", "titulo": "Pentecostés"},
    {"id": "PC07-C02", "titulo": "El Espíritu Santo llega a los apóstoles"},
    {"id": "PC07-C03", "titulo": "Fuerza, alegría y valor"},
    {"id": "PC07-C04", "titulo": "Dones del Espíritu"},
    {"id": "PC07-C05", "titulo": "El Espíritu guía la fe"},
    {"id": "PC07-C06", "titulo": "Testimonio alegre"},
    {"id": "PC08-C01", "titulo": "El hombre herido"},
    {"id": "PC08-C02", "titulo": "El Buen Samaritano ayuda"},
    {"id": "PC08-C03", "titulo": "Amar sin distinción"},
    {"id": "PC08-C04", "titulo": "La compasión"},
    {"id": "PC08-C05", "titulo": "Ayudar al que sufre"},
    {"id": "PC08-C06", "titulo": "Ser buen samaritano hoy"},
    {"id": "PC09-C01", "titulo": "Jesús enseña a orar"},
    {"id": "PC09-C02", "titulo": "Orar con sinceridad"},
    {"id": "PC09-C03", "titulo": "Padre Nuestro"},
    {"id": "PC09-C04", "titulo": "La oración como diálogo de amor"},
    {"id": "PC09-C05", "titulo": "Pedir y agradecer"},
    {"id": "PC09-C06", "titulo": "Orar en familia y comunidad"},
    {"id": "PC10-C01", "titulo": "La anunciación"},
    {"id": "PC10-C02", "titulo": "El mensaje del ángel"},
    {"id": "PC10-C03", "titulo": "El sí de María"},
    {"id": "PC10-C04", "titulo": "Fe y obediencia"},
    {"id": "PC10-C05", "titulo": "María nos acerca a Jesús"},
    {"id": "PC10-C06", "titulo": "Disponibilidad y alegría"},
    {"id": "PC11-C01", "titulo": "Jesús nos llama amigos"},
    {"id": "PC11-C02", "titulo": "La amistad se comparte"},
    {"id": "PC11-C03", "titulo": "El envío de los apóstoles"},
    {"id": "PC11-C04", "titulo": "Ser testigos de Jesús"},
    {"id": "PC11-C05", "titulo": "Anunciar con la vida"},
    {"id": "PC11-C06", "titulo": "Misioneros en la familia y la escuela"},
    {"id": "PC12-C01", "titulo": "Jesús vence a la muerte"},
    {"id": "PC12-C02", "titulo": "\"Yo soy la resurrección y la vida\""},
    {"id": "PC12-C03", "titulo": "El cielo, la casa del Padre"},
    {"id": "PC12-C04", "titulo": "Vivir con esperanza"},
    {"id": "PC12-C05", "titulo": "Los santos ya viven con Dios"},
    {"id": "PC12-C06", "titulo": "Caminar hacia la vida eterna"},
    {"id": "PC13-C01", "titulo": "El Espíritu Santo, don de Jesús resucitado"},
    {"id": "PC13-C02", "titulo": "Recibimos fuerza para ser testigos"},
    {"id": "PC13-C03", "titulo": "Los dones del Espíritu Santo"},
    {"id": "PC13-C04", "titulo": "Los frutos del Espíritu Santo"},
    {"id": "PC13-C05", "titulo": "El Espíritu Santo guía a la Iglesia"},
    {"id": "PC13-C06", "titulo": "Enviados como Jesús fue enviado"},
    {"id": "PC14-C01", "titulo": "La Iglesia, Pueblo de Dios"},
    {"id": "PC14-C02", "titulo": "Caminar juntos: qué es la sinodalidad"},
    {"id": "PC14-C03", "titulo": "Escuchar a todos en la comunidad"},
    {"id": "PC14-C04", "titulo": "Decidir en comunión"},
    {"id": "PC14-C05", "titulo": "Cada uno tiene un don para la comunidad"},
    {"id": "PC14-C06", "titulo": "Somos Iglesia: cada uno importa"},
    {"id": "PC15-C01", "titulo": "Jesús, luz del mundo"},
    {"id": "PC15-C02", "titulo": "Ustedes son la luz del mundo"},
    {"id": "PC15-C03", "titulo": "Una lámpara no se esconde"},
    {"id": "PC15-C04", "titulo": "Que brille la luz de las buenas obras"},
    {"id": "PC15-C05", "titulo": "Vencer la oscuridad con el bien"},
    {"id": "PC15-C06", "titulo": "Caminar en la luz"},
    {"id": "PC16-C01", "titulo": "Recordamos nuestro camino de fe"},
    {"id": "PC16-C02", "titulo": "La Ascensión: Jesús vuelve al Padre"},
    {"id": "PC16-C03", "titulo": "La alegría de la fe recibida"},
    {"id": "PC16-C04", "titulo": "Enviados a anunciar el Evangelio"},
    {"id": "PC16-C05", "titulo": "Acompañados por María, Madre de la Iglesia"},
    {"id": "PC16-C06", "titulo": "Celebración final: nuestro envío misionero"},
]

FEEDBACK_OK = "¡Excelente! Sigue profundizando tu fe."
FEEDBACK_OK_RELACION = "¡Muy bien! Has relacionado las ideas."
FEEDBACK_OK_RECORDASTE = "¡Muy bien! Has recordado la idea."
FEEDBACK_OK_COMPRENDISTE = "¡Excelente! Comprendiste el mensaje."
FEEDBACK_FALTA = "Vamos a pensar juntos. Puedes intentarlo otra vez."

# Mensaje que recibe el niño cuando su respuesta abierta contiene una
# palabra de PALABRAS_ALERTA (ver más abajo), en vez del feedback_falta
# genérico de la actividad.
FEEDBACK_ALERTA = ("Esa respuesta no refleja lo que hemos aprendido. Vuelve a pensarlo: "
                    "¿qué nos enseña este tema sobre el amor de Dios?")

# Mensaje que recibe el niño cuando su respuesta abierta no contiene
# ninguna palabra de alerta, pero tampoco toca el tema que se le pregunta
# (ver "palabras_esperadas" en los ítems y _evaluar_item_abierto en
# app.py) — por ejemplo, responder "hacer incendios" a una pregunta sobre
# el cuidado de la creación.
FEEDBACK_FUERA_DE_TEMA = ("Escribiste algo, pero no se relaciona con lo que acabamos de leer. "
                           "Vuelve a leer la cita bíblica y responde otra vez con lo que ella dice.")

# ---------------------------------------------------------------------
# Filtro de respuestas abiertas ("abierta": True, usado en "Práctica con
# la Biblia" y en algunos ítems de "Recuperación"): por defecto el motor
# solo exige que el niño escriba *algo* para dar por lograda esa parte de
# la actividad (ver _evaluar_item_abierto en app.py). Dos mecanismos
# ajustan eso:
#
#   1. PALABRAS_ALERTA (abajo): si la respuesta contiene alguna de estas
#      palabras, NO cuenta como lograda, sin importar el resto del texto
#      (ejemplo: responder "odiar" a "¿qué nos manda Jesús?").
#
#   2. "palabras_esperadas" (opcional, en el propio ítem del contenido):
#      cuando la pregunta tiene una dirección correcta clara según la
#      cita bíblica o la situación planteada, el ítem declara una lista
#      de palabras esperadas y la respuesta debe contener al menos una
#      (ejemplo: "hacer incendios" no contiene ninguna palabra de
#      PC01-C06-A03 como CUIDAR/RESPETAR/PROTEGER/LIMPIAR/CREACION, así
#      que no cuenta como lograda aunque no use ninguna palabra de
#      alerta). Las preguntas genuinamente personales (p. ej. "¿cuándo
#      has sentido que Jesús es tu amigo?") se dejan sin esta lista a
#      propósito, para no rechazar respuestas honestas y variadas.
#
# Ambos son filtros simples por palabra (no un modelo de lenguaje): no
# captan paráfrasis, y pueden tener falsos positivos o negativos
# ocasionales. Ampliar o afinar cualquiera de los dos no requiere tocar
# la lógica de app.py, solo esta lista o el campo "palabras_esperadas"
# del ítem correspondiente.
PALABRAS_ALERTA = {
    "ODIAR", "ODIO", "MATAR", "MATARIA", "PEGAR", "GOLPEAR", "GOLPE",
    "INSULTAR", "INSULTO", "MENTIR", "MENTIRA", "ROBAR", "ROBO",
    "HERIR", "LASTIMAR", "MALTRATAR", "MALTRATO", "BURLARSE", "BURLAR",
    "HUMILLAR", "DESPRECIAR", "DESTRUIR", "PELEAR", "PELEA", "VENGAR",
    "VENGANZA", "ABANDONAR", "TRAICIONAR", "TRAICION",
}

ACTIVIDADES = {}


def _agregar(contenido_id, sufijo, actividad):
    actividad = dict(actividad)
    actividad["contenido_id"] = contenido_id
    actividad.setdefault("feedback_ok", FEEDBACK_OK)
    actividad.setdefault("feedback_falta", FEEDBACK_FALTA)
    actividad.setdefault("pistas", [])
    ACTIVIDADES[f"{contenido_id}-{sufijo}"] = actividad


# ==========================================================================
# PC01-C01 — Dios es Creador   (Génesis 1,26-31)
# ==========================================================================
C = "PC01-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Dios es Creador",
    "items": [
        {"texto": "Quien existe desde siempre y nos ama.", "respuesta": "DIOS"},
        {"texto": "El que hace que algo exista.", "respuesta": "CREADOR"},
        {"texto": "Todo lo que Dios hizo: el cielo, la tierra, los animales, las personas.",
         "respuesta": "CREACION"},
        {"texto": "Lo que sentimos cuando queremos el bien de alguien.", "respuesta": "AMOR"},
        {"texto": "El regalo de existir y de vivir.", "respuesta": "VIDA"},
        {"texto": "El lugar donde vivimos, parte de la creación de Dios.", "respuesta": "MUNDO"},
    ],
    "incluir": ["DIOS", "CREADOR"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Recuerda Génesis 1,26-31: todo lo que existe viene de Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Dios es Creador",
    "palabras": ["DIOS", "CREADOR", "CREACION", "AMOR", "VIDA", "MUNDO"],
    "incluir": ["DIOS", "CREADOR"], "requisito": 5,
    "pistas": ["Busca palabras en horizontal y en vertical.",
               "DIOS y CREADOR son de las palabras más cortas: empieza por esas."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Génesis 1,26-31",
    "items": [
        {"texto": "Busca en tu Biblia Católica Génesis 1,26-31 y completa: «Y creó Dios al ser humano "
                  "a su ______.»", "respuesta": "IMAGEN", "banco": ["IMAGEN", "TAMAÑO", "GUSTO"]},
        {"texto": "¿Qué significa para ti que Dios te haya creado a su imagen?", "abierta": True, "palabras_esperadas": ["PARECIDO", "SEMEJANTE", "IMAGEN", "AMADO", "VALIOSO", "ESPECIAL", "DIGNIDAD", "HIJO", "DIOS"], "respuestas_referencia": ["Que me parezco a Dios y por eso soy valioso.", "Que Dios me hizo a su semejanza, con dignidad de hijo suyo.", "Que llevo algo de Dios en mí, por eso soy especial."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de Génesis en el índice de tu Biblia; el capítulo es el 1.",
               "Lee los versículos 26 al 31 completos: la palabra que falta aparece tal como está en el texto."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dios es nuestro ______.", "respuesta": "CREADOR",
         "banco": ["CREADOR", "AMIGO", "MAESTRO"]},
        {"texto": "Dios creó el ______ y todo lo que existe.", "respuesta": "MUNDO",
         "banco": ["CIELO", "MUNDO", "AGUA"]},
        {"texto": "Dios nos creó por ______.", "respuesta": "AMOR",
         "banco": ["AMOR", "OBLIGACIÓN", "CASUALIDAD"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la palabra que mejor completa la idea de Génesis 1,26-31.",
               "La primera respuesta empieza con «C»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Dios es nuestro Creador.", "respuesta": True},
        {"texto": "La creación no tiene relación con Dios.", "respuesta": False},
        {"texto": "Dios creó el mundo y todo lo que existe.", "respuesta": True},
        {"texto": "Este encuentro nos invita a reconocer a Dios como Creador.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Génesis 1,26-31: todo lo que existe viene de Dios.",
               "Si una frase dice que la creación NO tiene que ver con Dios, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Quién es el Creador?",
         "opciones": ["El sol", "Dios", "Los ángeles", "Nadie"], "correcta": 1},
        {"texto": "¿Qué significa reconocer a Dios como Creador?",
         "opciones": ["Que Dios hizo solo el cielo",
                      "Que Dios creó el mundo y todo lo que existe",
                      "Que el mundo se creó solo",
                      "Que Dios ya no cuida el mundo"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Elimina primero la opción que claramente no tiene sentido.",
               "Recuerda el relato de Génesis: Dios hizo el mundo y todo lo que existe."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DIOS", "definicion": "Quien crea"},
        {"termino": "CREACIÓN", "definicion": "Obra de Dios"},
        {"termino": "AMOR", "definicion": "Razón por la que Dios creó"},
        {"termino": "MUNDO", "definicion": "Parte de lo creado"},
        {"termino": "VIDA", "definicion": "Don de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "DIOS se relaciona con la acción de crear."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "completar", "titulo": "Reto: ¿Cuánto recuerdas?",
    "items": [
        {"texto": "El regalo de existir y vivir se llama ______.", "respuesta": "VIDA",
         "banco": ["VIDA", "JUEGO", "ESCUELA"]},
        {"texto": "Todo lo que Dios hizo —el cielo, la tierra, los animales, las personas— es su ______.",
         "respuesta": "CREACION", "banco": ["CREACION", "CASUALIDAD", "NADA"]},
        {"texto": "Reconocer que Dios hizo todo es reconocerlo como nuestro ______.", "respuesta": "CREADOR",
         "banco": ["CREADOR", "AMIGO", "MAESTRO"]},
    ],
    "requisito": 2,
    "pistas": ["Repasa las actividades anteriores de este tema antes de responder.",
               "Las tres respuestas ya aparecieron en el crucigrama y en la sopa de letras."],
})
_agregar(C, "A09", {
    "tipo": "sopa_letras", "titulo": "Recuperación: repasa los 6 temas",
    "palabras": ["CREADOR", "AMOR", "IMAGEN", "UNICO", "CUIDAR", "JUNTOS"],
    "incluir": ["CREADOR", "CUIDAR"], "requisito": 5,
    "reflexion": "¿Cuál de los 6 temas de este encuentro te costó más recordar? Coméntaselo a tu catequista.",
    "pistas": ["Cada palabra representa uno de los 6 temas de este encuentro: Creador, Amor, Imagen, Único, "
               "Cuidar y Juntos.",
               "Busca primero las palabras más cortas: AMOR. Recuerda que ÚNICO va sin tilde en la sopa: UNICO."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: cuido lo que Dios creó",
    "situacion": "Ya sabes que Dios es el Creador de todo lo que existe: el cielo, la tierra, los animales, "
                 "las personas.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para cuidar lo que Dios creó?",
         "opciones": ["Recoger basura de un parque o espacio público",
                      "Ayudar a limpiar tu casa",
                      "Tratar bien a tus mascotas",
                      "Quedarme sin hacer nada"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no ayuda a cuidar la creación de Dios."],
    "feedback_ok": "¡Muy bien! Cuidar lo que Dios creó también es una forma de agradecerle.",
})

# ==========================================================================
# PC01-C02 — Dios nos creó por amor
# ==========================================================================
C = "PC01-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama del amor de Dios",
    "items": [
        {"texto": "Quien nos creó por amor.", "respuesta": "DIOS", "banco": ["DIOS", "VIDA", "PERSONA"]},
        {"texto": "La razón por la que Dios nos hizo.", "respuesta": "AMOR", "banco": ["AMOR", "CASUALIDAD", "OBLIGACIÓN"]},
        {"texto": "El don que Dios nos regaló al existir.", "respuesta": "VIDA", "banco": ["VIDA", "JUEGO", "TAREA"]},
        {"texto": "Un regalo que no se compra, se recibe.", "respuesta": "DON", "banco": ["DON", "PRÉSTAMO", "PREMIO"]},
        {"texto": "Lo que Dios hizo con nosotros: darnos existencia.", "respuesta": "CREO", "banco": ["CREO", "OLVIDO", "IGNORO"]},
        {"texto": "Cada ser humano, querido por Dios.", "respuesta": "PERSONA", "banco": ["PERSONA", "OBJETO", "COSA"]},
    ],
    "incluir": ["DIOS", "AMOR"], "requisito": 4,
    "pistas": ["Piensa en la primera letra de cada palabra.", "Recuerda: todo lo que Dios hace nace de su amor."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Dios nos creó por amor",
    "palabras": ["DIOS", "AMOR", "VIDA", "DON", "CREO", "PERSONA"],
    "incluir": ["DIOS", "AMOR"], "requisito": 5,
    "pistas": ["DON es una de las palabras más cortas: búscala primero.",
               "PERSONA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Génesis 1,1-5",
    "items": [
        {"texto": "Busca en tu Biblia Católica Génesis 1,1-5 y completa: «En el ______ creó Dios los "
                  "cielos y la tierra.»", "respuesta": "PRINCIPIO", "banco": ["PRINCIPIO", "FINAL", "MEDIO"]},
        {"texto": "¿Por qué crees que Dios quiso crear el mundo y crearte a ti?", "abierta": True, "palabras_esperadas": ["AMOR", "AMA", "QUISO", "BUENO", "FELIZ", "VIDA", "REGALO", "CREO", "CREAR", "MUNDO"], "respuestas_referencia": ["Porque Dios nos ama y quiso regalarnos la vida.", "Porque a Dios le pareció bueno crear el mundo por amor.", "Dios me creó porque me ama y quiere que sea feliz."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de Génesis en el índice de tu Biblia; el capítulo es el 1, los primeros versículos.",
               "Es la primera frase de toda la Biblia: cuenta cómo empezó todo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dios nos creó por ______.", "respuesta": "AMOR", "banco": ["AMOR", "OBLIGACIÓN", "CASUALIDAD"]},
        {"texto": "Nuestra ______ es un don.", "respuesta": "VIDA", "banco": ["VIDA", "PROBLEMA", "ACCIDENTE"]},
        {"texto": "Dios nos creó porque nos ______.", "respuesta": "AMA", "banco": ["AMA", "IGNORA", "OLVIDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que sentimos cuando alguien nos regala algo.",
               "La primera respuesta empieza con «A»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Dios nos creó por amor.", "respuesta": True},
        {"texto": "Nuestra vida no tiene valor.", "respuesta": False},
        {"texto": "La vida es un don.", "respuesta": True},
        {"texto": "Dios nos crea por indiferencia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: todo lo que Dios hace nace de su amor.",
               "Si una frase dice que a Dios no le importamos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué significa decir que Dios nos creó por amor?",
         "opciones": ["Que nuestra vida no tiene valor",
                      "Que nuestra vida es un don y somos amados por Dios",
                      "Que solo algunas personas le importan a Dios"], "correcta": 1},
    ],
    "requisito": 1,
    "pistas": ["Piensa en la razón que motivó a Dios a crearnos.",
               "La mejor respuesta habla de un don y de sentirnos amados."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DIOS", "definicion": "Nos creó"},
        {"termino": "AMOR", "definicion": "Motivo por el que Dios nos hizo"},
        {"termino": "VIDA", "definicion": "Un don"},
        {"termino": "PERSONA", "definicion": "Ser amado por Dios"},
        {"termino": "DON", "definicion": "Regalo que recibimos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe recibir un regalo.", "AMOR es la razón detrás de todo lo demás."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["DIOS", "AMOR", "VIDA", "DON", "RESPETO", "CUIDAR"],
    "correctas": ["DIOS", "AMOR", "VIDA", "DON"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Dios - Amor - Vida - Don.", "Descarta las palabras que no aparecieron en este tema."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Dios nos creó por ______.", "respuesta": "AMOR", "banco": ["AMOR", "CASUALIDAD", "OBLIGACIÓN"]},
    ],
    "reflexion": "¿Qué significa para ti que la vida sea un don de Dios?",
    "requisito": 1,
    "pistas": ["Piensa en la razón por la que Dios te creó.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: comparto ese amor",
    "situacion": "Ya sabes que Dios te creó por amor, sin que tuvieras que ganártelo.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para mostrar ese mismo amor a los demás?",
         "opciones": ["Dar las gracias a Dios en una oración por tu vida",
                      "Ayudar a un familiar sin que te lo pidan",
                      "Compartir algo tuyo con un amigo",
                      "Ignorar a alguien que necesita ayuda"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra amor a los demás."],
    "feedback_ok": "¡Muy bien! El amor que recibimos de Dios se nota cuando lo compartimos.",
})

# ==========================================================================
# PC01-C03 — Somos creados a imagen de Dios
# ==========================================================================
C = "PC01-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama de la dignidad",
    "items": [
        {"texto": "Quien nos hizo parecidos a Él por dentro.", "respuesta": "DIOS", "banco": ["DIOS", "PERSONA", "AMOR"]},
        {"texto": "El parecido que tenemos con Dios.", "respuesta": "IMAGEN", "banco": ["IMAGEN", "SOMBRA", "COPIA"]},
        {"texto": "El valor que tiene cada persona, siempre.", "respuesta": "DIGNIDAD", "banco": ["DIGNIDAD", "SUERTE", "FAMA"]},
        {"texto": "Cada ser humano, creado a imagen de Dios.", "respuesta": "PERSONA", "banco": ["PERSONA", "OBJETO", "COSA"]},
        {"texto": "La forma correcta de tratar a los demás.", "respuesta": "RESPETO", "banco": ["RESPETO", "MIEDO", "DUDA"]},
        {"texto": "Lo que Dios siente por cada persona.", "respuesta": "AMOR", "banco": ["AMOR", "INDIFERENCIA", "ENOJO"]},
    ],
    "incluir": ["IMAGEN", "DIGNIDAD"], "requisito": 4,
    "pistas": ["Piensa en la primera letra de cada palabra.", "Todas se relacionan con el valor de cada persona."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Somos imagen de Dios",
    "palabras": ["DIOS", "IMAGEN", "DIGNIDAD", "PERSONA", "RESPETO", "AMOR"],
    "incluir": ["IMAGEN", "DIGNIDAD"], "requisito": 5,
    "pistas": ["DIOS y AMOR son las palabras más cortas: búscalas primero.",
               "DIGNIDAD es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Salmo 8,4-6",
    "items": [
        {"texto": "Busca en tu Biblia Católica el Salmo 8,4-6 y completa: «Lo coronaste de ______ y de "
                  "honra.»", "respuesta": "GLORIA", "banco": ["GLORIA", "ORO", "FLORES"]},
        {"texto": "¿Qué dice este salmo sobre el valor que Dios da a cada persona?", "abierta": True, "palabras_esperadas": ["VALIOSO", "VALOR", "IMPORTANTE", "GLORIA", "HONRA", "GRANDE", "CORONA"], "respuestas_referencia": ["Dice que Dios nos hizo poco menos que a los ángeles y nos coronó de gloria.", "Que cada persona es muy importante y valiosa para Dios.", "Que Dios nos dio honra y grandeza."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Salmos en el índice de tu Biblia; es el salmo número 8.",
               "Es una pregunta que el salmo le hace a Dios: «¿qué es el hombre, para que tengas de él memoria?»."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Somos creados a ______ de Dios.", "respuesta": "IMAGEN", "banco": ["IMAGEN", "ENEMIGO", "DUEÑO"]},
        {"texto": "Toda persona tiene ______.", "respuesta": "DIGNIDAD", "banco": ["DIGNIDAD", "SUERTE", "DINERO"]},
        {"texto": "Debemos tratar a los demás con ______.", "respuesta": "RESPETO", "banco": ["RESPETO", "MIEDO", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la palabra que describe «ser parecido a Dios».", "La última respuesta empieza con «R»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Toda persona tiene dignidad.", "respuesta": True},
        {"texto": "Solo algunas personas merecen respeto.", "respuesta": False},
        {"texto": "Somos imagen de Dios.", "respuesta": True},
        {"texto": "Podemos despreciar a quien es diferente.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Piensa: ¿a cuántas personas creó Dios a su imagen?",
               "Si una frase dice «solo algunos», probablemente es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué enseña que fuimos creados a imagen de Dios?",
         "opciones": ["Que algunas personas valen más que otras",
                      "Que cada persona tiene dignidad, sin importar cómo sea",
                      "Que debemos parecernos físicamente a Dios"], "correcta": 1},
    ],
    "requisito": 1,
    "pistas": ["Ser imagen de Dios no es sobre el parecido físico.",
               "Piensa en lo que vale cada persona, sin excepción."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DIOS", "definicion": "Creador"},
        {"termino": "IMAGEN", "definicion": "Relación con Dios"},
        {"termino": "DIGNIDAD", "definicion": "Valor de la persona"},
        {"termino": "RESPETO", "definicion": "Trato adecuado"},
        {"termino": "PERSONA", "definicion": "Creación de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe el valor que tiene cada persona.",
               "RESPETO tiene que ver con cómo tratamos a los demás."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: Todos tenemos valor",
    "instruccion": "Piensa en cada situación y elige la actitud correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Llega un niño nuevo al salón de catequesis.",
         "opciones": ["Ignorarlo", "Tratarlo con respeto", "Burlarse de él"], "correcta": 1},
        {"texto": "Un compañero tiene dificultad para aprender.",
         "opciones": ["Burlarse de él", "Ayudarlo con paciencia y respeto", "Dejarlo solo"], "correcta": 1},
        {"texto": "Un anciano necesita ayuda para caminar.",
         "opciones": ["Ayudarlo con respeto", "Ignorarlo", "Reírse"], "correcta": 0},
        {"texto": "Una persona se ve o vive distinto a ti.",
         "opciones": ["Tratarla con el mismo respeto", "Alejarte de ella", "Burlarte"], "correcta": 0},
    ],
    "requisito": 3,
    "pistas": ["La palabra clave que se repite en las cuatro situaciones es RESPETO.",
               "Descarta primero la opción que claramente no muestra respeto."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Si una persona es creada a imagen de Dios, ¿cómo debemos tratarla?",
         "respuesta": "RESPETO", "banco": ["RESPETO", "INDIFERENCIA", "BURLA"]},
    ],
    "reflexion": "Explica con tus palabras por qué toda persona merece respeto.",
    "requisito": 1,
    "pistas": ["Piensa en la palabra clave de este tema.", "Repasa la actividad de completar."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: trato a todos con dignidad",
    "situacion": "Ya sabes que cada persona es creada a imagen de Dios, sin importar cómo sea o de dónde venga.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para reconocer la dignidad de los demás?",
         "opciones": ["Tratar con respeto a un compañero distinto a ti",
                      "Defender a alguien de una burla",
                      "Saludar con cariño a quien casi no ves",
                      "Burlarte de alguien porque es diferente"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra respeto por la otra persona."],
    "feedback_ok": "¡Muy bien! Así se nota que reconoces a Dios en cada persona.",
})

# ==========================================================================
# PC01-C04 — Soy único y valioso para Dios
# ==========================================================================
C = "PC01-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama",
    "items": [
        {"texto": "Lo que Dios te regaló al crearte.", "respuesta": "VIDA", "banco": ["VIDA", "JUEGO", "TAREA"]},
        {"texto": "Quien te hizo único y te ama.", "respuesta": "DIOS", "banco": ["DIOS", "AMIGO", "MAESTRO"]},
        {"texto": "Que no hay otra persona exactamente igual a ti.", "respuesta": "UNICO", "banco": ["UNICO", "IGUAL", "COMÚN"]},
        {"texto": "Que tienes un gran valor para Dios.", "respuesta": "VALIOSO", "banco": ["VALIOSO", "INVISIBLE", "COMÚN"]},
        {"texto": "Lo que Dios siente por ti, tal como eres.", "respuesta": "AMOR", "banco": ["AMOR", "DUDA", "MIEDO"]},
        {"texto": "Un regalo especial que Dios te dio.", "respuesta": "DON", "banco": ["DON", "ERROR", "ACCIDENTE"]},
    ],
    "incluir": ["UNICO", "VALIOSO"], "requisito": 4,
    "pistas": ["Piensa en la primera letra de cada palabra.", "Todas hablan de tu valor para Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Soy único y valioso",
    "palabras": ["VIDA", "DIOS", "UNICO", "VALIOSO", "AMOR", "DON"],
    "requisito": 5,
    "pistas": ["DON y DIOS son de las palabras más cortas: búscalas primero.",
               "VALIOSO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Salmo 139,13-14",
    "items": [
        {"texto": "Busca en tu Biblia Católica el Salmo 139,13-14 y completa: «Te alabaré porque "
                  "formidables, ______ son tus obras.»", "respuesta": "MARAVILLOSAS",
         "banco": ["MARAVILLOSAS", "PEQUEÑAS", "COMUNES"]},
        {"texto": "¿Cómo dice el salmo que Dios te formó?", "abierta": True, "palabras_esperadas": ["MARAVILLOSO", "MARAVILLA", "CUIDADO", "UNICO", "PERFECTO", "AMOR", "FORMIDABLE"], "respuestas_referencia": ["Dice que Dios me formó de manera maravillosa en el vientre de mi madre.", "Que fui hecho de forma admirable y única por Dios.", "Que Dios me tejió con cuidado y amor antes de nacer."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Salmos en el índice de tu Biblia; es el salmo número 139.",
               "Habla de cómo Dios nos formó incluso antes de nacer, en el vientre de nuestra madre."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dios me creó ______.", "respuesta": "UNICO", "banco": ["UNICO", "IGUAL", "COMÚN"]},
        {"texto": "Mi vida es un ______.", "respuesta": "DON", "banco": ["DON", "ERROR", "ACCIDENTE"]},
        {"texto": "Soy ______ para Dios.", "respuesta": "VALIOSO", "banco": ["VALIOSO", "INVISIBLE", "IGUAL"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la palabra que dice que no hay nadie más como tú.", "La primera respuesta empieza con «U»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Mi vida tiene valor.", "respuesta": True},
        {"texto": "Dios solo ama a los perfectos.", "respuesta": False},
        {"texto": "Cada persona es única.", "respuesta": True},
        {"texto": "No tengo nada bueno que ofrecer.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Piensa: ¿el amor de Dios depende de ser perfecto?",
               "El valor que Dios te da no depende de lo que otros piensen."],
    "feedback_ok": "¡Excelente! Sigue creciendo en tu fe.",
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué significa ser único y valioso para Dios?",
         "opciones": ["Que soy mejor que los demás", "Que mi vida tiene valor y es un don de Dios",
                      "Que no necesito a nadie"], "correcta": 1},
    ],
    "requisito": 1,
    "pistas": ["Tu valor no depende de ser mejor que otros.", "Piensa en un regalo que solo tú recibiste."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ÚNICO", "definicion": "No hay otra persona igual a mí"},
        {"termino": "VALIOSO", "definicion": "Tengo valor para Dios"},
        {"termino": "VIDA", "definicion": "Un don"},
        {"termino": "DIOS", "definicion": "Me ama tal como soy"},
        {"termino": "PERSONA", "definicion": "Creación de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra habla de recibir un regalo.", "DIOS tiene que ver con cómo te quiere."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubro mis dones",
    "instruccion": "En 45 segundos, elige tres cualidades o dones que tengas.",
    "tiempo_segundos": 45,
    "banco": ["Ayudar", "Escuchar", "Dibujar", "Estudiar", "Compartir", "Cantar", "Cuidar"],
    "correctas": None, "minimo": 3, "requisito": 3,
    "pistas": ["No existe una respuesta única: elige lo que sea verdad para ti.",
               "Piensa en algo que sabes hacer bien o que te gusta hacer por otros."],
    "feedback_ok": "¡Muy bien! Cada uno de esos dones también viene de Dios.",
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Completa: Soy valioso para Dios porque…", "abierta": True, "palabras_esperadas": ["DIOS", "AMA", "CREO", "HIJO", "IMAGEN", "AMOR"], "respuestas_referencia": ["Soy valioso porque Dios me creó a su imagen y me ama.", "Porque soy hijo de Dios y él me ama tal como soy.", "Porque Dios me hizo con amor y soy importante para él."]},
    ],
    "requisito": 1,
    "pistas": ["No hay una única respuesta correcta: escribe lo que sientas.",
               "Piensa en algo que aprendiste hoy sobre ti mismo."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: valoro lo que Dios me dio",
    "situacion": "Ya sabes que eres único y valioso para Dios, tal como eres.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para valorar lo que Dios te regaló?",
         "opciones": ["Agradecer a Dios por cómo te hizo",
                      "Usar uno de tus dones para ayudar a alguien",
                      "Cuidar tu cuerpo y tu salud",
                      "Compararte todo el tiempo con los demás"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no ayuda a valorarte a ti mismo."],
    "feedback_ok": "¡Muy bien! Valorarte a ti mismo también es una forma de agradecerle a Dios.",
})

# ==========================================================================
# PC01-C05 — Dios nos confió el cuidado de su creación
# ==========================================================================
C = "PC01-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama",
    "items": [
        {"texto": "Quien creó todo y nos pidió cuidarlo.", "respuesta": "DIOS", "banco": ["DIOS", "VIDA", "AGUA"]},
        {"texto": "Todo lo que Dios hizo: el mundo, los animales, las plantas.",
         "respuesta": "CREACION", "banco": ["CREACION", "CASUALIDAD", "NADA"]},
        {"texto": "Proteger y tratar bien lo que Dios nos confió.", "respuesta": "CUIDAR",
         "banco": ["CUIDAR", "IGNORAR", "DESTRUIR"]},
        {"texto": "Los árboles, animales, ríos y montañas que Dios creó.", "respuesta": "NATURALEZA",
         "banco": ["NATURALEZA", "CIUDAD", "TECNOLOGÍA"]},
        {"texto": "Lo que hay que proteger en todo ser vivo.", "respuesta": "VIDA", "banco": ["VIDA", "JUEGO", "TAREA"]},
        {"texto": "La tarea que Dios nos confió de cuidar su creación.", "respuesta": "RESPONSABILIDAD",
         "banco": ["RESPONSABILIDAD", "CASUALIDAD", "DISTRACCIÓN"]},
    ],
    "incluir": ["CREACION", "CUIDAR"], "requisito": 4,
    "pistas": ["Piensa en la primera letra de cada palabra.", "Todas hablan de cuidar lo que Dios hizo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Cuidamos la creación",
    "palabras": ["DIOS", "CREACION", "CUIDAR", "NATURALEZA", "VIDA", "AGUA"],
    "requisito": 5,
    "pistas": ["DIOS y AGUA son de las palabras más cortas: búscalas primero.",
               "NATURALEZA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Génesis 2,15",
    "items": [
        {"texto": "Busca en tu Biblia Católica Génesis 2,15 y completa: «Tomó Dios al hombre y lo puso "
                  "en el jardín para que lo labrara y lo ______.»", "respuesta": "CUIDARA",
         "banco": ["CUIDARA", "VENDIERA", "DESTRUYERA"]},
        {"texto": "¿Qué tarea le dio Dios al ser humano en el jardín?", "abierta": True, "palabras_esperadas": ["CUIDAR", "TRABAJAR", "LABRAR", "PROTEGER", "JARDIN"], "respuestas_referencia": ["Le dio la tarea de cuidar y cultivar el jardín.", "Dios le pidió que trabajara y protegiera el jardín del Edén.", "Cuidar la creación y labrar la tierra."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de Génesis en el índice de tu Biblia; el capítulo es el 2.",
               "Dios pone al primer ser humano en un jardín y le confía una tarea."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dios creó la ______.", "respuesta": "CREACION", "banco": ["CREACION", "CASUALIDAD", "NADA"]},
        {"texto": "Debemos ______ lo creado.", "respuesta": "CUIDAR", "banco": ["CUIDAR", "IGNORAR", "DESTRUIR"]},
        {"texto": "El agua es importante para la ______.", "respuesta": "VIDA",
         "banco": ["VIDA", "DECORACIÓN", "NADA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Dios nos pidió hacer con el mundo.", "La segunda respuesta empieza con «C»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Debemos cuidar la creación.", "respuesta": True},
        {"texto": "Podemos desperdiciar el agua sin problema.", "respuesta": False},
        {"texto": "Los animales forman parte de la creación.", "respuesta": True},
        {"texto": "Cuidar la creación no tiene relación con la fe.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: Dios nos pidió cuidar lo que Él creó.",
               "Si una frase dice que está bien desperdiciar recursos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué acción demuestra que cuidamos la creación?",
         "opciones": ["Tirar basura al río", "Maltratar a los animales",
                      "Cuidar las plantas y no desperdiciar el agua"], "correcta": 2},
    ],
    "requisito": 1,
    "pistas": ["Piensa en la responsabilidad que Dios nos dio en Génesis.", "Cuidar es una acción, no solo una idea."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CREACIÓN", "definicion": "Obra de Dios"},
        {"termino": "AGUA", "definicion": "Debemos cuidarla"},
        {"termino": "ANIMALES", "definicion": "Seres vivos que Dios creó"},
        {"termino": "PLANTAS", "definicion": "Parte de la creación"},
        {"termino": "CUIDAR", "definicion": "Responsabilidad que Dios nos dio"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe nuestro hogar común.", "CUIDAR tiene que ver con una tarea, no solo una idea."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: ¿Qué harías?",
    "instruccion": "Piensa en cada situación y elige la acción correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Ves una llave de agua abierta sin que nadie la use.",
         "opciones": ["Cerrarla", "Dejarla así", "Abrirla más"], "correcta": 0},
        {"texto": "Ves basura tirada en el suelo.",
         "opciones": ["Pisarla y seguir caminando", "Recogerla y botarla en su lugar", "Patearla"], "correcta": 1},
        {"texto": "Ves una planta que nadie riega.",
         "opciones": ["Regarla o avisar a alguien", "Arrancarla", "No hacer nada"], "correcta": 0},
        {"texto": "Encuentras un animal abandonado.",
         "opciones": ["Ignorarlo", "Buscar ayuda para cuidarlo", "Asustarlo"], "correcta": 1},
    ],
    "requisito": 3,
    "pistas": ["Piensa en la responsabilidad que Dios nos dio de cuidar su creación.",
               "Descarta primero la opción que claramente hace daño."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "En tu casa se desperdicia agua y se dejan luces encendidas sin necesidad. ¿Qué podrías hacer?",
         "abierta": True, "palabras_esperadas": ["CERRAR", "APAGAR", "CUIDAR", "AHORRAR"], "respuestas_referencia": ["Cerraría la llave mientras no se usa para no desperdiciar agua.", "Avisaría a mi familia para cuidar y ahorrar el agua.", "Trataría de cerrar bien las llaves y usar el agua con cuidado."]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en pequeñas acciones que sí están en tus manos.",
               "Repasa lo que trabajaste en la actividad de verdadero o falso."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: cuido los recursos que Dios me confió",
    "situacion": "Ya sabes que Dios nos confió el cuidado de su creación: el agua, las plantas, los animales.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para cuidar esos recursos?",
         "opciones": ["Cerrar bien la llave del agua cuando no la uses",
                      "Cuidar una planta o una mascota",
                      "Separar la basura para reciclar",
                      "Dejar las luces encendidas sin necesidad"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que desperdicia un recurso en vez de cuidarlo."],
    "feedback_ok": "¡Muy bien! Esa es la responsabilidad que Dios te confió.",
})

# ==========================================================================
# PC01-C06 — Cuidamos juntos la creación
# ==========================================================================
C = "PC01-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama misionero",
    "items": [
        {"texto": "Hacer algo en compañía de otros, no solos.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "NUNCA"]},
        {"texto": "Proteger y tratar bien lo que Dios nos confió.", "respuesta": "CUIDAR",
         "banco": ["CUIDAR", "IGNORAR", "OLVIDAR"]},
        {"texto": "Todo lo que Dios hizo y nos pidió cuidar.", "respuesta": "CREACION",
         "banco": ["CREACION", "CASUALIDAD", "NADA"]},
        {"texto": "Un grupo de personas que trabajan por lo mismo.", "respuesta": "EQUIPO",
         "banco": ["EQUIPO", "COMPETENCIA", "DESORDEN"]},
        {"texto": "Lo que motiva a cuidar la creación y a los demás.", "respuesta": "AMOR",
         "banco": ["AMOR", "PEREZA", "INDIFERENCIA"]},
        {"texto": "Una tarea importante que se hace con compromiso.", "respuesta": "MISION",
         "banco": ["MISION", "CASUALIDAD", "JUEGO"]},
    ],
    "incluir": ["JUNTOS", "CUIDAR"], "requisito": 4,
    "pistas": ["Piensa en la primera letra de cada palabra.", "Todas hablan de cuidar en comunidad."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Cuidamos juntos la creación",
    "palabras": ["JUNTOS", "CUIDAR", "CREACION", "EQUIPO", "AMOR", "MISION"],
    "requisito": 5,
    "pistas": ["JUNTOS y CUIDAR son de las palabras más cortas: búscalas primero.",
               "CREACIÓN es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Salmo 24,1-2",
    "items": [
        {"texto": "Busca en tu Biblia Católica el Salmo 24,1-2 y completa: «Del Señor es la ______ y su "
                  "plenitud.»", "respuesta": "TIERRA", "banco": ["TIERRA", "LUNA", "CASA"]},
        {"texto": "¿Qué significa que la tierra sea del Señor, para el cuidado que le debemos?", "abierta": True, "palabras_esperadas": ["CUIDAR", "RESPETAR", "PROTEGER", "LIMPIAR", "CREACION"], "respuestas_referencia": ["Significa que debemos cuidar y respetar la creación porque es de Dios.", "Que la tierra no es solo nuestra, es un regalo de Dios que hay que proteger.", "Debemos cuidarla y no contaminarla porque le pertenece a Dios."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Salmos en el índice de tu Biblia; es el salmo número 24.",
               "El salmo empieza diciendo a quién pertenece la tierra y todo lo que hay en ella."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Podemos cuidar la creación ______.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "NUNCA"]},
        {"texto": "Cuidar la creación requiere ______.", "respuesta": "COMPROMISO",
         "banco": ["COMPROMISO", "OLVIDO", "DESINTERÉS"]},
        {"texto": "Podemos dar ejemplo de ______.", "respuesta": "AMOR", "banco": ["AMOR", "INDIFERENCIA", "PEREZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la palabra que dice que no lo hacemos solos.", "La segunda respuesta empieza con «C»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Cuidar la creación puede ser una tarea comunitaria.", "respuesta": True},
        {"texto": "Cada uno debe cuidar solo lo suyo, sin ayudar a los demás.", "respuesta": False},
        {"texto": "Podemos organizarnos para cuidar juntos.", "respuesta": True},
        {"texto": "El compromiso cristiano también se expresa en acciones concretas.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Piensa: ¿se cuida mejor el mundo solo o entre todos?",
               "Si una frase dice que no hay que ayudar a los demás, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué representa mejor la frase «cuidamos juntos»?",
         "opciones": ["Ignorar el problema y esperar", "Un grupo que se organiza para cuidar un espacio",
                      "Esperar a que otro lo resuelva"], "correcta": 1},
    ],
    "requisito": 1,
    "pistas": ["Cuidar la creación es tarea de todos, no de uno solo.", "Piensa en equipo, no en una sola persona."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "JUNTOS", "definicion": "Lo hacemos en comunidad"},
        {"termino": "CUIDAR", "definicion": "Responsabilidad que compartimos"},
        {"termino": "CREACIÓN", "definicion": "Don de Dios"},
        {"termino": "EQUIPO", "definicion": "Trabajo compartido"},
        {"termino": "MISIÓN", "definicion": "Compromiso que asumimos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe una decisión que se mantiene en el tiempo.",
               "EQUIPO tiene que ver con trabajar acompañado."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Misión en equipo",
    "instruccion": "En 60 segundos, elige una acción que podrían hacer en equipo y luego explica cómo la realizarían.",
    "tiempo_segundos": 60,
    "banco": ["Limpiar un espacio", "Cuidar una planta", "Recoger basura", "Ahorrar agua", "Proteger animales"],
    "correctas": None, "minimo": 1, "requisito": 1,
    "reflexion": "Explica cómo la realizarían entre todos.",
    "pistas": ["Cualquier acción de la lista es una buena propuesta.",
               "Piensa en algo que de verdad podrían organizar como grupo."],
    "feedback_ok": "¡Muy buena propuesta! Eso también es ser misionero.",
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Hay un espacio comunitario lleno de basura. ¿Qué podrían hacer como grupo?", "abierta": True, "palabras_esperadas": ["LIMPIAR", "RECOGER", "ORDENAR"], "respuestas_referencia": ["Ayudaría a limpiar y recoger la basura del lugar.", "Organizaría con otros para limpiar y ordenar ese espacio.", "Recogería la basura para dejar el lugar limpio."]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción organizada, no en una sola persona.",
               "Repasa lo que conversaron en el reto de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: lo organizamos en equipo",
    "situacion": "Ya sabes que cuidar la creación es una tarea que se hace mejor entre todos, no solos.",
    "items": [
        {"texto": "¿Qué pueden hacer ustedes en equipo esta semana (familia, amigos o el grupo de catequesis)?",
         "opciones": ["Organizar una jornada de limpieza en su barrio o parque",
                      "Cuidar entre varios una planta o una mascota",
                      "Hacer una campaña en casa para ahorrar agua",
                      "Decir que eso no es tarea de ustedes"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta que puedan organizar en grupo.",
               "Descarta la única opción que no muestra compromiso con cuidar la creación."],
    "feedback_ok": "¡Muy bien! Cuidar juntos la creación también es una forma de ser misioneros.",
})

# ==========================================================================
# ==========================================================================
# PC02 — Jesús es nuestro amigo   (Encuentro 2, Marcos 10,13-16)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC02-C01 — Jesús acoge a los niños
# ==========================================================================
C = "PC02-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús acoge",
    "items": [
        {"texto": "Quien recibió a los niños con cariño.", "respuesta": "JESUS"},
        {"texto": "Quienes se acercaron a Jesús.", "respuesta": "NINOS"},
        {"texto": "Recibir a alguien con cariño.", "respuesta": "ACOGER"},
        {"texto": "Lo que Jesús sintió por los niños.", "respuesta": "AMOR"},
        {"texto": "Jesús los cargó entre sus ______ para bendecirlos.", "respuesta": "BRAZOS"},
        {"texto": "Alguien cercano en quien confías.", "respuesta": "AMIGO"},
    ],
    "incluir": ["JESUS", "NINOS"], "requisito": 4,
    "pistas": ["Piensa en el relato de Marcos 10,13-16: Jesús y los niños.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús acoge",
    "palabras": ["JESUS", "NIÑOS", "ACOGER", "AMOR", "BRAZOS", "AMIGO"],
    "incluir": ["JESUS", "NINOS"], "requisito": 5,
    "pistas": ["Busca palabras en horizontal y en vertical.",
               "JESÚS y AMOR son de las palabras más cortas: empieza por esas."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Marcos 10,13-16",
    "items": [
        {"texto": "Busca en tu Biblia Católica Marcos 10,13-16 y completa: «Dejad que los ______ "
                  "vengan a mí.»", "respuesta": "NIÑOS", "banco": ["NIÑOS", "ANCIANOS", "RICOS"]},
        {"texto": "¿Cómo reaccionó Jesús cuando los discípulos querían alejar a los niños?", "abierta": True, "palabras_esperadas": ["DEFENDIO", "ACOGIO", "CORRIGIO", "BENDIJO", "DEJAD", "ENOJO", "INDIGNO", "NINOS"], "respuestas_referencia": ["Jesús se enojó y les dijo que dejaran que los niños se acercaran.", "Jesús defendió a los niños y los bendijo.", "Se indignó con los discípulos y acogió a los niños con cariño."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Marcos en el índice de tu Biblia; el capítulo es el 10.",
               "Los discípulos querían impedir que los niños se acercaran, y Jesús los corrige."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los niños se acercaron a ______.", "respuesta": "JESUS",
         "banco": ["JESUS", "MAESTRO", "SACERDOTE"]},
        {"texto": "Jesús los ______ con cariño.", "respuesta": "ACOGIÓ",
         "banco": ["ACOGIÓ", "RECHAZÓ", "IGNORÓ"]},
        {"texto": "Jesús quiere que todos se sientan ______.", "respuesta": "ACOGIDOS",
         "banco": ["ACOGIDOS", "SOLOS", "APARTADOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hizo Jesús cuando los niños se acercaron.",
               "La segunda respuesta empieza con «A»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los niños podían acercarse a Jesús.", "respuesta": True},
        {"texto": "Jesús los rechazó.", "respuesta": False},
        {"texto": "Jesús los acogió con cariño.", "respuesta": True},
        {"texto": "Acoger significa rechazar a alguien.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Marcos 10,13-16: Jesús recibió a los niños.",
               "Acoger es lo contrario de rechazar."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hizo Jesús cuando los niños se acercaron?",
         "opciones": ["Los rechazó", "Los acogió con cariño", "Se fue sin decir nada"], "correcta": 1},
        {"texto": "¿Por qué al principio los discípulos no querían que los niños se acercaran?",
         "opciones": ["Pensaban que Jesús estaba ocupado con cosas más importantes",
                      "Porque los niños no le importaban a Jesús",
                      "Porque Jesús se lo había pedido"], "correcta": 0},
        {"texto": "¿Qué nos enseña Jesús con este gesto?",
         "opciones": ["Que solo los adultos importan", "Que todos, incluidos los niños, son importantes para Él",
                      "Que hay que alejar a los niños"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que de verdad hizo Jesús, no en lo que pensaban los discípulos.",
               "El mensaje central es que Jesús acoge a todos, también a los más pequeños."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "JESUS", "definicion": "Acoge a los niños"},
        {"termino": "NIÑOS", "definicion": "Se acercan a Jesús"},
        {"termino": "ACOGER", "definicion": "Recibir con cariño"},
        {"termino": "AMOR", "definicion": "Actitud de Jesús hacia los niños"},
        {"termino": "AMIGO", "definicion": "Alguien cercano y de confianza"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe recibir a alguien con cariño.",
               "AMOR es lo que mueve a Jesús a acoger a los niños."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Recuerda la escena",
    "instruccion": "En 45 segundos, marca tres palabras relacionadas con Jesús y los niños.",
    "tiempo_segundos": 45,
    "banco": ["JESUS", "NIÑOS", "ACOGER", "AMOR", "BRAZOS", "AMIGO"],
    "correctas": ["JESUS", "NIÑOS", "ACOGER", "AMOR", "BRAZOS", "AMIGO"], "minimo": 3, "requisito": 3,
    "pistas": ["Cualquiera de las palabras de este tema es una buena respuesta.",
               "Repasa el crucigrama y la sopa de letras de este tema."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Un niño nuevo llega a tu grupo de catequesis. ¿Qué harías para recibirlo como Jesús "
                  "recibió a los niños? Explica por qué.", "abierta": True, "palabras_esperadas": ["ACOGER", "RECIBIR", "PRESENTAR", "AYUDAR", "AMIGO", "SALUDAR", "JUGAR"], "respuestas_referencia": ["Lo acogería, me presentaría y lo invitaría a jugar conmigo.", "Le daría la bienvenida y trataría de ser su amigo.", "Lo saludaría y lo ayudaría a sentirse parte del grupo."]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en cómo Jesús trató a los niños que se acercaron a Él.",
               "No hay una única respuesta correcta: cuenta lo que tú harías."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: recibo como Jesús enseñó",
    "situacion": "Un niño nuevo llega al catecismo y no conoce a nadie.",
    "items": [
        {"texto": "¿Qué puedes hacer para recibirlo como Jesús enseñó?",
         "opciones": ["Invitarlo a sentarse contigo y presentarle a los demás",
                      "Preguntarle su nombre y acompañarlo un rato",
                      "Explicarle las actividades para que no se sienta perdido",
                      "Ignorarlo hasta que se acostumbre solo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra acogida."],
})

# ==========================================================================
# PC02-C02 — Jesús ama y bendice
# ==========================================================================
C = "PC02-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Amor y bendición",
    "items": [
        {"texto": "Quien ama y bendice a los niños.", "respuesta": "JESUS"},
        {"texto": "Lo que Jesús siente por los niños.", "respuesta": "AMOR"},
        {"texto": "Gesto de Jesús que desea un bien a alguien.", "respuesta": "BENDICION"},
        {"texto": "Quienes reciben el amor y la bendición de Jesús.", "respuesta": "NINOS"},
        {"texto": "Forma tierna de mostrar amor.", "respuesta": "CARINO"},
        {"texto": "Alguien cercano que te quiere bien.", "respuesta": "AMIGO"},
    ],
    "incluir": ["AMOR", "BENDICION"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús hizo con los niños además de acogerlos.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús ama y bendice",
    "palabras": ["JESUS", "AMOR", "BENDICION", "NIÑOS", "CARIÑO", "AMIGO"],
    "incluir": ["AMOR", "BENDICION"], "requisito": 5,
    "pistas": ["JESÚS y AMOR son de las palabras más cortas: búscalas primero.",
               "BENDICIÓN es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 19,13-15",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 19,13-15 y completa: «Y poniendo las ______ sobre "
                  "ellos, se fue de allí.»", "respuesta": "MANOS", "banco": ["MANOS", "OJOS", "PIES"]},
        {"texto": "¿Qué gesto de cariño hizo Jesús con los niños?", "abierta": True, "palabras_esperadas": ["MANOS", "BENDIJO", "ABRAZO", "TOCO", "BENDECIR", "CARINO"], "respuestas_referencia": ["Los abrazó, puso las manos sobre ellos y los bendijo.", "Tomó a los niños en sus brazos y los bendijo.", "Les mostró cariño abrazándolos y bendiciéndolos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 19.",
               "Es un relato parecido al de Marcos: unos niños se acercan a Jesús y él los bendice."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús ______ a los niños.", "respuesta": "AMA", "banco": ["AMA", "IGNORA", "OLVIDA"]},
        {"texto": "Jesús los ______.", "respuesta": "BENDICE", "banco": ["BENDICE", "CASTIGA", "APARTA"]},
        {"texto": "El trato de Jesús está lleno de ______.", "respuesta": "AMOR",
         "banco": ["AMOR", "INDIFERENCIA", "ENOJO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús siente y hace por los niños.",
               "La segunda respuesta empieza con «B»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús ama a los niños.", "respuesta": True},
        {"texto": "Jesús los trata con indiferencia.", "respuesta": False},
        {"texto": "Jesús bendice a los niños.", "respuesta": True},
        {"texto": "El mensaje de Jesús es de rechazo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: Jesús ama y bendice a los niños.",
               "Si una frase dice que a Jesús no le importan los niños, es falsa."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué muestra que Jesús ama a los niños?",
         "opciones": ["Los aparta de su lado", "Los recibe y los bendice",
                      "Los ignora cuando se acercan"], "correcta": 1},
        {"texto": "¿Qué significa que Jesús «bendice» a alguien?",
         "opciones": ["Que le desea y le da un bien de parte de Dios",
                      "Que lo castiga por algo que hizo",
                      "Que no quiere volver a verlo"], "correcta": 0},
        {"texto": "¿Qué sentimos cuando alguien nos trata con cariño, como Jesús?",
         "opciones": ["Que no le importamos a nadie", "Que somos queridos y valorados",
                      "Que debemos alejarnos"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la diferencia entre bendecir y castigar.",
               "El mensaje central es que Jesús ama y bendice, no que rechaza."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "JESUS", "definicion": "Ama y bendice a los niños"},
        {"termino": "BENDICIÓN", "definicion": "Gesto de bien que Jesús regala"},
        {"termino": "NIÑOS", "definicion": "Acogidos y amados por Jesús"},
        {"termino": "AMOR", "definicion": "El cariño de Jesús hacia nosotros"},
        {"termino": "AMIGO", "definicion": "Cercanía y confianza"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe el gesto de desear un bien a alguien.",
               "AMOR es lo que hay detrás de todo lo que Jesús hace por los niños."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Palabras del corazón",
    "instruccion": "En 45 segundos, marca tres palabras que expresen cómo Jesús trata a los niños.",
    "tiempo_segundos": 45,
    "banco": ["JESUS", "AMOR", "BENDICIÓN", "NIÑOS", "CARIÑO", "AMIGO"],
    "correctas": ["JESUS", "AMOR", "BENDICIÓN", "NIÑOS", "CARIÑO", "AMIGO"], "minimo": 3, "requisito": 3,
    "pistas": ["Cualquiera de las palabras de este tema es una buena respuesta.",
               "Repasa el crucigrama y la sopa de letras de este tema."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Completa: Jesús me ama y me ______.", "respuesta": "BENDICE",
         "banco": ["BENDICE", "IGNORA", "OLVIDA"]},
    ],
    "reflexion": "¿Qué significa para ti que Jesús te bendiga?",
    "requisito": 1,
    "pistas": ["Piensa en lo que Jesús hace además de amar a los niños.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: muestro el amor de Jesús",
    "situacion": "Un compañero de tu grupo está triste porque tuvo un mal día.",
    "items": [
        {"texto": "¿Qué puedes hacer para mostrarle el amor de Jesús?",
         "opciones": ["Acompañarlo y preguntarle qué le pasa",
                      "Decirle una palabra de ánimo",
                      "Ofrecerle ayuda con algo que necesite",
                      "Burlarte de él porque está triste"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra amor ni cariño."],
})

# ==========================================================================
# PC02-C03 — Los discípulos aprenden a acoger
# ==========================================================================
C = "PC02-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Aprendemos a acoger",
    "items": [
        {"texto": "Quienes seguían a Jesús y aprendían de Él.", "respuesta": "DISCIPULOS"},
        {"texto": "Recibir con cariño a alguien.", "respuesta": "ACOGER"},
        {"texto": "Quien enseñó a los discípulos a acoger.", "respuesta": "JESUS"},
        {"texto": "Quienes se acercaban y a veces eran apartados.", "respuesta": "NINOS"},
        {"texto": "Lo que mueve a Jesús a acoger a todos.", "respuesta": "AMOR"},
        {"texto": "Forma correcta de tratar a los demás.", "respuesta": "RESPETO"},
    ],
    "incluir": ["DISCIPULOS", "ACOGER"], "requisito": 4,
    "pistas": ["Piensa en quiénes acompañaban siempre a Jesús.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Aprendemos a acoger",
    "palabras": ["DISCIPULOS", "ACOGER", "JESUS", "NIÑOS", "AMOR", "RESPETO"],
    "requisito": 5,
    "pistas": ["JESÚS y AMOR son de las palabras más cortas: búscalas primero.",
               "DISCÍPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 9,46-48",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 9,46-48 y completa: «El que reciba a este niño en "
                  "mi nombre, a mí me ______.»", "respuesta": "RECIBE", "banco": ["RECIBE", "IGNORA", "RECHAZA"]},
        {"texto": "¿Qué discutían los discípulos antes de que Jesús les enseñara con el niño?", "abierta": True, "palabras_esperadas": ["IMPORTANTE", "MAYOR", "DISCUTIAN", "QUIEN", "MEJOR", "GRANDE"], "respuestas_referencia": ["Discutían quién de ellos era el más importante.", "Estaban discutiendo sobre quién sería el mayor entre ellos.", "Querían saber quién era el más grande del grupo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 9.",
               "Los discípulos discutían sobre quién de ellos era el más importante."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los ______ aprendieron de Jesús a acoger.", "respuesta": "DISCÍPULOS",
         "banco": ["DISCÍPULOS", "MAESTROS", "SOLDADOS"]},
        {"texto": "Debemos ______ a los demás, como Jesús enseñó.", "respuesta": "ACOGER",
         "banco": ["ACOGER", "RECHAZAR", "IGNORAR"]},
        {"texto": "Acogemos a los demás con ______.", "respuesta": "RESPETO",
         "banco": ["RESPETO", "MIEDO", "DESCONFIANZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quiénes siguieron a Jesús y aprendieron de Él.",
               "La segunda respuesta es lo opuesto a rechazar."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los discípulos aprendieron de Jesús a acoger.", "respuesta": True},
        {"texto": "Debemos excluir a quien es diferente.", "respuesta": False},
        {"texto": "Jesús enseña a acoger a todos.", "respuesta": True},
        {"texto": "Rechazar a alguien es una forma de amar.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: Jesús enseñó a sus discípulos a acoger, no a excluir.",
               "Si una frase dice que rechazar es amar, es falsa."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué debían aprender los discípulos de Jesús?",
         "opciones": ["A rechazar a los niños", "A acoger a los niños", "A ignorarlos"], "correcta": 1},
        {"texto": "¿Por qué al principio los discípulos apartaban a los niños?",
         "opciones": ["Porque no entendían que también eran importantes para Jesús",
                      "Porque Jesús se lo había ordenado",
                      "Porque los niños no querían acercarse"], "correcta": 0},
        {"texto": "¿Qué actitud enseñó Jesús a sus discípulos?",
         "opciones": ["Acoger y respetar a todos", "Solo atender a los adultos",
                      "Elegir a quién tratar bien"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo cambió la actitud de los discípulos después de la enseñanza de Jesús.",
               "El mensaje central es acoger a todos, sin excepción."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DISCÍPULOS", "definicion": "Seguidores de Jesús"},
        {"termino": "ACOGER", "definicion": "Recibir con cariño"},
        {"termino": "RESPETO", "definicion": "Valorar a cada persona"},
        {"termino": "JESUS", "definicion": "Modelo de acogida"},
        {"termino": "NIÑOS", "definicion": "Acogidos por Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe a quienes seguían a Jesús.",
               "RESPETO tiene que ver con cómo tratamos a los demás."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: Cambia la actitud",
    "instruccion": "En cada caso, indica si la acción muestra acoger o rechazar.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Invitar a alguien a participar.", "opciones": ["Acoger", "Rechazar"], "correcta": 0},
        {"texto": "Escuchar con atención a un compañero.", "opciones": ["Acoger", "Rechazar"], "correcta": 0},
        {"texto": "Burlarse de alguien.", "opciones": ["Acoger", "Rechazar"], "correcta": 1},
        {"texto": "Apartar a alguien del grupo.", "opciones": ["Acoger", "Rechazar"], "correcta": 1},
        {"texto": "Ayudar a quien lo necesita.", "opciones": ["Acoger", "Rechazar"], "correcta": 0},
        {"texto": "Ignorar a alguien a propósito.", "opciones": ["Acoger", "Rechazar"], "correcta": 1},
    ],
    "requisito": 5,
    "pistas": ["Piensa si la acción hace que alguien se sienta bien recibido o dejado de lado.",
               "Burlarse, apartar e ignorar siempre son formas de rechazar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Alguien en tu salón se queda solo casi siempre. ¿Qué haría un discípulo que aprendió "
                  "de Jesús a acoger?", "abierta": True, "palabras_esperadas": ["ACOMPANAR", "INVITAR", "JUGAR", "ACOGER", "HABLAR"], "respuestas_referencia": ["Me acercaría a acompañarlo e invitarlo a jugar.", "Lo invitaría a estar conmigo para que no se sienta solo.", "Trataría de hablar con esa persona y hacerme su amigo."]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en cómo Jesús enseñó a sus discípulos a tratar a los demás.",
               "No hay una única respuesta correcta: cuenta lo que tú harías."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: integro al que está solo",
    "situacion": "En tu grupo, alguien suele quedarse solo y nadie lo invita a jugar.",
    "items": [
        {"texto": "¿Qué acción ayudaría a integrarlo, como enseñó Jesús?",
         "opciones": ["Invitarlo a participar en el juego o la actividad",
                      "Sentarte con él y conversar un rato",
                      "Presentárselo a otros compañeros",
                      "Seguir jugando sin decirle nada"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que deja a esa persona igual de sola."],
})

# ==========================================================================
# PC02-C04 — Jesús es amigo cercano
# ==========================================================================
C = "PC02-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Mi amigo Jesús",
    "items": [
        {"texto": "Quien es amigo cercano de cada uno de nosotros.", "respuesta": "JESUS"},
        {"texto": "Alguien en quien confías y te quiere bien.", "respuesta": "AMIGO"},
        {"texto": "Estar junto a alguien, no lejos.", "respuesta": "CERCA"},
        {"texto": "Lo que sostiene una amistad verdadera.", "respuesta": "AMOR"},
        {"texto": "Poder contarle a alguien lo que sientes sin miedo.", "respuesta": "CONFIANZA"},
        {"texto": "Lo que Jesús hace: caminar junto a nosotros.", "respuesta": "ACOMPANA"},
    ],
    "incluir": ["JESUS", "AMIGO"], "requisito": 4,
    "pistas": ["Piensa en lo que significa que Jesús esté cerca de ti.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús, amigo cercano",
    "palabras": ["JESUS", "AMIGO", "CERCA", "AMOR", "CONFIANZA", "ACOMPAÑA"],
    "requisito": 5,
    "pistas": ["JESÚS y AMOR son de las palabras más cortas: búscalas primero.",
               "CONFIANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 15,13-15",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 15,13-15 y completa: «Ya no os llamo siervos... os "
                  "he llamado ______.»", "respuesta": "AMIGOS", "banco": ["AMIGOS", "EXTRAÑOS", "SIERVOS"]},
        {"texto": "¿Qué significa para ti que Jesús te llame amigo?", "abierta": True, "palabras_esperadas": ["AMIGO", "CERCANO", "CONFIANZA", "AMOR", "ACOMPANA"], "respuestas_referencia": ["Que puedo confiar en él y sentirlo cerca de mí.", "Que Jesús me quiere y me acompaña como un amigo de verdad.", "Significa que tengo una relación cercana y de confianza con él."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 15.",
               "Jesús explica la diferencia entre ser siervo y ser amigo suyo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús es mi ______.", "respuesta": "AMIGO", "banco": ["AMIGO", "DESCONOCIDO", "JUEZ"]},
        {"texto": "Jesús está ______ de mí, siempre.", "respuesta": "CERCA",
         "banco": ["CERCA", "LEJOS", "AUSENTE"]},
        {"texto": "Puedo confiar en su ______.", "respuesta": "AMOR", "banco": ["AMOR", "SILENCIO", "OLVIDO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo es Jesús contigo, como lo es un buen amigo.",
               "La primera respuesta describe a Jesús mismo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús es un amigo cercano.", "respuesta": True},
        {"texto": "La amistad con Jesús impide amar a otros.", "respuesta": False},
        {"texto": "Puedo confiar en Jesús.", "respuesta": True},
        {"texto": "Jesús quiere mi bien.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: Jesús es un amigo que acompaña, no que aleja de los demás.",
               "Si una frase dice que Jesús no quiere tu bien, es falsa."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué significa reconocer a Jesús como amigo?",
         "opciones": ["Hablar con Él y confiarle lo que vivo", "Olvidarme de los demás",
                      "Hacer siempre lo que yo quiero"], "correcta": 0},
        {"texto": "¿Cómo se nota que alguien es un amigo cercano?",
         "opciones": ["Porque nunca está cuando lo necesitas", "Porque te acompaña y te escucha",
                      "Porque solo aparece cuando le conviene"], "correcta": 1},
        {"texto": "¿Qué puedo hacer para vivir mi amistad con Jesús?",
         "opciones": ["Hablarle en oración y confiar en Él", "Alejarme de Él cuando tengo un problema",
                      "Solo pensar en Él una vez al año"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace un buen amigo por ti.",
               "El mensaje central es hablar con Jesús y confiar en Él."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "JESUS", "definicion": "Mi amigo cercano"},
        {"termino": "AMOR", "definicion": "Lo que sostiene la amistad"},
        {"termino": "CONFIANZA", "definicion": "Abrir el corazón sin miedo"},
        {"termino": "ACOMPAÑA", "definicion": "Está conmigo siempre"},
        {"termino": "CERCA", "definicion": "Su presencia junto a mí"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe abrirle el corazón a alguien.",
               "ACOMPAÑA tiene que ver con estar presente, no con estar lejos."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Mi amistad con Jesús",
    "instruccion": "En 45 segundos, marca tres palabras que describan qué significa que Jesús sea tu amigo.",
    "tiempo_segundos": 45,
    "banco": ["JESUS", "AMIGO", "CERCA", "AMOR", "CONFIANZA", "ACOMPAÑA"],
    "correctas": ["JESUS", "AMIGO", "CERCA", "AMOR", "CONFIANZA", "ACOMPAÑA"], "minimo": 3, "requisito": 3,
    "pistas": ["Cualquiera de las palabras de este tema es una buena respuesta.",
               "Repasa el crucigrama y la sopa de letras de este tema."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "¿Cuándo has sentido que Jesús es tu amigo?", "abierta": True},
    ],
    "requisito": 1,
    "pistas": ["No hay una única respuesta correcta: escribe lo que sientas.",
               "Piensa en un momento en que te sentiste acompañado."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: confío en mi amigo Jesús",
    "situacion": "Sientes miedo o tristeza por algo que está pasando en tu vida.",
    "items": [
        {"texto": "¿Qué puedes hacer, recordando que Jesús es tu amigo cercano?",
         "opciones": ["Contarle a Jesús en oración lo que sientes",
                      "Recordar que Él te acompaña siempre",
                      "Buscar también el apoyo de alguien de confianza",
                      "Guardarte todo y no contárselo a nadie, ni siquiera a Jesús"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que te aleja de tu amigo Jesús."],
})

# ==========================================================================
# PC02-C05 — La amistad con Jesús se vive en oración
# ==========================================================================
C = "PC02-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Oración",
    "items": [
        {"texto": "Momento de diálogo con Jesús.", "respuesta": "ORACION"},
        {"texto": "A quien le hablamos cuando oramos.", "respuesta": "JESUS"},
        {"texto": "Alguien de confianza con quien hablamos de todo.", "respuesta": "AMIGO"},
        {"texto": "Contarle a Jesús lo que vivo y siento.", "respuesta": "HABLAR"},
        {"texto": "Abrir el corazón para recibir lo que Jesús quiere decirme.", "respuesta": "ESCUCHAR"},
        {"texto": "Entregarle a Dios lo que siento, sin miedo.", "respuesta": "CONFIAR"},
    ],
    "incluir": ["ORACION", "JESUS"], "requisito": 4,
    "pistas": ["Piensa en cómo se llama hablar con Jesús.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: La oración",
    "palabras": ["ORACION", "JESUS", "AMIGO", "HABLAR", "ESCUCHAR", "CONFIAR"],
    "requisito": 5,
    "pistas": ["JESÚS y AMIGO son de las palabras más cortas: búscalas primero.",
               "ESCUCHAR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 11,1-4",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 11,1-4 y completa: «Señor, enséñanos a ______.»",
         "respuesta": "ORAR", "banco": ["ORAR", "CANTAR", "CORRER"]},
        {"texto": "¿Qué le pidieron los discípulos a Jesús?", "abierta": True, "palabras_esperadas": ["ORAR", "ENSENAR", "REZAR", "ORACION"], "respuestas_referencia": ["Le pidieron que les enseñara a orar.", "Los discípulos le pidieron a Jesús que les enseñara a rezar.", "Querían que Jesús les enseñara una oración."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 11.",
               "Un discípulo le hace un pedido a Jesús después de verlo orar."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Cuando hago ______, hablo con Jesús.", "respuesta": "ORACIÓN",
         "banco": ["ORACIÓN", "TAREA", "JUEGO"]},
        {"texto": "Puedo ______ con Jesús de lo que vivo.", "respuesta": "HABLAR",
         "banco": ["HABLAR", "ESCONDER", "CALLAR"]},
        {"texto": "En oración también puedo ______.", "respuesta": "ESCUCHAR",
         "banco": ["ESCUCHAR", "GRITAR", "DISTRAERME"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se llama el momento de hablar con Jesús.",
               "La segunda respuesta es lo que haces cuando le cuentas algo a un amigo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La oración puede ser un diálogo con Jesús.", "respuesta": True},
        {"texto": "Solo se puede orar dentro de una iglesia.", "respuesta": False},
        {"texto": "Puedo contarle a Jesús lo que vivo.", "respuesta": True},
        {"texto": "La oración expresa nuestra amistad con Jesús.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: puedes hablar con Jesús en cualquier momento y lugar.",
               "Si una frase dice que solo se puede orar en un lugar, es falsa."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué puedo contarle a Jesús en oración?",
         "opciones": ["Solo cosas perfectas", "Lo que vivo y siento, tal como es",
                      "Nada, porque Él ya lo sabe todo"], "correcta": 1},
        {"texto": "¿Dónde puedo orar a Jesús?",
         "opciones": ["Solo en la iglesia", "En cualquier lugar y momento",
                      "Solo si alguien me lo pide"], "correcta": 1},
        {"texto": "¿Qué es escuchar a Jesús en oración?",
         "opciones": ["Abrir el corazón y estar en silencio", "Hablar sin parar sin dejar espacio",
                      "Distraerme pensando en otra cosa"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["La oración es un diálogo: también hay que escuchar, no solo hablar.",
               "Piensa que Jesús es un amigo con quien puedes hablar de todo."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ORACIÓN", "definicion": "Diálogo con Jesús"},
        {"termino": "JESUS", "definicion": "Mi amigo, a quien le hablo"},
        {"termino": "HABLAR", "definicion": "Contarle lo que vivo"},
        {"termino": "ESCUCHAR", "definicion": "Abrir el corazón en silencio"},
        {"termino": "CONFIAR", "definicion": "Entregarle a Dios lo que siento"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe el momento de hablar con Jesús.",
               "ESCUCHAR es la otra mitad de un buen diálogo, además de hablar."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: 30 segundos con Jesús",
    "instruccion": "En 30 segundos, completa mentalmente «Jesús, hoy quiero contarte…» y elige qué le dirías.",
    "tiempo_segundos": 30,
    "banco": ["Mi día", "Mis miedos", "Mi alegría", "Mi familia", "Nada"],
    "correctas": ["Mi día", "Mis miedos", "Mi alegría", "Mi familia"], "minimo": 1, "requisito": 1,
    "pistas": ["Cualquiera de esas cosas es algo que sí le puedes contar a Jesús.",
               "Descarta la única opción que no le cuenta nada a un amigo."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Antes de dormir, ¿qué podrías decirle a Jesús?", "abierta": True},
    ],
    "requisito": 1,
    "pistas": ["No hay una única respuesta correcta: escribe lo que sientas.",
               "Piensa en algo que viviste hoy y que le podrías contar."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: mi oración a Jesús amigo",
    "situacion": "Quieres tener un momento de oración personal, como con un amigo de confianza.",
    "items": [
        {"texto": "¿Qué podrías decirle a Jesús en una oración corta?",
         "opciones": ["Gracias, Jesús, por ser mi amigo y cuidarme",
                      "Jesús, hoy quiero contarte cómo me siento",
                      "Jesús, ayúdame a tratar bien a los demás",
                      "No tengo nada que decirle a Jesús"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en algo real que le dirías a un amigo de confianza.",
               "Descarta la única opción que no es en realidad una oración."],
})

# ==========================================================================
# PC02-C06 — Mostramos la amistad de Jesús
# ==========================================================================
C = "PC02-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Amistad que se demuestra",
    "items": [
        {"texto": "Relación de cariño y cercanía entre personas.", "respuesta": "AMISTAD"},
        {"texto": "Lo que mueve a cuidar y a servir a otros.", "respuesta": "AMOR"},
        {"texto": "Dar una mano a quien lo necesita.", "respuesta": "AYUDA"},
        {"texto": "Tratar bien a los demás, valorándolos.", "respuesta": "RESPETO"},
        {"texto": "Recibir a alguien con cariño.", "respuesta": "ACOGER"},
        {"texto": "Dar parte de lo que tienes a otro.", "respuesta": "COMPARTIR"},
    ],
    "incluir": ["AMISTAD", "AMOR"], "requisito": 4,
    "pistas": ["Piensa en cómo se llama la relación de cariño entre dos personas.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Mostramos la amistad",
    "palabras": ["AMISTAD", "AMOR", "AYUDA", "RESPETO", "ACOGER", "COMPARTIR"],
    "requisito": 5,
    "pistas": ["AMOR y AYUDA son de las palabras más cortas: búscalas primero.",
               "COMPARTIR es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 13,34-35",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 13,34-35 y completa: «Un mandamiento nuevo os doy: "
                  "que os ______ unos a otros.»", "respuesta": "AMÉIS", "banco": ["AMÉIS", "OLVIDÉIS", "EVITÉIS"]},
        {"texto": "¿Cómo reconocerán que somos discípulos de Jesús, según este versículo?", "abierta": True, "palabras_esperadas": ["AMOR", "AMANDONOS", "AMEMOS", "AMAR"], "respuestas_referencia": ["Por el amor que nos tengamos unos a otros.", "Nos reconocerán como discípulos si nos amamos entre nosotros.", "Amándonos unos a otros como Jesús nos amó."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 13.",
               "Jesús da un mandamiento «nuevo» a sus discípulos antes de su pasión."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Mostrar amistad significa ______ a quien lo necesita.", "respuesta": "AYUDAR",
         "banco": ["AYUDAR", "IGNORAR", "COMPETIR"]},
        {"texto": "También significa ______ a los demás.", "respuesta": "RESPETAR",
         "banco": ["RESPETAR", "DESPRECIAR", "BURLARSE"]},
        {"texto": "Y ______ lo que tenemos con otros.", "respuesta": "COMPARTIR",
         "banco": ["COMPARTIR", "GUARDAR", "ESCONDER"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en acciones concretas, no solo en palabras bonitas.",
               "La tercera respuesta es dar parte de lo tuyo a otro."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La amistad cristiana se demuestra con acciones.", "respuesta": True},
        {"texto": "Ayudar a alguien expresa amor.", "respuesta": True},
        {"texto": "Burlarse de un amigo demuestra amistad.", "respuesta": False},
        {"texto": "Acoger a alguien expresa cariño.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: la amistad se demuestra con hechos, no solo con palabras.",
               "Burlarse nunca es una forma de mostrar amistad."],
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cuál acción muestra mejor la amistad de Jesús?",
         "opciones": ["Excluir a quien es distinto", "Ayudar y acoger a los demás",
                      "Burlarse de alguien"], "correcta": 1},
        {"texto": "¿Qué significa compartir, como enseñó Jesús?",
         "opciones": ["Dar solo lo que ya no necesitas", "Dar parte de lo tuyo a quien lo necesita",
                      "No dar nunca nada a nadie"], "correcta": 1},
        {"texto": "¿Cómo se nota el respeto hacia otra persona?",
         "opciones": ["Tratándola con burla", "Valorándola tal como es",
                      "Ignorando lo que siente"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en acciones, no en actitudes que alejan a los demás.",
               "El mensaje central es ayudar, acoger y compartir."],
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "AMISTAD", "definicion": "Cercanía y cariño entre personas"},
        {"termino": "AMOR", "definicion": "Lo que mueve a cuidar al otro"},
        {"termino": "AYUDA", "definicion": "Servicio a quien lo necesita"},
        {"termino": "RESPETO", "definicion": "Valorar a cada persona"},
        {"termino": "COMPARTIR", "definicion": "Dar parte de lo tuyo al otro"},
    ],
    "requisito": 4,
    "pistas": ["Piensa qué palabra describe dar una mano a quien lo necesita.",
               "COMPARTIR tiene que ver con dar, no con guardar."],
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Misión de amistad",
    "instruccion": "En 60 segundos, elige una acción para mostrar amistad a un compañero o vecino.",
    "tiempo_segundos": 60,
    "banco": ["Ayudar a un compañero con una tarea", "Invitar a jugar a alguien que está solo",
              "Compartir algo tuyo con un vecino", "Escuchar a un amigo triste", "Burlarse de alguien"],
    "correctas": ["Ayudar a un compañero con una tarea", "Invitar a jugar a alguien que está solo",
                  "Compartir algo tuyo con un vecino", "Escuchar a un amigo triste"],
    "minimo": 1, "requisito": 1,
    "pistas": ["Cualquiera de esas acciones, menos una, muestra amistad de verdad.",
               "Descarta la única opción que le hace daño a alguien."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Un vecino tuyo casi siempre está solo. ¿Qué podrías hacer para mostrarle el amor "
                  "de Jesús?", "abierta": True, "palabras_esperadas": ["VISITAR", "ACOMPANAR", "SALUDAR", "AYUDAR", "HABLAR"], "respuestas_referencia": ["Lo visitaría y lo acompañaría de vez en cuando.", "Lo saludaría y le ofrecería ayuda si la necesita.", "Trataría de hablar con él para que no se sienta tan solo."]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción sencilla que sí está en tus manos.",
               "Repasa lo que trabajaste en el reto de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: Misión semanal",
    "situacion": "Esta semana puedes vivir una «misión de amistad» con un compañero o vecino.",
    "items": [
        {"texto": "¿Qué acción puedes realizar y luego contarle a tu catequista?",
         "opciones": ["Ayudar a un compañero con una tarea o mandado",
                      "Invitar a jugar a alguien que casi no tiene amigos",
                      "Compartir algo tuyo (tiempo, un juguete, comida) con un vecino",
                      "Esperar a que alguien más lo haga por mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta que puedas realizar tú mismo esta semana.",
               "Descarta la única opción que no es en realidad una acción tuya."],
})

# ==========================================================================
# PC03 — Dios nos habla en la Biblia   (Encuentro 3, 2 Timoteo 3,14-17 / Lucas 24,13-35)
# ==========================================================================

# ==========================================================================
# PC03-C01 — La Biblia es Palabra de Dios
# ==========================================================================
C = "PC03-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Biblia es Palabra de Dios",
    "items": [
        {"texto": "El libro sagrado donde Dios nos habla.", "respuesta": "BIBLIA"},
        {"texto": "Lo que Dios nos dice y nos comunica.", "respuesta": "PALABRA"},
        {"texto": "Quien nos habla a través de la Biblia.", "respuesta": "DIOS"},
        {"texto": "Otro nombre para los textos sagrados de la Biblia.", "respuesta": "ESCRITURA"},
        {"texto": "Escrita con la ayuda de Dios, como dice san Pablo de la Biblia.", "respuesta": "INSPIRADA"},
        {"texto": "Lo que la Biblia nos enseña, sin mentira.", "respuesta": "VERDAD"},
    ],
    "incluir": ["BIBLIA", "PALABRA"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "2 Timoteo 3,14-17 dice que toda Escritura es inspirada por Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Biblia es Palabra de Dios",
    "palabras": ["BIBLIA", "PALABRA", "DIOS", "ESCRITURA", "INSPIRADA", "VERDAD"],
    "incluir": ["BIBLIA", "PALABRA"], "requisito": 5,
    "pistas": ["DIOS es una de las palabras más cortas: búscala primero.",
               "INSPIRADA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 2 Timoteo 3,14-17",
    "items": [
        {"texto": "Busca en tu Biblia Católica 2 Timoteo 3,14-17 y completa: «Toda Escritura es "
                  "inspirada por ______.»", "respuesta": "DIOS", "banco": ["DIOS", "LOS HOMBRES", "LA HISTORIA"]},
        {"texto": "¿Qué dice san Pablo sobre las Escrituras?", "abierta": True, "palabras_esperadas": ["INSPIRADA", "DIOS", "VERDAD", "ENSENA"], "respuestas_referencia": ["Dice que toda la Escritura está inspirada por Dios y es útil para enseñar.", "Que la Biblia viene de Dios y nos enseña la verdad.", "Que las Escrituras son inspiradas por Dios y nos forman en la fe."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la segunda carta a Timoteo en el índice de tu Biblia; el capítulo es el 3.",
               "San Pablo le explica a Timoteo de dónde viene la autoridad de la Escritura."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "La Biblia es la ______ de Dios.", "respuesta": "PALABRA",
         "banco": ["PALABRA", "HISTORIA", "NOVELA"]},
        {"texto": "Toda Escritura es ______ por Dios.", "respuesta": "INSPIRADA",
         "banco": ["INSPIRADA", "INVENTADA", "COPIADA"]},
        {"texto": "La Biblia nos enseña la ______.", "respuesta": "VERDAD",
         "banco": ["VERDAD", "MENTIRA", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llamamos a lo que Dios nos comunica.",
               "La segunda respuesta empieza con «I»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La Biblia es la Palabra de Dios.", "respuesta": True},
        {"texto": "La Biblia es un libro cualquiera, como cualquier novela.", "respuesta": False},
        {"texto": "Dios nos habla a través de la Biblia.", "respuesta": True},
        {"texto": "La Biblia no tiene nada que ver con nuestra vida.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda: la Biblia es Palabra de Dios, escrita para hablarnos.",
               "Si una frase dice que la Biblia no nos sirve, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué es la Biblia?",
         "opciones": ["Un libro de cuentos inventados", "La Palabra de Dios escrita",
                      "Una novela de aventuras"], "correcta": 1},
        {"texto": "¿Quién inspiró a quienes escribieron la Biblia?",
         "opciones": ["Solo ellos mismos", "Dios", "Otros pueblos"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién le habla al ser humano a través de este libro.",
               "San Pablo dice que la Escritura es «inspirada» por alguien."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "BIBLIA", "definicion": "Palabra de Dios escrita"},
        {"termino": "ESCRITURA", "definicion": "Texto sagrado"},
        {"termino": "INSPIRADA", "definicion": "Escrita con la ayuda de Dios"},
        {"termino": "VERDAD", "definicion": "Lo que la Biblia nos enseña"},
        {"termino": "DIOS", "definicion": "Quien nos habla en la Biblia"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "BIBLIA se relaciona con la idea de un texto escrito por Dios."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["BIBLIA", "PALABRA", "DIOS", "CUENTO", "VERDAD", "INVENCIÓN"],
    "correctas": ["BIBLIA", "PALABRA", "DIOS", "VERDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Biblia - Palabra - Dios - Verdad.",
               "Descarta las palabras que no tienen que ver con la fe."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La Biblia es la ______ de Dios.", "respuesta": "PALABRA",
         "banco": ["PALABRA", "HISTORIA", "NOVELA"]},
    ],
    "reflexion": "¿Por qué crees que es importante leer la Biblia?",
    "requisito": 1,
    "pistas": ["Piensa en cómo llamamos a lo que Dios nos comunica.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: me acerco a la Biblia",
    "situacion": "Ya sabes que la Biblia es la Palabra de Dios, escrita para hablarnos y guiarnos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para acercarte más a la Biblia?",
         "opciones": ["Leer un pasaje corto con tu familia",
                      "Preguntarle a tu catequista una duda sobre la Biblia",
                      "Llevar tu Biblia a la catequesis",
                      "Dejarla cerrada en un estante"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no te acerca a la Biblia."],
    "feedback_ok": "¡Muy bien! Acercarte a la Biblia es acercarte a la voz de Dios.",
})

# ==========================================================================
# PC03-C02 — La Palabra guía la vida
# ==========================================================================
C = "PC03-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Palabra guía la vida",
    "items": [
        {"texto": "Objeto que alumbra en la oscuridad; así llama el salmo a la Palabra de Dios.",
         "respuesta": "LAMPARA"},
        {"texto": "Lo que ilumina nuestro camino.", "respuesta": "LUZ"},
        {"texto": "El recorrido que hacemos en la vida.", "respuesta": "CAMINO"},
        {"texto": "Lo que hace la Palabra de Dios con nuestra vida.", "respuesta": "GUIA"},
        {"texto": "Parte del cuerpo con la que caminamos; ahí alumbra la lámpara, según el salmo.",
         "respuesta": "PIES"},
        {"texto": "Otra palabra para camino o vereda.", "respuesta": "SENDA"},
    ],
    "incluir": ["LAMPARA", "LUZ"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "El Salmo 119,105 compara la Palabra de Dios con una lámpara."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Palabra guía la vida",
    "palabras": ["LAMPARA", "LUZ", "CAMINO", "GUIA", "PIES", "SENDA"],
    "incluir": ["LAMPARA", "CAMINO"], "requisito": 5,
    "pistas": ["LUZ y PIES son de las palabras más cortas: búscalas primero.",
               "LAMPARA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Salmo 119,105",
    "items": [
        {"texto": "Busca en tu Biblia Católica el Salmo 119,105 y completa: «Lámpara es tu palabra "
                  "para mis pies, ______ para mi camino.»", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "RUIDO"]},
        {"texto": "¿Con qué compara el salmo la Palabra de Dios?", "abierta": True, "palabras_esperadas": ["LAMPARA", "LUZ", "CAMINO", "GUIA"], "respuestas_referencia": ["La compara con una lámpara que alumbra el camino.", "Dice que es como una luz que guía nuestros pasos.", "La compara con una lámpara y una luz para el camino."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Salmos en el índice de tu Biblia; es el salmo número 119.",
               "Es uno de los versículos más conocidos de este salmo sobre la Palabra de Dios."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Lámpara es tu palabra para mis ______.", "respuesta": "PIES",
         "banco": ["PIES", "MANOS", "OJOS"]},
        {"texto": "Es ______ para mi camino.", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "RUIDO"]},
        {"texto": "La Palabra de Dios nos ______ en la vida.", "respuesta": "GUIA",
         "banco": ["GUIA", "CONFUNDE", "ABANDONA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en qué compara el salmo la Palabra de Dios.",
               "La segunda respuesta empieza con «L»."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La Palabra de Dios ilumina nuestro camino.", "respuesta": True},
        {"texto": "La Biblia no sirve para tomar decisiones.", "respuesta": False},
        {"texto": "El salmo compara la Palabra con una lámpara.", "respuesta": True},
        {"texto": "Seguir la Palabra de Dios nos aleja del buen camino.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda el Salmo 119,105: la Palabra es lámpara y luz.",
               "Si una frase dice que la Palabra nos hace daño, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con qué compara el salmo la Palabra de Dios?",
         "opciones": ["Con una lámpara y una luz", "Con una piedra", "Con un río"], "correcta": 0},
        {"texto": "¿Para qué nos sirve la luz de la Palabra de Dios?",
         "opciones": ["Para nada en especial", "Para guiar nuestro camino y nuestras decisiones",
                      "Solo para leer de noche"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en un objeto que alumbra la oscuridad.",
               "La Palabra nos ayuda a decidir cómo actuar."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "LAMPARA", "definicion": "Ilumina la oscuridad"},
        {"termino": "LUZ", "definicion": "Lo que guía el camino"},
        {"termino": "CAMINO", "definicion": "La vida que recorremos"},
        {"termino": "GUIA", "definicion": "Lo que hace la Palabra con nosotros"},
        {"termino": "SENDA", "definicion": "Otro nombre del camino"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "LAMPARA y LUZ están relacionadas entre sí."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["LAMPARA", "LUZ", "CAMINO", "OSCURIDAD", "GUIA", "PERDIDO"],
    "correctas": ["LAMPARA", "LUZ", "CAMINO", "GUIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Lámpara - Luz - Camino - Guía.",
               "Descarta las palabras que hablan de perderse, no de encontrar el camino."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Es ______ para mi camino.", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "RUIDO"]},
    ],
    "reflexion": "¿En qué momento de tu vida la Palabra de Dios te podría servir de guía?",
    "requisito": 1,
    "pistas": ["Piensa en qué compara el salmo la Palabra de Dios.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: la Palabra guía mis decisiones",
    "situacion": "Ya sabes que la Palabra de Dios es como una lámpara que guía nuestro camino.",
    "items": [
        {"texto": "¿Qué puedes hacer cuando no sabes qué decisión tomar?",
         "opciones": ["Buscar un pasaje de la Biblia y pensar en lo que enseña",
                      "Preguntarle a tu catequista o a un adulto de confianza",
                      "Orar pidiendo luz a Dios",
                      "Decidir sin pensarlo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no busca ninguna guía."],
    "feedback_ok": "¡Muy bien! Buscar la luz de Dios te ayuda a decidir mejor.",
})

# ==========================================================================
# PC03-C03 — Jesús se revela en la Escritura
# ==========================================================================
C = "PC03-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús se revela en la Escritura",
    "items": [
        {"texto": "Pueblo al que iban dos discípulos cuando se encontraron con Jesús resucitado.",
         "respuesta": "EMAUS"},
        {"texto": "El recorrido que hacían los discípulos mientras hablaban con Jesús.",
         "respuesta": "CAMINO"},
        {"texto": "Quien se acercó y caminó con los discípulos sin que lo reconocieran.",
         "respuesta": "JESUS"},
        {"texto": "Lo que hacía Jesús con los textos sagrados mientras caminaban.",
         "respuesta": "EXPLICABA"},
        {"texto": "Los textos sagrados en los que Jesús se revela.", "respuesta": "ESCRITURAS"},
        {"texto": "Lo que ardía en los discípulos mientras Jesús les hablaba.", "respuesta": "CORAZON"},
    ],
    "incluir": ["EMAUS", "JESUS"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Lucas 24,13-35 cuenta el encuentro con Jesús en el camino a Emaús."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús se revela en la Escritura",
    "palabras": ["EMAUS", "CAMINO", "JESUS", "EXPLICABA", "ESCRITURAS", "CORAZON"],
    "incluir": ["EMAUS", "ESCRITURAS"], "requisito": 5,
    "pistas": ["EMAUS y JESUS son de las palabras más cortas: búscalas primero.",
               "ESCRITURAS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 24,25-27",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 24,25-27 y completa: «Y comenzando por Moisés... "
                  "les explicaba lo que de él decían todas las ______.»", "respuesta": "ESCRITURAS",
         "banco": ["ESCRITURAS", "CIUDADES", "FIESTAS"]},
        {"texto": "¿Qué hizo Jesús con los discípulos en el camino?", "abierta": True, "palabras_esperadas": ["EXPLICO", "EXPLICABA", "ENSENO", "CAMINO", "ESCRITURAS"], "respuestas_referencia": ["Les explicó las Escrituras mientras caminaban juntos.", "Caminó con ellos y les explicó lo que decía la Palabra de Dios.", "Les enseñó el sentido de las Escrituras en el camino a Emaús."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 24.",
               "Jesús les va explicando, libro por libro, lo que hablaba de él."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dos discípulos iban camino a ______.", "respuesta": "EMAUS",
         "banco": ["EMAUS", "JERUSALEN", "BELEN"]},
        {"texto": "Comenzando por Moisés, Jesús les ______ las Escrituras.", "respuesta": "EXPLICABA",
         "banco": ["EXPLICABA", "ESCONDIA", "OLVIDABA"]},
        {"texto": "¿No ardía nuestro ______ mientras nos hablaba?", "respuesta": "CORAZON",
         "banco": ["CORAZON", "ESTOMAGO", "CUERPO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el nombre del pueblo al que iban los discípulos.",
               "La última respuesta es lo que sintieron los discípulos al escuchar a Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Dos discípulos se encontraron con Jesús en el camino a Emaús.", "respuesta": True},
        {"texto": "Los discípulos reconocieron a Jesús de inmediato.", "respuesta": False},
        {"texto": "Jesús les explicó las Escrituras que hablaban de él.", "respuesta": True},
        {"texto": "Las Escrituras no tienen relación con Jesús.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Lucas 24,13-35: los discípulos no reconocieron a Jesús enseguida.",
               "Si una frase dice que la Escritura no habla de Jesús, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hacía Jesús con los discípulos en el camino?",
         "opciones": ["Los ignoraba", "Les explicaba las Escrituras", "Se burlaba de ellos"], "correcta": 1},
        {"texto": "¿Qué sintieron los discípulos mientras Jesús les hablaba?",
         "opciones": ["Que el corazón les ardía", "Que se aburrían", "Que tenían miedo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús va haciendo mientras caminan juntos.",
               "Los discípulos lo cuentan después usando la palabra «arder»."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "EMAUS", "definicion": "Pueblo del encuentro"},
        {"termino": "CAMINO", "definicion": "Donde caminaban los discípulos"},
        {"termino": "ESCRITURAS", "definicion": "Lo que Jesús les explicaba"},
        {"termino": "CORAZON", "definicion": "Lo que ardía al escucharlo"},
        {"termino": "JESUS", "definicion": "Quien se reveló en el camino"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "EMAUS es el lugar hacia donde iban los discípulos."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["EMAUS", "JESUS", "CAMINO", "ESCRITURAS", "OLVIDO", "IGNORANCIA"],
    "correctas": ["EMAUS", "JESUS", "CAMINO", "ESCRITURAS"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Emaús - Jesús - Camino - Escrituras.",
               "Descarta las palabras que hablan de no saber o no recordar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Comenzando por Moisés, Jesús les ______ las Escrituras.", "respuesta": "EXPLICABA",
         "banco": ["EXPLICABA", "ESCONDIA", "OLVIDABA"]},
    ],
    "reflexion": "¿Alguna vez sentiste que algo de la Biblia te «tocó el corazón»? Cuéntaselo a tu catequista.",
    "requisito": 1,
    "pistas": ["Piensa en lo que Jesús va haciendo mientras caminan juntos.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: reconozco a Jesús",
    "situacion": "Los discípulos de Emaús descubrieron a Jesús escuchando y comprendiendo las Escrituras.",
    "items": [
        {"texto": "¿Qué puedes hacer para reconocer mejor a Jesús en tu vida?",
         "opciones": ["Leer y conversar sobre un pasaje del Evangelio",
                      "Participar con atención en la catequesis",
                      "Preguntar cuando no entiendas algo de la Biblia",
                      "Ignorar lo que no entiendes"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que te aleja de comprender la Biblia."],
    "feedback_ok": "¡Muy bien! Escuchar y comprender la Palabra nos ayuda a reconocer a Jesús.",
})

# ==========================================================================
# PC03-C04 — Los discípulos de Emaús reconocen a Jesús
# ==========================================================================
C = "PC03-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: los discípulos reconocen a Jesús",
    "items": [
        {"texto": "Alimento que Jesús partió en la mesa de Emaús.", "respuesta": "PAN"},
        {"texto": "Lo que Jesús hizo con el pan justo antes de que lo reconocieran.", "respuesta": "PARTIR"},
        {"texto": "Lo que se les abrió a los discípulos al ver a Jesús partir el pan.", "respuesta": "OJOS"},
        {"texto": "Lo que hicieron los discípulos al ver el gesto de Jesús.", "respuesta": "RECONOCER"},
        {"texto": "Donde se sentaron Jesús y los discípulos a comer.", "respuesta": "MESA"},
        {"texto": "Quienes seguían a Jesús y caminaban con él.", "respuesta": "DISCIPULOS"},
    ],
    "incluir": ["PAN", "RECONOCER"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Lucas 24,28-32 cuenta el momento en que reconocen a Jesús."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: los discípulos reconocen a Jesús",
    "palabras": ["PAN", "PARTIR", "OJOS", "RECONOCER", "MESA", "DISCIPULOS"],
    "incluir": ["PAN", "MESA"], "requisito": 5,
    "pistas": ["PAN y OJOS son de las palabras más cortas: búscalas primero.",
               "DISCIPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 24,28-32",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 24,28-32 y completa: «Al ______ el pan, se les "
                  "abrieron los ojos y le reconocieron.»", "respuesta": "PARTIR",
         "banco": ["PARTIR", "GUARDAR", "VENDER"]},
        {"texto": "¿En qué momento reconocieron los discípulos a Jesús?", "abierta": True, "palabras_esperadas": ["PARTIR", "PAN", "OJOS", "RECONOCIERON"], "respuestas_referencia": ["Lo reconocieron cuando partió el pan.", "Se les abrieron los ojos al partir el pan y lo reconocieron.", "En el momento de partir el pan en la cena."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 24.",
               "Es el mismo gesto que Jesús hizo en la Última Cena."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Al ______ el pan, se les abrieron los ojos.", "respuesta": "PARTIR",
         "banco": ["PARTIR", "GUARDAR", "VENDER"]},
        {"texto": "Y le ______.", "respuesta": "RECONOCIERON",
         "banco": ["RECONOCIERON", "IGNORARON", "OLVIDARON"]},
        {"texto": "Se sentaron juntos a la ______.", "respuesta": "MESA",
         "banco": ["MESA", "PUERTA", "CALLE"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el gesto que hizo Jesús con el pan.",
               "La segunda respuesta es lo que hicieron los discípulos al ver ese gesto."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús partió el pan en la mesa con los discípulos.", "respuesta": True},
        {"texto": "Los discípulos nunca reconocieron a Jesús.", "respuesta": False},
        {"texto": "Al partir el pan, se les abrieron los ojos.", "respuesta": True},
        {"texto": "Los discípulos se quedaron indiferentes después de reconocerlo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Lucas 24,28-32: el gesto de partir el pan fue clave.",
               "Si una frase dice que nunca lo reconocieron, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿En qué momento reconocieron los discípulos a Jesús?",
         "opciones": ["Cuando entró al pueblo", "Cuando partió el pan",
                      "Cuando se sentaron a la mesa sin más"], "correcta": 1},
        {"texto": "¿Qué hicieron los discípulos después de reconocer a Jesús?",
         "opciones": ["Se quedaron callados", "Volvieron corriendo a contarlo", "Se fueron a dormir"],
         "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el gesto que hizo Jesús con el pan.",
               "Los discípulos no se quedaron con la noticia para ellos solos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PAN", "definicion": "Lo que Jesús partió"},
        {"termino": "PARTIR", "definicion": "Gesto que abrió sus ojos"},
        {"termino": "OJOS", "definicion": "Lo que se les abrió"},
        {"termino": "MESA", "definicion": "Donde compartieron la cena"},
        {"termino": "DISCIPULOS", "definicion": "Quienes reconocieron a Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "PAN y PARTIR están relacionadas entre sí."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["PAN", "PARTIR", "MESA", "RECONOCER", "OLVIDO", "IGNORAR"],
    "correctas": ["PAN", "PARTIR", "MESA", "RECONOCER"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Pan - Partir - Mesa - Reconocer.",
               "Descarta las palabras que hablan de no darse cuenta."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Al ______ el pan, se les abrieron los ojos.", "respuesta": "PARTIR",
         "banco": ["PARTIR", "GUARDAR", "VENDER"]},
    ],
    "reflexion": "¿En qué momentos sencillos de tu día puedes reconocer a Jesús cerca de ti?",
    "requisito": 1,
    "pistas": ["Piensa en el gesto que hizo Jesús con el pan.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: Jesús está cerca",
    "situacion": "Los discípulos reconocieron a Jesús en un gesto sencillo: partir el pan.",
    "items": [
        {"texto": "¿En qué momento sencillo de tu semana puedes reconocer que Jesús está cerca?",
         "opciones": ["Al compartir la comida en familia",
                      "Al ayudar a alguien sin esperar nada a cambio",
                      "Al rezar antes de dormir",
                      "Al ignorar a los demás"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que aleja a Jesús de nuestra vida."],
    "feedback_ok": "¡Muy bien! Jesús se hace presente en los gestos sencillos de cada día.",
})

# ==========================================================================
# PC03-C05 — Escuchar y meditar la Palabra
# ==========================================================================
C = "PC03-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: escuchar y meditar la Palabra",
    "items": [
        {"texto": "Prestar atención a lo que Dios nos dice.", "respuesta": "ESCUCHAR"},
        {"texto": "Pensar despacio y con calma en la Palabra de Dios.", "respuesta": "MEDITAR"},
        {"texto": "Poner en práctica lo que la Palabra enseña, no solo escucharla.", "respuesta": "PRACTICAR"},
        {"texto": "Quienes solo escuchan la Palabra sin ponerla en práctica, según Santiago.",
         "respuesta": "OIDORES"},
        {"texto": "Quienes ponen en práctica la Palabra, según Santiago.", "respuesta": "HACEDORES"},
        {"texto": "Donde María guardaba y meditaba las palabras que escuchaba.", "respuesta": "CORAZON"},
    ],
    "incluir": ["ESCUCHAR", "MEDITAR"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Santiago 1,22-23 distingue entre oír la Palabra y ponerla en práctica."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: escuchar y meditar la Palabra",
    "palabras": ["ESCUCHAR", "MEDITAR", "PRACTICAR", "OIDORES", "HACEDORES", "CORAZON"],
    "incluir": ["ESCUCHAR", "PRACTICAR"], "requisito": 5,
    "pistas": ["CORAZON es una de las palabras más cortas: búscala primero.",
               "HACEDORES es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Santiago 1,22-23",
    "items": [
        {"texto": "Busca en tu Biblia Católica Santiago 1,22-23 y completa: «Sed hacedores de la "
                  "palabra, y no tan solamente ______.»", "respuesta": "OIDORES",
         "banco": ["OIDORES", "MAESTROS", "JUECES"]},
        {"texto": "¿Qué dice Santiago sobre escuchar y poner en práctica la Palabra?", "abierta": True, "palabras_esperadas": ["PRACTICAR", "HACEDORES", "ESCUCHAR", "OIR", "PONER"], "respuestas_referencia": ["Dice que hay que ser hacedores de la Palabra y no solo oyentes.", "Que no basta con escuchar la Palabra, hay que practicarla.", "Pide poner en práctica lo que se escucha, no solo oírlo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta de Santiago en el índice de tu Biblia; el capítulo es el 1.",
               "Santiago compara al que solo escucha con alguien que se mira al espejo y luego se olvida."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Sed ______ de la palabra, y no solo oidores.", "respuesta": "HACEDORES",
         "banco": ["HACEDORES", "OIDORES", "OLVIDADORES"]},
        {"texto": "Escuchar la Palabra no basta: hay que ______ la en la vida.", "respuesta": "PRACTICAR",
         "banco": ["PRACTICAR", "OLVIDAR", "IGNORAR"]},
        {"texto": "María guardaba y ______ todas estas cosas en su corazón.", "respuesta": "MEDITABA",
         "banco": ["MEDITABA", "OLVIDABA", "IGNORABA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo contrario de «solo escuchar».",
               "La tercera respuesta describe pensar algo con calma."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Escuchar la Palabra de Dios es suficiente si nunca la ponemos en práctica.",
         "respuesta": False},
        {"texto": "Santiago pide que seamos hacedores de la Palabra, no solo oidores.", "respuesta": True},
        {"texto": "Meditar la Palabra es pensarla con calma.", "respuesta": True},
        {"texto": "No sirve de nada guardar la Palabra en el corazón.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Santiago 1,22-23: no basta con escuchar.",
               "Si una frase dice que da igual practicar la Palabra o no, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pide Santiago que seamos, además de oidores de la palabra?",
         "opciones": ["Jueces", "Hacedores", "Maestros"], "correcta": 1},
        {"texto": "¿Qué significa meditar la Palabra de Dios?",
         "opciones": ["Leerla rápido y olvidarla", "Pensarla con calma y dejar que hable a tu vida",
                      "No prestarle atención"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo contrario de «solo escuchar».",
               "Meditar no es lo mismo que leer deprisa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ESCUCHAR", "definicion": "Prestar atención a la Palabra"},
        {"termino": "MEDITAR", "definicion": "Pensarla con calma"},
        {"termino": "PRACTICAR", "definicion": "Ponerla en obras"},
        {"termino": "OIDORES", "definicion": "Solo escuchan"},
        {"termino": "HACEDORES", "definicion": "La ponen en práctica"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "OIDORES y HACEDORES son opuestos entre sí."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["ESCUCHAR", "MEDITAR", "PRACTICAR", "OLVIDAR", "IGNORAR", "HACEDORES"],
    "correctas": ["ESCUCHAR", "MEDITAR", "PRACTICAR", "HACEDORES"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Escuchar - Meditar - Practicar - Hacedores.",
               "Descarta las palabras que hablan de no prestar atención."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Sed ______ de la palabra, y no solo oidores.", "respuesta": "HACEDORES",
         "banco": ["HACEDORES", "OIDORES", "OLVIDADORES"]},
    ],
    "reflexion": "¿Qué parte de lo que aprendes en la catequesis podrías poner en práctica esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en lo contrario de «solo escuchar».",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: pongo en práctica la Palabra",
    "situacion": "Santiago nos pide ser hacedores de la Palabra, no solo oidores.",
    "items": [
        {"texto": "¿Qué puedes hacer para poner en práctica algo que escuchaste en la catequesis?",
         "opciones": ["Elegir una idea y aplicarla esta semana",
                      "Comentarla en casa con tu familia",
                      "Anotarla para no olvidarla",
                      "Escucharla y olvidarla enseguida"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que es igual a no hacer nada."],
    "feedback_ok": "¡Muy bien! Ser hacedor de la Palabra es vivirla, no solo escucharla.",
})

# ==========================================================================
# PC03-C06 — Compartir la Palabra en familia y comunidad
# ==========================================================================
C = "PC03-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: compartir la Palabra en familia",
    "items": [
        {"texto": "Lugar natural donde se comparte la fe y la Palabra.", "respuesta": "FAMILIA"},
        {"texto": "Dar a otros lo que uno ha recibido, como la Palabra de Dios.", "respuesta": "COMPARTIR"},
        {"texto": "Lo que se nos pide hacer con la Palabra: transmitirla a nuestros hijos.",
         "respuesta": "ENSEÑAR"},
        {"texto": "A quienes se les debe repetir las palabras de Dios, según Deuteronomio.",
         "respuesta": "HIJOS"},
        {"texto": "Donde deben estar las palabras de Dios, según Deuteronomio.", "respuesta": "CORAZON"},
        {"texto": "Volver a decir algo varias veces para que no se olvide.", "respuesta": "REPETIR"},
    ],
    "incluir": ["FAMILIA", "COMPARTIR"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Deuteronomio 6,6-7 pide repetir la Palabra de Dios a los hijos."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: compartir la Palabra en familia",
    "palabras": ["FAMILIA", "COMPARTIR", "ENSEÑAR", "HIJOS", "CORAZON", "REPETIR"],
    "incluir": ["FAMILIA", "ENSEÑAR"], "requisito": 5,
    "pistas": ["HIJOS es una de las palabras más cortas: búscala primero.",
               "COMPARTIR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Deuteronomio 6,6-7",
    "items": [
        {"texto": "Busca en tu Biblia Católica Deuteronomio 6,6-7 y completa: «Estas palabras que hoy "
                  "te mando estarán en tu corazón, y se las repetirás a tus ______.»", "respuesta": "HIJOS",
         "banco": ["HIJOS", "VECINOS", "ENEMIGOS"]},
        {"texto": "¿Qué se nos pide hacer con la Palabra de Dios en familia?", "abierta": True, "palabras_esperadas": ["COMPARTIR", "ENSENAR", "HIJOS", "REPETIR"], "respuestas_referencia": ["Se nos pide compartirla y enseñarla a nuestros hijos.", "Que la familia repita y enseñe la Palabra de Dios a los hijos.", "Compartir y transmitir la Palabra de Dios en casa."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro del Deuteronomio en el índice de tu Biblia; el capítulo es el 6.",
               "Moisés le explica al pueblo cómo transmitir la Palabra dentro de la familia."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Estas palabras estarán en tu ______.", "respuesta": "CORAZON",
         "banco": ["CORAZON", "BOLSILLO", "MOCHILA"]},
        {"texto": "Se las ______ a tus hijos.", "respuesta": "REPETIRAS",
         "banco": ["REPETIRAS", "ESCONDERAS", "OLVIDARAS"]},
        {"texto": "La Palabra de Dios se vive y se ______ en familia.", "respuesta": "COMPARTE",
         "banco": ["COMPARTE", "GUARDA", "ESCONDE"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en dónde deben estar las palabras de Dios, según Deuteronomio.",
               "La segunda respuesta es lo que se hace con los hijos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Deuteronomio pide guardar la Palabra de Dios en el corazón.", "respuesta": True},
        {"texto": "La Palabra de Dios solo se debe compartir en la iglesia.", "respuesta": False},
        {"texto": "Se nos pide repetir la Palabra de Dios a nuestros hijos.", "respuesta": True},
        {"texto": "Compartir la fe en familia no tiene ningún valor.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda Deuteronomio 6,6-7: las palabras estarán en el corazón y se repetirán a los hijos.",
               "Si una frase dice que compartir la fe en casa no sirve, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué se nos pide hacer con la Palabra de Dios en familia?",
         "opciones": ["Guardarla solo para uno mismo", "Repetirla y compartirla con los hijos",
                      "Olvidarla al salir de la iglesia"], "correcta": 1},
        {"texto": "¿Dónde deben estar las palabras de Dios, según Deuteronomio?",
         "opciones": ["En un libro cerrado", "En el corazón", "En ningún lugar en especial"],
         "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que se pide hacer con los hijos.",
               "Deuteronomio habla de un lugar interior, no de un objeto."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FAMILIA", "definicion": "Lugar donde se comparte la fe"},
        {"termino": "COMPARTIR", "definicion": "Dar a otros la Palabra"},
        {"termino": "ENSEÑAR", "definicion": "Transmitir la Palabra a los hijos"},
        {"termino": "CORAZON", "definicion": "Donde deben estar las palabras de Dios"},
        {"termino": "REPETIR", "definicion": "No dejar que se olviden"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "FAMILIA y COMPARTIR están relacionadas entre sí."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["FAMILIA", "COMPARTIR", "ENSEÑAR", "OLVIDAR", "ESCONDER", "CORAZON"],
    "correctas": ["FAMILIA", "COMPARTIR", "ENSEÑAR", "CORAZON"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Familia - Compartir - Enseñar - Corazón.",
               "Descarta las palabras que hablan de no transmitir la Palabra."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Se las ______ a tus hijos.", "respuesta": "REPETIRAS",
         "banco": ["REPETIRAS", "ESCONDERAS", "OLVIDARAS"]},
    ],
    "reflexion": "¿Con quién de tu familia podrías compartir algo que aprendiste en la catequesis?",
    "requisito": 1,
    "pistas": ["Piensa en lo que se pide hacer con los hijos.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: comparto la Palabra en casa",
    "situacion": "Dios nos pide guardar su Palabra en el corazón y compartirla en familia.",
    "items": [
        {"texto": "¿Qué puedes hacer esta semana para compartir la Palabra de Dios en tu familia?",
         "opciones": ["Contarles algo que aprendiste en la catequesis",
                      "Leer juntos un pasaje corto de la Biblia",
                      "Invitar a rezar juntos antes de dormir",
                      "Guardarlo todo solo para ti"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no comparte nada con nadie."],
    "feedback_ok": "¡Muy bien! La Palabra de Dios se vive mejor cuando se comparte en familia.",
})


# ==========================================================================
# PC04 — La familia de Jesús: la Iglesia   (Encuentro 4, Hechos 2,42-47)
# ==========================================================================
C = "PC04-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la primera comunidad cristiana",
    "items": [
        {"texto": "Grupo de personas que viven y creen juntas.", "respuesta": "COMUNIDAD"},
        {"texto": "Los enviados de Jesús que enseñaban a los primeros cristianos.", "respuesta": "APOSTOLES"},
        {"texto": "Hablar con Dios, algo que practicaban juntos los primeros cristianos.", "respuesta": "ORACION"},
        {"texto": "Lo partían juntos para recordar a Jesús.", "respuesta": "PAN"},
        {"texto": "Con qué compartían la comida, según los Hechos de los Apóstoles.", "respuesta": "ALEGRIA"},
        {"texto": "Cómo estaban los primeros cristianos entre sí.", "respuesta": "UNIDOS"},
    ],
    "incluir": ["COMUNIDAD", "APOSTOLES"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Hechos 2,42-47 cuenta cómo vivían unidos los primeros cristianos."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la primera comunidad cristiana",
    "palabras": ["COMUNIDAD", "APOSTOLES", "ORACION", "PAN", "ALEGRIA", "UNIDOS"],
    "incluir": ["COMUNIDAD", "APOSTOLES"], "requisito": 5,
    "pistas": ["PAN es una de las palabras más cortas: búscala primero.",
               "COMUNIDAD es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 2,42-47",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 2,42-47 y completa: «Perseveraban en la enseñanza "
                  "de los apóstoles, en la comunión, en la fracción del pan y en las ______.»",
         "respuesta": "ORACIONES", "banco": ["ORACIONES", "FIESTAS", "DISCUSIONES"]},
        {"texto": "¿En qué perseveraban los primeros cristianos?", "abierta": True, "palabras_esperadas": ["ORACION", "ENSENANZA", "PAN", "COMUNION", "APOSTOLES"], "respuestas_referencia": ["Perseveraban en la enseñanza de los apóstoles, la oración y partir el pan.", "En la oración, la comunión y la enseñanza de los apóstoles.", "Se mantenían fieles a la oración y a compartir el pan juntos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 2.",
               "Son cuatro cosas que hacían juntos: enseñanza, comunión, partir el pan y..."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "La primera comunidad cristiana se reunía para escuchar a los ______.",
         "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "EXTRAÑOS", "SOLDADOS"]},
        {"texto": "Los primeros cristianos compartían todo con ______.", "respuesta": "ALEGRIA",
         "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Vivían ______ como una gran familia.", "respuesta": "UNIDOS",
         "banco": ["UNIDOS", "SEPARADOS", "LEJOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quiénes enseñaban a la primera comunidad.",
               "La última respuesta describe cómo vivían entre ellos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los primeros cristianos se reunían para orar juntos.", "respuesta": True},
        {"texto": "Los primeros cristianos vivían cada uno por su cuenta, sin ayudarse.", "respuesta": False},
        {"texto": "Partían el pan juntos para recordar a Jesús.", "respuesta": True},
        {"texto": "A los primeros cristianos no les importaba compartir.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo describe el libro de los Hechos a la primera comunidad.",
               "Si una frase dice que no compartían o no se ayudaban, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hacían juntos los primeros cristianos?",
         "opciones": ["Vivían separados y sin comunicarse", "Se reunían para orar, compartir y partir el pan",
                      "Solo se veían una vez al año"], "correcta": 1},
        {"texto": "¿Quiénes enseñaban a la primera comunidad cristiana?",
         "opciones": ["Los apóstoles", "Los soldados romanos", "Nadie, cada uno aprendía solo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en las cuatro cosas que hacían juntos.",
               "Son los discípulos que Jesús envió a anunciar la Buena Noticia."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "COMUNIDAD", "definicion": "Grupo unido de creyentes"},
        {"termino": "APOSTOLES", "definicion": "Enseñaban a los primeros cristianos"},
        {"termino": "ORACION", "definicion": "Hablar con Dios en comunidad"},
        {"termino": "PAN", "definicion": "Se partía para recordar a Jesús"},
        {"termino": "ALEGRIA", "definicion": "Con qué compartían lo que tenían"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "COMUNIDAD se relaciona con la idea de un grupo unido."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["COMUNIDAD", "APOSTOLES", "ORACION", "PAN", "EGOISMO", "INDIFERENCIA"],
    "correctas": ["COMUNIDAD", "APOSTOLES", "ORACION", "PAN"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Comunidad - Apóstoles - Oración - Pan.",
               "Descarta las palabras que hablan de estar separados o no importarle el otro."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La primera comunidad cristiana se reunía para escuchar a los ______.",
         "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "EXTRAÑOS", "SOLDADOS"]},
    ],
    "reflexion": "¿Qué te gustaría vivir tú de la primera comunidad cristiana?",
    "requisito": 1,
    "pistas": ["Piensa en quiénes enseñaban a la primera comunidad.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo en comunidad",
    "situacion": "Ya sabes cómo vivían unidos los primeros cristianos: orando, compartiendo y partiendo "
                 "el pan juntos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para vivir como la primera comunidad cristiana?",
         "opciones": ["Compartir algo tuyo con un compañero", "Rezar en familia antes de comer",
                      "Participar en la misa de tu parroquia", "Guardar todo solo para ti"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no tiene que ver con compartir o unirse."],
    "feedback_ok": "¡Muy bien! Vivir en comunidad es vivir como los primeros cristianos.",
})

# ==========================================================================
# PC04-C02 — Los cristianos viven como hermanos
# ==========================================================================
C = "PC04-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: los cristianos viven como hermanos",
    "items": [
        {"texto": "Así se llamaban entre sí los primeros cristianos.", "respuesta": "HERMANOS"},
        {"texto": "El grupo al que pertenecemos por el Bautismo, según san Pablo.", "respuesta": "FAMILIA"},
        {"texto": "Lo que sentían los cristianos al estar juntos.", "respuesta": "UNION"},
        {"texto": "El sentimiento que los unía como hermanos.", "respuesta": "AMOR"},
        {"texto": "La comunidad de los que creen en Jesús.", "respuesta": "IGLESIA"},
        {"texto": "Compartir la vida y la fe con los demás.", "respuesta": "COMUNION"},
    ],
    "incluir": ["HERMANOS", "FAMILIA"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Efesios 2,19 explica a qué pertenecemos los que creemos en Jesús."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: los cristianos viven como hermanos",
    "palabras": ["HERMANOS", "FAMILIA", "UNION", "AMOR", "IGLESIA", "COMUNION"],
    "incluir": ["HERMANOS", "FAMILIA"], "requisito": 5,
    "pistas": ["AMOR es una de las palabras más cortas: búscala primero.",
               "HERMANOS es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Efesios 2,19",
    "items": [
        {"texto": "Busca en tu Biblia Católica Efesios 2,19 y completa: «Ya no sois extraños ni "
                  "forasteros, sino... miembros de la ______ de Dios.»", "respuesta": "FAMILIA",
         "banco": ["FAMILIA", "CIUDAD", "ESCUELA"]},
        {"texto": "¿Cómo describe san Pablo la pertenencia a la comunidad cristiana?", "abierta": True, "palabras_esperadas": ["FAMILIA", "HERMANOS", "MIEMBROS", "DIOS", "CIUDADANOS"], "respuestas_referencia": ["Dice que somos miembros de una misma familia, hermanos entre nosotros.", "Nos describe como una familia, como hermanos en Dios.", "Como parte de la familia de Dios, todos hermanos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Efesios en el índice de tu Biblia; el capítulo es el 2.",
               "San Pablo dice que ya no somos extraños, sino parte de algo más cercano."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los cristianos se llamaban ______ entre sí.", "respuesta": "HERMANOS",
         "banco": ["HERMANOS", "EXTRAÑOS", "RIVALES"]},
        {"texto": "Por el Bautismo formamos parte de la ______ de Dios.", "respuesta": "FAMILIA",
         "banco": ["FAMILIA", "OFICINA", "EMPRESA"]},
        {"texto": "El ______ es lo que une a los hermanos en la fe.", "respuesta": "AMOR",
         "banco": ["AMOR", "MIEDO", "ORGULLO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se trataban los primeros cristianos entre ellos.",
               "La última respuesta es el sentimiento que más los unía."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los primeros cristianos se llamaban hermanos entre sí.", "respuesta": True},
        {"texto": "Ser parte de la Iglesia es estar solo, sin nadie más.", "respuesta": False},
        {"texto": "El amor une a los cristianos como una familia.", "respuesta": True},
        {"texto": "A los cristianos no les importa tratarse como hermanos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo se llamaban entre sí los primeros cristianos.",
               "Si una frase dice que estar en la Iglesia es estar solo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo se llamaban entre sí los primeros cristianos?",
         "opciones": ["Hermanos", "Desconocidos", "Rivales"], "correcta": 0},
        {"texto": "¿Qué dice san Pablo que somos, por el Bautismo?",
         "opciones": ["Extraños", "Miembros de la familia de Dios", "Visitantes de paso"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se trataban los primeros cristianos.",
               "San Pablo habla de pertenecer a algo mucho más cercano que ser extraño."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "HERMANOS", "definicion": "Cómo se llamaban entre sí los primeros cristianos"},
        {"termino": "FAMILIA", "definicion": "Lo que formamos por el Bautismo, según san Pablo"},
        {"termino": "UNION", "definicion": "Lo que sentían los cristianos al estar juntos"},
        {"termino": "AMOR", "definicion": "Lo que unía a los hermanos en la fe"},
        {"termino": "IGLESIA", "definicion": "La comunidad de los que creen en Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "HERMANOS se relaciona con la forma en que se trataban entre ellos."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["HERMANOS", "FAMILIA", "AMOR", "UNION", "EXTRAÑOS", "RIVALIDAD"],
    "correctas": ["HERMANOS", "FAMILIA", "AMOR", "UNION"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Hermanos - Familia - Amor - Unión.",
               "Descarta las palabras que hablan de estar separados o de pelear."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los cristianos se llamaban ______ entre sí.", "respuesta": "HERMANOS",
         "banco": ["HERMANOS", "EXTRAÑOS", "RIVALES"]},
    ],
    "reflexion": "¿A quién puedes tratar como hermano esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en cómo se trataban los primeros cristianos entre ellos.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: trato a otros como hermanos",
    "situacion": "Ya sabes que los cristianos se llaman hermanos porque forman una sola familia en la fe.",
    "items": [
        {"texto": "¿Qué puedes hacer para tratar a otros como hermanos?",
         "opciones": ["Compartir con un compañero que lo necesite", "Perdonar cuando alguien te ofende",
                      "Saludar con cariño a quienes ves en la parroquia", "Ignorar a quien no conoces"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no tiene que ver con acercarse a otros."],
    "feedback_ok": "¡Muy bien! Tratar a otros como hermanos es vivir el amor de Jesús.",
})

# ==========================================================================
# PC04-C03 — Compartir es parte de la comunidad
# ==========================================================================
C = "PC04-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: compartir es parte de la comunidad",
    "items": [
        {"texto": "Dar a otros parte de lo que tenemos.", "respuesta": "COMPARTIR"},
        {"texto": "Lo que tienen quienes carecen de algo importante.", "respuesta": "NECESIDAD"},
        {"texto": "Lo que ofrecemos a quien lo necesita.", "respuesta": "AYUDA"},
        {"texto": "Actitud de dar sin esperar nada a cambio.", "respuesta": "GENEROSIDAD"},
        {"texto": "Recibir bien a quien llega, según pide san Pablo.", "respuesta": "HOSPITALIDAD"},
        {"texto": "Unirse para apoyar a los demás en sus dificultades.", "respuesta": "SOLIDARIDAD"},
    ],
    "incluir": ["COMPARTIR", "AYUDA"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Romanos 12,13 pide compartir con quienes tienen necesidad."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: compartir es parte de la comunidad",
    "palabras": ["COMPARTIR", "NECESIDAD", "AYUDA", "GENEROSIDAD", "HOSPITALIDAD", "SOLIDARIDAD"],
    "incluir": ["COMPARTIR", "AYUDA"], "requisito": 5,
    "pistas": ["AYUDA es la palabra más corta: búscala primero.",
               "GENEROSIDAD, HOSPITALIDAD y SOLIDARIDAD son las palabras más largas."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Romanos 12,13",
    "items": [
        {"texto": "Busca en tu Biblia Católica Romanos 12,13 y completa: «Compartid las necesidades de "
                  "los santos; practicad la ______.»", "respuesta": "HOSPITALIDAD",
         "banco": ["HOSPITALIDAD", "INDIFERENCIA", "DISTANCIA"]},
        {"texto": "¿Qué actitud pide san Pablo hacia quienes tienen necesidad?", "abierta": True, "palabras_esperadas": ["COMPARTIR", "AYUDAR", "HOSPITALIDAD", "GENEROSIDAD"], "respuestas_referencia": ["Pide compartir con generosidad y practicar la hospitalidad.", "Que ayudemos a quienes tienen necesidad, con generosidad.", "Ser hospitalarios y compartir lo que tenemos con los demás."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Romanos en el índice de tu Biblia; el capítulo es el 12.",
               "San Pablo pide dos cosas: compartir y ser hospitalarios."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo nos pide compartir las ______ de los demás.", "respuesta": "NECESIDADES",
         "banco": ["NECESIDADES", "FIESTAS", "VACACIONES"]},
        {"texto": "Practicar la hospitalidad es recibir bien a quien ______.", "respuesta": "LLEGA",
         "banco": ["LLEGA", "MOLESTA", "SOBRA"]},
        {"texto": "La ______ es dar sin esperar nada a cambio.", "respuesta": "GENEROSIDAD",
         "banco": ["GENEROSIDAD", "AVARICIA", "ENVIDIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que san Pablo pide compartir con los demás.",
               "La segunda respuesta describe cómo recibimos a quien llega."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo nos pide compartir con quienes tienen necesidad.", "respuesta": True},
        {"texto": "Ser generoso significa guardarlo todo para uno mismo.", "respuesta": False},
        {"texto": "La hospitalidad es recibir bien a los demás.", "respuesta": True},
        {"texto": "Compartir no tiene nada que ver con ser cristiano.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que san Pablo pide en Romanos 12,13.",
               "Si una frase dice que hay que guardarlo todo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué nos pide san Pablo en Romanos 12,13?",
         "opciones": ["Compartir con quienes tienen necesidad", "Guardar todo para nosotros",
                      "Evitar a los demás"], "correcta": 0},
        {"texto": "¿Qué es la hospitalidad?",
         "opciones": ["Rechazar a los extraños", "Recibir bien a quien llega",
                      "No abrir la puerta a nadie"], "correcta": 1},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que san Pablo pide compartir con los demás.",
               "Es lo contrario de rechazar o ignorar a quien llega."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "COMPARTIR", "definicion": "Dar a otros parte de lo que tenemos"},
        {"termino": "NECESIDAD", "definicion": "Lo que tiene quien carece de algo"},
        {"termino": "AYUDA", "definicion": "Lo que ofrecemos a quien lo necesita"},
        {"termino": "GENEROSIDAD", "definicion": "Dar sin esperar nada a cambio"},
        {"termino": "HOSPITALIDAD", "definicion": "Recibir bien a quien llega"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "COMPARTIR se relaciona con dar parte de lo que tenemos."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["COMPARTIR", "AYUDA", "GENEROSIDAD", "HOSPITALIDAD", "EGOISMO", "INDIFERENCIA"],
    "correctas": ["COMPARTIR", "AYUDA", "GENEROSIDAD", "HOSPITALIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Compartir - Ayuda - Generosidad - Hospitalidad.",
               "Descarta las palabras que hablan de no importarle el otro."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo nos pide compartir las ______ de los demás.", "respuesta": "NECESIDADES",
         "banco": ["NECESIDADES", "FIESTAS", "VACACIONES"]},
    ],
    "reflexion": "¿Con quién puedes compartir algo esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en lo que san Pablo pide compartir con los demás.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: comparto con los demás",
    "situacion": "Ya sabes que compartir y ayudar a quien tiene necesidad es parte de vivir en comunidad.",
    "items": [
        {"texto": "¿Qué puedes hacer tú para compartir con los demás?",
         "opciones": ["Prestar algo tuyo a un compañero", "Ayudar en casa sin que te lo pidan",
                      "Invitar a jugar a quien está solo", "Quedarte con todo para ti"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no tiene que ver con compartir."],
    "feedback_ok": "¡Muy bien! Compartir es una forma concreta de amar como Jesús.",
})

# ==========================================================================
# PC04-C04 — La Iglesia es familia
# ==========================================================================
C = "PC04-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Iglesia es familia",
    "items": [
        {"texto": "La comunidad de los que creen en Jesús, llamada casa de Dios.", "respuesta": "IGLESIA"},
        {"texto": "El grupo al que pertenecemos por ser hijos de Dios.", "respuesta": "FAMILIA"},
        {"texto": "Así llama san Pablo a la Iglesia.", "respuesta": "CASA"},
        {"texto": "Lo que somos todos los bautizados, ante Dios.", "respuesta": "HIJOS"},
        {"texto": "Cómo nos tratamos los que formamos la Iglesia.", "respuesta": "HERMANOS"},
        {"texto": "El Padre de toda la familia de la Iglesia.", "respuesta": "DIOS"},
    ],
    "incluir": ["IGLESIA", "FAMILIA"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "1 Timoteo 3,15 dice cómo hay que portarse en la casa de Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Iglesia es familia",
    "palabras": ["IGLESIA", "FAMILIA", "CASA", "HIJOS", "HERMANOS", "DIOS"],
    "incluir": ["IGLESIA", "FAMILIA"], "requisito": 5,
    "pistas": ["DIOS y CASA son de las palabras más cortas: búscalas primero.",
               "HERMANOS es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Timoteo 3,15",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Timoteo 3,15 y completa: «...cómo hay que portarse en "
                  "la ______ de Dios, que es la Iglesia del Dios vivo.»", "respuesta": "CASA",
         "banco": ["CASA", "PLAZA", "ESCUELA"]},
        {"texto": "¿Cómo llama san Pablo a la Iglesia?", "abierta": True, "palabras_esperadas": ["CASA", "FAMILIA", "VIVO", "VERDAD", "COLUMNA", "SOSTEN"], "respuestas_referencia": ["La llama la casa y familia de Dios, columna y sostén de la verdad.", "La llama la Iglesia del Dios vivo.", "Dice que es la casa de Dios, columna de la verdad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a Timoteo en el índice de tu Biblia; el capítulo es el 3.",
               "San Pablo compara a la Iglesia con el lugar donde vive una familia."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo llama a la Iglesia la ______ de Dios.", "respuesta": "CASA",
         "banco": ["CASA", "TIENDA", "OFICINA"]},
        {"texto": "En la Iglesia todos somos ______ de Dios.", "respuesta": "HIJOS",
         "banco": ["HIJOS", "EXTRAÑOS", "VISITANTES"]},
        {"texto": "En la Iglesia nos tratamos como ______.", "respuesta": "HERMANOS",
         "banco": ["HERMANOS", "RIVALES", "DESCONOCIDOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama san Pablo a la Iglesia.",
               "La última respuesta describe cómo nos tratamos dentro de ella."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo llama a la Iglesia la casa de Dios.", "respuesta": True},
        {"texto": "En la Iglesia cada uno vive sin relacionarse con los demás.", "respuesta": False},
        {"texto": "Todos los bautizados somos hijos de Dios.", "respuesta": True},
        {"texto": "La Iglesia no tiene nada que ver con ser familia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo llama san Pablo a la Iglesia.",
               "Si una frase dice que la Iglesia no es familia, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo describe san Pablo a la Iglesia?",
         "opciones": ["Como una casa de Dios, una familia", "Como un edificio vacío",
                      "Como un lugar solo para adultos"], "correcta": 0},
        {"texto": "¿Qué somos todos los bautizados, según este tema?",
         "opciones": ["Hijos de Dios", "Extraños entre nosotros", "Visitantes de paso"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama san Pablo a la Iglesia.",
               "Es la misma respuesta que usaste en la actividad de completar."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "IGLESIA", "definicion": "Comunidad de los que creen en Jesús"},
        {"termino": "FAMILIA", "definicion": "Grupo al que pertenecemos por el Bautismo"},
        {"termino": "CASA", "definicion": "Así llama san Pablo a la Iglesia"},
        {"termino": "HIJOS", "definicion": "Lo que somos ante Dios los bautizados"},
        {"termino": "HERMANOS", "definicion": "Cómo nos tratamos en la Iglesia"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "CASA se relaciona con cómo llama san Pablo a la Iglesia."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["IGLESIA", "FAMILIA", "CASA", "HIJOS", "SOLEDAD", "DISTANCIA"],
    "correctas": ["IGLESIA", "FAMILIA", "CASA", "HIJOS"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Iglesia - Familia - Casa - Hijos.",
               "Descarta las palabras que hablan de estar lejos o solos."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo llama a la Iglesia la ______ de Dios.", "respuesta": "CASA",
         "banco": ["CASA", "TIENDA", "OFICINA"]},
    ],
    "reflexion": "¿Qué significa para ti que la Iglesia sea tu familia?",
    "requisito": 1,
    "pistas": ["Piensa en cómo llama san Pablo a la Iglesia.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: la Iglesia, mi familia",
    "situacion": "Ya sabes que la Iglesia es la casa y familia de Dios, donde todos somos hermanos.",
    "items": [
        {"texto": "¿Qué puedes hacer para sentir la Iglesia como tu familia?",
         "opciones": ["Participar en la misa con tu comunidad", "Saludar y conocer a otros niños de la parroquia",
                      "Cuidar el espacio de tu iglesia", "Ir solo cuando te obligan y sin participar"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra interés por participar."],
    "feedback_ok": "¡Muy bien! Vivir la Iglesia como familia es reconocerte hijo de Dios.",
})

# ==========================================================================
# PC04-C05 — Pertenecer a la comunidad
# ==========================================================================
C = "PC04-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: pertenecer a la comunidad",
    "items": [
        {"texto": "Así llama san Pablo a la Iglesia entera.", "respuesta": "CUERPO"},
        {"texto": "Cada persona es una parte de este cuerpo.", "respuesta": "MIEMBRO"},
        {"texto": "La cabeza del cuerpo que es la Iglesia.", "respuesta": "CRISTO"},
        {"texto": "Lo que se vive cuando todos los miembros están unidos.", "respuesta": "UNIDAD"},
        {"texto": "Sentirse parte de algo más grande que uno mismo.", "respuesta": "PERTENECER"},
        {"texto": "El grupo de creyentes al que pertenecemos.", "respuesta": "COMUNIDAD"},
    ],
    "incluir": ["CUERPO", "MIEMBRO"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "1 Corintios 12,27 compara a la Iglesia con un cuerpo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: pertenecer a la comunidad",
    "palabras": ["CUERPO", "MIEMBRO", "CRISTO", "UNIDAD", "PERTENECER", "COMUNIDAD"],
    "incluir": ["CUERPO", "MIEMBRO"], "requisito": 5,
    "pistas": ["CUERPO es una de las palabras más cortas: búscala primero.",
               "PERTENECER y COMUNIDAD son las palabras más largas."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 12,27",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 12,27 y completa: «Vosotros sois el ______ de "
                  "Cristo, y miembros cada uno en particular.»", "respuesta": "CUERPO",
         "banco": ["CUERPO", "NOMBRE", "REINO"]},
        {"texto": "¿Qué somos cada uno dentro del cuerpo de Cristo?", "abierta": True, "palabras_esperadas": ["MIEMBRO", "PARTE", "CUERPO"], "respuestas_referencia": ["Somos miembros, cada uno una parte del cuerpo de Cristo.", "Cada uno es un miembro distinto pero parte del mismo cuerpo.", "Formamos parte del cuerpo de Cristo, cada uno con su función."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a los Corintios en el índice de tu Biblia; el capítulo es el 12.",
               "San Pablo compara a la Iglesia con un cuerpo humano."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un ______.", "respuesta": "CUERPO",
         "banco": ["CUERPO", "EDIFICIO", "JARDIN"]},
        {"texto": "Cada persona es un ______ de ese cuerpo.", "respuesta": "MIEMBRO",
         "banco": ["MIEMBRO", "EXTRAÑO", "VISITANTE"]},
        {"texto": "Todos los miembros forman parte de una sola ______.", "respuesta": "COMUNIDAD",
         "banco": ["COMUNIDAD", "ISLA", "EMPRESA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con qué compara san Pablo a la Iglesia.",
               "La segunda respuesta es lo que somos cada uno dentro de ese cuerpo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un cuerpo.", "respuesta": True},
        {"texto": "Cada miembro del cuerpo no tiene ninguna importancia.", "respuesta": False},
        {"texto": "Todos pertenecemos a la misma comunidad de fe.", "respuesta": True},
        {"texto": "Pertenecer a la comunidad significa estar solo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda con qué compara san Pablo a la Iglesia.",
               "Si una frase dice que un miembro no importa, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con qué compara san Pablo a la Iglesia?",
         "opciones": ["Con un cuerpo, donde cada uno es un miembro", "Con un edificio vacío",
                      "Con una isla sin gente"], "correcta": 0},
        {"texto": "¿Qué significa pertenecer a la comunidad?",
         "opciones": ["Sentirse parte de algo más grande", "Vivir sin relacionarse con nadie",
                      "No importarle la Iglesia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con qué compara san Pablo a la Iglesia.",
               "Es lo contrario de vivir aislado."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CUERPO", "definicion": "Así llama san Pablo a la Iglesia entera"},
        {"termino": "MIEMBRO", "definicion": "Cada persona es una parte de ese cuerpo"},
        {"termino": "CRISTO", "definicion": "La cabeza del cuerpo que es la Iglesia"},
        {"termino": "UNIDAD", "definicion": "Lo que se vive cuando todos están unidos"},
        {"termino": "COMUNIDAD", "definicion": "El grupo de creyentes al que pertenecemos"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "CUERPO se relaciona con la comparación que hace san Pablo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["CUERPO", "MIEMBRO", "UNIDAD", "COMUNIDAD", "SOLEDAD", "DIVISION"],
    "correctas": ["CUERPO", "MIEMBRO", "UNIDAD", "COMUNIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Cuerpo - Miembro - Unidad - Comunidad.",
               "Descarta las palabras que hablan de estar separados."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un ______.", "respuesta": "CUERPO",
         "banco": ["CUERPO", "EDIFICIO", "JARDIN"]},
    ],
    "reflexion": "¿Cómo puedes cuidar tu lugar dentro de la comunidad?",
    "requisito": 1,
    "pistas": ["Piensa en con qué compara san Pablo a la Iglesia.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: mi lugar en la comunidad",
    "situacion": "Ya sabes que la Iglesia es como un cuerpo, y tú eres un miembro importante de él.",
    "items": [
        {"texto": "¿Qué puedes hacer para vivir tu lugar en la comunidad?",
         "opciones": ["Participar activamente en tu parroquia", "Colaborar con tus catequistas y compañeros",
                      "Sentirte importante dentro del grupo", "Alejarte porque crees que no importas"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que te aleja del grupo."],
    "feedback_ok": "¡Muy bien! Cada miembro es necesario para el cuerpo de la Iglesia.",
})

# ==========================================================================
# PC04-C06 — Construir fraternidad
# ==========================================================================
C = "PC04-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: construir fraternidad",
    "items": [
        {"texto": "Vivir como hermanos, cuidándose y ayudándose.", "respuesta": "FRATERNIDAD"},
        {"texto": "El vínculo que une a la comunidad, según san Pablo.", "respuesta": "AMOR"},
        {"texto": "Lo contrario de estar divididos.", "respuesta": "UNION"},
        {"texto": "Tratar bien a los demás, valorando su dignidad.", "respuesta": "RESPETO"},
        {"texto": "Lo que se vive cuando reina la fraternidad.", "respuesta": "PAZ"},
        {"texto": "Otro nombre para vivir como hermanos.", "respuesta": "HERMANDAD"},
    ],
    "incluir": ["FRATERNIDAD", "AMOR"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Colosenses 3,14 dice cuál es el vínculo de la unidad perfecta."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: construir fraternidad",
    "palabras": ["FRATERNIDAD", "AMOR", "UNION", "RESPETO", "PAZ", "HERMANDAD"],
    "incluir": ["FRATERNIDAD", "AMOR"], "requisito": 5,
    "pistas": ["PAZ y AMOR son las palabras más cortas: búscalas primero.",
               "FRATERNIDAD es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Colosenses 3,14",
    "items": [
        {"texto": "Busca en tu Biblia Católica Colosenses 3,14 y completa: «Y por encima de todo esto, "
                  "vestíos de ______, que es el vínculo de la unidad perfecta.»", "respuesta": "AMOR",
         "banco": ["AMOR", "ORGULLO", "ENVIDIA"]},
        {"texto": "¿Qué virtud une a la comunidad, según san Pablo?", "abierta": True, "palabras_esperadas": ["AMOR", "CARIDAD", "VINCULO", "UNIDAD"], "respuestas_referencia": ["El amor es lo que une a la comunidad.", "La caridad, el vínculo que nos mantiene unidos.", "El amor y la unidad entre todos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Colosenses en el índice de tu Biblia; el capítulo es el 3.",
               "Es la misma virtud que Jesús nos manda vivir con los demás."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo dice que el ______ es el vínculo que une a la comunidad.", "respuesta": "AMOR",
         "banco": ["AMOR", "MIEDO", "ORGULLO"]},
        {"texto": "Construir fraternidad es tratar a otros con ______.", "respuesta": "RESPETO",
         "banco": ["RESPETO", "DESPRECIO", "INDIFERENCIA"]},
        {"texto": "Donde hay fraternidad, también hay ______.", "respuesta": "PAZ",
         "banco": ["PAZ", "PELEA", "RIVALIDAD"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la virtud que, según san Pablo, une a la comunidad.",
               "La última respuesta es lo que se vive cuando hay fraternidad."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El amor es lo que une a la comunidad cristiana.", "respuesta": True},
        {"texto": "Construir fraternidad significa pelear con los demás.", "respuesta": False},
        {"texto": "El respeto ayuda a vivir en paz con los demás.", "respuesta": True},
        {"texto": "La fraternidad no tiene nada que ver con ser cristiano.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cuál es la virtud que, según san Pablo, une a la comunidad.",
               "Si una frase dice que hay que pelear, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué virtud, según san Pablo, une a la comunidad?",
         "opciones": ["El amor", "La envidia", "El orgullo"], "correcta": 0},
        {"texto": "¿Qué significa construir fraternidad?",
         "opciones": ["Vivir como hermanos, con respeto y amor", "Alejarse de los demás",
                      "Competir para ser el mejor"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la virtud que, según san Pablo, une a la comunidad.",
               "Es lo contrario de alejarse o competir con otros."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FRATERNIDAD", "definicion": "Vivir como hermanos, cuidándose y ayudándose"},
        {"termino": "AMOR", "definicion": "El vínculo que une a la comunidad"},
        {"termino": "RESPETO", "definicion": "Tratar bien a los demás"},
        {"termino": "PAZ", "definicion": "Lo que se vive cuando hay fraternidad"},
        {"termino": "HERMANDAD", "definicion": "Otro nombre para vivir como hermanos"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "AMOR se relaciona con el vínculo que une a la comunidad."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["FRATERNIDAD", "AMOR", "RESPETO", "PAZ", "EGOISMO", "RIVALIDAD"],
    "correctas": ["FRATERNIDAD", "AMOR", "RESPETO", "PAZ"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Fraternidad - Amor - Respeto - Paz.",
               "Descarta las palabras que hablan de pelear o competir."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo dice que el ______ es el vínculo que une a la comunidad.", "respuesta": "AMOR",
         "banco": ["AMOR", "MIEDO", "ORGULLO"]},
    ],
    "reflexion": "¿Qué puedes hacer para construir fraternidad en tu grupo?",
    "requisito": 1,
    "pistas": ["Piensa en la virtud que, según san Pablo, une a la comunidad.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: construyo fraternidad",
    "situacion": "Ya sabes que el amor es el vínculo que construye fraternidad entre los hermanos en la fe.",
    "items": [
        {"texto": "¿Qué puedes hacer tú para construir fraternidad?",
         "opciones": ["Tratar con respeto a tus compañeros", "Ayudar a resolver un conflicto con paz",
                      "Incluir a quien se siente solo", "Burlarte de quien piensa distinto"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que aleja o hiere a otros."],
    "feedback_ok": "¡Muy bien! La fraternidad se construye con amor, día a día.",
})

# ==========================================================================
# PC05 — El Bautismo: somos hijos de Dios   (Encuentro 5, Mateo 28,18-20 / Juan 3,5)
# ==========================================================================
C = "PC05-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús manda bautizar",
    "items": [
        {"texto": "El sacramento que Jesús mandó dar a todas las naciones.", "respuesta": "BAUTISMO"},
        {"texto": "A quienes Jesús envió a bautizar.", "respuesta": "DISCIPULOS"},
        {"texto": "La tarea que Jesús encargó a sus discípulos.", "respuesta": "MISION"},
        {"texto": "Primera persona de la Trinidad, nombrada en el Bautismo.", "respuesta": "PADRE"},
        {"texto": "Segunda persona de la Trinidad, nombrada en el Bautismo.", "respuesta": "HIJO"},
        {"texto": "Tercera persona de la Trinidad, nombrada en el Bautismo.", "respuesta": "ESPIRITU"},
    ],
    "incluir": ["BAUTISMO", "DISCIPULOS"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Mateo 28,18-20 cuenta el último mandato de Jesús antes de subir al cielo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús manda bautizar",
    "palabras": ["BAUTISMO", "DISCIPULOS", "MISION", "PADRE", "HIJO", "ESPIRITU"],
    "incluir": ["BAUTISMO", "DISCIPULOS"], "requisito": 5,
    "pistas": ["HIJO y PADRE son de las palabras más cortas: búscalas primero.",
               "DISCIPULOS es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 28,18-20",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 28,18-20 y completa: «Id, y haced ______ a todas "
                  "las naciones, bautizándolas en el nombre del Padre, del Hijo y del Espíritu Santo.»",
         "respuesta": "DISCIPULOS", "banco": ["DISCIPULOS", "SOLDADOS", "REYES"]},
        {"texto": "¿Qué mandó Jesús a sus discípulos antes de subir al cielo?", "abierta": True, "palabras_esperadas": ["BAUTIZAR", "DISCIPULOS", "NACIONES", "ENSENAR"], "respuestas_referencia": ["Les mandó ir y bautizar a todas las naciones.", "Que fueran a enseñar y bautizar a todos los pueblos.", "Los envió a predicar y bautizar en el nombre del Padre, el Hijo y el Espíritu Santo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 28.",
               "Es el último mandato de Jesús antes de subir al cielo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús mandó bautizar a todas las ______.", "respuesta": "NACIONES",
         "banco": ["NACIONES", "CASAS", "FAMILIAS"]},
        {"texto": "El Bautismo se da en el nombre del Padre, del Hijo y del ______.", "respuesta": "ESPIRITU",
         "banco": ["ESPIRITU", "CIELO", "MUNDO"]},
        {"texto": "Jesús envió a sus discípulos en una ______.", "respuesta": "MISION",
         "banco": ["MISION", "FIESTA", "VACACION"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a quiénes mandó bautizar Jesús.",
               "El Bautismo se da en el nombre de las tres personas de la Trinidad."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús mandó a sus discípulos bautizar a todas las naciones.", "respuesta": True},
        {"texto": "El Bautismo no tiene relación con la Santísima Trinidad.", "respuesta": False},
        {"texto": "Jesús encargó a sus discípulos una misión antes de subir al cielo.", "respuesta": True},
        {"texto": "A Jesús no le importaba que sus discípulos bautizaran.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda el mandato final de Jesús en Mateo 28.",
               "Si una frase dice que a Jesús no le importaba, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué mandó Jesús a sus discípulos?",
         "opciones": ["Bautizar a todas las naciones", "Quedarse encerrados sin hacer nada",
                      "Olvidar lo que él les enseñó"], "correcta": 0},
        {"texto": "¿En el nombre de quiénes se bautiza?",
         "opciones": ["Del Padre, del Hijo y del Espíritu Santo", "Solo del Padre",
                      "De los apóstoles"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el mandato final de Jesús a sus discípulos.",
               "Son las tres personas de la Santísima Trinidad."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "BAUTISMO", "definicion": "Sacramento que Jesús mandó dar a todas las naciones"},
        {"termino": "DISCIPULOS", "definicion": "A quienes Jesús envió a bautizar"},
        {"termino": "MISION", "definicion": "La tarea que Jesús encargó antes de subir al cielo"},
        {"termino": "PADRE", "definicion": "Primera persona de la Trinidad"},
        {"termino": "ESPIRITU", "definicion": "Tercera persona de la Trinidad"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "BAUTISMO se relaciona con lo que Jesús mandó dar a todas las naciones."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["BAUTISMO", "DISCIPULOS", "MISION", "TRINIDAD", "OLVIDO", "INDIFERENCIA"],
    "correctas": ["BAUTISMO", "DISCIPULOS", "MISION", "TRINIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Bautismo - Discípulos - Misión - Trinidad.",
               "Descarta las palabras que hablan de olvidar o no importar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Bautismo se da en el nombre del Padre, del Hijo y del ______.", "respuesta": "ESPIRITU",
         "banco": ["ESPIRITU", "CIELO", "MUNDO"]},
    ],
    "reflexion": "¿Qué sabes de tu propio Bautismo?",
    "requisito": 1,
    "pistas": ["Piensa en las tres personas de la Trinidad.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: valoro mi Bautismo",
    "situacion": "Ya sabes que Jesús mandó a sus discípulos bautizar en el nombre del Padre, del Hijo y "
                 "del Espíritu Santo.",
    "items": [
        {"texto": "¿Qué puedes hacer para valorar tu Bautismo?",
         "opciones": ["Preguntar a tus padres cuándo fuiste bautizado", "Dar gracias a Dios por ser su hijo",
                      "Vivir como cristiano cada día", "Pensar que el Bautismo no tiene importancia"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que resta importancia al Bautismo."],
    "feedback_ok": "¡Muy bien! El Bautismo es el comienzo de tu vida como hijo de Dios.",
})

# ==========================================================================
# PC05-C02 — Bautismo en el nombre de la Trinidad
# ==========================================================================
C = "PC05-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Bautismo en el nombre de la Trinidad",
    "items": [
        {"texto": "Padre, Hijo y Espíritu Santo: un solo Dios en tres personas.", "respuesta": "TRINIDAD"},
        {"texto": "Primera persona de la Santísima Trinidad.", "respuesta": "PADRE"},
        {"texto": "Segunda persona de la Santísima Trinidad, Jesucristo.", "respuesta": "HIJO"},
        {"texto": "Tercera persona de la Santísima Trinidad.", "respuesta": "ESPIRITU"},
        {"texto": "Forma en que bajó el Espíritu Santo sobre Jesús.", "respuesta": "PALOMA"},
        {"texto": "Se abrió cuando Jesús fue bautizado.", "respuesta": "CIELO"},
    ],
    "incluir": ["TRINIDAD", "ESPIRITU"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Mateo 3,16-17 cuenta lo que sucedió cuando Jesús fue bautizado."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Bautismo en el nombre de la Trinidad",
    "palabras": ["TRINIDAD", "PADRE", "HIJO", "ESPIRITU", "PALOMA", "CIELO"],
    "incluir": ["TRINIDAD", "ESPIRITU"], "requisito": 5,
    "pistas": ["HIJO es la palabra más corta: búscala primero.",
               "TRINIDAD y ESPIRITU son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 3,16-17",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 3,16-17 y completa: «...vio al Espíritu de Dios que "
                  "bajaba como ______ y venía sobre él.»", "respuesta": "PALOMA",
         "banco": ["PALOMA", "LLUVIA", "ESTRELLA"]},
        {"texto": "¿Qué sucedió cuando Jesús fue bautizado?", "abierta": True, "palabras_esperadas": ["PALOMA", "ESPIRITU", "CIELO", "VOZ", "HIJO", "AMADO"], "respuestas_referencia": ["El Espíritu Santo bajó como paloma y se oyó la voz del Padre.", "Se abrieron los cielos y una voz dijo que era su Hijo amado.", "Bajó el Espíritu Santo en forma de paloma sobre él."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 3.",
               "El Espíritu Santo bajó sobre Jesús como un ave conocida por su color blanco."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Al bautizarse Jesús, se abrieron los ______.", "respuesta": "CIELOS",
         "banco": ["CIELOS", "CAMINOS", "LIBROS"]},
        {"texto": "El Espíritu de Dios bajó como una ______.", "respuesta": "PALOMA",
         "banco": ["PALOMA", "AGUILA", "LLUVIA"]},
        {"texto": "Una voz dijo: «Este es mi Hijo ______.»", "respuesta": "AMADO",
         "banco": ["AMADO", "DESCONOCIDO", "LEJANO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que se abrió cuando Jesús fue bautizado.",
               "El Espíritu Santo bajó en forma de un ave conocida."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Cuando Jesús fue bautizado, se abrieron los cielos.", "respuesta": True},
        {"texto": "El Espíritu Santo bajó sobre Jesús como una tormenta.", "respuesta": False},
        {"texto": "Una voz llamó a Jesús «Hijo amado».", "respuesta": True},
        {"texto": "La Trinidad no aparece en el relato del Bautismo de Jesús.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que sucedió cuando Jesús fue bautizado en el Jordán.",
               "Si una frase dice que la Trinidad no aparece, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué bajó sobre Jesús en forma de paloma?",
         "opciones": ["El Espíritu Santo", "Un ángel", "Una nube de tormenta"], "correcta": 0},
        {"texto": "¿Cuántas personas forman la Santísima Trinidad?",
         "opciones": ["Tres", "Una", "Cinco"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que bajó sobre Jesús cuando fue bautizado.",
               "Padre, Hijo y Espíritu Santo: cuenta cuántos son."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "TRINIDAD", "definicion": "Un solo Dios en tres personas"},
        {"termino": "PADRE", "definicion": "Primera persona de la Trinidad"},
        {"termino": "HIJO", "definicion": "Segunda persona de la Trinidad, Jesucristo"},
        {"termino": "ESPIRITU", "definicion": "Tercera persona de la Trinidad"},
        {"termino": "PALOMA", "definicion": "Forma en que bajó el Espíritu Santo"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "TRINIDAD se relaciona con las tres personas de Dios."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["TRINIDAD", "PADRE", "HIJO", "ESPIRITU", "CONFUSION", "OLVIDO"],
    "correctas": ["TRINIDAD", "PADRE", "HIJO", "ESPIRITU"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Trinidad - Padre - Hijo - Espíritu.",
               "Descarta las palabras que no nombran a las personas de Dios."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu de Dios bajó como una ______.", "respuesta": "PALOMA",
         "banco": ["PALOMA", "AGUILA", "LLUVIA"]},
    ],
    "reflexion": "¿Qué te gustaría preguntar sobre la Santísima Trinidad?",
    "requisito": 1,
    "pistas": ["Piensa en la forma en que bajó el Espíritu Santo sobre Jesús.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: bautizado en la Trinidad",
    "situacion": "Ya sabes que en el Bautismo de Jesús se manifestó la Santísima Trinidad: Padre, Hijo y "
                 "Espíritu Santo.",
    "items": [
        {"texto": "¿Qué puedes hacer para recordar que fuiste bautizado en el nombre de la Trinidad?",
         "opciones": ["Hacer la señal de la cruz con atención", "Aprender a nombrar al Padre, al Hijo y "
                      "al Espíritu Santo", "Preguntar a tu catequista sobre la Trinidad",
                      "No darle importancia a la señal de la cruz"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que resta importancia a la señal de la cruz."],
    "feedback_ok": "¡Muy bien! Cada vez que haces la señal de la cruz, recuerdas tu Bautismo.",
})

# ==========================================================================
# PC05-C03 — El agua como signo bautismal
# ==========================================================================
C = "PC05-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el agua como signo bautismal",
    "items": [
        {"texto": "Elemento con el que se bautiza.", "respuesta": "AGUA"},
        {"texto": "Algo visible que representa una realidad de fe.", "respuesta": "SIGNO"},
        {"texto": "Lo que simboliza el agua al lavar.", "respuesta": "PUREZA"},
        {"texto": "Nacer de nuevo por el agua y el Espíritu, según Jesús.", "respuesta": "RENACER"},
        {"texto": "Lo que hace el agua con lo que está sucio.", "respuesta": "LIMPIEZA"},
        {"texto": "El don de Dios que recibimos en el Bautismo.", "respuesta": "GRACIA"},
    ],
    "incluir": ["AGUA", "SIGNO"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Juan 3,5 cuenta lo que Jesús le dijo a Nicodemo sobre nacer de nuevo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el agua como signo bautismal",
    "palabras": ["AGUA", "SIGNO", "PUREZA", "RENACER", "LIMPIEZA", "GRACIA"],
    "incluir": ["AGUA", "SIGNO"], "requisito": 5,
    "pistas": ["AGUA es la palabra más corta: búscala primero.",
               "LIMPIEZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 3,5",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 3,5 y completa: «El que no naciere del ______ y del "
                  "Espíritu, no puede entrar en el reino de Dios.»", "respuesta": "AGUA",
         "banco": ["AGUA", "FUEGO", "VIENTO"]},
        {"texto": "¿Qué le dice Jesús a Nicodemo sobre nacer del agua y del Espíritu?", "abierta": True, "palabras_esperadas": ["AGUA", "ESPIRITU", "NACER", "REINO"], "respuestas_referencia": ["Le dice que hay que nacer del agua y del Espíritu para entrar al reino de Dios.", "Que quien no nace del agua y del Espíritu no puede entrar en el reino de Dios.", "Le explica que necesita un nuevo nacimiento por el agua y el Espíritu."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 3.",
               "Jesús habla de nacer de nuevo, de dos elementos: uno visible y otro invisible."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El agua es un ______ visible del Bautismo.", "respuesta": "SIGNO",
         "banco": ["SIGNO", "ADORNO", "JUEGO"]},
        {"texto": "Jesús dijo que hay que nacer del agua y del ______.", "respuesta": "ESPIRITU",
         "banco": ["ESPIRITU", "VIENTO", "FUEGO"]},
        {"texto": "El agua simboliza una vida ______, limpia de pecado.", "respuesta": "NUEVA",
         "banco": ["NUEVA", "VIEJA", "IGUAL"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en qué es el agua dentro del Bautismo.",
               "Jesús habla de nacer del agua y de otra realidad invisible."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús habló con Nicodemo sobre nacer del agua y del Espíritu.", "respuesta": True},
        {"texto": "El agua del Bautismo no significa nada.", "respuesta": False},
        {"texto": "El agua es signo de una vida nueva y limpia.", "respuesta": True},
        {"texto": "Para Jesús, el Bautismo no tiene ninguna importancia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la conversación de Jesús con Nicodemo.",
               "Si una frase dice que el agua no significa nada, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "Según Jesús, ¿de qué hay que nacer para entrar en el reino de Dios?",
         "opciones": ["Del agua y del Espíritu", "Solo de la tierra",
                      "De ningún elemento en especial"], "correcta": 0},
        {"texto": "¿Qué simboliza el agua en el Bautismo?",
         "opciones": ["Una vida nueva y limpia de pecado", "Un simple lavado del cuerpo",
                      "Nada en particular"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús le dice a Nicodemo.",
               "El agua tiene un significado espiritual, no solo físico."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "AGUA", "definicion": "Elemento con el que se bautiza"},
        {"termino": "SIGNO", "definicion": "Algo visible que representa una realidad de fe"},
        {"termino": "PUREZA", "definicion": "Lo que simboliza el agua al lavar"},
        {"termino": "RENACER", "definicion": "Nacer de nuevo por el agua y el Espíritu"},
        {"termino": "GRACIA", "definicion": "Don de Dios que recibimos en el Bautismo"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "AGUA se relaciona con el elemento con que se bautiza."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["AGUA", "SIGNO", "PUREZA", "RENACER", "SUCIEDAD", "OLVIDO"],
    "correctas": ["AGUA", "SIGNO", "PUREZA", "RENACER"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Agua - Signo - Pureza - Renacer.",
               "Descarta las palabras que no tienen que ver con la limpieza o la vida nueva."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El agua es un ______ visible del Bautismo.", "respuesta": "SIGNO",
         "banco": ["SIGNO", "ADORNO", "JUEGO"]},
    ],
    "reflexion": "¿Qué sientes al pensar en el agua de tu Bautismo?",
    "requisito": 1,
    "pistas": ["Piensa en qué representa el agua en el Bautismo.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: recuerdo el signo del agua",
    "situacion": "Ya sabes que el agua del Bautismo es signo de una vida nueva, limpia y llena de la "
                 "gracia de Dios.",
    "items": [
        {"texto": "¿Qué puedes hacer para recordar el signo de tu Bautismo?",
         "opciones": ["Tocar el agua bendita al entrar a la iglesia", "Dar gracias por la vida nueva que "
                      "Dios te regaló", "Preguntar a tus padres sobre el día de tu Bautismo",
                      "No prestarle atención al agua bendita"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que resta importancia al agua bendita."],
    "feedback_ok": "¡Muy bien! El agua te recuerda que eres una nueva creación en Cristo.",
})

# ==========================================================================
# PC05-C04 — Somos hijos de Dios
# ==========================================================================
C = "PC05-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: somos hijos de Dios",
    "items": [
        {"texto": "Lo que somos de Dios, gracias al Bautismo.", "respuesta": "HIJOS"},
        {"texto": "Quien da testimonio de que somos hijos de Dios.", "respuesta": "ESPIRITU"},
        {"texto": "Lo que da el Espíritu a nuestro corazón.", "respuesta": "TESTIMONIO"},
        {"texto": "Palabra cariñosa con la que llamamos a Dios Padre.", "respuesta": "ABBA"},
        {"texto": "El espíritu que hemos recibido, según san Pablo.", "respuesta": "ADOPCION"},
        {"texto": "Quiénes somos de verdad, ante Dios.", "respuesta": "IDENTIDAD"},
    ],
    "incluir": ["HIJOS", "ESPIRITU"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Romanos 8,14-16 habla del testimonio del Espíritu en nosotros."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: somos hijos de Dios",
    "palabras": ["HIJOS", "ESPIRITU", "TESTIMONIO", "ABBA", "ADOPCION", "IDENTIDAD"],
    "incluir": ["HIJOS", "ESPIRITU"], "requisito": 5,
    "pistas": ["ABBA es la palabra más corta: búscala primero.",
               "TESTIMONIO e IDENTIDAD son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Romanos 8,14-16",
    "items": [
        {"texto": "Busca en tu Biblia Católica Romanos 8,14-16 y completa: «El Espíritu mismo da "
                  "testimonio a nuestro espíritu de que somos ______ de Dios.»", "respuesta": "HIJOS",
         "banco": ["HIJOS", "SIERVOS", "EXTRAÑOS"]},
        {"texto": "¿Qué testimonio da el Espíritu Santo en nosotros?", "abierta": True, "palabras_esperadas": ["HIJOS", "ESPIRITU", "ABBA", "PADRE"], "respuestas_referencia": ["Da testimonio de que somos hijos de Dios.", "El Espíritu nos hace llamar a Dios 'Abba, Padre'.", "Nos asegura que somos hijos y herederos de Dios."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Romanos en el índice de tu Biblia; el capítulo es el 8.",
               "El Espíritu nos hace sentir una relación muy cercana con Dios, como hijos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo nos hace llamar a Dios «______», es decir, Padre.", "respuesta": "ABBA",
         "banco": ["ABBA", "SEÑOR", "REY"]},
        {"texto": "San Pablo dice que hemos recibido el espíritu de ______.", "respuesta": "ADOPCION",
         "banco": ["ADOPCION", "MIEDO", "ESCLAVITUD"]},
        {"texto": "Por el Bautismo, nuestra ______ es ser hijos de Dios.", "respuesta": "IDENTIDAD",
         "banco": ["IDENTIDAD", "OCUPACION", "EDAD"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo el Espíritu nos permite llamar a Dios.",
               "La última respuesta es quiénes somos de verdad, ante Dios."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo nos hace sentir hijos de Dios.", "respuesta": True},
        {"texto": "San Pablo dice que somos esclavos sin ninguna dignidad.", "respuesta": False},
        {"texto": "Podemos llamar a Dios «Abba», es decir, Padre.", "respuesta": True},
        {"texto": "Ser hijo de Dios no cambia nada en nuestra vida.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que dice san Pablo sobre el espíritu de adopción.",
               "Si una frase dice que somos esclavos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué testimonio da el Espíritu Santo en nosotros?",
         "opciones": ["Que somos hijos de Dios", "Que estamos solos",
                      "Que no le importamos a Dios"], "correcta": 0},
        {"texto": "¿Cómo podemos llamar a Dios, según san Pablo?",
         "opciones": ["Abba, Padre", "Un extraño", "Un juez lejano"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que el Espíritu da testimonio en nosotros.",
               "Es una palabra cariñosa para llamar al Padre."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "HIJOS", "definicion": "Lo que somos de Dios, gracias al Bautismo"},
        {"termino": "ESPIRITU", "definicion": "Quien da testimonio de nuestra filiación"},
        {"termino": "ABBA", "definicion": "Palabra cariñosa para llamar a Dios Padre"},
        {"termino": "ADOPCION", "definicion": "El espíritu que hemos recibido, según san Pablo"},
        {"termino": "IDENTIDAD", "definicion": "Quiénes somos de verdad, ante Dios"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "HIJOS se relaciona con lo que somos de Dios por el Bautismo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["HIJOS", "ESPIRITU", "ABBA", "IDENTIDAD", "MIEDO", "ESCLAVITUD"],
    "correctas": ["HIJOS", "ESPIRITU", "ABBA", "IDENTIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Hijos - Espíritu - Abba - Identidad.",
               "Descarta las palabras que hablan de miedo o esclavitud."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu Santo nos hace llamar a Dios «______», es decir, Padre.", "respuesta": "ABBA",
         "banco": ["ABBA", "SEÑOR", "REY"]},
    ],
    "reflexion": "¿Qué significa para ti saber que eres hijo de Dios?",
    "requisito": 1,
    "pistas": ["Piensa en cómo el Espíritu nos permite llamar a Dios.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo como hijo de Dios",
    "situacion": "Ya sabes que, por el Espíritu, eres hijo de Dios y puedes llamarlo «Abba, Padre».",
    "items": [
        {"texto": "¿Qué puedes hacer para vivir como verdadero hijo de Dios?",
         "opciones": ["Hablar con Dios como a un padre cercano", "Confiar en su amor cada día",
                      "Tratar a otros como hijos de un mismo Padre", "Olvidarte de que eres su hijo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que te aleja de tu identidad como hijo de Dios."],
    "feedback_ok": "¡Muy bien! Ser hijo de Dios es tu identidad más verdadera.",
})

# ==========================================================================
# PC05-C05 — Somos miembros de la Iglesia
# ==========================================================================
C = "PC05-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: somos miembros de la Iglesia",
    "items": [
        {"texto": "Lo que somos de la Iglesia, por el Bautismo.", "respuesta": "MIEMBROS"},
        {"texto": "El cuerpo de Cristo, formado por todos los bautizados.", "respuesta": "IGLESIA"},
        {"texto": "Así llama san Pablo a la Iglesia.", "respuesta": "CUERPO"},
        {"texto": "Lo que forman todos los bautizados en un solo Espíritu.", "respuesta": "UNIDAD"},
        {"texto": "El grupo de fe al que pertenecemos por el Bautismo.", "respuesta": "COMUNIDAD"},
        {"texto": "El sacramento que nos incorpora a la Iglesia.", "respuesta": "BAUTISMO"},
    ],
    "incluir": ["MIEMBROS", "BAUTISMO"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "1 Corintios 12,12-13 dice en qué nos convierte el Bautismo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: somos miembros de la Iglesia",
    "palabras": ["MIEMBROS", "IGLESIA", "CUERPO", "UNIDAD", "COMUNIDAD", "BAUTISMO"],
    "incluir": ["MIEMBROS", "BAUTISMO"], "requisito": 5,
    "pistas": ["CUERPO y UNIDAD son de las palabras más cortas: búscalas primero.",
               "MIEMBROS y COMUNIDAD son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 12,12-13",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 12,12-13 y completa: «Por un solo Espíritu "
                  "fuimos todos ______ en un cuerpo.»", "respuesta": "BAUTIZADOS",
         "banco": ["BAUTIZADOS", "SEPARADOS", "OLVIDADOS"]},
        {"texto": "¿En qué nos convierte el Bautismo, según san Pablo?", "abierta": True, "palabras_esperadas": ["CUERPO", "MIEMBRO", "BAUTIZADOS", "IGLESIA"], "respuestas_referencia": ["Nos convierte en miembros del cuerpo de Cristo, la Iglesia.", "Nos hace parte de un mismo cuerpo, bautizados en un mismo Espíritu.", "En hijos de Dios y miembros de la Iglesia."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a los Corintios en el índice de tu Biblia; el capítulo es el 12.",
               "San Pablo dice que un solo Espíritu nos hace parte de un solo cuerpo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Por el Bautismo somos ______ de la Iglesia.", "respuesta": "MIEMBROS",
         "banco": ["MIEMBROS", "VISITANTES", "EXTRAÑOS"]},
        {"texto": "Todos los bautizados formamos un solo ______.", "respuesta": "CUERPO",
         "banco": ["CUERPO", "EDIFICIO", "EQUIPO"]},
        {"texto": "El Bautismo nos une en una sola ______.", "respuesta": "COMUNIDAD",
         "banco": ["COMUNIDAD", "ISLA", "DISTANCIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que somos de la Iglesia por el Bautismo.",
               "La segunda respuesta es la misma imagen que usa san Pablo para la Iglesia."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Por un solo Espíritu, todos fuimos bautizados en un cuerpo.", "respuesta": True},
        {"texto": "Cada bautizado pertenece a una Iglesia distinta y separada.", "respuesta": False},
        {"texto": "El Bautismo nos hace miembros de la Iglesia.", "respuesta": True},
        {"texto": "Ser miembro de la Iglesia no significa nada para san Pablo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que dice san Pablo en 1 Corintios 12.",
               "Si una frase dice que cada uno pertenece a una Iglesia distinta, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿En qué nos convierte el Bautismo, según san Pablo?",
         "opciones": ["En miembros de un solo cuerpo, la Iglesia", "En personas totalmente independientes",
                      "En rivales dentro de la comunidad"], "correcta": 0},
        {"texto": "¿Qué forman todos los bautizados juntos?",
         "opciones": ["Una sola comunidad de fe", "Grupos que no se relacionan",
                      "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la imagen del cuerpo que usa san Pablo.",
               "Es lo contrario de vivir separados."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "MIEMBROS", "definicion": "Lo que somos de la Iglesia por el Bautismo"},
        {"termino": "IGLESIA", "definicion": "El cuerpo de Cristo formado por los bautizados"},
        {"termino": "CUERPO", "definicion": "Así llama san Pablo a la Iglesia"},
        {"termino": "UNIDAD", "definicion": "Lo que forman los bautizados en un solo Espíritu"},
        {"termino": "BAUTISMO", "definicion": "El sacramento que nos incorpora a la Iglesia"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "MIEMBROS se relaciona con lo que somos de la Iglesia."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["MIEMBROS", "IGLESIA", "CUERPO", "UNIDAD", "DIVISION", "AISLAMIENTO"],
    "correctas": ["MIEMBROS", "IGLESIA", "CUERPO", "UNIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Miembros - Iglesia - Cuerpo - Unidad.",
               "Descarta las palabras que hablan de estar separados."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Por el Bautismo somos ______ de la Iglesia.", "respuesta": "MIEMBROS",
         "banco": ["MIEMBROS", "VISITANTES", "EXTRAÑOS"]},
    ],
    "reflexion": "¿Cómo puedes vivir tu pertenencia a la Iglesia?",
    "requisito": 1,
    "pistas": ["Piensa en lo que somos de la Iglesia por el Bautismo.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: miembro activo de la Iglesia",
    "situacion": "Ya sabes que el Bautismo te hace miembro de la Iglesia, el cuerpo de Cristo.",
    "items": [
        {"texto": "¿Qué puedes hacer para vivir como miembro activo de la Iglesia?",
         "opciones": ["Participar en las actividades de tu parroquia", "Colaborar con tu comunidad de "
                      "catequesis", "Sentirte parte importante del grupo", "Alejarte sin ninguna razón"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que te aleja de la comunidad."],
    "feedback_ok": "¡Muy bien! Cada miembro tiene un lugar valioso en el cuerpo de la Iglesia.",
})

# ==========================================================================
# PC05-C06 — Recordamos y vivimos el Bautismo
# ==========================================================================
C = "PC05-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: recordamos y vivimos el Bautismo",
    "items": [
        {"texto": "Traer a la memoria el día de nuestro Bautismo.", "respuesta": "RECORDAR"},
        {"texto": "Poner en práctica lo que Dios nos regaló en el Bautismo.", "respuesta": "VIVIR"},
        {"texto": "Lo que asumimos al vivir como bautizados.", "respuesta": "COMPROMISO"},
        {"texto": "Lo que profesamos al renovar las promesas del Bautismo.", "respuesta": "FE"},
        {"texto": "Lo que representa el cirio encendido en el Bautismo.", "respuesta": "LUZ"},
        {"texto": "La vela que se enciende el día del Bautismo.", "respuesta": "CIRIO"},
    ],
    "incluir": ["RECORDAR", "VIVIR"], "requisito": 4,
    "pistas": ["Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama.",
               "Gálatas 3,27 dice de qué nos revestimos al ser bautizados."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: recordamos y vivimos el Bautismo",
    "palabras": ["RECORDAR", "VIVIR", "COMPROMISO", "FE", "LUZ", "CIRIO"],
    "incluir": ["RECORDAR", "VIVIR"], "requisito": 5,
    "pistas": ["FE y LUZ son las palabras más cortas: búscalas primero.",
               "COMPROMISO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Gálatas 3,27",
    "items": [
        {"texto": "Busca en tu Biblia Católica Gálatas 3,27 y completa: «Todos los que habéis sido "
                  "bautizados en Cristo, de Cristo estáis ______.»", "respuesta": "REVESTIDOS",
         "banco": ["REVESTIDOS", "OLVIDADOS", "ALEJADOS"]},
        {"texto": "¿De qué nos revestimos al ser bautizados?", "abierta": True, "palabras_esperadas": ["CRISTO", "REVESTIDOS", "VESTIDOS"], "respuestas_referencia": ["Nos revestimos de Cristo.", "Nos vestimos de Cristo al ser bautizados.", "Quedamos revestidos de Cristo, como una nueva vida."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Gálatas en el índice de tu Biblia; el capítulo es el 3.",
               "San Pablo compara el Bautismo con vestirse de alguien."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El cirio encendido representa la ______ de Cristo.", "respuesta": "LUZ",
         "banco": ["LUZ", "SOMBRA", "NOCHE"]},
        {"texto": "Al ser bautizados, nos revestimos de ______.", "respuesta": "CRISTO",
         "banco": ["CRISTO", "MIEDO", "DUDA"]},
        {"texto": "Vivir el Bautismo es un ______ de cada día.", "respuesta": "COMPROMISO",
         "banco": ["COMPROMISO", "OLVIDO", "DESCUIDO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que representa el cirio encendido.",
               "San Pablo dice que nos revestimos de alguien en el Bautismo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Al ser bautizados, nos revestimos de Cristo.", "respuesta": True},
        {"texto": "El cirio encendido en el Bautismo no tiene ningún significado.", "respuesta": False},
        {"texto": "Vivir el Bautismo es un compromiso de cada día.", "respuesta": True},
        {"texto": "Una vez bautizados, ya no hace falta recordar ni vivir la fe.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que dice san Pablo en Gálatas 3,27.",
               "Si una frase dice que ya no hace falta vivir la fe, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "Según Gálatas 3,27, ¿de qué nos revestimos al ser bautizados?",
         "opciones": ["De Cristo", "De una capa cualquiera", "De nada en especial"], "correcta": 0},
        {"texto": "¿Qué representa el cirio encendido en el Bautismo?",
         "opciones": ["La luz de Cristo", "Solo una tradición sin sentido",
                      "El fuego del enojo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en de quién nos revestimos, según san Pablo.",
               "Es lo mismo que representa el cirio encendido."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "RECORDAR", "definicion": "Traer a la memoria el día de nuestro Bautismo"},
        {"termino": "VIVIR", "definicion": "Poner en práctica lo recibido en el Bautismo"},
        {"termino": "COMPROMISO", "definicion": "Lo que asumimos al vivir como bautizados"},
        {"termino": "LUZ", "definicion": "Lo que representa el cirio encendido"},
        {"termino": "CIRIO", "definicion": "La vela que se enciende en el Bautismo"},
    ],
    "requisito": 4,
    "pistas": ["Empieza por la pareja que te parezca más clara.",
               "CIRIO se relaciona con la vela que se enciende en el Bautismo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Descubre el mensaje",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de este tema.",
    "tiempo_segundos": 45,
    "banco": ["RECORDAR", "VIVIR", "COMPROMISO", "LUZ", "OLVIDO", "DESCUIDO"],
    "correctas": ["RECORDAR", "VIVIR", "COMPROMISO", "LUZ"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Recordar - Vivir - Compromiso - Luz.",
               "Descarta las palabras que hablan de olvidar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El cirio encendido representa la ______ de Cristo.", "respuesta": "LUZ",
         "banco": ["LUZ", "SOMBRA", "NOCHE"]},
    ],
    "reflexion": "¿Cómo puedes vivir hoy el compromiso de tu Bautismo?",
    "requisito": 1,
    "pistas": ["Piensa en lo que representa el cirio encendido.",
               "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo mi Bautismo cada día",
    "situacion": "Ya sabes que vivir el Bautismo es un compromiso diario de llevar la luz de Cristo.",
    "items": [
        {"texto": "¿Qué puedes hacer para vivir tu Bautismo cada día?",
         "opciones": ["Hacer el bien a quienes te rodean", "Rezar y dar gracias por tu fe",
                      "Ser como una luz para los demás", "Olvidarte de que eres bautizado"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que significa olvidar tu Bautismo."],
    "feedback_ok": "¡Muy bien! Cada día puedes vivir la luz de tu Bautismo.",
})


def actividades_de_contenido(contenido_id):
    return [aid for aid, a in ACTIVIDADES.items() if a["contenido_id"] == contenido_id]


def contenido_de(contenido_id):
    return next((c for c in CONTENIDOS if c["id"] == contenido_id), None)


def encuentro_de(encuentro_id):
    return next((e for e in ENCUENTROS if e["id"] == encuentro_id), None)


def contenidos_de_encuentro(encuentro_id):
    """Los contenidos cuyo id empieza por «<encuentro_id>-», en el orden en
    que aparecen en CONTENIDOS (ej.: 'PC02' -> los 6 contenidos PC02-C01 a
    PC02-C06)."""
    return [c for c in CONTENIDOS if c["id"].split("-")[0] == encuentro_id]


# ==========================================================================
# ==========================================================================
# PC06 — La Eucaristía: Jesús se queda con nosotros   (Encuentro 6, Lucas 22,19-20 / Juan 6,51)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC06-C01 — La Última Cena
# ==========================================================================
C = "PC06-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Última Cena",
    "items": [
        {"texto": "La comida que Jesús compartió con sus apóstoles la noche antes de morir.", "respuesta": "CENA", "banco": ["CENA", "FIESTA", "REUNION"]},
        {"texto": "El alimento que Jesús partió y dio a sus discípulos.", "respuesta": "PAN", "banco": ["PAN", "CARNE", "FRUTA"]},
        {"texto": "La bebida que Jesús compartió en una copa.", "respuesta": "VINO", "banco": ["VINO", "AGUA", "LECHE"]},
        {"texto": "Donde se sentaron Jesús y sus discípulos a comer juntos.", "respuesta": "MESA", "banco": ["MESA", "CAMINO", "MONTE"]},
        {"texto": "Los doce discípulos más cercanos de Jesús.", "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "SOLDADOS", "FARISEOS"]},
        {"texto": "Darse por completo a los demás, como hizo Jesús.", "respuesta": "ENTREGA", "banco": ["ENTREGA", "DISTANCIA", "DUDA"]},
    ],
    "incluir": ["CENA", "PAN"], "requisito": 4,
    "pistas": ["Piensa en la última comida de Jesús con sus apóstoles.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Última Cena",
    "palabras": ["CENA", "PAN", "VINO", "MESA", "APOSTOLES", "ENTREGA"],
    "incluir": ["CENA", "PAN"], "requisito": 5,
    "pistas": ["CENA y PAN son de las palabras más cortas: búscalas primero.",
               "APÓSTOLES es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 22,14-20",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 22,14-20 y completa: «Esto es mi ______, que se "
                  "entrega por vosotros.»", "respuesta": "CUERPO", "banco": ["CUERPO", "PAN", "REGALO"]},
        {"texto": "¿Qué hizo Jesús con el pan y el cáliz en la Última Cena?", "abierta": True, "palabras_esperadas": ["PARTIO", "DIO", "CUERPO", "PAN", "COPA", "SANGRE", "ENTREGO", "GRACIAS"], "respuestas_referencia": ["Tomó el pan, lo partió y lo dio diciendo que era su cuerpo entregado por nosotros.", "Compartió el pan y la copa como su cuerpo y su sangre entregados por amor.", "Dio gracias, partió el pan y lo repartió diciendo que era su cuerpo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 22.",
               "Jesús toma el pan, da gracias, lo parte y lo reparte diciendo unas palabras muy importantes."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús compartió la Última ______ con sus apóstoles.", "respuesta": "CENA", "banco": ["CENA", "FIESTA", "REUNIÓN"]},
        {"texto": "En la mesa había ______ y vino.", "respuesta": "PAN", "banco": ["PAN", "CARNE", "FRUTA"]},
        {"texto": "Jesús se ______ por amor a todos.", "respuesta": "ENTREGÓ", "banco": ["ENTREGÓ", "ESCONDIÓ", "ALEJÓ"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la comida que Jesús compartió antes de morir.",
               "La tercera respuesta describe lo que Jesús hizo por amor."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La Última Cena fue la última comida de Jesús con sus apóstoles antes de morir.", "respuesta": True},
        {"texto": "Jesús compartió esa cena completamente solo, sin nadie más.", "respuesta": False},
        {"texto": "En la Última Cena, Jesús compartió pan y vino.", "respuesta": True},
        {"texto": "La Última Cena no tiene relación con la Eucaristía.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda con quiénes compartió Jesús esa cena.",
               "Si una frase dice que la Última Cena no tiene relación con la Eucaristía, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con quiénes compartió Jesús la Última Cena?",
         "opciones": ["Con los apóstoles", "Con soldados romanos", "Con nadie", "Con los fariseos"], "correcta": 0},
        {"texto": "¿Qué compartió Jesús en esa cena?",
         "opciones": ["Pan y vino", "Solo agua", "Solo pan", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quiénes estaban con Jesús esa noche.",
               "Recuerda lo que Jesús tomó, bendijo y repartió."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CENA", "definicion": "Última comida de Jesús con sus apóstoles"},
        {"termino": "PAN", "definicion": "Alimento que Jesús partió"},
        {"termino": "VINO", "definicion": "Bebida compartida en la copa"},
        {"termino": "APÓSTOLES", "definicion": "Discípulos que compartieron la cena"},
        {"termino": "ENTREGA", "definicion": "Darse por amor a los demás"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que Jesús compartió esa noche.",
               "ENTREGA describe la actitud de Jesús, no un objeto de la mesa."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la Última Cena",
    "instruccion": "En 45 segundos, marca las palabras que resumen la Última Cena.",
    "tiempo_segundos": 45,
    "banco": ["CENA", "PAN", "VINO", "ENTREGA", "SOLEDAD", "INDIFERENCIA"],
    "correctas": ["CENA", "PAN", "VINO", "ENTREGA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Cena - Pan - Vino - Entrega.",
               "Descarta las palabras que no aparecieron en este relato."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La Última Cena fue la comida que Jesús compartió con sus ______ antes de morir.",
         "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "VECINOS", "SOLDADOS"]},
    ],
    "reflexion": "¿Qué sentirías si Jesús te invitara a esa cena?",
    "requisito": 1,
    "pistas": ["Piensa en quiénes estaban con Jesús esa noche.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: comparto como Jesús",
    "situacion": "Ya sabes que en la Última Cena Jesús compartió pan y vino con sus apóstoles, como signo de su entrega.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para compartir con los demás como Jesús?",
         "opciones": ["Compartir mi comida con alguien",
                      "Invitar a alguien a la mesa familiar",
                      "Ayudar a preparar la cena en casa",
                      "Comer solo, sin compartir con nadie"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra el gesto de compartir de Jesús."],
    "feedback_ok": "¡Muy bien! Compartir la mesa también es una forma de vivir la Eucaristía.",
})

# ==========================================================================
# PC06-C02 — Pan y vino en la entrega de Jesús
# ==========================================================================
C = "PC06-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: pan y vino",
    "items": [
        {"texto": "Alimento que Jesús convirtió en su cuerpo.", "respuesta": "PAN", "banco": ["PAN", "ARROZ", "CARNE"]},
        {"texto": "Bebida que Jesús convirtió en su sangre.", "respuesta": "VINO", "banco": ["VINO", "AGUA", "JUGO"]},
        {"texto": "Lo que Jesús dijo que era el pan.", "respuesta": "CUERPO", "banco": ["CUERPO", "REGALO", "SIGNO"]},
        {"texto": "Lo que Jesús dijo que era el vino.", "respuesta": "SANGRE", "banco": ["SANGRE", "AGUA", "MIEL"]},
        {"texto": "Pacto nuevo que Jesús sella con su sangre.", "respuesta": "ALIANZA", "banco": ["ALIANZA", "DISTANCIA", "DUDA"]},
        {"texto": "Lo que hizo Jesús antes de partir el pan.", "respuesta": "BENDIJO", "banco": ["BENDIJO", "ESCONDIÓ", "ROMPIÓ"]},
    ],
    "incluir": ["PAN", "VINO"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús dio a sus discípulos.", "Todas las palabras se relacionan con la entrega de Jesús."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: pan y vino",
    "palabras": ["PAN", "VINO", "CUERPO", "SANGRE", "ALIANZA", "BENDIJO"],
    "incluir": ["PAN", "VINO"], "requisito": 5,
    "pistas": ["PAN y VINO son las palabras más cortas: búscalas primero.",
               "ALIANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 26,26-28",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 26,26-28 y completa: «Tomad, comed, esto es mi "
                  "______.»", "respuesta": "CUERPO", "banco": ["CUERPO", "REGALO", "ALIMENTO"]},
        {"texto": "¿Qué dijo Jesús al dar el pan y el vino a sus discípulos?", "abierta": True, "palabras_esperadas": ["SANGRE", "ALIANZA", "CUERPO", "DERRAMADA", "PERDON"], "respuestas_referencia": ["Dijo que el pan era su cuerpo y el vino su sangre de la alianza.", "Que esta es su sangre derramada por muchos para el perdón de los pecados.", "Que el pan y el vino eran su cuerpo y su sangre entregados por nosotros."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 26.",
               "Jesús habla primero del pan y luego del vino, dando gracias antes de cada uno."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús ______ el pan antes de partirlo.", "respuesta": "BENDIJO", "banco": ["BENDIJO", "ESCONDIÓ", "ROMPIÓ"]},
        {"texto": "El vino se convirtió en la ______ de Jesús.", "respuesta": "SANGRE", "banco": ["SANGRE", "AGUA", "MIEL"]},
        {"texto": "Jesús selló una nueva ______ con su sangre.", "respuesta": "ALIANZA", "banco": ["ALIANZA", "DISTANCIA", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús hizo antes de repartir el pan.",
               "La segunda respuesta es lo que Jesús dijo que era el vino."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús dio el pan diciendo que era su cuerpo.", "respuesta": True},
        {"texto": "El vino no tiene ningún significado en la Última Cena.", "respuesta": False},
        {"texto": "Jesús selló una nueva alianza con su sangre.", "respuesta": True},
        {"texto": "Jesús compartió el pan y el vino sin decir nada.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda las palabras que dijo Jesús sobre el pan y el vino.",
               "Si una frase dice que Jesús no dijo nada, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué dijo Jesús sobre el pan?",
         "opciones": ["Que era su cuerpo", "Que era una piedra", "Que no servía", "Que era de otro"], "correcta": 0},
        {"texto": "¿Para qué se derrama la sangre de Jesús, según el evangelio?",
         "opciones": ["Para el perdón de los pecados", "Para nada", "Para castigar", "Para separar"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Recuerda las palabras exactas de Jesús sobre el pan.",
               "Piensa en el motivo por el que Jesús entrega su sangre."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PAN", "definicion": "Se convierte en el cuerpo de Jesús"},
        {"termino": "VINO", "definicion": "Se convierte en la sangre de Jesús"},
        {"termino": "ALIANZA", "definicion": "Pacto nuevo sellado por Jesús"},
        {"termino": "BENDIJO", "definicion": "Acción de Jesús antes de partir el pan"},
        {"termino": "SANGRE", "definicion": "Derramada para el perdón"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en qué se convierten el pan y el vino.",
               "ALIANZA es el pacto nuevo, no un alimento."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: las palabras de Jesús",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "«Esto es mi ______», dijo Jesús del pan.",
         "opciones": ["cuerpo", "plato", "regalo"], "correcta": 0},
        {"texto": "«Esta es mi ______ de la alianza», dijo Jesús del vino.",
         "opciones": ["sangre", "bebida", "agua"], "correcta": 0},
        {"texto": "Jesús selló una nueva ______ con su sangre.",
         "opciones": ["alianza", "distancia", "receta"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Recuerda las palabras exactas que dijo Jesús sobre el pan y el vino.",
               "Piensa en el pacto nuevo que Jesús sella con su sangre."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús dio el pan diciendo que era su ______.", "respuesta": "CUERPO", "banco": ["CUERPO", "PLATO", "REGALO"]},
    ],
    "reflexion": "¿Qué significa para ti recibir el cuerpo de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en las palabras de Jesús al repartir el pan.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: agradezco el regalo de Jesús",
    "situacion": "Ya sabes que Jesús entregó su cuerpo y su sangre por amor a todos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para agradecer ese regalo?",
         "opciones": ["Participar con atención en la Misa",
                      "Dar gracias a Jesús en una oración",
                      "Prepararme bien para recibir la comunión",
                      "Distraerme durante la Misa"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra agradecimiento por ese regalo."],
    "feedback_ok": "¡Muy bien! Agradecer también es una forma de valorar la entrega de Jesús.",
})

# ==========================================================================
# PC06-C03 — Jesús se entrega por amor
# ==========================================================================
C = "PC06-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús se entrega",
    "items": [
        {"texto": "Jesús se compara con este alimento que da vida.", "respuesta": "PAN", "banco": ["PAN", "AGUA", "SAL"]},
        {"texto": "Lo que Jesús promete a quien come de este pan.", "respuesta": "VIDA", "banco": ["VIDA", "FAMA", "SUERTE"]},
        {"texto": "El lugar por el cual Jesús entrega su vida.", "respuesta": "MUNDO", "banco": ["MUNDO", "GRUPO", "PUEBLO"]},
        {"texto": "Darse completamente por los demás.", "respuesta": "ENTREGA", "banco": ["ENTREGA", "DISTANCIA", "OLVIDO"]},
        {"texto": "Lo que Jesús daría, según este pasaje, para la vida del mundo.", "respuesta": "CARNE", "banco": ["CARNE", "ORO", "TIEMPO"]},
        {"texto": "Razón por la que Jesús se entrega.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "DEBER"]},
    ],
    "incluir": ["PAN", "VIDA"], "requisito": 4,
    "pistas": ["Piensa en cómo se describe Jesús a sí mismo en este pasaje.",
               "Todas las palabras hablan de la entrega de Jesús por amor."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús se entrega",
    "palabras": ["PAN", "VIDA", "MUNDO", "ENTREGA", "CARNE", "AMOR"],
    "incluir": ["PAN", "VIDA"], "requisito": 5,
    "pistas": ["PAN y VIDA son de las palabras más cortas: búscalas primero.",
               "ENTREGA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 6,51",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 6,51 y completa: «Yo soy el pan ______ bajado del "
                  "cielo.»", "respuesta": "VIVO", "banco": ["VIVO", "DURO", "VIEJO"]},
        {"texto": "¿Qué dice Jesús sobre el pan que él dará?", "abierta": True, "palabras_esperadas": ["CARNE", "VIDA", "MUNDO", "ENTREGA", "AMOR"], "respuestas_referencia": ["Dice que el pan que dará es su carne para la vida del mundo.", "Que él es el pan vivo bajado del cielo y da vida eterna.", "Que entrega su carne por amor, para la vida del mundo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 6.",
               "Jesús se compara a sí mismo con un alimento que baja del cielo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús es el pan ______ bajado del cielo.", "respuesta": "VIVO", "banco": ["VIVO", "VIEJO", "DURO"]},
        {"texto": "Jesús entrega su vida por ______ a todos.", "respuesta": "AMOR", "banco": ["AMOR", "OBLIGACIÓN", "CASUALIDAD"]},
        {"texto": "El pan que Jesús da es para la vida del ______.", "respuesta": "MUNDO", "banco": ["MUNDO", "CIELO", "GRUPO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se llama Jesús a sí mismo en este pasaje.",
               "La segunda respuesta es el motivo de la entrega de Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús se compara con el pan de vida.", "respuesta": True},
        {"texto": "Jesús se entrega por amor a la humanidad.", "respuesta": True},
        {"texto": "A Jesús no le importa el mundo.", "respuesta": False},
        {"texto": "El pan que Jesús da no tiene ningún significado.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo se describe Jesús a sí mismo en este pasaje.",
               "Si una frase dice que a Jesús no le importa el mundo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo se llama Jesús a sí mismo en este pasaje?",
         "opciones": ["Pan de vida", "Piedra", "Río", "Solo un camino"], "correcta": 0},
        {"texto": "¿Por qué se entrega Jesús, según este pasaje?",
         "opciones": ["Por amor", "Por obligación", "Por casualidad", "Por miedo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la comparación que hace Jesús de sí mismo.",
               "Recuerda el motivo detrás de toda entrega de Jesús."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PAN", "definicion": "Jesús se compara con este alimento"},
        {"termino": "VIDA", "definicion": "Lo que Jesús da a quien cree en él"},
        {"termino": "MUNDO", "definicion": "Por quien Jesús entrega su vida"},
        {"termino": "ENTREGA", "definicion": "Darse por completo a los demás"},
        {"termino": "AMOR", "definicion": "Motivo de la entrega de Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo se describe Jesús a sí mismo.",
               "AMOR es la razón detrás de todo lo demás."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Jesús se entrega",
    "instruccion": "En 45 segundos, marca las palabras que resumen este pasaje.",
    "tiempo_segundos": 45,
    "banco": ["PAN", "VIDA", "ENTREGA", "AMOR", "INDIFERENCIA", "OLVIDO"],
    "correctas": ["PAN", "VIDA", "ENTREGA", "AMOR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Pan - Vida - Entrega - Amor.",
               "Descarta las palabras que no aparecieron en este pasaje."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús se llama a sí mismo el pan de la ______.", "respuesta": "VIDA", "banco": ["VIDA", "TIERRA", "NOCHE"]},
    ],
    "reflexion": "¿Qué significa para ti que Jesús se entregue como pan de vida?",
    "requisito": 1,
    "pistas": ["Piensa en cómo se describe Jesús a sí mismo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: me entrego un poco más",
    "situacion": "Ya sabes que Jesús se entrega por amor, como pan de vida para todos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para entregarte un poco más a los demás?",
         "opciones": ["Ayudar a un compañero sin esperar nada a cambio",
                      "Compartir mi tiempo con mi familia",
                      "Ofrecer mi ayuda a quien la necesite",
                      "Pensar solo en mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra entrega a los demás."],
    "feedback_ok": "¡Muy bien! Entregarte a los demás también es imitar a Jesús.",
})

# ==========================================================================
# PC06-C04 — La Eucaristía es presencia viva de Jesús
# ==========================================================================
C = "PC06-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: presencia viva",
    "items": [
        {"texto": "Sacramento en el que Jesús se hace presente bajo el pan y el vino.", "respuesta": "EUCARISTIA", "banco": ["EUCARISTIA", "BAUTISMO", "CONFIRMACION"]},
        {"texto": "Estar realmente ahí, no solo en el recuerdo.", "respuesta": "PRESENCIA", "banco": ["PRESENCIA", "AUSENCIA", "DISTANCIA"]},
        {"texto": "Lo que recibimos bajo la forma del pan.", "respuesta": "CUERPO", "banco": ["CUERPO", "NOMBRE", "IMAGEN"]},
        {"texto": "Lo que recibimos bajo la forma del vino.", "respuesta": "SANGRE", "banco": ["SANGRE", "AGUA", "MIEL"]},
        {"texto": "Lo que Jesús promete a quien come su cuerpo.", "respuesta": "VIVIR", "banco": ["VIVIR", "OLVIDAR", "DUDAR"]},
        {"texto": "Quedarse, no irse.", "respuesta": "PERMANECER", "banco": ["PERMANECER", "ALEJARSE", "HUIR"]},
    ],
    "incluir": ["EUCARISTIA", "PRESENCIA"], "requisito": 4,
    "pistas": ["Piensa en el sacramento que celebramos en la Misa.",
               "Todas las palabras hablan de que Jesús está realmente presente."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: presencia viva",
    "palabras": ["EUCARISTIA", "PRESENCIA", "CUERPO", "SANGRE", "VIVIR", "PERMANECER"],
    "incluir": ["EUCARISTIA", "PRESENCIA"], "requisito": 5,
    "pistas": ["CUERPO es una de las palabras más cortas: búscala primero.",
               "PERMANECER es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 6,53-56",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 6,53-56 y completa: «El que come mi carne y bebe mi "
                  "sangre tiene vida ______.»", "respuesta": "ETERNA", "banco": ["ETERNA", "CORTA", "DIFICIL"]},
        {"texto": "¿Qué promete Jesús a quien come su cuerpo y bebe su sangre?", "abierta": True, "palabras_esperadas": ["VIDA", "ETERNA", "PERMANECE", "PRESENCIA", "JESUS"], "respuestas_referencia": ["Promete que tendrá vida eterna y que permanecerá en él.", "Que quien lo recibe permanece en Jesús y Jesús en él.", "Le promete vida eterna y su presencia permanente."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 6.",
               "Jesús habla de permanecer en quien lo recibe, y de una vida que nunca termina."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "La Eucaristía es la ______ viva de Jesús.", "respuesta": "PRESENCIA", "banco": ["PRESENCIA", "AUSENCIA", "IDEA"]},
        {"texto": "Quien recibe la Eucaristía recibe el ______ de Jesús.", "respuesta": "CUERPO", "banco": ["CUERPO", "NOMBRE", "RECUERDO"]},
        {"texto": "Jesús promete vida ______ a quien lo recibe.", "respuesta": "ETERNA", "banco": ["ETERNA", "CORTA", "TRISTE"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que significa que Jesús esté realmente presente.",
               "La tercera respuesta es lo que Jesús promete para siempre."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "La Eucaristía es solo un símbolo sin ninguna importancia.", "respuesta": False},
        {"texto": "En la Eucaristía, Jesús está realmente presente.", "respuesta": True},
        {"texto": "Jesús promete vida eterna a quien recibe su cuerpo y sangre.", "respuesta": True},
        {"texto": "Recibir la Eucaristía no cambia nada en nuestra vida.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué es realmente la Eucaristía.",
               "Si una frase dice que la Eucaristía es solo un símbolo vacío, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué es la Eucaristía?",
         "opciones": ["La presencia viva de Jesús", "Solo un recuerdo", "Una comida cualquiera", "Un símbolo vacío"], "correcta": 0},
        {"texto": "¿Qué promete Jesús a quien recibe su cuerpo y sangre?",
         "opciones": ["Vida eterna", "Nada en especial", "Riqueza", "Fama"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que realmente sucede en la Eucaristía.",
               "Recuerda la promesa de Jesús a quien lo recibe."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "EUCARISTÍA", "definicion": "Presencia viva de Jesús"},
        {"termino": "CUERPO", "definicion": "Lo que recibimos bajo la forma del pan"},
        {"termino": "SANGRE", "definicion": "Lo que recibimos bajo la forma del vino"},
        {"termino": "VIVIR", "definicion": "Lo que Jesús promete para siempre"},
        {"termino": "PERMANECER", "definicion": "Quedarse en Jesús y Jesús en nosotros"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en qué recibimos bajo cada forma.",
               "PERMANECER describe una relación que dura, no un objeto."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: presencia viva",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "La Eucaristía es la ______ viva de Jesús.",
         "opciones": ["presencia", "ausencia", "idea"], "correcta": 0},
        {"texto": "Recibir la Eucaristía nos da vida ______.",
         "opciones": ["eterna", "corta", "difícil"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que celebramos en cada Misa.",
               "Recuerda la promesa de Jesús a quien lo recibe."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La Eucaristía es la presencia ______ de Jesús.", "respuesta": "VIVA", "banco": ["VIVA", "LEJANA", "ANTIGUA"]},
    ],
    "reflexion": "¿Cómo te sientes al saber que Jesús está realmente presente en la Eucaristía?",
    "requisito": 1,
    "pistas": ["Piensa en lo que hace especial a la Eucaristía.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: valoro ese regalo",
    "situacion": "Ya sabes que en la Eucaristía Jesús está realmente presente, no solo como recuerdo.",
    "items": [
        {"texto": "¿Qué puedes hacer tú para valorar más ese regalo?",
         "opciones": ["Prepararme con atención antes de comulgar",
                      "Dar gracias después de recibir la comunión",
                      "Participar con respeto en la Misa",
                      "Distraerme y no darle importancia"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra que valoras ese regalo."],
    "feedback_ok": "¡Muy bien! Valorar la Eucaristía también se nota en cómo la vivimos.",
})

# ==========================================================================
# PC06-C05 — La Misa y la comunión
# ==========================================================================
C = "PC06-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Misa y la comunión",
    "items": [
        {"texto": "Celebración donde revivimos la entrega de Jesús.", "respuesta": "MISA", "banco": ["MISA", "FIESTA", "REUNION"]},
        {"texto": "Recibir el cuerpo de Jesús en la Misa.", "respuesta": "COMUNION", "banco": ["COMUNION", "ENTRADA", "SALIDA"]},
        {"texto": "Lo que hacemos al repetir lo que hizo Jesús.", "respuesta": "MEMORIA", "banco": ["MEMORIA", "OLVIDO", "SILENCIO"]},
        {"texto": "Mesa donde se celebra la Eucaristía.", "respuesta": "ALTAR", "banco": ["ALTAR", "BANCO", "PASILLO"]},
        {"texto": "Quien preside la Misa.", "respuesta": "SACERDOTE", "banco": ["SACERDOTE", "CANTOR", "MONAGUILLO"]},
        {"texto": "Tomar parte activa en algo.", "respuesta": "PARTICIPAR", "banco": ["PARTICIPAR", "OBSERVAR", "IGNORAR"]},
    ],
    "incluir": ["MISA", "COMUNION"], "requisito": 4,
    "pistas": ["Piensa en lo que celebramos cada domingo.",
               "Todas las palabras se relacionan con la celebración de la Eucaristía."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Misa y la comunión",
    "palabras": ["MISA", "COMUNION", "MEMORIA", "ALTAR", "SACERDOTE", "PARTICIPAR"],
    "incluir": ["MISA", "COMUNION"], "requisito": 5,
    "pistas": ["MISA es una de las palabras más cortas: búscala primero.",
               "SACERDOTE y PARTICIPAR son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 11,23-26",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 11,23-26 y completa: «Haced esto en "
                  "______ de mí.»", "respuesta": "MEMORIA", "banco": ["MEMORIA", "SILENCIO", "SECRETO"]},
        {"texto": "¿Qué pidió Jesús que hiciéramos en memoria de él?", "abierta": True, "palabras_esperadas": ["MEMORIA", "RECORDAR", "PAN", "VINO", "MISA"], "respuestas_referencia": ["Pidió que repitiéramos esto, el pan y el vino, en memoria de él.", "Que celebráramos la cena en su memoria, como él la vivió.", "Que hiciéramos esto, partir el pan, para recordarlo siempre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta de san Pablo a los Corintios; el capítulo es el 11.",
               "San Pablo repite las mismas palabras que Jesús dijo en la Última Cena."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "En la Misa recordamos la ______ de Jesús.", "respuesta": "ENTREGA", "banco": ["ENTREGA", "FIESTA", "ESCUELA"]},
        {"texto": "Jesús pidió que hiciéramos esto en su ______.", "respuesta": "MEMORIA", "banco": ["MEMORIA", "OLVIDO", "SILENCIO"]},
        {"texto": "En la comunión recibimos a ______.", "respuesta": "JESUS", "banco": ["JESUS", "UN AMIGO", "UN REGALO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que celebramos cada vez que vamos a Misa.",
               "La tercera respuesta es a quien recibimos en la comunión."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "En la Misa revivimos lo que Jesús hizo en la Última Cena.", "respuesta": True},
        {"texto": "La comunión es recibir el cuerpo de Jesús.", "respuesta": True},
        {"texto": "La Misa no tiene relación con la Última Cena.", "respuesta": False},
        {"texto": "Jesús pidió que nos olvidáramos de lo que hizo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que celebramos en cada Misa.",
               "Si una frase dice que Jesús pidió que lo olvidáramos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué celebramos en la Misa?",
         "opciones": ["La entrega de Jesús en la Última Cena", "Un cumpleaños", "Una fiesta cualquiera", "Nada en especial"], "correcta": 0},
        {"texto": "¿Qué recibimos en la comunión?",
         "opciones": ["El cuerpo de Jesús", "Solo pan común", "Agua bendita", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús pidió que hiciéramos en su memoria.",
               "Recuerda lo que recibimos al comulgar."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "MISA", "definicion": "Celebración de la entrega de Jesús"},
        {"termino": "COMUNIÓN", "definicion": "Recibir el cuerpo de Jesús"},
        {"termino": "MEMORIA", "definicion": "Lo que Jesús pidió que hiciéramos"},
        {"termino": "ALTAR", "definicion": "Mesa de la celebración"},
        {"termino": "SACERDOTE", "definicion": "Quien preside la Misa"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en las partes y personas de la celebración.",
               "MEMORIA es lo que Jesús nos pidió hacer, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la Misa y la comunión",
    "instruccion": "En 45 segundos, marca las palabras que se relacionan con la Misa y la comunión.",
    "tiempo_segundos": 45,
    "banco": ["MISA", "COMUNION", "MEMORIA", "PARTICIPAR", "DISTRACCION", "PRISA"],
    "correctas": ["MISA", "COMUNION", "MEMORIA", "PARTICIPAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Misa - Comunión - Memoria - Participar.",
               "Descarta las palabras que muestran una actitud contraria a la celebración."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "En la Misa recibimos el cuerpo de Jesús en la ______.", "respuesta": "COMUNION", "banco": ["COMUNION", "ENTRADA", "FILA"]},
    ],
    "reflexion": "¿Cómo te preparas antes de ir a Misa?",
    "requisito": 1,
    "pistas": ["Piensa en el momento central de la Misa.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: participo mejor",
    "situacion": "Ya sabes que en la Misa revivimos la entrega de Jesús y que la comunión es recibirlo de verdad.",
    "items": [
        {"texto": "¿Qué puedes hacer tú para participar mejor en la Misa?",
         "opciones": ["Escuchar con atención la Palabra de Dios",
                      "Cantar y responder con el resto de la comunidad",
                      "Llegar con tiempo y prepararme antes de comulgar",
                      "Hablar con otros durante toda la Misa"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra verdadera participación."],
    "feedback_ok": "¡Muy bien! Participar bien en la Misa también es una forma de amar a Jesús.",
})

# ==========================================================================
# PC06-C06 — Participar con respeto y alegría
# ==========================================================================
C = "PC06-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: respeto y alegría",
    "items": [
        {"texto": "Actitud que mostramos al tratar algo sagrado con cuidado.", "respuesta": "RESPETO", "banco": ["RESPETO", "PRISA", "INDIFERENCIA"]},
        {"texto": "Lo que sentían los primeros cristianos al compartir el pan.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Tomar parte activa en la Misa.", "respuesta": "PARTICIPAR", "banco": ["PARTICIPAR", "OBSERVAR", "IGNORAR"]},
        {"texto": "Grupo de creyentes unidos en la fe.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "MULTITUD", "COMPETENCIA"]},
        {"texto": "Alimento que compartían los primeros cristianos.", "respuesta": "PAN", "banco": ["PAN", "ARROZ", "FRUTA"]},
        {"texto": "Actitud humilde y sin complicaciones.", "respuesta": "SENCILLEZ", "banco": ["SENCILLEZ", "ORGULLO", "LUJO"]},
    ],
    "incluir": ["RESPETO", "ALEGRIA"], "requisito": 4,
    "pistas": ["Piensa en cómo vivían su fe los primeros cristianos.",
               "Todas las palabras describen una buena actitud al participar."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: respeto y alegría",
    "palabras": ["RESPETO", "ALEGRIA", "PARTICIPAR", "COMUNIDAD", "PAN", "SENCILLEZ"],
    "incluir": ["RESPETO", "ALEGRIA"], "requisito": 5,
    "pistas": ["PAN es la palabra más corta: búscala primero.",
               "PARTICIPAR y COMUNIDAD son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 2,46",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 2,46 y completa: «Partían el pan... y tomaban el "
                  "alimento con ______ y sencillez de corazón.»", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "PRISA"]},
        {"texto": "¿Cómo participaban los primeros cristianos de la fracción del pan?", "abierta": True, "palabras_esperadas": ["ALEGRIA", "SENCILLEZ", "COMUNIDAD", "JUNTOS", "CASAS"], "respuestas_referencia": ["Participaban con alegría y sencillez de corazón, reunidos en las casas.", "Compartían el pan juntos, con alegría y de manera sencilla.", "Se reunían con alegría y sencillez para partir el pan juntos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles; el capítulo es el 2.",
               "El texto describe con qué actitud de corazón compartían su comida."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los primeros cristianos participaban con ______ y sencillez.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Se reunían como una verdadera ______.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "COMPETENCIA", "MULTITUD"]},
        {"texto": "Participar en la Misa merece nuestro ______.", "respuesta": "RESPETO", "banco": ["RESPETO", "DESINTERÉS", "OLVIDO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo vivían su fe los primeros cristianos.",
               "La tercera respuesta es la actitud que debemos tener ante algo sagrado."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los primeros cristianos compartían el pan con alegría.", "respuesta": True},
        {"texto": "Participar en la Misa no requiere ningún respeto.", "respuesta": False},
        {"texto": "La sencillez de corazón es parte de cómo vivían su fe.", "respuesta": True},
        {"texto": "A los primeros cristianos no les importaba reunirse.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda con qué actitud compartían el pan los primeros cristianos.",
               "Si una frase dice que no les importaba reunirse, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo participaban los primeros cristianos en la fracción del pan?",
         "opciones": ["Con alegría y sencillez", "Con indiferencia", "Con miedo", "A escondidas"], "correcta": 0},
        {"texto": "¿Qué actitud debemos tener al participar en la Misa?",
         "opciones": ["Respeto y alegría", "Prisa y distracción", "Indiferencia", "Aburrimiento"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Recuerda con qué actitud de corazón se reunían los primeros cristianos.",
               "Piensa en cómo te gustaría que otros te trataran si tú presidieras algo importante."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "RESPETO", "definicion": "Actitud ante algo sagrado"},
        {"termino": "ALEGRÍA", "definicion": "Sentimiento al compartir con los demás"},
        {"termino": "COMUNIDAD", "definicion": "Grupo unido en la fe"},
        {"termino": "SENCILLEZ", "definicion": "Actitud humilde de corazón"},
        {"termino": "PARTICIPAR", "definicion": "Tomar parte activa en la celebración"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en las actitudes de los primeros cristianos.",
               "SENCILLEZ describe una forma de ser, no un grupo de personas."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: cómo vivían su fe",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo vivían su fe los primeros cristianos.",
    "tiempo_segundos": 45,
    "banco": ["RESPETO", "ALEGRIA", "SENCILLEZ", "COMUNIDAD", "PRISA", "DISTRACCION"],
    "correctas": ["RESPETO", "ALEGRIA", "SENCILLEZ", "COMUNIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Respeto - Alegría - Sencillez - Comunidad.",
               "Descarta las palabras que muestran una mala actitud."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los primeros cristianos compartían el pan con ______ y sencillez de corazón.",
         "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "PRISA", "MIEDO"]},
    ],
    "reflexion": "¿Con qué actitud participas tú en la Misa?",
    "requisito": 1,
    "pistas": ["Piensa en la actitud de corazón de los primeros cristianos.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: participo con respeto y alegría",
    "situacion": "Ya sabes que los primeros cristianos participaban de la fracción del pan con respeto y alegría.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para participar mejor en la Misa?",
         "opciones": ["Llegar con actitud de respeto y alegría",
                      "Ayudar a que otros también participen bien",
                      "Prepararme con tiempo antes de ir",
                      "Distraerme y hablar con otros durante la Misa"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no muestra respeto ni alegría."],
    "feedback_ok": "¡Muy bien! Vivir con respeto y alegría también es una forma de anunciar tu fe.",
})

# ==========================================================================
# ==========================================================================
# PC07 — El Espíritu Santo nos da fuerza   (Encuentro 7, Hechos 2,1-4)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC07-C01 — Pentecostés
# ==========================================================================
C = "PC07-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Pentecostés",
    "items": [
        {"texto": "Fiesta en la que el Espíritu Santo descendió sobre los apóstoles.", "respuesta": "PENTECOSTES", "banco": ["PENTECOSTES", "NAVIDAD", "PASCUA"]},
        {"texto": "Quien llegó sobre los apóstoles como fuego y viento.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "ANGEL", "PROFETA"]},
        {"texto": "Forma en que se posó el Espíritu Santo sobre cada uno.", "respuesta": "FUEGO", "banco": ["FUEGO", "HUMO", "AGUA"]},
        {"texto": "Sonido fuerte que se escuchó del cielo, como un recio ______.", "respuesta": "VIENTO", "banco": ["VIENTO", "TRUENO", "GRITO"]},
        {"texto": "Quienes recibieron al Espíritu Santo reunidos en un mismo lugar.", "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "SOLDADOS", "FARISEOS"]},
        {"texto": "Lo que los apóstoles empezaron a hablar en distintos idiomas.", "respuesta": "LENGUAS", "banco": ["LENGUAS", "CANTOS", "GRITOS"]},
    ],
    "incluir": ["PENTECOSTES", "ESPIRITU"], "requisito": 4,
    "pistas": ["Piensa en el día en que bajó el Espíritu Santo sobre los apóstoles.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Pentecostés",
    "palabras": ["PENTECOSTES", "ESPIRITU", "FUEGO", "VIENTO", "APOSTOLES", "LENGUAS"],
    "incluir": ["PENTECOSTES", "ESPIRITU"], "requisito": 5,
    "pistas": ["FUEGO es una de las palabras más cortas: búscala primero.",
               "PENTECOSTÉS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 2,1-4",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 2,1-4 y completa: «Se llenaron todos de Espíritu "
                  "______.»", "respuesta": "SANTO", "banco": ["SANTO", "SOLO", "LEJANO"]},
        {"texto": "¿Qué sucedió el día de Pentecostés?", "abierta": True, "palabras_esperadas": ["ESPIRITU", "SANTO", "FUEGO", "VIENTO", "LENGUAS"], "respuestas_referencia": ["Los apóstoles se llenaron del Espíritu Santo y hablaron en otras lenguas.", "Bajó como un viento fuerte y lenguas de fuego sobre cada uno.", "El Espíritu Santo descendió sobre ellos como fuego y viento."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles; el capítulo es el 2.",
               "El texto describe un ruido como de viento fuerte y algo parecido a lenguas de fuego."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El día de ______ bajó el Espíritu Santo.", "respuesta": "PENTECOSTES", "banco": ["PENTECOSTES", "NAVIDAD", "PASCUA"]},
        {"texto": "El Espíritu Santo se posó como lenguas de ______.", "respuesta": "FUEGO", "banco": ["FUEGO", "HUMO", "AGUA"]},
        {"texto": "Los apóstoles empezaron a hablar en otras ______.", "respuesta": "LENGUAS", "banco": ["LENGUAS", "VOCES", "CANCIONES"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el nombre de esta fiesta.",
               "La segunda respuesta describe cómo se posó el Espíritu Santo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "En Pentecostés el Espíritu Santo bajó sobre los apóstoles.", "respuesta": True},
        {"texto": "Los apóstoles estaban solos y dispersos ese día.", "respuesta": False},
        {"texto": "El Espíritu Santo se manifestó como viento y fuego.", "respuesta": True},
        {"texto": "Pentecostés no tiene relación con el Espíritu Santo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo se manifestó el Espíritu Santo ese día.",
               "Si una frase dice que Pentecostés no tiene relación con el Espíritu Santo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué recibieron los apóstoles en Pentecostés?",
         "opciones": ["El Espíritu Santo", "Solo un mensaje", "Nada especial", "Una visita"], "correcta": 0},
        {"texto": "¿Cómo se manifestó el Espíritu Santo?",
         "opciones": ["Como viento y fuego", "Como un terremoto", "Como lluvia", "Como oscuridad"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que recibieron los apóstoles ese día.",
               "Recuerda las dos señales que describe el texto."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PENTECOSTÉS", "definicion": "Fiesta en que bajó el Espíritu Santo"},
        {"termino": "ESPÍRITU", "definicion": "Quien llenó a los apóstoles"},
        {"termino": "FUEGO", "definicion": "Forma en que se posó sobre cada uno"},
        {"termino": "VIENTO", "definicion": "Sonido fuerte que se escuchó del cielo"},
        {"termino": "LENGUAS", "definicion": "Lo que los apóstoles hablaron de nuevas formas"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en las señales que acompañaron la llegada del Espíritu Santo.",
               "LENGUAS se refiere a idiomas, no a un objeto."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: Pentecostés",
    "instruccion": "En 45 segundos, marca las palabras que se relacionan con Pentecostés.",
    "tiempo_segundos": 45,
    "banco": ["PENTECOSTES", "ESPIRITU", "FUEGO", "VIENTO", "SILENCIO", "MIEDO"],
    "correctas": ["PENTECOSTES", "ESPIRITU", "FUEGO", "VIENTO"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Pentecostés - Espíritu - Fuego - Viento.",
               "Descarta las palabras que no aparecieron en este relato."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El día de Pentecostés bajó el ______ Santo sobre los apóstoles.",
         "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "VIENTO", "ANGEL"]},
    ],
    "reflexion": "¿Qué crees que sintieron los apóstoles ese día?",
    "requisito": 1,
    "pistas": ["Piensa en quién descendió sobre los apóstoles.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: pido fuerza al Espíritu Santo",
    "situacion": "Ya sabes que en Pentecostés el Espíritu Santo llenó de fuerza a los apóstoles.",
    "items": [
        {"texto": "¿Qué puedes pedirle tú al Espíritu Santo esta semana?",
         "opciones": ["Fuerza para hacer el bien",
                      "Valor para defender lo que es justo",
                      "Ayuda para perdonar a alguien",
                      "Nada, prefiero no pedir nada"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una petición concreta, no en una idea.",
               "Descarta la única opción que muestra indiferencia."],
    "feedback_ok": "¡Muy bien! Pedirle al Espíritu Santo también es una forma de orar.",
})

# ==========================================================================
# PC07-C02 — El Espíritu Santo llega a los apóstoles
# ==========================================================================
C = "PC07-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Espíritu llega",
    "items": [
        {"texto": "Lo que Jesús hizo antes de decir «recibid el Espíritu Santo».", "respuesta": "SOPLO", "banco": ["SOPLO", "GRITO", "SILENCIO"]},
        {"texto": "Lo que Jesús deseó a sus discípulos al aparecerse resucitado.", "respuesta": "PAZ", "banco": ["PAZ", "MIEDO", "DUDA"]},
        {"texto": "Tarea que Jesús encomienda a sus discípulos.", "respuesta": "MISION", "banco": ["MISION", "VACACION", "CASTIGO"]},
        {"texto": "Aquellos a quienes Jesús envía, como el Padre lo envió a él.", "respuesta": "DISCIPULOS", "banco": ["DISCIPULOS", "SOLDADOS", "REYES"]},
        {"texto": "Lo que Jesús hace con sus discípulos, como el Padre lo hizo con él.", "respuesta": "ENVIO", "banco": ["ENVIO", "OLVIDO", "DEJO"]},
        {"texto": "Palabra que Jesús dijo al dar el Espíritu Santo.", "respuesta": "RECIBID", "banco": ["RECIBID", "BUSCAD", "ESPERAD"]},
    ],
    "incluir": ["SOPLO", "PAZ"], "requisito": 4,
    "pistas": ["Piensa en lo que hizo Jesús al aparecerse resucitado.",
               "Todas las palabras hablan del envío y del Espíritu Santo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Espíritu llega",
    "palabras": ["ENVIO", "SOPLO", "RECIBID", "PAZ", "MISION", "DISCIPULOS"],
    "incluir": ["SOPLO", "PAZ"], "requisito": 5,
    "pistas": ["PAZ es la palabra más corta: búscala primero.",
               "DISCÍPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 20,21-22",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 20,21-22 y completa: «Como el Padre me envió, "
                  "también yo os ______.»", "respuesta": "ENVIO", "banco": ["ENVIO", "DEJO", "OLVIDO"]},
        {"texto": "¿Qué hizo Jesús resucitado con sus discípulos?", "abierta": True, "palabras_esperadas": ["SOPLO", "ESPIRITU", "PAZ", "ENVIO", "MISION"], "respuestas_referencia": ["Sopló sobre ellos y les dijo que recibieran el Espíritu Santo.", "Les dio la paz y los envió como el Padre lo había enviado a él.", "Sopló sobre ellos, les dio el Espíritu Santo y los envió en misión."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 20.",
               "Jesús se aparece resucitado, les desea la paz y hace un gesto muy especial."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús ______ sobre sus discípulos y les dio el Espíritu Santo.", "respuesta": "SOPLO", "banco": ["SOPLO", "GRITÓ", "CALLÓ"]},
        {"texto": "Jesús les deseó ______ al aparecerse.", "respuesta": "PAZ", "banco": ["PAZ", "MIEDO", "DUDA"]},
        {"texto": "Jesús envía a sus discípulos en ______.", "respuesta": "MISION", "banco": ["MISION", "VACACIONES", "CASTIGO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el gesto que hizo Jesús antes de hablar.",
               "La segunda respuesta es el saludo de Jesús resucitado."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús sopló sobre sus discípulos y les dio el Espíritu Santo.", "respuesta": True},
        {"texto": "Jesús envió a sus discípulos igual que el Padre lo envió a él.", "respuesta": True},
        {"texto": "Jesús no quería que sus discípulos hicieran nada más.", "respuesta": False},
        {"texto": "Jesús les deseó la paz al aparecerse resucitado.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que hizo y dijo Jesús al aparecerse resucitado.",
               "Si una frase dice que Jesús no quería que hicieran nada más, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hizo Jesús antes de dar el Espíritu Santo?",
         "opciones": ["Sopló sobre ellos", "Los regañó", "Se fue en silencio", "Nada"], "correcta": 0},
        {"texto": "¿Para qué envía Jesús a sus discípulos?",
         "opciones": ["Para continuar su misión", "Para descansar", "Para esconderse", "Para nada en particular"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el gesto de Jesús antes de sus palabras.",
               "Recuerda para qué envía Jesús a sus discípulos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SOPLO", "definicion": "Gesto de Jesús al dar el Espíritu Santo"},
        {"termino": "PAZ", "definicion": "Lo que Jesús deseó a sus discípulos"},
        {"termino": "MISIÓN", "definicion": "Tarea que Jesús encomienda"},
        {"termino": "ENVÍO", "definicion": "Lo que Jesús hace, como el Padre lo hizo con él"},
        {"termino": "DISCÍPULOS", "definicion": "Quienes reciben el Espíritu y la misión"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el gesto, el saludo y la tarea de Jesús.",
               "ENVÍO describe una acción, no una persona."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: el envío de Jesús",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús ______ sobre sus discípulos.",
         "opciones": ["sopló", "gritó", "calló"], "correcta": 0},
        {"texto": "Jesús deseó ______ a sus discípulos.",
         "opciones": ["paz", "miedo", "dudas"], "correcta": 0},
        {"texto": "Jesús los envía a continuar su ______.",
         "opciones": ["misión", "vacación", "castigo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Recuerda el gesto y el saludo de Jesús resucitado.",
               "Piensa en la tarea que Jesús encomienda a sus discípulos."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús ______ sobre sus discípulos y les dio el Espíritu Santo.",
         "respuesta": "SOPLO", "banco": ["SOPLO", "GRITO", "CALLO"]},
    ],
    "reflexion": "¿Qué misión crees que Jesús te encomienda a ti?",
    "requisito": 1,
    "pistas": ["Piensa en el gesto de Jesús antes de sus palabras.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo la misión de Jesús",
    "situacion": "Ya sabes que Jesús envía a sus discípulos con su Espíritu, como el Padre lo envió a él.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para vivir esa misión?",
         "opciones": ["Hablar de Jesús con alguien cercano",
                      "Ayudar a otros con alegría",
                      "Llevar la paz a mi casa o mi grupo",
                      "Quedarme sin hacer nada"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que muestra indiferencia."],
    "feedback_ok": "¡Muy bien! Llevar la paz y el amor de Jesús también es cumplir su misión.",
})

# ==========================================================================
# PC07-C03 — Fuerza, alegría y valor
# ==========================================================================
C = "PC07-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: fuerza y valor",
    "items": [
        {"texto": "Lo que el Espíritu Santo da para enfrentar dificultades.", "respuesta": "FUERZA", "banco": ["FUERZA", "DEBILIDAD", "DUDA"]},
        {"texto": "Actuar sin miedo aunque haya peligro.", "respuesta": "VALOR", "banco": ["VALOR", "TEMOR", "VERGÜENZA"]},
        {"texto": "Lo que sentían los discípulos al anunciar la fe.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Lo que los discípulos hicieron con valentía después de orar.", "respuesta": "HABLAR", "banco": ["HABLAR", "CALLAR", "HUIR"]},
        {"texto": "Lo que el Espíritu Santo ayuda a vencer.", "respuesta": "TEMOR", "banco": ["TEMOR", "GOZO", "AMOR"]},
        {"texto": "Quien da fuerza y valor a los discípulos.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "ANGEL", "PROFETA"]},
    ],
    "incluir": ["FUERZA", "VALOR"], "requisito": 4,
    "pistas": ["Piensa en lo que sintieron los discípulos después de orar juntos.",
               "Todas las palabras hablan de cómo el Espíritu Santo transforma el miedo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: fuerza y valor",
    "palabras": ["FUERZA", "VALOR", "ALEGRIA", "HABLAR", "TEMOR", "ESPIRITU"],
    "incluir": ["FUERZA", "VALOR"], "requisito": 5,
    "pistas": ["VALOR es una de las palabras más cortas: búscala primero.",
               "ESPÍRITU es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 4,31",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 4,31 y completa: «Se llenaron todos del Espíritu "
                  "Santo y hablaban la palabra de Dios con ______.»", "respuesta": "DENUEDO", "banco": ["DENUEDO", "MIEDO", "SILENCIO"]},
        {"texto": "¿Cómo cambió el Espíritu Santo la manera de hablar de los discípulos?", "abierta": True, "palabras_esperadas": ["FUERZA", "VALOR", "VALENTIA", "DENUEDO", "ESPIRITU"], "respuestas_referencia": ["Los llenó de valor y hablaban la palabra de Dios sin miedo.", "Les dio fuerza para hablar con valentía, ya sin temor.", "Cambió su temor en valentía para anunciar la palabra de Dios."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles; el capítulo es el 4.",
               "El texto describe cómo hablaban los discípulos después de orar juntos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo da ______ para hablar sin miedo.", "respuesta": "FUERZA", "banco": ["FUERZA", "DEBILIDAD", "DUDA"]},
        {"texto": "Los discípulos hablaban con ______ después de orar.", "respuesta": "VALOR", "banco": ["VALOR", "TEMOR", "VERGÜENZA"]},
        {"texto": "El Espíritu Santo ayuda a vencer el ______.", "respuesta": "TEMOR", "banco": ["TEMOR", "GOZO", "AMOR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que da el Espíritu Santo ante las dificultades.",
               "La tercera respuesta es lo que ayuda a superar el Espíritu Santo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo da fuerza y valor a los discípulos.", "respuesta": True},
        {"texto": "Después de orar, los discípulos hablaron con más miedo.", "respuesta": False},
        {"texto": "El Espíritu Santo ayuda a superar el temor.", "respuesta": True},
        {"texto": "La alegría no tiene relación con el Espíritu Santo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo cambió la actitud de los discípulos después de orar.",
               "Si una frase dice que la alegría no tiene relación con el Espíritu Santo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué recibieron los discípulos después de orar?",
         "opciones": ["Fuerza y valor para hablar", "Más miedo", "Cansancio", "Indiferencia"], "correcta": 0},
        {"texto": "¿Qué ayuda a vencer el Espíritu Santo?",
         "opciones": ["El temor", "La alegría", "La fe", "El amor"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que cambió en los discípulos después de orar.",
               "Recuerda qué sentimiento negativo transforma el Espíritu Santo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FUERZA", "definicion": "Lo que da el Espíritu Santo ante las dificultades"},
        {"termino": "VALOR", "definicion": "Actuar sin miedo aunque haya peligro"},
        {"termino": "ALEGRÍA", "definicion": "Lo que sentían al anunciar la fe"},
        {"termino": "TEMOR", "definicion": "Lo que el Espíritu Santo ayuda a vencer"},
        {"termino": "HABLAR", "definicion": "Lo que hicieron con valentía después de orar"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que sintieron y en lo que hicieron los discípulos.",
               "TEMOR es lo que se vence, no lo que se recibe."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: lo que da el Espíritu",
    "instruccion": "En 45 segundos, marca las palabras que describen lo que el Espíritu Santo da a los discípulos.",
    "tiempo_segundos": 45,
    "banco": ["FUERZA", "VALOR", "ALEGRIA", "CONFIANZA", "TEMOR", "SILENCIO"],
    "correctas": ["FUERZA", "VALOR", "ALEGRIA", "CONFIANZA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Fuerza - Valor - Alegría - Confianza.",
               "Descarta las palabras que describen lo que el Espíritu Santo ayuda a vencer."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Después de orar, los discípulos hablaban la palabra de Dios con ______.",
         "respuesta": "VALOR", "banco": ["VALOR", "MIEDO", "DUDA"]},
    ],
    "reflexion": "¿Cuándo has sentido que Dios te da fuerza para algo difícil?",
    "requisito": 1,
    "pistas": ["Piensa en cómo hablaban los discípulos después de orar.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: uso esa fuerza",
    "situacion": "Ya sabes que el Espíritu Santo da fuerza, valor y alegría para vivir y anunciar la fe.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana con esa fuerza?",
         "opciones": ["Hablar de Jesús sin miedo a la burla",
                      "Defender a alguien que es tratado injustamente",
                      "Hacer lo correcto aunque sea difícil",
                      "Quedarme callado por miedo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que muestra miedo en vez de valor."],
    "feedback_ok": "¡Muy bien! Actuar con valor también es dejarte guiar por el Espíritu Santo.",
})

# ==========================================================================
# PC07-C04 — Dones del Espíritu
# ==========================================================================
C = "PC07-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: dones del Espíritu",
    "items": [
        {"texto": "Regalos que el Espíritu Santo reparte a cada uno.", "respuesta": "DONES", "banco": ["DONES", "CASTIGOS", "PROBLEMAS"]},
        {"texto": "Quien reparte los dones a cada persona.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "ANGEL", "PROFETA"]},
        {"texto": "Los dones no son todos iguales, son ______.", "respuesta": "DIVERSOS", "banco": ["DIVERSOS", "IGUALES", "INUTILES"]},
        {"texto": "Para qué se usan los dones del Espíritu.", "respuesta": "SERVICIO", "banco": ["SERVICIO", "COMPETENCIA", "ORGULLO"]},
        {"texto": "Lo que buscan los dones del Espíritu para la comunidad.", "respuesta": "BIEN", "banco": ["BIEN", "DAÑO", "OLVIDO"]},
        {"texto": "Lo que se busca junto a los demás, no solo para uno.", "respuesta": "COMUN", "banco": ["COMUN", "PROPIO", "PERSONAL"]},
    ],
    "incluir": ["DONES", "ESPIRITU"], "requisito": 4,
    "pistas": ["Piensa en lo que san Pablo dice sobre los distintos dones.",
               "Todas las palabras hablan de los regalos que reparte el Espíritu Santo."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: dones del Espíritu",
    "palabras": ["DONES", "ESPIRITU", "DIVERSOS", "SERVICIO", "BIEN", "COMUN"],
    "incluir": ["DONES", "ESPIRITU"], "requisito": 5,
    "pistas": ["DONES y BIEN son de las palabras más cortas: búscalas primero.",
               "DIVERSOS y SERVICIO son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 12,4-7",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 12,4-7 y completa: «Hay diversidad de "
                  "______, pero un mismo Espíritu.»", "respuesta": "DONES", "banco": ["DONES", "PROBLEMAS", "DUDAS"]},
        {"texto": "¿Qué dice san Pablo sobre los distintos dones?", "abierta": True, "palabras_esperadas": ["DONES", "DIVERSOS", "ESPIRITU", "SERVICIO", "BIEN", "COMUN"], "respuestas_referencia": ["Dice que hay diversos dones, pero es el mismo Espíritu quien los da.", "Que cada uno recibe un don distinto, para el bien de todos.", "Que los dones son diferentes, pero todos vienen del mismo Espíritu y sirven a la comunidad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta de san Pablo a los Corintios; el capítulo es el 12.",
               "San Pablo compara los distintos dones con un mismo origen: el Espíritu."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo reparte ______ distintos a cada uno.", "respuesta": "DONES", "banco": ["DONES", "CASTIGOS", "PROBLEMAS"]},
        {"texto": "Los dones se usan para el ______ de todos.", "respuesta": "BIEN", "banco": ["BIEN", "DAÑO", "OLVIDO"]},
        {"texto": "Cada persona recibe un don ______.", "respuesta": "DIVERSO", "banco": ["DIVERSO", "IGUAL", "INUTIL"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que reparte el Espíritu Santo a cada persona.",
               "La segunda respuesta es para qué sirven los dones."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo reparte dones distintos a cada persona.", "respuesta": True},
        {"texto": "Los dones del Espíritu son solo para el que los recibe.", "respuesta": False},
        {"texto": "Los dones sirven para el bien de la comunidad.", "respuesta": True},
        {"texto": "Todos los dones son exactamente iguales.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda para qué sirven los dones del Espíritu.",
               "Si una frase dice que los dones son solo para uno mismo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué reparte el Espíritu Santo, según san Pablo?",
         "opciones": ["Dones diversos", "Solo un don igual para todos", "Nada", "Castigos"], "correcta": 0},
        {"texto": "¿Para qué sirven los dones del Espíritu?",
         "opciones": ["Para el bien de todos", "Solo para uno mismo", "Para competir", "Para nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que reparte el Espíritu Santo.",
               "Recuerda para quién son los dones, según san Pablo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DONES", "definicion": "Regalos que reparte el Espíritu Santo"},
        {"termino": "DIVERSOS", "definicion": "Los dones no son todos iguales"},
        {"termino": "SERVICIO", "definicion": "Para qué se usan los dones"},
        {"termino": "BIEN", "definicion": "Lo que buscan los dones para la comunidad"},
        {"termino": "ESPÍRITU", "definicion": "Quien reparte los dones"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en quién reparte los dones y para qué sirven.",
               "DIVERSOS describe una característica de los dones."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: los dones del Espíritu",
    "instruccion": "En 45 segundos, marca las palabras que describen los dones del Espíritu.",
    "tiempo_segundos": 45,
    "banco": ["DONES", "SERVICIO", "BIEN", "COMUN", "EGOISMO", "COMPETENCIA"],
    "correctas": ["DONES", "SERVICIO", "BIEN", "COMUN"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Dones - Servicio - Bien - Común.",
               "Descarta las palabras que muestran una actitud contraria a compartir."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu Santo reparte dones ______ a cada persona, para el bien de todos.",
         "respuesta": "DIVERSOS", "banco": ["DIVERSOS", "IGUALES", "INUTILES"]},
    ],
    "reflexion": "¿Qué don crees que Dios te ha dado a ti?",
    "requisito": 1,
    "pistas": ["Piensa en lo que reparte el Espíritu Santo a cada persona.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: uso mi don para servir",
    "situacion": "Ya sabes que cada uno recibe del Espíritu Santo un don distinto, para el bien de todos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana con el don que tienes?",
         "opciones": ["Usarlo para ayudar a mi familia o mis amigos",
                      "Compartirlo con mi grupo de catequesis",
                      "Ponerlo al servicio de alguien que lo necesite",
                      "Guardarlo solo para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no comparte el don con nadie."],
    "feedback_ok": "¡Muy bien! Compartir tus dones también es servir a los demás.",
})

# ==========================================================================
# PC07-C05 — El Espíritu guía la fe
# ==========================================================================
C = "PC07-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Espíritu guía",
    "items": [
        {"texto": "Nombre que Jesús da al Espíritu Santo, quien acompaña y da ánimo.", "respuesta": "CONSOLADOR", "banco": ["CONSOLADOR", "EXTRAÑO", "ENEMIGO"]},
        {"texto": "Lo que el Espíritu Santo hace con los discípulos, como maestro.", "respuesta": "ENSEÑA", "banco": ["ENSEÑA", "CONFUNDE", "IGNORA"]},
        {"texto": "Lo que el Espíritu Santo ayuda a no olvidar.", "respuesta": "RECUERDA", "banco": ["RECUERDA", "BORRA", "OCULTA"]},
        {"texto": "Lo que el Espíritu Santo hace con nuestra fe, como un camino.", "respuesta": "GUIA", "banco": ["GUIA", "COMPLICA", "DETIENE"]},
        {"texto": "Lo que el Espíritu Santo enseña, sin engaño.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
        {"texto": "Lo que el Espíritu Santo fortalece en nosotros.", "respuesta": "FE", "banco": ["FE", "MIEDO", "DUDA"]},
    ],
    "incluir": ["CONSOLADOR", "GUIA"], "requisito": 4,
    "pistas": ["Piensa en el nombre que Jesús le da al Espíritu Santo.",
               "Todas las palabras hablan de cómo el Espíritu Santo acompaña nuestra fe."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Espíritu guía",
    "palabras": ["CONSOLADOR", "ENSEÑA", "RECUERDA", "GUIA", "VERDAD", "FE"],
    "incluir": ["CONSOLADOR", "GUIA"], "requisito": 5,
    "pistas": ["FE es la palabra más corta: búscala primero.",
               "CONSOLADOR es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 14,26",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 14,26 y completa: «El Espíritu Santo... os lo "
                  "______ todo y os recordará todo lo que os he dicho.»", "respuesta": "ENSEÑARA", "banco": ["ENSEÑARA", "OCULTARA", "OLVIDARA"]},
        {"texto": "¿Qué promete Jesús que hará el Espíritu Santo?", "abierta": True, "palabras_esperadas": ["ENSEÑA", "RECUERDA", "GUIA", "VERDAD", "CONSOLADOR"], "respuestas_referencia": ["Promete que el Espíritu les enseñará todo y les recordará sus palabras.", "Que el Espíritu Santo, el Consolador, los guiará en la verdad.", "Que enseñará y recordará a los discípulos todo lo que Jesús dijo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 14.",
               "Jesús promete enviar al Espíritu Santo con dos tareas: enseñar y recordar."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo nos ______ el camino de la fe.", "respuesta": "GUIA", "banco": ["GUIA", "COMPLICA", "OLVIDA"]},
        {"texto": "Jesús llama al Espíritu Santo ______.", "respuesta": "CONSOLADOR", "banco": ["CONSOLADOR", "EXTRAÑO", "ENEMIGO"]},
        {"texto": "El Espíritu Santo nos ayuda a recordar la ______.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con nuestra fe.",
               "La segunda respuesta es el nombre que Jesús le da al Espíritu Santo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo nos ayuda a recordar las palabras de Jesús.", "respuesta": True},
        {"texto": "El Espíritu Santo no tiene nada que ver con nuestra fe.", "respuesta": False},
        {"texto": "Jesús llama al Espíritu Santo el Consolador.", "respuesta": True},
        {"texto": "El Espíritu Santo nos aleja de la verdad.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda las tareas que Jesús promete que hará el Espíritu Santo.",
               "Si una frase dice que el Espíritu Santo nos aleja de la verdad, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hace el Espíritu Santo, según Jesús?",
         "opciones": ["Enseña y recuerda su palabra", "Nos hace olvidar", "Nos confunde", "Nada"], "correcta": 0},
        {"texto": "¿Cómo llama Jesús al Espíritu Santo?",
         "opciones": ["Consolador", "Juez", "Extraño", "Enemigo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en las dos tareas que Jesús promete del Espíritu Santo.",
               "Recuerda el nombre especial que Jesús usa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CONSOLADOR", "definicion": "Nombre que Jesús da al Espíritu Santo"},
        {"termino": "ENSEÑA", "definicion": "Lo que hace el Espíritu Santo con los discípulos"},
        {"termino": "RECUERDA", "definicion": "Lo que el Espíritu Santo ayuda a no olvidar"},
        {"termino": "GUÍA", "definicion": "Lo que el Espíritu Santo hace con nuestra fe"},
        {"termino": "VERDAD", "definicion": "Lo que el Espíritu Santo enseña, sin engaño"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el nombre y en las tareas del Espíritu Santo.",
               "CONSOLADOR es un nombre, no una acción."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: el Espíritu nos guía",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El Espíritu Santo nos ______ el camino de la fe.",
         "opciones": ["guía", "complica", "olvida"], "correcta": 0},
        {"texto": "Jesús llama al Espíritu Santo ______.",
         "opciones": ["Consolador", "extraño", "enemigo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el camino que el Espíritu Santo traza en nuestra fe.",
               "Recuerda el nombre especial que Jesús usa para el Espíritu Santo."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu Santo nos ayuda a recordar las ______ de Jesús.",
         "respuesta": "PALABRAS", "banco": ["PALABRAS", "DUDAS", "DISTANCIAS"]},
    ],
    "reflexion": "¿En qué momento sientes que el Espíritu Santo te guía?",
    "requisito": 1,
    "pistas": ["Piensa en las dos tareas del Espíritu Santo que enseña Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: me dejo guiar",
    "situacion": "Ya sabes que el Espíritu Santo nos enseña, nos recuerda y guía nuestra fe.",
    "items": [
        {"texto": "¿Qué puedes hacer tú para dejarte guiar más por el Espíritu Santo?",
         "opciones": ["Pedirle su ayuda antes de decidir algo importante",
                      "Escuchar la Palabra de Dios con más atención",
                      "Pedir su guía en la oración",
                      "Ignorar su ayuda y decidir siempre solo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no busca la guía del Espíritu Santo."],
    "feedback_ok": "¡Muy bien! Dejarte guiar por el Espíritu Santo también fortalece tu fe.",
})

# ==========================================================================
# PC07-C06 — Testimonio alegre
# ==========================================================================
C = "PC07-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: testimonio alegre",
    "items": [
        {"texto": "Resultado visible de tener al Espíritu Santo en la vida.", "respuesta": "FRUTOS", "banco": ["FRUTOS", "CASTIGOS", "PROBLEMAS"]},
        {"texto": "El primer fruto del Espíritu que menciona san Pablo.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "ENOJO"]},
        {"texto": "Fruto del Espíritu que se nota en un corazón contento.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "ENVIDIA"]},
        {"texto": "Fruto del Espíritu que se nota en un corazón tranquilo.", "respuesta": "PAZ", "banco": ["PAZ", "PRISA", "ENOJO"]},
        {"texto": "Mostrar con la vida lo que se cree.", "respuesta": "TESTIMONIO", "banco": ["TESTIMONIO", "SILENCIO", "DISTANCIA"]},
        {"texto": "Fruto del Espíritu que se muestra al hacer el bien a otros.", "respuesta": "BONDAD", "banco": ["BONDAD", "MALDAD", "PEREZA"]},
    ],
    "incluir": ["FRUTOS", "AMOR"], "requisito": 4,
    "pistas": ["Piensa en lo que produce el Espíritu Santo en quien lo recibe.",
               "Todas las palabras hablan de cómo se nota el Espíritu Santo en la vida diaria."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: testimonio alegre",
    "palabras": ["FRUTOS", "AMOR", "ALEGRIA", "PAZ", "TESTIMONIO", "BONDAD"],
    "incluir": ["FRUTOS", "AMOR"], "requisito": 5,
    "pistas": ["AMOR y PAZ son de las palabras más cortas: búscalas primero.",
               "TESTIMONIO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Gálatas 5,22-23",
    "items": [
        {"texto": "Busca en tu Biblia Católica Gálatas 5,22-23 y completa: «El fruto del Espíritu es "
                  "amor, ______, paz...»", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "ENVIDIA"]},
        {"texto": "¿Qué frutos produce el Espíritu Santo en quien lo recibe?", "abierta": True, "palabras_esperadas": ["AMOR", "ALEGRIA", "PAZ", "BONDAD", "FRUTOS"], "respuestas_referencia": ["Produce amor, alegría, paz, paciencia y bondad, entre otros frutos.", "Da como fruto el amor, la alegría, la paz y la bondad.", "El Espíritu produce amor, alegría y paz en quien lo recibe."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta de san Pablo a los Gálatas; el capítulo es el 5.",
               "San Pablo enumera una lista de frutos, uno después del otro."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El fruto del Espíritu comienza con el ______.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "ENOJO"]},
        {"texto": "Otro fruto del Espíritu es la ______.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "ENVIDIA"]},
        {"texto": "Vivir con los frutos del Espíritu es dar ______ de fe.", "respuesta": "TESTIMONIO", "banco": ["TESTIMONIO", "SILENCIO", "DISTANCIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la lista de frutos que menciona san Pablo.",
               "La tercera respuesta es mostrar con la vida lo que se cree."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El amor es uno de los frutos del Espíritu Santo.", "respuesta": True},
        {"texto": "La tristeza es un fruto del Espíritu Santo.", "respuesta": False},
        {"texto": "Nuestra vida puede dar testimonio de fe con alegría.", "respuesta": True},
        {"texto": "Los frutos del Espíritu no se notan en la vida diaria.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la lista de frutos que menciona san Pablo.",
               "Si una frase dice que los frutos no se notan en la vida diaria, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cuál de estos es un fruto del Espíritu Santo?",
         "opciones": ["La alegría", "La envidia", "El enojo", "El miedo"], "correcta": 0},
        {"texto": "¿Qué significa dar testimonio alegre de la fe?",
         "opciones": ["Mostrar con la vida lo que creemos", "Esconder lo que creemos", "Discutir con los demás", "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la lista de frutos que menciona san Pablo.",
               "Recuerda qué significa vivir con testimonio."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FRUTOS", "definicion": "Resultado visible de tener al Espíritu Santo"},
        {"termino": "AMOR", "definicion": "Primer fruto que menciona san Pablo"},
        {"termino": "ALEGRÍA", "definicion": "Fruto que se nota en un corazón contento"},
        {"termino": "PAZ", "definicion": "Fruto que se nota en un corazón tranquilo"},
        {"termino": "TESTIMONIO", "definicion": "Mostrar con la vida lo que se cree"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en los frutos que enumera san Pablo.",
               "TESTIMONIO describe una forma de vivir, no un sentimiento."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: los frutos del Espíritu",
    "instruccion": "En 45 segundos, marca las palabras que son frutos del Espíritu Santo.",
    "tiempo_segundos": 45,
    "banco": ["AMOR", "ALEGRIA", "PAZ", "BONDAD", "ENVIDIA", "ENOJO"],
    "correctas": ["AMOR", "ALEGRIA", "PAZ", "BONDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Amor - Alegría - Paz - Bondad.",
               "Descarta las palabras que no son frutos del Espíritu."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El fruto del Espíritu es amor, alegría y ______.",
         "respuesta": "PAZ", "banco": ["PAZ", "ENOJO", "ENVIDIA"]},
    ],
    "reflexion": "¿Cuál de estos frutos te gustaría vivir más esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en la lista de frutos que menciona san Pablo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: doy testimonio alegre",
    "situacion": "Ya sabes que el Espíritu Santo produce frutos como el amor, la alegría y la paz en quien lo recibe.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para dar testimonio alegre de tu fe?",
         "opciones": ["Tratar a los demás con amor y paciencia",
                      "Compartir mi alegría de creer en Jesús",
                      "Buscar la paz en lugar de pelear",
                      "Esconder que soy creyente"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que esconde la fe en vez de mostrarla."],
    "feedback_ok": "¡Muy bien! Vivir con alegría los frutos del Espíritu también es anunciar tu fe.",
})

# ==========================================================================
# ==========================================================================
# PC08 — Jesús nos enseña a amar a todos   (Encuentro 8, Lucas 10,25-37)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC08-C01 — El hombre herido
# ==========================================================================
C = "PC08-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el hombre herido",
    "items": [
        {"texto": "Persona que fue asaltada y dejada medio muerta en el camino.", "respuesta": "HERIDO", "banco": ["HERIDO", "DORMIDO", "PERDIDO"]},
        {"texto": "Ruta que bajaba de Jerusalén a Jericó.", "respuesta": "CAMINO", "banco": ["CAMINO", "RIO", "MONTE"]},
        {"texto": "Quienes atacaron y despojaron al hombre.", "respuesta": "LADRONES", "banco": ["LADRONES", "AMIGOS", "VECINOS"]},
        {"texto": "Religioso que vio al hombre y pasó de largo.", "respuesta": "SACERDOTE", "banco": ["SACERDOTE", "PASTOR", "REY"]},
        {"texto": "Otro religioso que también pasó de largo.", "respuesta": "LEVITA", "banco": ["LEVITA", "SOLDADO", "MERCADER"]},
        {"texto": "Actitud de no importarle a alguien lo que le pasa a otro.", "respuesta": "INDIFERENCIA", "banco": ["INDIFERENCIA", "COMPASION", "AYUDA"]},
    ],
    "incluir": ["HERIDO", "CAMINO"], "requisito": 4,
    "pistas": ["Piensa en lo que le pasó al hombre que bajaba a Jericó.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el hombre herido",
    "palabras": ["HERIDO", "CAMINO", "LADRONES", "SACERDOTE", "LEVITA", "INDIFERENCIA"],
    "incluir": ["HERIDO", "CAMINO"], "requisito": 5,
    "pistas": ["HERIDO y CAMINO son de las palabras más cortas: búscalas primero.",
               "INDIFERENCIA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 10,29-32",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 10,29-32 y completa: «Cayó en manos de ______, "
                  "que lo despojaron, lo golpearon y se fueron dejándolo medio muerto.»", "respuesta": "LADRONES",
         "banco": ["LADRONES", "AMIGOS", "VECINOS"]},
        {"texto": "¿Qué le pasó al hombre que bajaba de Jerusalén a Jericó?", "abierta": True, "palabras_esperadas": ["HERIDO", "GOLPEARON", "LADRONES", "PASARON", "INDIFERENCIA"], "respuestas_referencia": ["Unos ladrones lo golpearon, lo robaron y lo dejaron medio muerto.", "Fue asaltado y herido, y un sacerdote y un levita pasaron sin ayudarlo.", "Lo hirieron unos ladrones, y quienes pasaron después no lo ayudaron."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 10.",
               "El texto describe primero el ataque, y luego a dos personas que pasan sin ayudar."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El hombre fue atacado por ______ en el camino.", "respuesta": "LADRONES", "banco": ["LADRONES", "AMIGOS", "VECINOS"]},
        {"texto": "El sacerdote y el levita ______ de largo.", "respuesta": "PASARON", "banco": ["PASARON", "AYUDARON", "SE DETUVIERON"]},
        {"texto": "El hombre quedó ______ en el camino.", "respuesta": "HERIDO", "banco": ["HERIDO", "DORMIDO", "CONTENTO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que le pasó al hombre en el camino.",
               "La segunda respuesta describe la actitud del sacerdote y el levita."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El hombre fue asaltado por unos ladrones.", "respuesta": True},
        {"texto": "El sacerdote se detuvo a ayudarlo de inmediato.", "respuesta": False},
        {"texto": "El levita también pasó de largo sin ayudar.", "respuesta": True},
        {"texto": "Nadie vio al hombre herido en el camino.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda quiénes pasaron cerca del hombre herido.",
               "Si una frase dice que nadie lo vio, es falsa: dos personas pasaron cerca."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué le pasó al hombre en el camino?",
         "opciones": ["Fue asaltado y herido", "Se perdió", "Se quedó dormido", "Nada"], "correcta": 0},
        {"texto": "¿Qué hicieron el sacerdote y el levita?",
         "opciones": ["Pasaron de largo", "Lo ayudaron enseguida", "Llamaron ayuda", "Se quedaron con él"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que le sucedió al hombre en el camino.",
               "Recuerda la actitud de las dos primeras personas que pasaron."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "HERIDO", "definicion": "Hombre asaltado en el camino"},
        {"termino": "LADRONES", "definicion": "Quienes lo atacaron"},
        {"termino": "SACERDOTE", "definicion": "Religioso que pasó de largo"},
        {"termino": "LEVITA", "definicion": "Otro religioso que tampoco ayudó"},
        {"termino": "INDIFERENCIA", "definicion": "Actitud de no importarle el sufrimiento ajeno"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en quién sufrió el ataque y quiénes pasaron sin ayudar.",
               "INDIFERENCIA describe una actitud, no una persona."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: lo que le pasó al hombre",
    "instruccion": "En 45 segundos, marca las palabras que describen lo que le pasó al hombre en el camino.",
    "tiempo_segundos": 45,
    "banco": ["HERIDO", "CAMINO", "LADRONES", "INDIFERENCIA", "AYUDA", "COMPASION"],
    "correctas": ["HERIDO", "CAMINO", "LADRONES", "INDIFERENCIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Herido - Camino - Ladrones - Indiferencia.",
               "Descarta las palabras que describen lo que todavía no había sucedido."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El hombre quedó ______ en el camino después del asalto.",
         "respuesta": "HERIDO", "banco": ["HERIDO", "DORMIDO", "PERDIDO"]},
    ],
    "reflexion": "¿Qué habrías sentido tú al ver a alguien así?",
    "requisito": 1,
    "pistas": ["Piensa en lo que le pasó al hombre en el camino.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: no paso de largo",
    "situacion": "Ya sabes que el hombre herido fue ignorado por quienes pasaron primero por el camino.",
    "items": [
        {"texto": "¿Qué puedes hacer tú si ves a alguien que necesita ayuda?",
         "opciones": ["Detenerme a ver qué necesita",
                      "Pedir ayuda a un adulto de confianza",
                      "Ofrecer lo que pueda para ayudar",
                      "Seguir de largo como si no lo viera"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que repite la indiferencia del sacerdote y el levita."],
    "feedback_ok": "¡Muy bien! Detenerte a ayudar también es imitar al buen samaritano.",
})

# ==========================================================================
# PC08-C02 — El Buen Samaritano ayuda
# ==========================================================================
C = "PC08-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Buen Samaritano",
    "items": [
        {"texto": "Viajero que se detuvo a ayudar al hombre herido.", "respuesta": "SAMARITANO", "banco": ["SAMARITANO", "SACERDOTE", "LEVITA"]},
        {"texto": "Lo que sintió el samaritano al ver al hombre herido.", "respuesta": "COMPASION", "banco": ["COMPASION", "MIEDO", "ENOJO"]},
        {"texto": "Lo que el samaritano hizo con las heridas del hombre.", "respuesta": "VENDO", "banco": ["VENDO", "IGNORO", "ESCONDIO"]},
        {"texto": "Lo que el samaritano usó para curar las heridas.", "respuesta": "ACEITE", "banco": ["ACEITE", "ARENA", "BARRO"]},
        {"texto": "Lugar donde el samaritano llevó al hombre herido.", "respuesta": "POSADA", "banco": ["POSADA", "CARCEL", "ESCUELA"]},
        {"texto": "Lo que el samaritano hizo por el hombre, sin abandonarlo.", "respuesta": "CUIDO", "banco": ["CUIDO", "OLVIDO", "DEJO"]},
    ],
    "incluir": ["SAMARITANO", "COMPASION"], "requisito": 4,
    "pistas": ["Piensa en quién se detuvo a ayudar al hombre herido.",
               "Todas las palabras describen las acciones del samaritano."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Buen Samaritano",
    "palabras": ["SAMARITANO", "COMPASION", "VENDO", "ACEITE", "POSADA", "CUIDO"],
    "incluir": ["SAMARITANO", "COMPASION"], "requisito": 5,
    "pistas": ["VENDÓ y CUIDÓ son de las palabras más cortas: búscalas primero.",
               "SAMARITANO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 10,33-35",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 10,33-35 y completa: «Se le acercó y, viendo sus "
                  "heridas, sintió ______ de él.»", "respuesta": "COMPASION", "banco": ["COMPASION", "MIEDO", "ENOJO"]},
        {"texto": "¿Qué hizo el samaritano al ver al hombre herido?", "abierta": True, "palabras_esperadas": ["CURO", "VENDO", "LLEVO", "POSADA", "CUIDO", "COMPASION"], "respuestas_referencia": ["Se compadeció, curó sus heridas, lo llevó a una posada y lo cuidó.", "Se acercó, le vendó las heridas y lo llevó a un lugar seguro para cuidarlo.", "Sintió compasión, lo curó y pagó para que lo cuidaran en la posada."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 10.",
               "El texto describe cómo el samaritano cura, transporta y paga por el cuidado del hombre."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El samaritano sintió ______ al ver al hombre herido.", "respuesta": "COMPASION", "banco": ["COMPASION", "INDIFERENCIA", "MIEDO"]},
        {"texto": "El samaritano ______ las heridas del hombre.", "respuesta": "VENDO", "banco": ["VENDO", "IGNORO", "ESCONDIO"]},
        {"texto": "El samaritano llevó al hombre a una ______.", "respuesta": "POSADA", "banco": ["POSADA", "CARCEL", "ESCUELA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que sintió el samaritano al ver al hombre herido.",
               "La tercera respuesta es a dónde llevó al hombre para cuidarlo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El samaritano sintió compasión al ver al hombre herido.", "respuesta": True},
        {"texto": "El samaritano pasó de largo, igual que los otros.", "respuesta": False},
        {"texto": "El samaritano curó las heridas del hombre.", "respuesta": True},
        {"texto": "El samaritano abandonó al hombre en el camino.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que hizo el samaritano al encontrar al hombre herido.",
               "Si una frase dice que el samaritano lo abandonó, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué sintió el samaritano al ver al hombre herido?",
         "opciones": ["Compasión", "Indiferencia", "Miedo", "Enojo"], "correcta": 0},
        {"texto": "¿Qué hizo el samaritano por el hombre?",
         "opciones": ["Lo curó y lo llevó a una posada", "Lo ignoró", "Le pidió dinero", "Se fue rápido"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la actitud del samaritano frente al hombre herido.",
               "Recuerda las acciones concretas que hizo por él."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SAMARITANO", "definicion": "Quien se detuvo a ayudar"},
        {"termino": "COMPASIÓN", "definicion": "Lo que sintió al ver al hombre herido"},
        {"termino": "VENDÓ", "definicion": "Lo que hizo con las heridas"},
        {"termino": "POSADA", "definicion": "Donde llevó al hombre herido"},
        {"termino": "CUIDÓ", "definicion": "Lo que hizo por él, sin abandonarlo"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el orden de las acciones del samaritano.",
               "POSADA es un lugar, no una acción."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: las acciones del samaritano",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El samaritano sintió ______ al ver al hombre herido.",
         "opciones": ["compasión", "indiferencia", "miedo"], "correcta": 0},
        {"texto": "El samaritano llevó al hombre a una ______.",
         "opciones": ["posada", "cárcel", "escuela"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la actitud del samaritano frente al hombre herido.",
               "Recuerda a dónde lo llevó para que lo cuidaran."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El samaritano sintió ______ y ayudó al hombre herido.",
         "respuesta": "COMPASION", "banco": ["COMPASION", "MIEDO", "ENOJO"]},
    ],
    "reflexion": "¿Cuándo has sentido compasión por alguien?",
    "requisito": 1,
    "pistas": ["Piensa en el sentimiento que llevó al samaritano a actuar.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: actúo como el samaritano",
    "situacion": "Ya sabes que el samaritano se detuvo, curó y cuidó al hombre herido, aunque no lo conocía.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para actuar como el buen samaritano?",
         "opciones": ["Ayudar a alguien aunque no sea mi amigo",
                      "Ofrecer consuelo a quien esté triste",
                      "Compartir lo que tengo con quien lo necesite",
                      "Ayudar solo a quienes ya conozco"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que sigue haciendo distinción entre las personas."],
    "feedback_ok": "¡Muy bien! Ayudar sin distinción también es imitar al buen samaritano.",
})

# ==========================================================================
# PC08-C03 — Amar sin distinción
# ==========================================================================
C = "PC08-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: amar sin distinción",
    "items": [
        {"texto": "La persona a quien debemos amar como a nosotros mismos.", "respuesta": "PROJIMO", "banco": ["PROJIMO", "ENEMIGO", "EXTRAÑO"]},
        {"texto": "Compasión que se convierte en ayuda concreta.", "respuesta": "MISERICORDIA", "banco": ["MISERICORDIA", "DISTANCIA", "INDIFERENCIA"]},
        {"texto": "Lo que Jesús pide hacer con el ejemplo del samaritano.", "respuesta": "IMITAR", "banco": ["IMITAR", "OLVIDAR", "IGNORAR"]},
        {"texto": "Diferencia que Jesús nos pide no hacer al amar.", "respuesta": "DISTINCION", "banco": ["DISTINCION", "UNION", "AMISTAD"]},
        {"texto": "A quiénes debemos amar, según Jesús.", "respuesta": "TODOS", "banco": ["TODOS", "ALGUNOS", "POCOS"]},
        {"texto": "Lo que Jesús pide que hagamos con el prójimo.", "respuesta": "AMAR", "banco": ["AMAR", "IGNORAR", "TEMER"]},
    ],
    "incluir": ["PROJIMO", "MISERICORDIA"], "requisito": 4,
    "pistas": ["Piensa en la pregunta que Jesús responde con esta parábola: ¿quién es mi prójimo?",
               "Todas las palabras hablan de amar sin poner condiciones."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: amar sin distinción",
    "palabras": ["PROJIMO", "MISERICORDIA", "IMITAR", "DISTINCION", "TODOS", "AMAR"],
    "incluir": ["PROJIMO", "MISERICORDIA"], "requisito": 5,
    "pistas": ["TODOS y AMAR son de las palabras más cortas: búscalas primero.",
               "MISERICORDIA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 10,36-37",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 10,36-37 y completa: «El que practicó la "
                  "______ con él.» Y Jesús le dijo: «Ve y haz tú lo mismo.»", "respuesta": "MISERICORDIA",
         "banco": ["MISERICORDIA", "DISTANCIA", "INDIFERENCIA"]},
        {"texto": "¿Cuál de los tres fue el prójimo del hombre herido, según Jesús?", "abierta": True, "palabras_esperadas": ["SAMARITANO", "MISERICORDIA", "AYUDO", "PROJIMO"], "respuestas_referencia": ["El que tuvo compasión y lo ayudó, es decir, el samaritano.", "El samaritano, porque practicó la misericordia con él.", "Fue el samaritano, el que actuó con misericordia."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 10.",
               "Jesús le hace la pregunta al maestro de la Ley, y este responde con una sola palabra."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús nos pide amar a todos sin ______.", "respuesta": "DISTINCION", "banco": ["DISTINCION", "RAZON", "MOTIVO"]},
        {"texto": "El verdadero prójimo es quien actúa con ______.", "respuesta": "MISERICORDIA", "banco": ["MISERICORDIA", "INDIFERENCIA", "DISTANCIA"]},
        {"texto": "Jesús nos pide ______ el ejemplo del samaritano.", "respuesta": "IMITAR", "banco": ["IMITAR", "OLVIDAR", "IGNORAR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús responde a la pregunta «¿quién es mi prójimo?».",
               "La tercera respuesta es lo que Jesús pide hacer con este ejemplo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El verdadero prójimo fue quien tuvo compasión y ayudó.", "respuesta": True},
        {"texto": "Jesús nos pide amar solo a quienes son como nosotros.", "respuesta": False},
        {"texto": "Jesús pide imitar el ejemplo del buen samaritano.", "respuesta": True},
        {"texto": "Amar sin distinción significa ayudar solo a los amigos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda a quién considera Jesús el verdadero prójimo.",
               "Si una frase dice que solo hay que amar a los amigos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Quién fue el verdadero prójimo del hombre herido?",
         "opciones": ["El que tuvo compasión y lo ayudó", "El sacerdote", "El levita", "Nadie"], "correcta": 0},
        {"texto": "¿Qué nos pide Jesús con esta parábola?",
         "opciones": ["Amar a todos sin distinción", "Amar solo a los cercanos", "Ignorar a los desconocidos", "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién actuó realmente como prójimo del hombre herido.",
               "Recuerda el mensaje final que Jesús deja con esta parábola."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PRÓJIMO", "definicion": "A quien debemos amar como a nosotros mismos"},
        {"termino": "MISERICORDIA", "definicion": "Compasión que se convierte en ayuda"},
        {"termino": "IMITAR", "definicion": "Lo que Jesús pide hacer con este ejemplo"},
        {"termino": "DISTINCIÓN", "definicion": "Diferencia que Jesús pide no hacer"},
        {"termino": "TODOS", "definicion": "A quiénes debemos amar, según Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el mensaje final de la parábola del buen samaritano.",
               "DISTINCIÓN es lo que Jesús pide eliminar, no practicar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: amar sin distinción",
    "instruccion": "En 45 segundos, marca las palabras que resumen el mensaje de amar sin distinción.",
    "tiempo_segundos": 45,
    "banco": ["PROJIMO", "MISERICORDIA", "TODOS", "AMAR", "DISTINCION", "INDIFERENCIA"],
    "correctas": ["PROJIMO", "MISERICORDIA", "TODOS", "AMAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Prójimo - Misericordia - Todos - Amar.",
               "Descarta las palabras que Jesús nos pide dejar atrás."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El verdadero prójimo es quien practica la ______ con los demás.",
         "respuesta": "MISERICORDIA", "banco": ["MISERICORDIA", "DISTANCIA", "INDIFERENCIA"]},
    ],
    "reflexion": "¿A quién te cuesta más amar como a tu prójimo?",
    "requisito": 1,
    "pistas": ["Piensa en la actitud del samaritano hacia el hombre herido.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: amo sin distinción",
    "situacion": "Ya sabes que Jesús nos pide amar a todos sin distinción, como hizo el buen samaritano.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para amar sin distinción?",
         "opciones": ["Tratar bien a alguien distinto a mí",
                      "Ayudar a quien no es mi amigo cercano",
                      "Ser amable con alguien nuevo",
                      "Ayudar solo a los que ya conozco"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que sigue haciendo distinción entre las personas."],
    "feedback_ok": "¡Muy bien! Amar sin distinción también se nota en los pequeños gestos.",
})

# ==========================================================================
# PC08-C04 — La compasión
# ==========================================================================
C = "PC08-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la compasión",
    "items": [
        {"texto": "Sentimiento que tuvo Jesús al ver a la gente.", "respuesta": "COMPASION", "banco": ["COMPASION", "ENOJO", "INDIFERENCIA"]},
        {"texto": "Gran grupo de personas que seguían a Jesús.", "respuesta": "MULTITUD", "banco": ["MULTITUD", "FAMILIA", "GRUPO PEQUEÑO"]},
        {"texto": "Quien cuida y guía a sus ovejas, como Jesús cuida a la gente.", "respuesta": "PASTOR", "banco": ["PASTOR", "REY", "JUEZ"]},
        {"texto": "Cómo estaban las personas, agotadas por su vida difícil.", "respuesta": "CANSADAS", "banco": ["CANSADAS", "ALEGRES", "TRANQUILAS"]},
        {"texto": "Cómo se sentían las personas, sin ánimo ni fuerza.", "respuesta": "ABATIDAS", "banco": ["ABATIDAS", "FELICES", "SEGURAS"]},
        {"texto": "Forma en que Jesús ve a las personas, con ternura.", "respuesta": "MIRADA", "banco": ["MIRADA", "DISTANCIA", "INDIFERENCIA"]},
    ],
    "incluir": ["COMPASION", "MULTITUD"], "requisito": 4,
    "pistas": ["Piensa en lo que sintió Jesús al ver a la gente cansada.",
               "Todas las palabras describen la actitud de Jesús ante el sufrimiento de la gente."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la compasión",
    "palabras": ["COMPASION", "MULTITUD", "PASTOR", "CANSADAS", "ABATIDAS", "MIRADA"],
    "incluir": ["COMPASION", "MULTITUD"], "requisito": 5,
    "pistas": ["PASTOR y MIRADA son de las palabras más cortas: búscalas primero.",
               "COMPASIÓN y MULTITUD son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 9,36",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 9,36 y completa: «Al ver a las multitudes, sintió "
                  "______ de ellas, porque estaban cansadas y abatidas.»", "respuesta": "COMPASION",
         "banco": ["COMPASION", "ENOJO", "INDIFERENCIA"]},
        {"texto": "¿Qué sintió Jesús al ver a las multitudes?", "abierta": True, "palabras_esperadas": ["COMPASION", "CANSADAS", "ABATIDAS", "PASTOR", "OVEJAS"], "respuestas_referencia": ["Sintió compasión, porque las vio cansadas y abatidas, como ovejas sin pastor.", "Tuvo compasión de la gente al verla agotada y sin guía.", "Se compadeció de ellos porque estaban como ovejas sin pastor."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 9.",
               "El texto compara a la gente con ovejas que no tienen quien las guíe."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús sintió ______ al ver a la gente cansada.", "respuesta": "COMPASION", "banco": ["COMPASION", "ENOJO", "INDIFERENCIA"]},
        {"texto": "La gente estaba como ovejas sin ______.", "respuesta": "PASTOR", "banco": ["PASTOR", "CASA", "COMIDA"]},
        {"texto": "Jesús mira con ternura a las personas ______.", "respuesta": "ABATIDAS", "banco": ["ABATIDAS", "ALEGRES", "TRANQUILAS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que sintió Jesús al ver a la gente.",
               "La segunda respuesta completa la comparación que hace el texto."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús sintió compasión al ver a las multitudes.", "respuesta": True},
        {"texto": "Jesús ignoró a la gente que estaba cansada.", "respuesta": False},
        {"texto": "Jesús comparó a la gente con ovejas sin pastor.", "respuesta": True},
        {"texto": "A Jesús no le importaba cómo se sentía la gente.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que sintió Jesús al ver a las multitudes.",
               "Si una frase dice que a Jesús no le importaba la gente, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué sintió Jesús al ver a las multitudes?",
         "opciones": ["Compasión", "Indiferencia", "Enojo", "Cansancio"], "correcta": 0},
        {"texto": "¿Con qué compara Jesús a la gente cansada y abatida?",
         "opciones": ["Con ovejas sin pastor", "Con un rebaño perdido para siempre", "Con extraños", "Con enemigos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el sentimiento de Jesús ante el sufrimiento de la gente.",
               "Recuerda la imagen que usa el texto para describir a la multitud."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "COMPASIÓN", "definicion": "Sentimiento de Jesús al ver a la gente"},
        {"termino": "MULTITUD", "definicion": "Gran grupo que seguía a Jesús"},
        {"termino": "PASTOR", "definicion": "Quien cuida y guía a sus ovejas"},
        {"termino": "CANSADAS", "definicion": "Cómo estaban las personas"},
        {"termino": "ABATIDAS", "definicion": "Cómo se sentían, sin ánimo"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo estaba la gente y en cómo reaccionó Jesús.",
               "PASTOR es una imagen usada para describir a Jesús."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la actitud de Jesús",
    "instruccion": "En 45 segundos, marca las palabras que describen la actitud de Jesús ante la gente.",
    "tiempo_segundos": 45,
    "banco": ["COMPASION", "MULTITUD", "PASTOR", "TERNURA", "INDIFERENCIA", "DISTANCIA"],
    "correctas": ["COMPASION", "MULTITUD", "PASTOR", "TERNURA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Compasión - Multitud - Pastor - Ternura.",
               "Descarta las palabras que muestran una actitud contraria a la de Jesús."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús sintió ______ al ver a la gente cansada y sin guía.",
         "respuesta": "COMPASION", "banco": ["COMPASION", "ENOJO", "INDIFERENCIA"]},
    ],
    "reflexion": "¿Cuándo has sentido compasión por alguien que sufre?",
    "requisito": 1,
    "pistas": ["Piensa en el sentimiento de Jesús ante la gente cansada.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: muestro compasión",
    "situacion": "Ya sabes que Jesús sintió compasión al ver a la gente cansada y sin guía.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para mostrar compasión?",
         "opciones": ["Escuchar a alguien que está triste",
                      "Acompañar a quien se siente solo",
                      "Ofrecer ayuda sin que me la pidan",
                      "Ignorar a quien parece cansado o triste"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que repite la indiferencia."],
    "feedback_ok": "¡Muy bien! Mostrar compasión también es imitar el corazón de Jesús.",
})

# ==========================================================================
# PC08-C05 — Ayudar al que sufre
# ==========================================================================
C = "PC08-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: ayudar al que sufre",
    "items": [
        {"texto": "Necesidad de comer que Jesús pide saciar.", "respuesta": "HAMBRE", "banco": ["HAMBRE", "SUEÑO", "FRIO"]},
        {"texto": "Necesidad de beber que Jesús pide saciar.", "respuesta": "SED", "banco": ["SED", "CALOR", "PRISA"]},
        {"texto": "Persona que llega de otro lugar y necesita acogida.", "respuesta": "FORASTERO", "banco": ["FORASTERO", "VECINO", "AMIGO"]},
        {"texto": "Quien necesita ropa, según lo que menciona Jesús.", "respuesta": "DESNUDO", "banco": ["DESNUDO", "CANSADO", "PERDIDO"]},
        {"texto": "Persona que necesita cuidado por su salud.", "respuesta": "ENFERMO", "banco": ["ENFERMO", "SANO", "FUERTE"]},
        {"texto": "Lo que Jesús pide hacer con el enfermo o el preso.", "respuesta": "VISITAR", "banco": ["VISITAR", "EVITAR", "OLVIDAR"]},
    ],
    "incluir": ["HAMBRE", "SED"], "requisito": 4,
    "pistas": ["Piensa en las necesidades que Jesús pide atender.",
               "Todas las palabras describen a quienes Jesús pide ayudar."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: ayudar al que sufre",
    "palabras": ["HAMBRE", "SED", "FORASTERO", "DESNUDO", "ENFERMO", "VISITAR"],
    "incluir": ["HAMBRE", "SED"], "requisito": 5,
    "pistas": ["SED es la palabra más corta: búscala primero.",
               "FORASTERO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 25,35-36",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 25,35-36 y completa: «Tuve ______ y me disteis de "
                  "comer; tuve sed y me disteis de beber.»", "respuesta": "HAMBRE", "banco": ["HAMBRE", "SUEÑO", "FRIO"]},
        {"texto": "¿Qué acciones concretas menciona Jesús como ayuda al que sufre?", "abierta": True, "palabras_esperadas": ["COMER", "BEBER", "VESTIR", "VISITAR", "ACOGER", "CUIDAR"], "respuestas_referencia": ["Menciona dar de comer, dar de beber, acoger, vestir y visitar al enfermo.", "Dar comida al hambriento, agua al sediento y visitar al enfermo o preso.", "Alimentar, dar de beber, vestir, acoger y visitar a quien sufre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 25.",
               "Jesús enumera varias necesidades y la acción que las responde a cada una."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús pide dar de comer a quien tiene ______.", "respuesta": "HAMBRE", "banco": ["HAMBRE", "SUEÑO", "FRIO"]},
        {"texto": "Jesús pide acoger al ______.", "respuesta": "FORASTERO", "banco": ["FORASTERO", "ENEMIGO", "DESCONOCIDO"]},
        {"texto": "Jesús pide ______ al enfermo.", "respuesta": "VISITAR", "banco": ["VISITAR", "EVITAR", "OLVIDAR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en las necesidades que Jesús menciona una por una.",
               "La tercera respuesta es lo que Jesús pide para el que está enfermo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús pide dar de comer al que tiene hambre.", "respuesta": True},
        {"texto": "Jesús pide ignorar al forastero.", "respuesta": False},
        {"texto": "Jesús pide visitar al enfermo.", "respuesta": True},
        {"texto": "A Jesús no le importa quien sufre.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda las acciones concretas que menciona Jesús.",
               "Si una frase dice que a Jesús no le importa quien sufre, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pide Jesús para quien tiene hambre?",
         "opciones": ["Darle de comer", "Ignorarlo", "Regañarlo", "Nada"], "correcta": 0},
        {"texto": "¿Qué pide Jesús para el enfermo?",
         "opciones": ["Visitarlo", "Evitarlo", "Olvidarlo", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la acción que responde a cada necesidad.",
               "Recuerda lo que Jesús pide para quien está enfermo o preso."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "HAMBRE", "definicion": "Necesidad que se sacia dando de comer"},
        {"termino": "SED", "definicion": "Necesidad que se sacia dando de beber"},
        {"termino": "FORASTERO", "definicion": "Quien necesita ser acogido"},
        {"termino": "ENFERMO", "definicion": "Quien necesita ser visitado"},
        {"termino": "VISITAR", "definicion": "Acción que pide Jesús para el que sufre solo"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cada necesidad y en la acción que la responde.",
               "VISITAR es una acción, no una necesidad."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: ayudar al que sufre",
    "instruccion": "En 45 segundos, marca las acciones que Jesús pide hacer por quien sufre.",
    "tiempo_segundos": 45,
    "banco": ["COMER", "BEBER", "VESTIR", "VISITAR", "IGNORAR", "EVITAR"],
    "correctas": ["COMER", "BEBER", "VESTIR", "VISITAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Comer - Beber - Vestir - Visitar.",
               "Descarta las acciones que muestran indiferencia."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús pide dar de comer, dar de beber, acoger y ______ al que sufre.",
         "respuesta": "VISITAR", "banco": ["VISITAR", "IGNORAR", "EVITAR"]},
    ],
    "reflexion": "¿A quién podrías ayudar tú esta semana de estas formas?",
    "requisito": 1,
    "pistas": ["Piensa en la lista de acciones que menciona Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: ayudo a quien sufre",
    "situacion": "Ya sabes que Jesús pide dar de comer, de beber, acoger y visitar a quien sufre.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para ayudar a alguien que sufre?",
         "opciones": ["Compartir mi comida con quien lo necesite",
                      "Visitar o llamar a alguien enfermo",
                      "Ayudar a alguien nuevo a sentirse bienvenido",
                      "Evitar a quien parece necesitar ayuda"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que repite la indiferencia."],
    "feedback_ok": "¡Muy bien! Ayudar concretamente también es amar como Jesús enseñó.",
})

# ==========================================================================
# PC08-C06 — Ser buen samaritano hoy
# ==========================================================================
C = "PC08-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: buen samaritano hoy",
    "items": [
        {"texto": "Lo que san Juan pide, además de hablar de amor.", "respuesta": "OBRAS", "banco": ["OBRAS", "SUEÑOS", "IDEAS"]},
        {"texto": "Cómo pide san Juan que amemos, no solo de palabra.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
        {"texto": "Quien necesita ayuda, según lo llama san Juan.", "respuesta": "HERMANO", "banco": ["HERMANO", "EXTRAÑO", "ENEMIGO"]},
        {"texto": "Lo que tiene quien sufre carencias.", "respuesta": "NECESIDAD", "banco": ["NECESIDAD", "ABUNDANCIA", "SUERTE"]},
        {"texto": "Lo que no basta con decir, según san Juan.", "respuesta": "PALABRAS", "banco": ["PALABRAS", "OBRAS", "GESTOS"]},
        {"texto": "Lo que de verdad demuestra el amor.", "respuesta": "ACCIONES", "banco": ["ACCIONES", "PROMESAS", "DISCURSOS"]},
    ],
    "incluir": ["OBRAS", "VERDAD"], "requisito": 4,
    "pistas": ["Piensa en lo que san Juan pide más allá de las palabras.",
               "Todas las palabras hablan de amar de manera concreta."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: buen samaritano hoy",
    "palabras": ["OBRAS", "VERDAD", "HERMANO", "NECESIDAD", "PALABRAS", "ACCIONES"],
    "incluir": ["OBRAS", "VERDAD"], "requisito": 5,
    "pistas": ["OBRAS es una de las palabras más cortas: búscala primero.",
               "NECESIDAD es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Juan 3,17-18",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Juan 3,17-18 y completa: «No amemos de palabra... "
                  "sino de ______ y en verdad.»", "respuesta": "OBRA", "banco": ["OBRA", "SUEÑO", "IDEA"]},
        {"texto": "¿Qué pide Juan que hagamos además de hablar de amor?", "abierta": True, "palabras_esperadas": ["OBRAS", "ACCIONES", "AYUDAR", "VERDAD", "HERMANO"], "respuestas_referencia": ["Pide que amemos con obras y en verdad, no solo con palabras.", "Que ayudemos de verdad a quien tiene necesidad, con acciones concretas.", "Que el amor se demuestre con hechos, ayudando a quien lo necesita."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta de san Juan; el capítulo es el 3.",
               "San Juan compara amar «de palabra» con amar «de obra»."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Juan pide amar de ______ y no solo de palabra.", "respuesta": "OBRA", "banco": ["OBRA", "SUEÑO", "IDEA"]},
        {"texto": "El amor verdadero se demuestra con ______.", "respuesta": "ACCIONES", "banco": ["ACCIONES", "PALABRAS", "PROMESAS"]},
        {"texto": "Debemos ayudar al ______ que tiene necesidad.", "respuesta": "HERMANO", "banco": ["HERMANO", "EXTRAÑO", "ENEMIGO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que san Juan pide más allá de las palabras.",
               "La tercera respuesta es a quién llama san Juan quien necesita ayuda."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Juan pide amar solo de palabra.", "respuesta": False},
        {"texto": "El amor verdadero se demuestra con obras.", "respuesta": True},
        {"texto": "Ser buen samaritano hoy significa ayudar de verdad a quien lo necesita.", "respuesta": True},
        {"texto": "A san Juan no le importa cómo tratamos a los demás.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que san Juan pide, además de hablar de amor.",
               "Si una frase dice que basta con hablar de amor, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pide san Juan además de hablar de amor?",
         "opciones": ["Obras y verdad", "Solo palabras bonitas", "Nada más", "Silencio"], "correcta": 0},
        {"texto": "¿Qué significa ser buen samaritano hoy?",
         "opciones": ["Ayudar de verdad a quien lo necesita", "Solo decir que amamos", "Ignorar a los demás", "Esperar a que otros ayuden"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que pide san Juan más allá de las palabras.",
               "Recuerda el ejemplo del buen samaritano de este encuentro."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "OBRAS", "definicion": "Lo que san Juan pide, además de palabras"},
        {"termino": "VERDAD", "definicion": "Cómo pide san Juan que amemos"},
        {"termino": "HERMANO", "definicion": "Quien necesita ayuda"},
        {"termino": "NECESIDAD", "definicion": "Lo que tiene quien sufre carencias"},
        {"termino": "ACCIONES", "definicion": "Lo que de verdad demuestra el amor"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que san Juan pide más allá de las palabras.",
               "NECESIDAD describe una carencia, no una acción."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: amar de verdad",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo debemos amar, según san Juan.",
    "tiempo_segundos": 45,
    "banco": ["OBRAS", "VERDAD", "ACCIONES", "AYUDAR", "PALABRAS VACIAS", "INDIFERENCIA"],
    "correctas": ["OBRAS", "VERDAD", "ACCIONES", "AYUDAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Obras - Verdad - Acciones - Ayudar.",
               "Descarta las palabras que describen un amor solo de palabra."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El amor verdadero se demuestra con ______, no solo con palabras.",
         "respuesta": "OBRAS", "banco": ["OBRAS", "PROMESAS", "IDEAS"]},
    ],
    "reflexion": "¿Qué obra concreta de amor has hecho esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en lo que san Juan pide, además de hablar de amor.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: soy buen samaritano hoy",
    "situacion": "Ya sabes que amar de verdad significa ayudar con obras, no solo con palabras.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para ser un buen samaritano hoy?",
         "opciones": ["Ayudar a alguien con una necesidad real",
                      "Compartir lo que tengo con quien lo necesite",
                      "Actuar y no solo decir que quiero ayudar",
                      "Decir que ayudaré pero no hacerlo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una promesa vacía.",
               "Descarta la única opción que se queda solo en palabras."],
    "feedback_ok": "¡Muy bien! Ser buen samaritano hoy también significa actuar, no solo prometer.",
})

# ==========================================================================
# ==========================================================================
# PC09 — Aprendemos a rezar con Jesús   (Encuentro 9, Mateo 6,5-13)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC09-C01 — Jesús enseña a orar
# ==========================================================================
C = "PC09-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús enseña a orar",
    "items": [
        {"texto": "Hablar con Dios de corazón a corazón.", "respuesta": "ORACION", "banco": ["ORACION", "LECCION", "TAREA"]},
        {"texto": "Lo que los discípulos pidieron que Jesús hiciera.", "respuesta": "ENSEÑAR", "banco": ["ENSEÑAR", "OLVIDAR", "IGNORAR"]},
        {"texto": "Quienes le pidieron a Jesús que les enseñara a orar.", "respuesta": "DISCIPULOS", "banco": ["DISCIPULOS", "SOLDADOS", "FARISEOS"]},
        {"texto": "Lo que hicieron los discípulos al acercarse a Jesús.", "respuesta": "PEDIR", "banco": ["PEDIR", "HUIR", "DUDAR"]},
        {"texto": "Otra palabra para orar.", "respuesta": "REZAR", "banco": ["REZAR", "JUGAR", "CANTAR"]},
        {"texto": "Quien enseñó a sus discípulos a orar.", "respuesta": "JESUS", "banco": ["JESUS", "MOISES", "PEDRO"]},
    ],
    "incluir": ["ORACION", "ENSEÑAR"], "requisito": 4,
    "pistas": ["Piensa en lo que los discípulos le pidieron a Jesús.",
               "Todas las palabras se relacionan con aprender a hablar con Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús enseña a orar",
    "palabras": ["ORACION", "ENSEÑAR", "DISCIPULOS", "PEDIR", "REZAR", "JESUS"],
    "incluir": ["ORACION", "ENSEÑAR"], "requisito": 5,
    "pistas": ["PEDIR y REZAR son de las palabras más cortas: búscalas primero.",
               "DISCÍPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 11,1-4",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 11,1-4 y completa: «Señor, enséñanos a ______, "
                  "como enseñó también Juan a sus discípulos.»", "respuesta": "ORAR", "banco": ["ORAR", "CANTAR", "ESPERAR"]},
        {"texto": "¿Qué le pidieron los discípulos a Jesús?", "abierta": True, "palabras_esperadas": ["ORAR", "ENSEÑAR", "REZAR", "ORACION"], "respuestas_referencia": ["Le pidieron que les enseñara a orar, como hizo Juan con los suyos.", "Pidieron a Jesús que les enseñara una oración.", "Le pidieron que les enseñara a orar."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 11.",
               "Uno de los discípulos habla en nombre de todos y hace un pedido concreto."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los discípulos le pidieron a Jesús que les enseñara a ______.", "respuesta": "ORAR", "banco": ["ORAR", "JUGAR", "CANTAR"]},
        {"texto": "Jesús respondió con una ______ para todos.", "respuesta": "ORACION", "banco": ["ORACION", "HISTORIA", "LEY"]},
        {"texto": "Orar es hablar con ______.", "respuesta": "DIOS", "banco": ["DIOS", "UN DESCONOCIDO", "NADIE"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que los discípulos le pidieron a Jesús.",
               "La tercera respuesta es con quién hablamos cuando oramos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los discípulos le pidieron a Jesús que les enseñara a orar.", "respuesta": True},
        {"texto": "Jesús se negó a enseñarles a orar.", "respuesta": False},
        {"texto": "Orar es hablar con Dios.", "respuesta": True},
        {"texto": "A Jesús no le importaba la oración.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué le pidieron los discípulos a Jesús.",
               "Si una frase dice que a Jesús no le importaba la oración, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué le pidieron los discípulos a Jesús?",
         "opciones": ["Que les enseñara a orar", "Que les diera de comer", "Que los dejara solos", "Nada"], "correcta": 0},
        {"texto": "¿Qué es la oración?",
         "opciones": ["Hablar con Dios", "Un juego", "Una tarea escolar", "Nada importante"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que pidieron los discípulos a Jesús.",
               "Recuerda con quién hablamos cuando oramos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ORACIÓN", "definicion": "Hablar con Dios de corazón a corazón"},
        {"termino": "ENSEÑAR", "definicion": "Lo que pidieron los discípulos a Jesús"},
        {"termino": "DISCÍPULOS", "definicion": "Quienes pidieron aprender a orar"},
        {"termino": "PEDIR", "definicion": "Lo que hicieron al acercarse a Jesús"},
        {"termino": "REZAR", "definicion": "Otra palabra para orar"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que pidieron los discípulos y en quiénes lo pidieron.",
               "REZAR y ORACIÓN significan casi lo mismo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: aprender a orar",
    "instruccion": "En 45 segundos, marca las palabras que se relacionan con aprender a orar.",
    "tiempo_segundos": 45,
    "banco": ["ORACION", "ENSEÑAR", "REZAR", "DIOS", "SILENCIO TOTAL", "OLVIDO"],
    "correctas": ["ORACION", "ENSEÑAR", "REZAR", "DIOS"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Oración - Enseñar - Rezar - Dios.",
               "Descarta las palabras que no tienen que ver con aprender a orar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los discípulos le pidieron a Jesús que les enseñara a ______.",
         "respuesta": "ORAR", "banco": ["ORAR", "JUGAR", "CANTAR"]},
    ],
    "reflexion": "¿Qué te gustaría aprender sobre la oración?",
    "requisito": 1,
    "pistas": ["Piensa en lo que los discípulos le pidieron a Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: aprendo a orar",
    "situacion": "Ya sabes que los discípulos le pidieron a Jesús que les enseñara a orar.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para aprender a orar mejor?",
         "opciones": ["Pedirle a alguien de confianza que te ayude a orar",
                      "Practicar una oración corta cada día",
                      "Preguntar tus dudas sobre la oración a tu catequista",
                      "No intentar orar nunca"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que muestra desinterés por orar."],
    "feedback_ok": "¡Muy bien! Aprender a orar, como los discípulos, también es parte del camino de fe.",
})

# ==========================================================================
# PC09-C02 — Orar con sinceridad
# ==========================================================================
C = "PC09-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: orar con sinceridad",
    "items": [
        {"texto": "Orar de verdad, sin fingir.", "respuesta": "SINCERIDAD", "banco": ["SINCERIDAD", "MENTIRA", "DUDA"]},
        {"texto": "Lugar privado donde Jesús pide orar.", "respuesta": "SECRETO", "banco": ["SECRETO", "PUBLICO", "RUIDO"]},
        {"texto": "Desde donde debe salir la oración verdadera.", "respuesta": "CORAZON", "banco": ["CORAZON", "MIEDO", "ORGULLO"]},
        {"texto": "Quien ora solo para que lo vean.", "respuesta": "HIPOCRITA", "banco": ["HIPOCRITA", "AMIGO", "NIÑO"]},
        {"texto": "Lo que hace quien ora para impresionar a otros.", "respuesta": "APARENTAR", "banco": ["APARENTAR", "COMPARTIR", "ESCUCHAR"]},
        {"texto": "Cercanía y confianza al hablar con Dios.", "respuesta": "INTIMIDAD", "banco": ["INTIMIDAD", "DISTANCIA", "MIEDO"]},
    ],
    "incluir": ["SINCERIDAD", "CORAZON"], "requisito": 4,
    "pistas": ["Piensa en cómo pide Jesús que oremos.",
               "Todas las palabras hablan de orar de verdad, sin aparentar."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: orar con sinceridad",
    "palabras": ["SINCERIDAD", "SECRETO", "CORAZON", "HIPOCRITA", "APARENTAR", "INTIMIDAD"],
    "incluir": ["SINCERIDAD", "CORAZON"], "requisito": 5,
    "pistas": ["CORAZÓN y SECRETO son de las palabras más cortas: búscalas primero.",
               "SINCERIDAD es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 6,5-6",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 6,5-6 y completa: «Tú, cuando ores, entra en tu "
                  "cuarto, cierra la puerta y ora a tu Padre en ______.»", "respuesta": "SECRETO",
         "banco": ["SECRETO", "PUBLICO", "SILENCIO"]},
        {"texto": "¿Cómo pide Jesús que oremos, y cómo no?", "abierta": True, "palabras_esperadas": ["SINCERIDAD", "SECRETO", "CORAZON", "SOLAS", "VERDAD"], "respuestas_referencia": ["Pide orar en secreto, con el corazón, y no para que otros nos vean.", "Que oremos con sinceridad, sin aparentar frente a los demás.", "Que oremos a solas y con el corazón, no para impresionar a otros."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 6.",
               "Jesús contrasta orar en secreto con orar para que otros nos vean."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús pide orar en ______, no para que nos vean.", "respuesta": "SECRETO", "banco": ["SECRETO", "PUBLICO", "RUIDO"]},
        {"texto": "La oración verdadera nace del ______.", "respuesta": "CORAZON", "banco": ["CORAZON", "MIEDO", "ORGULLO"]},
        {"texto": "No debemos orar como los ______, que solo quieren aparentar.", "respuesta": "HIPOCRITAS", "banco": ["HIPOCRITAS", "AMIGOS", "NIÑOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el lugar donde Jesús pide orar.",
               "La tercera respuesta describe a quien ora solo para impresionar."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús pide orar con sinceridad, no para aparentar.", "respuesta": True},
        {"texto": "Jesús pide orar solo para que otros nos vean.", "respuesta": False},
        {"texto": "La oración verdadera nace del corazón.", "respuesta": True},
        {"texto": "A Jesús no le importa cómo oramos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Jesús critica de los hipócritas.",
               "Si una frase dice que a Jesús no le importa cómo oramos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo pide Jesús que oremos?",
         "opciones": ["Con sinceridad, en secreto", "Para que nos vean", "Con orgullo", "Sin importancia"], "correcta": 0},
        {"texto": "¿Qué critica Jesús de los hipócritas?",
         "opciones": ["Que oran para aparentar", "Que oran demasiado", "Que no oran nunca", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el lugar y la actitud con que Jesús pide orar.",
               "Recuerda lo que Jesús critica de los hipócritas."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SINCERIDAD", "definicion": "Orar de verdad, sin fingir"},
        {"termino": "SECRETO", "definicion": "Lugar privado donde Jesús pide orar"},
        {"termino": "CORAZÓN", "definicion": "Desde donde debe salir la oración verdadera"},
        {"termino": "HIPÓCRITA", "definicion": "Quien ora solo para que lo vean"},
        {"termino": "APARENTAR", "definicion": "Lo que hace quien ora para impresionar"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo pide Jesús que oremos, y en qué critica.",
               "HIPÓCRITA describe a una persona, no una actitud."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: orar de verdad",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús pide orar en ______, no para que nos vean.",
         "opciones": ["secreto", "público", "ruido"], "correcta": 0},
        {"texto": "La oración verdadera nace del ______.",
         "opciones": ["corazón", "miedo", "orgullo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el lugar donde Jesús pide orar.",
               "Recuerda desde dónde debe salir la oración verdadera."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús pide orar con el ______, no solo para aparentar.",
         "respuesta": "CORAZON", "banco": ["CORAZON", "ORGULLO", "MIEDO"]},
    ],
    "reflexion": "¿Cómo te gusta orar a ti: en voz alta, en silencio, con otros?",
    "requisito": 1,
    "pistas": ["Piensa en cómo pide Jesús que oremos.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: oro con sinceridad",
    "situacion": "Ya sabes que Jesús pide orar con sinceridad, desde el corazón, y no para que otros nos vean.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para orar con más sinceridad?",
         "opciones": ["Buscar un momento tranquilo para hablar con Dios",
                      "Orar aunque nadie me esté mirando",
                      "Decirle a Dios lo que realmente siento",
                      "Orar solo cuando otros me ven hacerlo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que describe orar solo para aparentar."],
    "feedback_ok": "¡Muy bien! Orar con sinceridad también fortalece tu amistad con Dios.",
})

# ==========================================================================
# PC09-C03 — Padre Nuestro
# ==========================================================================
C = "PC09-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Padre Nuestro",
    "items": [
        {"texto": "Cómo llama Jesús a Dios en esta oración.", "respuesta": "PADRE", "banco": ["PADRE", "JUEZ", "REY"]},
        {"texto": "Lo que pedimos que venga, según la oración de Jesús.", "respuesta": "REINO", "banco": ["REINO", "CASTIGO", "SILENCIO"]},
        {"texto": "Alimento diario que pedimos en esta oración.", "respuesta": "PAN", "banco": ["PAN", "ORO", "JUEGO"]},
        {"texto": "Lo que pedimos recibir y también dar a los demás.", "respuesta": "PERDON", "banco": ["PERDON", "CASTIGO", "OLVIDO"]},
        {"texto": "Lo que pedimos no caer, según el Padre Nuestro.", "respuesta": "TENTACION", "banco": ["TENTACION", "ORACION", "ALEGRIA"]},
        {"texto": "Lo que pedimos que se haga, como en el cielo.", "respuesta": "VOLUNTAD", "banco": ["VOLUNTAD", "DUDA", "COSTUMBRE"]},
    ],
    "incluir": ["PADRE", "PAN"], "requisito": 4,
    "pistas": ["Piensa en la oración que Jesús enseñó a sus discípulos.",
               "Todas las palabras son parte de lo que pedimos en el Padre Nuestro."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Padre Nuestro",
    "palabras": ["PADRE", "REINO", "PAN", "PERDON", "TENTACION", "VOLUNTAD"],
    "incluir": ["PADRE", "PAN"], "requisito": 5,
    "pistas": ["PAN es la palabra más corta: búscala primero.",
               "TENTACIÓN es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 6,9-13",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 6,9-13 y completa: «______ nuestro, que estás en "
                  "el cielo, santificado sea tu nombre.»", "respuesta": "PADRE", "banco": ["PADRE", "SEÑOR", "DIOS"]},
        {"texto": "¿Cómo comienza la oración que enseñó Jesús? ¿Qué le pedimos a Dios en ella?", "abierta": True, "palabras_esperadas": ["PADRE", "PAN", "PERDON", "REINO", "VOLUNTAD"], "respuestas_referencia": ["Comienza llamando a Dios Padre nuestro, y le pedimos el pan, el perdón y su reino.", "Empieza «Padre nuestro» y pedimos el pan de cada día y el perdón de nuestras ofensas.", "Se dirige a Dios como Padre y le pedimos su reino, el pan y el perdón."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 6.",
               "Es la oración más conocida que enseñó Jesús: empieza igual que la que tú ya sabes de memoria."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "En el Padre Nuestro llamamos a Dios ______.", "respuesta": "PADRE", "banco": ["PADRE", "JUEZ", "REY"]},
        {"texto": "Pedimos el ______ de cada día.", "respuesta": "PAN", "banco": ["PAN", "ORO", "JUEGO"]},
        {"texto": "Pedimos perdón, así como nosotros ______ a los demás.", "respuesta": "PERDONAMOS", "banco": ["PERDONAMOS", "CASTIGAMOS", "IGNORAMOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo empieza esta oración.",
               "La segunda respuesta es lo que pedimos para cada día."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Padre Nuestro comienza llamando a Dios «Padre».", "respuesta": True},
        {"texto": "En el Padre Nuestro pedimos el pan de cada día.", "respuesta": True},
        {"texto": "El Padre Nuestro no habla del perdón.", "respuesta": False},
        {"texto": "Jesús nos enseñó esta oración para todos.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo empieza esta oración y qué pedimos en ella.",
               "Si una frase dice que el Padre Nuestro no habla del perdón, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo llama Jesús a Dios en esta oración?",
         "opciones": ["Padre", "Juez", "Rey", "Extraño"], "correcta": 0},
        {"texto": "¿Qué pedimos en el Padre Nuestro?",
         "opciones": ["El pan de cada día y el perdón", "Riquezas", "Fama", "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo empieza la oración.",
               "Recuerda lo que pedimos a lo largo de toda la oración."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PADRE", "definicion": "Cómo llama Jesús a Dios en esta oración"},
        {"termino": "REINO", "definicion": "Lo que pedimos que venga"},
        {"termino": "PAN", "definicion": "Alimento diario que pedimos"},
        {"termino": "PERDÓN", "definicion": "Lo que pedimos recibir y dar"},
        {"termino": "TENTACIÓN", "definicion": "Lo que pedimos no caer"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cada parte del Padre Nuestro.",
               "TENTACIÓN es algo que pedimos evitar, no algo que pedimos recibir."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: las partes del Padre Nuestro",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El Padre Nuestro comienza llamando a Dios ______.",
         "opciones": ["Padre", "Juez", "Rey"], "correcta": 0},
        {"texto": "En el Padre Nuestro pedimos el ______ de cada día.",
         "opciones": ["pan", "oro", "juego"], "correcta": 0},
        {"texto": "También pedimos el ______ de nuestras ofensas.",
         "opciones": ["perdón", "castigo", "olvido"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el orden de lo que pedimos en esta oración.",
               "Recuerda cómo empieza, y qué pedimos para cada día."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Padre Nuestro es la oración que Jesús mismo nos ______.",
         "respuesta": "ENSEÑO", "banco": ["ENSEÑO", "OCULTO", "OLVIDO"]},
    ],
    "reflexion": "¿Qué parte del Padre Nuestro te gusta más?",
    "requisito": 1,
    "pistas": ["Piensa en quién nos enseñó esta oración.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: rezo el Padre Nuestro",
    "situacion": "Ya sabes que el Padre Nuestro es la oración que Jesús mismo enseñó a sus discípulos.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana con esta oración?",
         "opciones": ["Rezar el Padre Nuestro pensando en lo que dice",
                      "Enseñarlo a alguien que no lo sepa",
                      "Rezarlo en familia antes de comer o dormir",
                      "Decirlo rápido sin pensar en su significado"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que reza sin pensar en lo que dice."],
    "feedback_ok": "¡Muy bien! Rezar con atención el Padre Nuestro es hacerlo tuyo de verdad.",
})

# ==========================================================================
# PC09-C04 — La oración como diálogo de amor
# ==========================================================================
C = "PC09-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: diálogo de amor",
    "items": [
        {"texto": "Conversación entre dos que se quieren y confían.", "respuesta": "DIALOGO", "banco": ["DIALOGO", "SILENCIO", "DISTANCIA"]},
        {"texto": "Lo que sostiene la oración de Jesús con el Padre.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "OBLIGACION"]},
        {"texto": "Lo que buscaba Jesús para orar, lejos del ruido.", "respuesta": "SILENCIO", "banco": ["SILENCIO", "RUIDO", "FIESTA"]},
        {"texto": "Momento del día en que Jesús se levantaba a orar.", "respuesta": "MADRUGADA", "banco": ["MADRUGADA", "MEDIODIA", "NOCHE"]},
        {"texto": "Lugar solitario al que Jesús se retiraba a orar.", "respuesta": "APARTE", "banco": ["APARTE", "PLAZA", "MERCADO"]},
        {"texto": "Lo que también hacemos al orar, no solo hablar.", "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "EVITAR"]},
    ],
    "incluir": ["DIALOGO", "AMOR"], "requisito": 4,
    "pistas": ["Piensa en cómo y cuándo oraba Jesús.",
               "Todas las palabras describen la oración como una conversación de amor."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: diálogo de amor",
    "palabras": ["DIALOGO", "AMOR", "SILENCIO", "MADRUGADA", "APARTE", "ESCUCHAR"],
    "incluir": ["DIALOGO", "AMOR"], "requisito": 5,
    "pistas": ["AMOR es la palabra más corta: búscala primero.",
               "MADRUGADA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Marcos 1,35",
    "items": [
        {"texto": "Busca en tu Biblia Católica Marcos 1,35 y completa: «Se levantó de madrugada, "
                  "cuando todavía estaba oscuro, y se fue a un lugar ______ a orar.»", "respuesta": "SOLITARIO",
         "banco": ["SOLITARIO", "RUIDOSO", "PUBLICO"]},
        {"texto": "¿Cuándo y dónde oraba Jesús?", "abierta": True, "palabras_esperadas": ["MADRUGADA", "SOLITARIO", "APARTE", "SILENCIO", "ORAR"], "respuestas_referencia": ["Oraba muy de madrugada, en un lugar solitario y en silencio.", "Se levantaba temprano y se apartaba a un lugar tranquilo para orar.", "Oraba de madrugada, lejos de todos, en un lugar apartado."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Marcos en el índice de tu Biblia; el capítulo es el 1.",
               "El texto describe el momento del día y el tipo de lugar que Jesús buscaba."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús se levantaba de ______ para orar.", "respuesta": "MADRUGADA", "banco": ["MADRUGADA", "MEDIODIA", "NOCHE"]},
        {"texto": "Jesús buscaba un lugar ______ para hablar con el Padre.", "respuesta": "SOLITARIO", "banco": ["SOLITARIO", "RUIDOSO", "PUBLICO"]},
        {"texto": "Orar es también ______ a Dios, no solo hablar.", "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "EVITAR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el momento del día y el tipo de lugar que buscaba Jesús.",
               "La tercera respuesta es lo que también hacemos al orar, además de hablar."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús se levantaba de madrugada para orar.", "respuesta": True},
        {"texto": "Jesús oraba siempre rodeado de mucha gente.", "respuesta": False},
        {"texto": "La oración es también escuchar a Dios en silencio.", "respuesta": True},
        {"texto": "A Jesús no le importaba dedicar tiempo a orar.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cuándo y dónde le gustaba orar a Jesús.",
               "Si una frase dice que a Jesús no le importaba orar, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cuándo oraba Jesús, según este pasaje?",
         "opciones": ["Muy de madrugada", "Al mediodía", "Nunca", "Solo los domingos"], "correcta": 0},
        {"texto": "¿Qué buscaba Jesús para orar?",
         "opciones": ["Un lugar tranquilo y apartado", "Mucho ruido", "Compañía constante", "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el momento del día que menciona el texto.",
               "Recuerda el tipo de lugar que buscaba Jesús."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DIÁLOGO", "definicion": "Conversación entre dos que se quieren"},
        {"termino": "AMOR", "definicion": "Lo que sostiene la oración de Jesús"},
        {"termino": "SILENCIO", "definicion": "Lo que buscaba Jesús para orar"},
        {"termino": "MADRUGADA", "definicion": "Momento del día en que Jesús oraba"},
        {"termino": "ESCUCHAR", "definicion": "Lo que también hacemos al orar"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo, cuándo y por qué oraba Jesús.",
               "ESCUCHAR es parte de la oración, no solo hablar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: cómo oraba Jesús",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo oraba Jesús.",
    "tiempo_segundos": 45,
    "banco": ["DIALOGO", "AMOR", "SILENCIO", "ESCUCHAR", "RUIDO", "PRISA"],
    "correctas": ["DIALOGO", "AMOR", "SILENCIO", "ESCUCHAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Diálogo - Amor - Silencio - Escuchar.",
               "Descarta las palabras que describen lo contrario a cómo oraba Jesús."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús se levantaba de ______ para orar en un lugar tranquilo.",
         "respuesta": "MADRUGADA", "banco": ["MADRUGADA", "MEDIODIA", "NOCHE"]},
    ],
    "reflexion": "¿En qué momento del día te gustaría orar tú?",
    "requisito": 1,
    "pistas": ["Piensa en cuándo se levantaba Jesús a orar.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo la oración como diálogo",
    "situacion": "Ya sabes que Jesús buscaba tiempo y silencio para hablar con el Padre, como un verdadero diálogo de amor.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para vivir la oración como un diálogo?",
         "opciones": ["Buscar un momento de silencio para orar",
                      "Hablarle a Dios con mis propias palabras",
                      "Escuchar en silencio después de orar",
                      "Orar solo por costumbre, sin pensar en lo que digo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que describe una oración sin atención."],
    "feedback_ok": "¡Muy bien! Un verdadero diálogo también incluye escuchar, no solo hablar.",
})

# ==========================================================================
# PC09-C05 — Pedir y agradecer
# ==========================================================================
C = "PC09-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: pedir y agradecer",
    "items": [
        {"texto": "Presentar a Dios nuestras necesidades.", "respuesta": "PEDIR", "banco": ["PEDIR", "OLVIDAR", "ESCONDER"]},
        {"texto": "Dar gracias a Dios por lo que recibimos.", "respuesta": "AGRADECER", "banco": ["AGRADECER", "RECLAMAR", "IGNORAR"]},
        {"texto": "Lo que debemos tener al presentar nuestras peticiones a Dios.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "DUDA", "MIEDO"]},
        {"texto": "Actitud tranquila al esperar la respuesta de Dios.", "respuesta": "PACIENCIA", "banco": ["PACIENCIA", "PRISA", "ENOJO"]},
        {"texto": "Lo que san Pablo dice que no debemos sentir por nada.", "respuesta": "INQUIETUD", "banco": ["INQUIETUD", "ALEGRIA", "PAZ"]},
        {"texto": "Sentimiento de agradecimiento sincero.", "respuesta": "GRATITUD", "banco": ["GRATITUD", "INDIFERENCIA", "QUEJA"]},
    ],
    "incluir": ["PEDIR", "AGRADECER"], "requisito": 4,
    "pistas": ["Piensa en la actitud que pide san Pablo al orar.",
               "Todas las palabras hablan de cómo presentar nuestras peticiones a Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: pedir y agradecer",
    "palabras": ["PEDIR", "AGRADECER", "CONFIANZA", "PACIENCIA", "INQUIETUD", "GRATITUD"],
    "incluir": ["PEDIR", "AGRADECER"], "requisito": 5,
    "pistas": ["PEDIR es la palabra más corta: búscala primero.",
               "AGRADECER es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Filipenses 4,6",
    "items": [
        {"texto": "Busca en tu Biblia Católica Filipenses 4,6 y completa: «No os inquietéis por nada, "
                  "sino presentad a Dios vuestras peticiones, acompañadas de acción de ______.»", "respuesta": "GRACIAS",
         "banco": ["GRACIAS", "ENOJO", "DUDA"]},
        {"texto": "¿Qué actitud pide san Pablo al presentar nuestras peticiones a Dios?", "abierta": True, "palabras_esperadas": ["CONFIANZA", "GRACIAS", "AGRADECER", "PETICIONES", "ORAR"], "respuestas_referencia": ["Pide presentar nuestras peticiones con oración y acción de gracias.", "Que oremos con confianza y demos gracias al pedir algo a Dios.", "Que no nos preocupemos, sino que pidamos con oración y gratitud."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta de san Pablo a los Filipenses; el capítulo es el 4.",
               "San Pablo une dos actitudes: no preocuparse, y dar gracias al pedir."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo pide no ______ por nada.", "respuesta": "INQUIETARNOS", "banco": ["INQUIETARNOS", "ALEGRARNOS", "CONFIAR"]},
        {"texto": "Debemos presentar a Dios nuestras ______.", "respuesta": "PETICIONES", "banco": ["PETICIONES", "DUDAS", "QUEJAS"]},
        {"texto": "Nuestras peticiones deben ir acompañadas de acción de ______.", "respuesta": "GRACIAS", "banco": ["GRACIAS", "ENOJO", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que san Pablo pide que no sintamos.",
               "La tercera respuesta es lo que debe acompañar nuestras peticiones."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo pide que no nos inquietemos por nada.", "respuesta": True},
        {"texto": "San Pablo pide que oremos sin dar gracias nunca.", "respuesta": False},
        {"texto": "Debemos presentar nuestras peticiones a Dios con confianza.", "respuesta": True},
        {"texto": "Agradecer no tiene relación con la oración.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda las dos actitudes que pide san Pablo al orar.",
               "Si una frase dice que agradecer no tiene relación con la oración, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pide san Pablo que no sintamos?",
         "opciones": ["Inquietud", "Alegría", "Confianza", "Gratitud"], "correcta": 0},
        {"texto": "¿Con qué deben ir acompañadas nuestras peticiones?",
         "opciones": ["Con acción de gracias", "Con enojo", "Con duda", "Con nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que san Pablo pide dejar de sentir.",
               "Recuerda lo que debe acompañar cada petición."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PEDIR", "definicion": "Presentar a Dios nuestras necesidades"},
        {"termino": "AGRADECER", "definicion": "Dar gracias a Dios por lo que recibimos"},
        {"termino": "CONFIANZA", "definicion": "Actitud al presentar nuestras peticiones"},
        {"termino": "INQUIETUD", "definicion": "Lo que san Pablo pide no sentir"},
        {"termino": "GRATITUD", "definicion": "Sentimiento de agradecimiento sincero"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en las dos acciones y las dos actitudes que menciona el pasaje.",
               "INQUIETUD es lo que se deja atrás, no lo que se practica."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: pedir y agradecer",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo debemos orar, según san Pablo.",
    "tiempo_segundos": 45,
    "banco": ["PEDIR", "AGRADECER", "CONFIANZA", "GRATITUD", "INQUIETUD", "DUDA"],
    "correctas": ["PEDIR", "AGRADECER", "CONFIANZA", "GRATITUD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Pedir - Agradecer - Confianza - Gratitud.",
               "Descarta las palabras que san Pablo pide dejar atrás."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo pide presentar nuestras peticiones a Dios con oración y acción de ______.",
         "respuesta": "GRACIAS", "banco": ["GRACIAS", "ENOJO", "DUDA"]},
    ],
    "reflexion": "¿Por qué cosa te gustaría dar gracias a Dios hoy?",
    "requisito": 1,
    "pistas": ["Piensa en lo que debe acompañar cada petición.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: pido y agradezco",
    "situacion": "Ya sabes que san Pablo pide pedir con confianza y agradecer siempre a Dios.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para pedir y agradecer mejor?",
         "opciones": ["Dar gracias por algo bueno que me pasó",
                      "Pedirle a Dios ayuda con confianza",
                      "Agradecer aunque las cosas no salgan como quiero",
                      "Solo pedir cosas sin nunca agradecer"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que solo pide sin agradecer nunca."],
    "feedback_ok": "¡Muy bien! Agradecer, no solo pedir, también fortalece tu oración.",
})

# ==========================================================================
# PC09-C06 — Orar en familia y comunidad
# ==========================================================================
C = "PC09-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: orar juntos",
    "items": [
        {"texto": "Primer lugar donde se aprende a orar.", "respuesta": "FAMILIA", "banco": ["FAMILIA", "ESCUELA", "CALLE"]},
        {"texto": "Grupo de creyentes que ora unido.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "MULTITUD", "COMPETENCIA"]},
        {"texto": "Cómo es más fuerte la oración, según Jesús.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "DISTRAIDOS"]},
        {"texto": "Lo que promete Jesús a quienes oran reunidos en su nombre.", "respuesta": "PRESENCIA", "banco": ["PRESENCIA", "AUSENCIA", "DISTANCIA"]},
        {"texto": "Cómo estaban los que Jesús menciona en su promesa.", "respuesta": "REUNIDOS", "banco": ["REUNIDOS", "DISPERSOS", "SOLOS"]},
        {"texto": "Lo que hacemos juntos cuando hablamos con Dios en comunidad.", "respuesta": "ORAR", "banco": ["ORAR", "COMPETIR", "DISCUTIR"]},
    ],
    "incluir": ["FAMILIA", "COMUNIDAD"], "requisito": 4,
    "pistas": ["Piensa en la promesa que Jesús hace a quienes oran reunidos.",
               "Todas las palabras hablan de orar acompañado, no en soledad."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: orar juntos",
    "palabras": ["FAMILIA", "COMUNIDAD", "JUNTOS", "PRESENCIA", "REUNIDOS", "ORAR"],
    "incluir": ["FAMILIA", "COMUNIDAD"], "requisito": 5,
    "pistas": ["ORAR y JUNTOS son de las palabras más cortas: búscalas primero.",
               "COMUNIDAD es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 18,20",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 18,20 y completa: «Donde están dos o tres "
                  "reunidos en mi nombre, ahí estoy yo en medio de ______.»", "respuesta": "ELLOS",
         "banco": ["ELLOS", "NADIE", "SILENCIO"]},
        {"texto": "¿Qué promete Jesús cuando oramos reunidos?", "abierta": True, "palabras_esperadas": ["PRESENCIA", "REUNIDOS", "JUNTOS", "COMUNIDAD"], "respuestas_referencia": ["Promete que él mismo está presente donde dos o tres se reúnen en su nombre.", "Que Jesús está en medio de quienes oran juntos, reunidos en su nombre.", "Su propia presencia cuando nos reunimos a orar en su nombre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 18.",
               "Jesús promete algo muy especial a quienes se reúnen en su nombre, aunque sean pocos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús promete estar presente cuando oramos ______.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "DISTRAIDOS"]},
        {"texto": "La familia es el primer lugar donde se aprende a ______.", "respuesta": "ORAR", "banco": ["ORAR", "JUGAR", "TRABAJAR"]},
        {"texto": "La oración en ______ también une a los creyentes.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "SOLEDAD", "SILENCIO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la promesa de Jesús a quienes oran reunidos.",
               "La segunda respuesta es dónde se aprende primero a orar."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús promete estar presente cuando oramos reunidos en su nombre.", "respuesta": True},
        {"texto": "Orar en familia no tiene ningún valor.", "respuesta": False},
        {"texto": "La oración en comunidad también une a los creyentes.", "respuesta": True},
        {"texto": "A Jesús no le importa cómo oramos juntos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la promesa de Jesús a quienes se reúnen a orar.",
               "Si una frase dice que orar en familia no tiene valor, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué promete Jesús a quienes oran reunidos en su nombre?",
         "opciones": ["Estar presente entre ellos", "Ignorarlos", "Nada especial", "Castigarlos"], "correcta": 0},
        {"texto": "¿Dónde se aprende primero a orar?",
         "opciones": ["En la familia", "En la escuela solamente", "En ningún lugar", "Solo en la iglesia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la promesa de Jesús a quienes se reúnen en su nombre.",
               "Recuerda cuál es el primer lugar donde aprendemos a orar."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FAMILIA", "definicion": "Primer lugar donde se aprende a orar"},
        {"termino": "COMUNIDAD", "definicion": "Grupo de creyentes que ora unido"},
        {"termino": "JUNTOS", "definicion": "Cómo es más fuerte la oración"},
        {"termino": "PRESENCIA", "definicion": "Lo que promete Jesús a quienes oran reunidos"},
        {"termino": "REUNIDOS", "definicion": "Cómo estaban los que Jesús menciona"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la promesa de Jesús a quienes se reúnen en su nombre.",
               "PRESENCIA es lo que Jesús promete, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: orar en familia y comunidad",
    "instruccion": "En 45 segundos, marca las palabras que describen orar en familia y comunidad.",
    "tiempo_segundos": 45,
    "banco": ["FAMILIA", "COMUNIDAD", "JUNTOS", "PRESENCIA", "SOLEDAD", "DISTANCIA"],
    "correctas": ["FAMILIA", "COMUNIDAD", "JUNTOS", "PRESENCIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Familia - Comunidad - Juntos - Presencia.",
               "Descarta las palabras que describen lo contrario a orar acompañado."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús promete estar presente cuando oramos ______ en su nombre.",
         "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "DISTRAIDOS"]},
    ],
    "reflexion": "¿Con quién te gustaría orar esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en la promesa de Jesús a quienes oran reunidos.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: oro acompañado",
    "situacion": "Ya sabes que Jesús promete estar presente cuando oramos reunidos en su nombre, sea en familia o en comunidad.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para orar acompañado?",
         "opciones": ["Proponer una oración en familia",
                      "Orar junto a mi grupo de catequesis",
                      "Invitar a un amigo a orar conmigo",
                      "Orar siempre solo, sin compartirlo con nadie"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no comparte la oración con nadie."],
    "feedback_ok": "¡Muy bien! Orar acompañado también fortalece a la familia y a la comunidad.",
})

# ==========================================================================
# ==========================================================================
# PC10 — María, la Madre de Jesús y Madre nuestra   (Encuentro 10, Lucas 1,26-38 / Juan 19,25-27)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC10-C01 — La anunciación
# ==========================================================================
C = "PC10-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la anunciación",
    "items": [
        {"texto": "Mensajero enviado por Dios a visitar a María.", "respuesta": "ANGEL", "banco": ["ANGEL", "PROFETA", "REY"]},
        {"texto": "Nombre del ángel que visitó a María.", "respuesta": "GABRIEL", "banco": ["GABRIEL", "MIGUEL", "RAFAEL"]},
        {"texto": "Lo que el ángel trajo de parte de Dios.", "respuesta": "ANUNCIO", "banco": ["ANUNCIO", "CASTIGO", "SILENCIO"]},
        {"texto": "Joven a quien Dios eligió como madre de su Hijo.", "respuesta": "MARIA", "banco": ["MARIA", "ISABEL", "ANA"]},
        {"texto": "Pueblo donde vivía María.", "respuesta": "NAZARET", "banco": ["NAZARET", "BELEN", "JERUSALEN"]},
        {"texto": "Lo que María fue por Dios para esta misión especial.", "respuesta": "ELEGIDA", "banco": ["ELEGIDA", "OLVIDADA", "IGNORADA"]},
    ],
    "incluir": ["ANGEL", "MARIA"], "requisito": 4,
    "pistas": ["Piensa en la visita que recibió María de parte de Dios.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la anunciación",
    "palabras": ["ANGEL", "GABRIEL", "ANUNCIO", "MARIA", "NAZARET", "ELEGIDA"],
    "incluir": ["ANGEL", "MARIA"], "requisito": 5,
    "pistas": ["ÁNGEL y MARÍA son de las palabras más cortas: búscalas primero.",
               "ELEGIDA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 1,26-33",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 1,26-33 y completa: «Dios te salve, María, "
                  "llena eres de ______, el Señor es contigo.»", "respuesta": "GRACIA", "banco": ["GRACIA", "ORO", "GLORIA"]},
        {"texto": "¿Quién visitó a María y qué le anunció?", "abierta": True, "palabras_esperadas": ["ANGEL", "GABRIEL", "ANUNCIO", "HIJO", "JESUS"], "respuestas_referencia": ["El ángel Gabriel la visitó y le anunció que sería madre del Hijo de Dios.", "El ángel Gabriel le anunció que concebiría y daría a luz a Jesús.", "La visitó el ángel Gabriel, anunciándole que sería la madre del Salvador."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 1.",
               "El ángel saluda a María con unas palabras muy conocidas, que rezamos hasta hoy."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Dios envió al ángel ______ a visitar a María.", "respuesta": "GABRIEL", "banco": ["GABRIEL", "MIGUEL", "RAFAEL"]},
        {"texto": "El ángel anunció que María sería ______ del Hijo de Dios.", "respuesta": "MADRE", "banco": ["MADRE", "VECINA", "AMIGA"]},
        {"texto": "María vivía en el pueblo de ______.", "respuesta": "NAZARET", "banco": ["NAZARET", "BELEN", "JERUSALEN"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién visitó a María.",
               "La tercera respuesta es el pueblo donde vivía María."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El ángel Gabriel visitó a María.", "respuesta": True},
        {"texto": "El ángel le anunció que sería madre del Hijo de Dios.", "respuesta": True},
        {"texto": "María vivía en Jerusalén.", "respuesta": False},
        {"texto": "Esta visita del ángel se llama la Anunciación.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda quién visitó a María y qué le anunció.",
               "Si una frase dice que María vivía en Jerusalén, es falsa: vivía en Nazaret."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Quién visitó a María?",
         "opciones": ["El ángel Gabriel", "Un rey", "Un profeta", "Nadie"], "correcta": 0},
        {"texto": "¿Qué le anunció el ángel a María?",
         "opciones": ["Que sería madre del Hijo de Dios", "Que se mudaría", "Que sería reina", "Nada importante"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién trajo el mensaje de Dios a María.",
               "Recuerda cuál fue ese mensaje tan importante."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ÁNGEL", "definicion": "Mensajero enviado por Dios"},
        {"termino": "GABRIEL", "definicion": "Nombre del ángel que visitó a María"},
        {"termino": "ANUNCIO", "definicion": "Lo que el ángel trajo de parte de Dios"},
        {"termino": "MARÍA", "definicion": "Elegida como madre del Hijo de Dios"},
        {"termino": "NAZARET", "definicion": "Pueblo donde vivía María"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en quién visitó a María y de dónde era ella.",
               "NAZARET es un lugar, no una persona."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la anunciación",
    "instruccion": "En 45 segundos, marca las palabras que se relacionan con la Anunciación.",
    "tiempo_segundos": 45,
    "banco": ["ANGEL", "MARIA", "ANUNCIO", "GRACIA", "DUDA", "MIEDO"],
    "correctas": ["ANGEL", "MARIA", "ANUNCIO", "GRACIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Ángel - María - Anuncio - Gracia.",
               "Descarta las palabras que no aparecieron en este relato."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El ángel ______ visitó a María para darle un anuncio de parte de Dios.",
         "respuesta": "GABRIEL", "banco": ["GABRIEL", "MIGUEL", "RAFAEL"]},
    ],
    "reflexion": "¿Qué habrías sentido tú al recibir esa visita?",
    "requisito": 1,
    "pistas": ["Piensa en el nombre del ángel que visitó a María.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: estoy atento al llamado de Dios",
    "situacion": "Ya sabes que Dios eligió a María para una misión especial y se lo anunció por medio de un ángel.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para estar atento a lo que Dios te pide?",
         "opciones": ["Dedicar un momento a escuchar a Dios en silencio",
                      "Estar atento a las oportunidades de hacer el bien",
                      "Pedirle a Dios que me ayude a reconocer su llamado",
                      "Ignorar cualquier cosa que Dios me pida"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que ignora el llamado de Dios."],
    "feedback_ok": "¡Muy bien! Estar atento, como María, también es una forma de fe.",
})

# ==========================================================================
# PC10-C02 — El mensaje del ángel
# ==========================================================================
C = "PC10-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el mensaje del ángel",
    "items": [
        {"texto": "Lo que hizo María al escuchar el anuncio del ángel.", "respuesta": "PREGUNTA", "banco": ["PREGUNTA", "RESPUESTA", "SILENCIO"]},
        {"texto": "Lo que para Dios nada es, según el ángel.", "respuesta": "IMPOSIBLE", "banco": ["IMPOSIBLE", "DIFICIL", "SEGURO"]},
        {"texto": "Quien cubriría a María con su sombra, según el ángel.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "ANGEL", "PROFETA"]},
        {"texto": "Lo que Dios tiene para hacer cosas que parecen imposibles.", "respuesta": "PODER", "banco": ["PODER", "MIEDO", "DUDA"]},
        {"texto": "Nombre con que el ángel se refiere a Dios.", "respuesta": "ALTISIMO", "banco": ["ALTISIMO", "LEJANO", "EXTRAÑO"]},
        {"texto": "Actitud de María al escuchar la respuesta del ángel.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "MIEDO", "DUDA"]},
    ],
    "incluir": ["PREGUNTA", "IMPOSIBLE"], "requisito": 4,
    "pistas": ["Piensa en la pregunta de María y en la respuesta del ángel.",
               "Todas las palabras hablan de cómo Dios puede hacer lo que parece imposible."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el mensaje del ángel",
    "palabras": ["PREGUNTA", "IMPOSIBLE", "ESPIRITU", "PODER", "ALTISIMO", "CONFIANZA"],
    "incluir": ["PREGUNTA", "IMPOSIBLE"], "requisito": 5,
    "pistas": ["PODER es una de las palabras más cortas: búscala primero.",
               "CONFIANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 1,34-37",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 1,34-37 y completa: «El ángel le respondió... "
                  "porque para Dios nada hay ______.»", "respuesta": "IMPOSIBLE", "banco": ["IMPOSIBLE", "DIFICIL", "SEGURO"]},
        {"texto": "¿Qué pregunta hace María al ángel? ¿Qué le responde él?", "abierta": True, "palabras_esperadas": ["PREGUNTA", "COMO", "ESPIRITU", "PODER", "IMPOSIBLE"], "respuestas_referencia": ["María pregunta cómo será posible, y el ángel responde que el Espíritu Santo vendrá sobre ella.", "Pregunta cómo puede ser, y el ángel le dice que nada es imposible para Dios.", "María pregunta cómo, y el ángel le explica que será obra del Espíritu Santo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 1.",
               "María hace una pregunta sincera, y el ángel le responde hablando del Espíritu Santo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "María preguntó al ángel cómo sería ______ eso.", "respuesta": "POSIBLE", "banco": ["POSIBLE", "IMPOSIBLE", "DIFICIL"]},
        {"texto": "El ángel respondió que para Dios nada es ______.", "respuesta": "IMPOSIBLE", "banco": ["IMPOSIBLE", "SEGURO", "DIFICIL"]},
        {"texto": "El ______ Santo cubriría a María con su poder.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "ANGEL", "PROFETA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la pregunta que María le hizo al ángel.",
               "La tercera respuesta es quien cubriría a María con su sombra."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "María le hizo una pregunta al ángel.", "respuesta": True},
        {"texto": "El ángel le dijo que para Dios nada es imposible.", "respuesta": True},
        {"texto": "María no mostró ninguna duda ni pregunta.", "respuesta": False},
        {"texto": "El Espíritu Santo cubriría a María con su poder.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que preguntó María y lo que le respondió el ángel.",
               "Si una frase dice que María no preguntó nada, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pregunta hace María al ángel?",
         "opciones": ["Cómo será posible eso", "Cuándo se irá", "Quién es él", "Nada"], "correcta": 0},
        {"texto": "¿Qué responde el ángel sobre el poder de Dios?",
         "opciones": ["Que para Dios nada es imposible", "Que Dios no puede todo", "Que es difícil", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la duda sincera de María.",
               "Recuerda la certeza que el ángel le ofrece como respuesta."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PREGUNTA", "definicion": "Lo que hizo María al escuchar el anuncio"},
        {"termino": "IMPOSIBLE", "definicion": "Lo que para Dios nada es"},
        {"termino": "ESPÍRITU", "definicion": "Quien cubriría a María con su sombra"},
        {"termino": "PODER", "definicion": "Lo que Dios tiene para hacer cosas así"},
        {"termino": "CONFIANZA", "definicion": "Actitud de María al escuchar la respuesta"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la pregunta de María y en la respuesta del ángel.",
               "CONFIANZA describe una actitud, no una acción del ángel."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: nada es imposible para Dios",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "María le preguntó al ángel cómo sería ______ eso.",
         "opciones": ["posible", "imposible", "difícil"], "correcta": 0},
        {"texto": "El ángel respondió que para Dios nada es ______.",
         "opciones": ["imposible", "seguro", "difícil"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la pregunta que María le hizo al ángel.",
               "Recuerda la certeza que el ángel le da sobre el poder de Dios."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El ángel le dijo a María que para Dios nada es ______.",
         "respuesta": "IMPOSIBLE", "banco": ["IMPOSIBLE", "SEGURO", "DIFICIL"]},
    ],
    "reflexion": "¿Qué cosa te parece imposible y te gustaría confiar más a Dios?",
    "requisito": 1,
    "pistas": ["Piensa en la respuesta que el ángel le dio a María.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: confío en el poder de Dios",
    "situacion": "Ya sabes que el ángel le aseguró a María que para Dios nada es imposible.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para confiar más en Dios ante algo difícil?",
         "opciones": ["Pedirle ayuda a Dios en la oración",
                      "Recordar que Dios puede ayudarme aunque algo parezca difícil",
                      "Hablar con alguien de confianza sobre lo que me preocupa",
                      "Dejar de confiar y resolverlo todo solo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que deja a Dios fuera de la solución."],
    "feedback_ok": "¡Muy bien! Confiar en Dios, como María, también es un acto de fe.",
})

# ==========================================================================
# PC10-C03 — El sí de María
# ==========================================================================
C = "PC10-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el sí de María",
    "items": [
        {"texto": "Palabra que describe lo que hizo María: dijo que sí.", "respuesta": "ACEPTO", "banco": ["ACEPTO", "NEGO", "DUDO"]},
        {"texto": "Cómo se llama María a sí misma ante el ángel.", "respuesta": "SIERVA", "banco": ["SIERVA", "REINA", "DUEÑA"]},
        {"texto": "Palabra clave de la respuesta de María: «______ en mí...».", "respuesta": "HAGASE", "banco": ["HAGASE", "NIEGO", "DUDO"]},
        {"texto": "Actitud de María al aceptar lo que Dios le pide.", "respuesta": "OBEDIENCIA", "banco": ["OBEDIENCIA", "REBELDIA", "DUDA"]},
        {"texto": "Lo que María hace de su vida al decir que sí.", "respuesta": "ENTREGA", "banco": ["ENTREGA", "DISTANCIA", "NEGACION"]},
        {"texto": "Lo que María acepta que se cumpla en su vida.", "respuesta": "VOLUNTAD", "banco": ["VOLUNTAD", "CASTIGO", "DUDA"]},
    ],
    "incluir": ["ACEPTO", "SIERVA"], "requisito": 4,
    "pistas": ["Piensa en cómo respondió María al ángel.",
               "Todas las palabras hablan de la respuesta de María a Dios."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el sí de María",
    "palabras": ["ACEPTO", "SIERVA", "HAGASE", "OBEDIENCIA", "ENTREGA", "VOLUNTAD"],
    "incluir": ["ACEPTO", "SIERVA"], "requisito": 5,
    "pistas": ["ACEPTÓ es una de las palabras más cortas: búscala primero.",
               "OBEDIENCIA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 1,38",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 1,38 y completa: «He aquí la sierva del Señor; "
                  "hágase en mí según tu ______.»", "respuesta": "PALABRA", "banco": ["PALABRA", "DESEO", "GUSTO"]},
        {"texto": "¿Cómo responde María al ángel?", "abierta": True, "palabras_esperadas": ["SIERVA", "HAGASE", "ACEPTO", "OBEDIENCIA"], "respuestas_referencia": ["Responde que es la sierva del Señor y que se haga en ella según su palabra.", "Acepta con humildad, diciendo que se cumpla la voluntad de Dios.", "Dice que sí, llamándose sierva del Señor."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 1.",
               "Esta es la última frase de María en el relato de la Anunciación, y es su respuesta final."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "María se llama a sí misma la ______ del Señor.", "respuesta": "SIERVA", "banco": ["SIERVA", "REINA", "DUEÑA"]},
        {"texto": "María dice: «______ en mí según tu palabra».", "respuesta": "HAGASE", "banco": ["HAGASE", "NIEGO", "DUDO"]},
        {"texto": "María acepta la ______ de Dios con humildad.", "respuesta": "VOLUNTAD", "banco": ["VOLUNTAD", "RIQUEZA", "FAMA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se describe María a sí misma.",
               "La tercera respuesta es lo que María acepta que se cumpla."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "María aceptó la misión que Dios le proponía.", "respuesta": True},
        {"texto": "María se llamó a sí misma la sierva del Señor.", "respuesta": True},
        {"texto": "María se negó a lo que Dios le pedía.", "respuesta": False},
        {"texto": "El sí de María fue un acto de obediencia y confianza.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo respondió María al ángel.",
               "Si una frase dice que María se negó, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo responde María al ángel?",
         "opciones": ["Acepta con humildad", "Se niega", "No responde nada", "Duda para siempre"], "correcta": 0},
        {"texto": "¿Cómo se llama María a sí misma?",
         "opciones": ["La sierva del Señor", "La reina", "La dueña", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la actitud final de María ante la propuesta de Dios.",
               "Recuerda las palabras exactas con que se describe a sí misma."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ACEPTÓ", "definicion": "Lo que hizo María ante la propuesta de Dios"},
        {"termino": "SIERVA", "definicion": "Cómo se llama María a sí misma"},
        {"termino": "HÁGASE", "definicion": "Palabra clave de la respuesta de María"},
        {"termino": "OBEDIENCIA", "definicion": "Actitud de María al aceptar"},
        {"termino": "ENTREGA", "definicion": "Lo que María hace de su vida"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la respuesta completa de María al ángel.",
               "HÁGASE es la palabra exacta que usa María."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la respuesta de María",
    "instruccion": "En 45 segundos, marca las palabras que describen la respuesta de María.",
    "tiempo_segundos": 45,
    "banco": ["ACEPTO", "SIERVA", "OBEDIENCIA", "CONFIANZA", "NEGACION", "DUDA PERMANENTE"],
    "correctas": ["ACEPTO", "SIERVA", "OBEDIENCIA", "CONFIANZA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Aceptó - Sierva - Obediencia - Confianza.",
               "Descarta las palabras que describen lo contrario a la respuesta de María."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "María respondió que era la ______ del Señor y aceptó su voluntad.",
         "respuesta": "SIERVA", "banco": ["SIERVA", "REINA", "DUEÑA"]},
    ],
    "reflexion": "¿Cuándo te ha costado a ti decir que sí a algo bueno pero difícil?",
    "requisito": 1,
    "pistas": ["Piensa en cómo se llamó María a sí misma.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: imito el sí de María",
    "situacion": "Ya sabes que María dijo que sí a Dios con humildad y confianza, aunque no entendía todo.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para imitar el sí de María?",
         "opciones": ["Aceptar hacer algo bueno aunque cueste",
                      "Confiar en Dios en una situación difícil",
                      "Decir que sí a ayudar a alguien aunque no tenga ganas",
                      "Negarme siempre a lo que me cuesta"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que repite una negación constante."],
    "feedback_ok": "¡Muy bien! Decir que sí, como María, también fortalece tu fe.",
})

# ==========================================================================
# PC10-C04 — Fe y obediencia
# ==========================================================================
C = "PC10-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: fe y obediencia",
    "items": [
        {"texto": "Confianza total en Dios y en su palabra.", "respuesta": "FE", "banco": ["FE", "DUDA", "MIEDO"]},
        {"texto": "Actitud de cumplir lo que Dios pide.", "respuesta": "OBEDIENCIA", "banco": ["OBEDIENCIA", "REBELDIA", "DUDA"]},
        {"texto": "Lo que hizo María, sin ver todavía el cumplimiento de la promesa.", "respuesta": "CREER", "banco": ["CREER", "DUDAR", "TEMER"]},
        {"texto": "Cómo llama Isabel a María por haber creído.", "respuesta": "DICHOSA", "banco": ["DICHOSA", "TRISTE", "CONFUNDIDA"]},
        {"texto": "Lo que Isabel dice que Dios hará con su promesa.", "respuesta": "CUMPLIRA", "banco": ["CUMPLIRA", "OLVIDARA", "NEGARA"]},
        {"texto": "Poner la vida en manos de Dios con seguridad.", "respuesta": "CONFIAR", "banco": ["CONFIAR", "DUDAR", "TEMER"]},
    ],
    "incluir": ["FE", "OBEDIENCIA"], "requisito": 4,
    "pistas": ["Piensa en lo que Isabel le dice a María sobre su fe.",
               "Todas las palabras hablan de creer en Dios sin verlo todo todavía."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: fe y obediencia",
    "palabras": ["FE", "OBEDIENCIA", "CREER", "DICHOSA", "CUMPLIRA", "CONFIAR"],
    "incluir": ["FE", "OBEDIENCIA"], "requisito": 5,
    "pistas": ["FE es la palabra más corta: búscala primero.",
               "OBEDIENCIA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 1,45",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 1,45 y completa: «Dichosa tú, que has ______, "
                  "porque lo que te fue dicho de parte del Señor se cumplirá.»", "respuesta": "CREIDO",
         "banco": ["CREIDO", "DUDADO", "TEMIDO"]},
        {"texto": "¿Qué le dice Isabel a María sobre su fe?", "abierta": True, "palabras_esperadas": ["FE", "CREER", "DICHOSA", "CUMPLIRA", "CONFIO"], "respuestas_referencia": ["Le dice que es dichosa por haber creído en lo que Dios le prometió.", "Que es feliz porque creyó, y lo que Dios prometió se cumplirá.", "La llama dichosa por su fe y confianza en la promesa de Dios."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 1.",
               "Isabel felicita a María, no por lo que tiene, sino por lo que creyó."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Isabel llama a María ______ por su fe.", "respuesta": "DICHOSA", "banco": ["DICHOSA", "TRISTE", "CONFUNDIDA"]},
        {"texto": "María creyó sin ver todavía el ______ de la promesa.", "respuesta": "CUMPLIMIENTO", "banco": ["CUMPLIMIENTO", "FIN", "OLVIDO"]},
        {"texto": "La ______ de María fue un ejemplo para todos.", "respuesta": "FE", "banco": ["FE", "DUDA", "TRISTEZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama Isabel a María.",
               "La tercera respuesta es lo que hace de María un ejemplo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Isabel llama a María dichosa por haber creído.", "respuesta": True},
        {"texto": "María dudó de la promesa de Dios y no confió.", "respuesta": False},
        {"texto": "La fe de María es un ejemplo para nosotros.", "respuesta": True},
        {"texto": "Isabel dice que la promesa de Dios no se cumplirá.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Isabel le dice a María sobre su fe.",
               "Si una frase dice que la promesa de Dios no se cumplirá, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo llama Isabel a María?",
         "opciones": ["Dichosa", "Confundida", "Triste", "Nada especial"], "correcta": 0},
        {"texto": "¿Por qué es dichosa María, según Isabel?",
         "opciones": ["Por haber creído en la promesa de Dios", "Por ser rica", "Por ser famosa", "Por nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el saludo que le da Isabel a María.",
               "Recuerda el motivo de esa felicitación."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FE", "definicion": "Confianza total en Dios y su palabra"},
        {"termino": "OBEDIENCIA", "definicion": "Actitud de cumplir lo que Dios pide"},
        {"termino": "CREER", "definicion": "Lo que hizo María sin ver el cumplimiento"},
        {"termino": "DICHOSA", "definicion": "Cómo llama Isabel a María"},
        {"termino": "CUMPLIRÁ", "definicion": "Lo que Isabel dice sobre la promesa de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el saludo de Isabel y en la actitud de María.",
               "DICHOSA es cómo la llama Isabel, no una acción de María."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: dichosa por creer",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Isabel llama a María ______ por su fe.",
         "opciones": ["dichosa", "triste", "confundida"], "correcta": 0},
        {"texto": "María creyó sin ver todavía el ______ de la promesa.",
         "opciones": ["cumplimiento", "fin", "olvido"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el saludo de Isabel a María.",
               "Recuerda que la fe de María fue creer sin ver todavía."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Isabel llama a María ______ por haber creído en la promesa de Dios.",
         "respuesta": "DICHOSA", "banco": ["DICHOSA", "TRISTE", "CONFUNDIDA"]},
    ],
    "reflexion": "¿En qué promesa de Dios te gustaría confiar más?",
    "requisito": 1,
    "pistas": ["Piensa en cómo saluda Isabel a María.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo con fe",
    "situacion": "Ya sabes que María es dichosa porque creyó en la promesa de Dios, aunque no veía todavía su cumplimiento.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para vivir con más fe?",
         "opciones": ["Confiar en Dios aunque no vea el resultado todavía",
                      "Seguir orando aunque las cosas tarden",
                      "Recordar la fe de María cuando dude",
                      "Dejar de creer cuando algo no se cumple rápido"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que abandona la fe ante la espera."],
    "feedback_ok": "¡Muy bien! Creer sin ver todavía también es un acto de fe, como el de María.",
})

# ==========================================================================
# PC10-C05 — María nos acerca a Jesús
# ==========================================================================
C = "PC10-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: las bodas de Caná",
    "items": [
        {"texto": "Celebración donde Jesús hizo su primer milagro.", "respuesta": "BODAS", "banco": ["BODAS", "FIESTA", "CENA"]},
        {"texto": "Pueblo donde ocurrió el primer milagro de Jesús.", "respuesta": "CANA", "banco": ["CANA", "NAZARET", "BELEN"]},
        {"texto": "Lo que faltó en la fiesta, según notó María.", "respuesta": "VINO", "banco": ["VINO", "PAN", "AGUA"]},
        {"texto": "A quienes María se dirige para dar un consejo.", "respuesta": "SIRVIENTES", "banco": ["SIRVIENTES", "INVITADOS", "MUSICOS"]},
        {"texto": "Palabra con la que María pide que obedezcan a Jesús: «______ lo que él les diga».", "respuesta": "HAGAN", "banco": ["HAGAN", "OLVIDEN", "IGNOREN"]},
        {"texto": "Lo que hace María al pedir ayuda a Jesús por los demás.", "respuesta": "INTERCEDE", "banco": ["INTERCEDE", "IGNORA", "OLVIDA"]},
    ],
    "incluir": ["BODAS", "VINO"], "requisito": 4,
    "pistas": ["Piensa en el primer milagro de Jesús, en una fiesta de bodas.",
               "Todas las palabras se relacionan con lo que pasó en Caná."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: las bodas de Caná",
    "palabras": ["BODAS", "CANA", "VINO", "SIRVIENTES", "HAGAN", "INTERCEDE"],
    "incluir": ["BODAS", "VINO"], "requisito": 5,
    "pistas": ["VINO y CANÁ son de las palabras más cortas: búscalas primero.",
               "SIRVIENTES es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 2,3-5",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 2,3-5 y completa: «Su madre dijo a los "
                  "sirvientes: Haced lo que él os ______.»", "respuesta": "DIGA", "banco": ["DIGA", "PIDA", "MANDE"]},
        {"texto": "¿Qué le pide María a los sirvientes en las bodas de Caná?", "abierta": True, "palabras_esperadas": ["HAGAN", "OBEDEZCAN", "JESUS", "SIRVIENTES"], "respuestas_referencia": ["Les pide que hagan lo que Jesús les diga.", "Les dice que obedezcan a Jesús en lo que él les pida.", "Pide a los sirvientes que hagan caso a lo que Jesús indique."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 2.",
               "María nota un problema en la fiesta y da un consejo muy sencillo a los sirvientes."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "En las bodas de ______ faltó el vino.", "respuesta": "CANA", "banco": ["CANA", "JERUSALEN", "BELEN"]},
        {"texto": "María notó que faltaba el ______ en la fiesta.", "respuesta": "VINO", "banco": ["VINO", "PAN", "AGUA"]},
        {"texto": "María dijo a los sirvientes que hicieran lo que Jesús les ______.", "respuesta": "DIJERA", "banco": ["DIJERA", "PROHIBIERA", "OCULTARA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que faltó durante la fiesta.",
               "La tercera respuesta es el consejo que María dio a los sirvientes."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "En las bodas de Caná faltó el vino.", "respuesta": True},
        {"texto": "María pidió a los sirvientes que ignoraran a Jesús.", "respuesta": False},
        {"texto": "María intercede y acerca a las personas a Jesús.", "respuesta": True},
        {"texto": "Jesús no hizo ningún milagro en esas bodas.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que faltó en la fiesta y lo que hizo María.",
               "Si una frase dice que Jesús no hizo ningún milagro, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué faltó en la fiesta de las bodas de Caná?",
         "opciones": ["El vino", "El pan", "La música", "Nada"], "correcta": 0},
        {"texto": "¿Qué les pide María a los sirvientes?",
         "opciones": ["Que hagan lo que Jesús les diga", "Que se vayan", "Que ignoren el problema", "Nada"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que faltó durante la fiesta.",
               "Recuerda el consejo tan sencillo que da María."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "BODAS", "definicion": "Celebración donde Jesús hizo su primer milagro"},
        {"termino": "CANÁ", "definicion": "Pueblo donde ocurrió el milagro"},
        {"termino": "VINO", "definicion": "Lo que faltó en la fiesta"},
        {"termino": "SIRVIENTES", "definicion": "A quienes María dio un consejo"},
        {"termino": "INTERCEDE", "definicion": "Lo que hace María al pedir ayuda a Jesús por los demás"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el lugar, el problema y la solución de este relato.",
               "INTERCEDE describe una acción de María, no un lugar ni un objeto."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: las bodas de Caná",
    "instruccion": "En 45 segundos, marca las palabras que se relacionan con las bodas de Caná.",
    "tiempo_segundos": 45,
    "banco": ["BODAS", "VINO", "SIRVIENTES", "INTERCEDE", "INDIFERENCIA", "SILENCIO TOTAL"],
    "correctas": ["BODAS", "VINO", "SIRVIENTES", "INTERCEDE"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Bodas - Vino - Sirvientes - Intercede.",
               "Descarta las palabras que no tienen que ver con este relato."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "María pidió a los sirvientes que hicieran lo que ______ les dijera.",
         "respuesta": "JESUS", "banco": ["JESUS", "NADIE", "ELLOS"]},
    ],
    "reflexion": "¿Qué le pedirías tú a María que intercediera por ti?",
    "requisito": 1,
    "pistas": ["Piensa en el consejo que María dio a los sirvientes.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: llevo mis necesidades a Jesús",
    "situacion": "Ya sabes que María, al notar una necesidad, la llevó a Jesús y pidió que le hicieran caso.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana como hizo María en las bodas de Caná?",
         "opciones": ["Contarle a Jesús en oración lo que me preocupa",
                      "Ayudar a resolver un problema que noto en mi familia",
                      "Pedir a María que interceda por alguien que lo necesita",
                      "Ignorar los problemas que veo a mi alrededor"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que ignora lo que ves a tu alrededor."],
    "feedback_ok": "¡Muy bien! Notar y acercar una necesidad a Jesús también es imitar a María.",
})

# ==========================================================================
# PC10-C06 — Disponibilidad y alegría
# ==========================================================================
C = "PC10-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Magníficat",
    "items": [
        {"texto": "Nombre del canto de alabanza de María.", "respuesta": "MAGNIFICAT", "banco": ["MAGNIFICAT", "SALMO", "ALELUYA"]},
        {"texto": "Parte de María que engrandece al Señor, según su canto.", "respuesta": "ALMA", "banco": ["ALMA", "CUERPO", "VOZ"]},
        {"texto": "Lo que hace el espíritu de María al pensar en Dios.", "respuesta": "ALEGRA", "banco": ["ALEGRA", "ENTRISTECE", "CONFUNDE"]},
        {"texto": "Lo que Dios ha hecho por María, según su propio canto.", "respuesta": "GRANDES", "banco": ["GRANDES", "PEQUEÑAS", "POCAS"]},
        {"texto": "Actitud de María al reconocer que Dios la miró, siendo pequeña.", "respuesta": "HUMILDAD", "banco": ["HUMILDAD", "ORGULLO", "FAMA"]},
        {"texto": "Lo que hace María al cantar su alegría a Dios.", "respuesta": "ALABAR", "banco": ["ALABAR", "CALLAR", "OLVIDAR"]},
    ],
    "incluir": ["MAGNIFICAT", "ALMA"], "requisito": 4,
    "pistas": ["Piensa en el canto de alegría de María al visitar a Isabel.",
               "Todas las palabras hablan de la alabanza y la humildad de María."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Magníficat",
    "palabras": ["MAGNIFICAT", "ALMA", "ALEGRA", "GRANDES", "HUMILDAD", "ALABAR"],
    "incluir": ["MAGNIFICAT", "ALMA"], "requisito": 5,
    "pistas": ["ALMA es la palabra más corta: búscala primero.",
               "MAGNÍFICAT es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 1,46-49",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 1,46-49 y completa: «Engrandece mi alma al "
                  "Señor, y mi espíritu se ______ en Dios, mi salvador.»", "respuesta": "ALEGRA",
         "banco": ["ALEGRA", "ENTRISTECE", "CONFUNDE"]},
        {"texto": "¿Cómo expresa María su alegría en el Magníficat?", "abierta": True, "palabras_esperadas": ["ALMA", "ALEGRA", "ALABA", "GRANDES", "HUMILDAD"], "respuestas_referencia": ["Dice que su alma engrandece al Señor y su espíritu se alegra en Dios.", "Alaba a Dios con alegría porque ha hecho grandes cosas por ella.", "Expresa su alegría alabando a Dios por las grandes cosas que hizo por ella siendo humilde."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 1.",
               "Este es el canto que María dice al visitar a su prima Isabel."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "María dice que su ______ engrandece al Señor.", "respuesta": "ALMA", "banco": ["ALMA", "CUERPO", "VOZ"]},
        {"texto": "El espíritu de María se ______ en Dios.", "respuesta": "ALEGRA", "banco": ["ALEGRA", "ENTRISTECE", "CONFUNDE"]},
        {"texto": "María reconoce que Dios ha hecho ______ cosas por ella.", "respuesta": "GRANDES", "banco": ["GRANDES", "PEQUEÑAS", "POCAS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en las primeras palabras del canto de María.",
               "La segunda respuesta es lo que siente el espíritu de María."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Magníficat es el canto de alabanza de María.", "respuesta": True},
        {"texto": "María no siente ninguna alegría en su canto.", "respuesta": False},
        {"texto": "María reconoce las grandes cosas que Dios hizo por ella.", "respuesta": True},
        {"texto": "El Magníficat expresa la humildad de María.", "respuesta": True},
    ],
    "requisito": 3,
    "pistas": ["Recuerda el sentimiento que expresa María en su canto.",
               "Si una frase dice que María no siente alegría, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo se llama el canto de alabanza de María?",
         "opciones": ["Magníficat", "Salmo", "Aleluya", "Ninguno"], "correcta": 0},
        {"texto": "¿Qué siente María al cantar este himno?",
         "opciones": ["Alegría y gratitud", "Tristeza", "Miedo", "Indiferencia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el nombre propio de este canto.",
               "Recuerda el sentimiento que llena el corazón de María."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "MAGNÍFICAT", "definicion": "Nombre del canto de alabanza de María"},
        {"termino": "ALMA", "definicion": "Parte de María que engrandece al Señor"},
        {"termino": "ALEGRA", "definicion": "Lo que hace el espíritu de María"},
        {"termino": "GRANDES", "definicion": "Lo que Dios ha hecho por María"},
        {"termino": "HUMILDAD", "definicion": "Actitud de María al reconocer la mirada de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el nombre del canto y en su contenido.",
               "HUMILDAD describe una actitud, no una acción concreta."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: el canto de María",
    "instruccion": "En 45 segundos, marca las palabras que describen el Magníficat de María.",
    "tiempo_segundos": 45,
    "banco": ["ALMA", "ALEGRA", "HUMILDAD", "ALABAR", "TRISTEZA", "ORGULLO"],
    "correctas": ["ALMA", "ALEGRA", "HUMILDAD", "ALABAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Alma - Alegra - Humildad - Alabar.",
               "Descarta las palabras que no describen el espíritu de este canto."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El canto de alabanza de María se llama el ______.",
         "respuesta": "MAGNIFICAT", "banco": ["MAGNIFICAT", "SALMO", "ALELUYA"]},
    ],
    "reflexion": "¿Por qué cosas grandes que Dios ha hecho por ti darías gracias?",
    "requisito": 1,
    "pistas": ["Piensa en el nombre propio de este canto.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo con disponibilidad y alegría",
    "situacion": "Ya sabes que María, con humildad y alegría, alabó a Dios por las grandes cosas que hizo por ella.",
    "items": [
        {"texto": "¿Qué puedes hacer tú esta semana para vivir con esa misma disponibilidad y alegría?",
         "opciones": ["Dar gracias a Dios por las cosas buenas de mi vida",
                      "Estar disponible para ayudar cuando se me necesite",
                      "Alabar a Dios con alegría en mi oración",
                      "Quejarme en vez de agradecer"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que muestra una actitud contraria a la de María."],
    "feedback_ok": "¡Muy bien! Vivir con alegría y disponibilidad también es imitar a María, Madre nuestra.",
})

# ==========================================================================
# ==========================================================================
# PC11 — Somos amigos y misioneros de Jesús   (Encuentro 11, Juan 15,15-17 / Mateo 28,19-20)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC11-C01 — Jesús nos llama amigos
# ==========================================================================
C = "PC11-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús nos llama amigos",
    "items": [
        {"texto": "Como Jesús nos llama ahora, en vez de siervos.", "respuesta": "AMIGOS", "banco": ["AMIGOS", "SIERVOS", "EXTRAÑOS"]},
        {"texto": "Como ya no nos llama Jesús, porque ahora somos sus amigos.", "respuesta": "SIERVOS", "banco": ["SIERVOS", "AMIGOS", "HERMANOS"]},
        {"texto": "Lo que hace fuerte a una amistad verdadera.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "DISTANCIA", "DUDA"]},
        {"texto": "Lo contrario de estar lejos de alguien.", "respuesta": "CERCANIA", "banco": ["CERCANIA", "LEJANIA", "SOLEDAD"]},
        {"texto": "Lo que hacemos cuando prestamos atención a un amigo que habla.", "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "OLVIDAR"]},
        {"texto": "Lo que Jesús nos permite, al compartirnos lo que oyó del Padre.", "respuesta": "CONOCER", "banco": ["CONOCER", "ESCONDER", "DUDAR"]},
    ],
    "incluir": ["AMIGOS", "SIERVOS"], "requisito": 4,
    "pistas": ["Piensa en cómo Jesús nos llama ahora, según el evangelio de Juan.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús nos llama amigos",
    "palabras": ["AMIGOS", "SIERVOS", "CONFIANZA", "CERCANIA", "ESCUCHAR", "CONOCER"],
    "incluir": ["AMIGOS", "CONFIANZA"], "requisito": 5,
    "pistas": ["AMIGOS es de las palabras más cortas: búscala primero.",
               "CONFIANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 15,15",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 15,15 y completa: «Ya no los llamo ______, "
                  "sino que los he llamado amigos.»", "respuesta": "SIERVOS",
         "banco": ["SIERVOS", "EXTRAÑOS", "DESCONOCIDOS"]},
        {"texto": "¿Por qué Jesús nos llama amigos y no siervos?", "abierta": True,
         "palabras_esperadas": ["CONFIANZA", "COMPARTE", "AMA", "CERCA", "CONOCE"],
         "respuestas_referencia": ["Porque Jesús confía en nosotros y comparte todo lo que sabe.",
                                    "Porque nos ama y nos hace conocer lo que el Padre le dijo.",
                                    "Porque un amigo comparte y confía, no solo obedece órdenes."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 15.",
               "El texto dice cómo nos llama Jesús ahora, en vez de siervos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús ya no nos llama siervos, sino ______.", "respuesta": "AMIGOS", "banco": ["AMIGOS", "EXTRAÑOS", "DESCONOCIDOS"]},
        {"texto": "Un verdadero amigo comparte lo que sabe y siente ______.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "MIEDO", "DUDA"]},
        {"texto": "Ser amigo de Jesús significa estar ______ de él.", "respuesta": "CERCA", "banco": ["CERCA", "LEJOS", "SOLO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo Jesús nos llama ahora.",
               "La tercera respuesta describe cómo debemos estar de Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús nos llama amigos, no siervos.", "respuesta": True},
        {"texto": "Un amigo de Jesús no necesita escucharlo.", "respuesta": False},
        {"texto": "La amistad con Jesús se basa en la confianza.", "respuesta": True},
        {"texto": "Jesús esconde de sus amigos lo que sabe.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo nos llama Jesús ahora.",
               "Piensa en lo que hace un verdadero amigo: compartir, no esconder."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo nos llama Jesús, según el evangelio de Juan?",
         "opciones": ["Amigos", "Siervos", "Extraños", "Enemigos"], "correcta": 0},
        {"texto": "¿Qué comparte Jesús con sus amigos?",
         "opciones": ["Lo que oyó del Padre", "Nada", "Solo órdenes", "Secretos que no entendemos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo Jesús nos llama ahora.",
               "Recuerda lo que Jesús comparte con quienes ama."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "AMIGOS", "definicion": "Como nos llama Jesús ahora"},
        {"termino": "SIERVOS", "definicion": "Como ya no nos llama Jesús"},
        {"termino": "CONFIANZA", "definicion": "Lo que sostiene una amistad verdadera"},
        {"termino": "ESCUCHAR", "definicion": "Lo que hacemos con un amigo que habla"},
        {"termino": "CONOCER", "definicion": "Lo que Jesús nos permite, al compartir lo que sabe"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo Jesús nos llama ahora, y en cómo ya no nos llama.",
               "CONFIANZA describe una actitud, no una acción."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: la amistad con Jesús",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús nos llama ______, no siervos.",
         "opciones": ["amigos", "extraños", "enemigos"], "correcta": 0},
        {"texto": "La amistad con Jesús se basa en la ______.",
         "opciones": ["confianza", "distancia", "duda"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo Jesús nos llama ahora.",
               "Recuerda lo que sostiene una amistad verdadera."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús ya no nos llama siervos, sino ______.",
         "respuesta": "AMIGOS", "banco": ["AMIGOS", "SIERVOS", "EXTRAÑOS"]},
    ],
    "reflexion": "¿Qué sientes al saber que Jesús te llama su amigo?",
    "requisito": 1,
    "pistas": ["Piensa en cómo Jesús nos llama ahora.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: cuido mi amistad con Jesús",
    "situacion": "Ya sabes que Jesús te llama su amigo y confía en ti.",
    "items": [
        {"texto": "¿Qué puedes hacer para cuidar tu amistad con Jesús?",
         "opciones": ["Hablar con él en oración",
                      "Escucharlo en la Biblia",
                      "Contarle lo que sientes",
                      "Solo pensar en él una vez al año"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que muestra una amistad muy lejana."],
    "feedback_ok": "¡Muy bien! Así se cuida una amistad verdadera con Jesús.",
})

# ==========================================================================
# PC11-C02 — La amistad se comparte
# ==========================================================================
C = "PC11-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la amistad se comparte",
    "items": [
        {"texto": "Discípulo que llevó a su hermano a conocer a Jesús.", "respuesta": "ANDRES", "banco": ["ANDRES", "PEDRO", "JUAN"]},
        {"texto": "Familiar de Andrés a quien le contó sobre Jesús.", "respuesta": "HERMANO", "banco": ["HERMANO", "AMIGO", "VECINO"]},
        {"texto": "Lo que hizo Andrés: hallar a Jesús.", "respuesta": "ENCONTRAR", "banco": ["ENCONTRAR", "PERDER", "OLVIDAR"]},
        {"texto": "Lo que hacemos cuando damos a otros algo bueno que tenemos.", "respuesta": "COMPARTIR", "banco": ["COMPARTIR", "GUARDAR", "ESCONDER"]},
        {"texto": "Lo que hacemos cuando llamamos a alguien a vivir algo con nosotros.", "respuesta": "INVITAR", "banco": ["INVITAR", "RECHAZAR", "IGNORAR"]},
        {"texto": "Lo que sentimos al compartir algo bueno con quienes amamos.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "ENOJO"]},
    ],
    "incluir": ["ANDRES", "COMPARTIR"], "requisito": 4,
    "pistas": ["Piensa en el discípulo que llevó a su hermano a conocer a Jesús.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la amistad se comparte",
    "palabras": ["ANDRES", "HERMANO", "ENCONTRAR", "COMPARTIR", "INVITAR", "ALEGRIA"],
    "incluir": ["ANDRES", "COMPARTIR"], "requisito": 5,
    "pistas": ["ANDRES es de las palabras más cortas: búscala primero.",
               "ENCONTRAR y COMPARTIR son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 1,41-42",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 1,41-42 y completa: «Hemos encontrado al ______.» "
                  "(así le dijo Andrés a su hermano Simón)", "respuesta": "MESIAS",
         "banco": ["MESIAS", "PROFETA", "MAESTRO"]},
        {"texto": "¿Qué hizo Andrés después de encontrar a Jesús?", "abierta": True,
         "palabras_esperadas": ["HERMANO", "SIMON", "LLEVO", "COMPARTIO", "CONTO"],
         "respuestas_referencia": ["Buscó a su hermano Simón y lo llevó a conocer a Jesús.",
                                    "Le contó a su hermano que habían encontrado al Mesías.",
                                    "Compartió con su hermano lo que había descubierto."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 1.",
               "El texto cuenta a quién le habló Andrés apenas encontró a Jesús."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Andrés encontró a Jesús y se lo contó a su ______.", "respuesta": "HERMANO", "banco": ["HERMANO", "VECINO", "AMIGO"]},
        {"texto": "Un amigo verdadero no guarda para sí lo bueno, sino que lo ______.", "respuesta": "COMPARTE", "banco": ["COMPARTE", "ESCONDE", "OLVIDA"]},
        {"texto": "Andrés sintió ______ de haber encontrado al Mesías.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a quién le contó Andrés sobre Jesús.",
               "La tercera respuesta describe lo que sintió Andrés."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Andrés encontró a Jesús y guardó el secreto para sí mismo.", "respuesta": False},
        {"texto": "Andrés llevó a su hermano Simón a conocer a Jesús.", "respuesta": True},
        {"texto": "Compartir la amistad con Jesús también es una forma de amar.", "respuesta": True},
        {"texto": "A nadie le importa cuando le compartimos algo bueno.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué hizo Andrés apenas encontró a Jesús.",
               "Si una frase dice que Andrés guardó el secreto, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿A quién le contó Andrés sobre Jesús?",
         "opciones": ["A su hermano Simón", "A nadie", "A un desconocido", "A un sacerdote"], "correcta": 0},
        {"texto": "¿Qué debemos hacer con la alegría de conocer a Jesús?",
         "opciones": ["Compartirla con otros", "Guardarla en secreto", "Olvidarla", "Ignorarla"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a quién le contó Andrés sobre Jesús.",
               "Recuerda lo que hizo Andrés con su alegría."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ANDRES", "definicion": "Discípulo que compartió su hallazgo"},
        {"termino": "SIMON", "definicion": "Hermano de Andrés, a quien llevó ante Jesús"},
        {"termino": "MESIAS", "definicion": "A quien Andrés había encontrado"},
        {"termino": "COMPARTIR", "definicion": "Lo contrario de guardarse algo para uno mismo"},
        {"termino": "ALEGRIA", "definicion": "Lo que sentimos al compartir algo bueno"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en quién compartió su hallazgo y con quién lo compartió.",
               "MESIAS es a quien Andrés encontró, no una persona de su familia."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: lo que hizo Andrés",
    "instruccion": "En 45 segundos, marca las palabras que describen lo que hizo Andrés.",
    "tiempo_segundos": 45,
    "banco": ["ENCONTRAR", "HERMANO", "COMPARTIR", "ESCONDER", "ALEGRIA", "OLVIDAR"],
    "correctas": ["ENCONTRAR", "HERMANO", "COMPARTIR", "ALEGRIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Encontrar - Hermano - Compartir - Alegría.",
               "Descarta las palabras que describen lo contrario de compartir."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Andrés compartió con su ______ la alegría de haber encontrado a Jesús.",
         "respuesta": "HERMANO", "banco": ["HERMANO", "VECINO", "MAESTRO"]},
    ],
    "reflexion": "¿A quién te gustaría contarle sobre tu amistad con Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en a quién le contó Andrés sobre Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: comparto mi amistad con Jesús",
    "situacion": "Ya sabes que Andrés no se guardó para sí mismo la alegría de conocer a Jesús.",
    "items": [
        {"texto": "¿Cómo puedes tú compartir con otros tu amistad con Jesús?",
         "opciones": ["Contándole a alguien cercano lo que sientes",
                      "Invitando a un amigo a la catequesis",
                      "Mostrando alegría al hablar de Jesús",
                      "Guardando el secreto para siempre"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que repite lo contrario de lo que hizo Andrés."],
    "feedback_ok": "¡Muy bien! Compartir tu amistad con Jesús también es una forma de amar.",
})

# ==========================================================================
# PC11-C03 — El envío de los apóstoles
# ==========================================================================
C = "PC11-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el envío de los apóstoles",
    "items": [
        {"texto": "Lo que Jesús hizo con sus discípulos antes de subir al cielo.", "respuesta": "ENVIO", "banco": ["ENVIO", "ESCONDIO", "OLVIDO"]},
        {"texto": "Seguidores de Jesús enviados a anunciar la Buena Noticia.", "respuesta": "DISCIPULOS", "banco": ["DISCIPULOS", "EXTRAÑOS", "SOLDADOS"]},
        {"texto": "Lo que Jesús pidió hacer en el nombre del Padre, del Hijo y del Espíritu Santo.", "respuesta": "BAUTIZAR", "banco": ["BAUTIZAR", "IGNORAR", "ESCONDER"]},
        {"texto": "Lo que los discípulos debían hacer con lo que Jesús les enseñó.", "respuesta": "ENSEÑAR", "banco": ["ENSEÑAR", "OLVIDAR", "CALLAR"]},
        {"texto": "A quiénes debía llegar el mensaje de Jesús, según el envío.", "respuesta": "PUEBLOS", "banco": ["PUEBLOS", "POCOS", "NADIE"]},
        {"texto": "Tarea importante que Jesús encomienda a sus discípulos.", "respuesta": "MISION", "banco": ["MISION", "DESCANSO", "CASTIGO"]},
    ],
    "incluir": ["ENVIO", "DISCIPULOS"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús hizo con sus discípulos antes de subir al cielo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el envío de los apóstoles",
    "palabras": ["ENVIO", "DISCIPULOS", "BAUTIZAR", "ENSEÑAR", "PUEBLOS", "MISION"],
    "incluir": ["ENVIO", "MISION"], "requisito": 5,
    "pistas": ["ENVIO y MISION son de las palabras más cortas: búscalas primero.",
               "DISCIPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 28,19-20",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 28,19-20 y completa: «Vayan y hagan ______ "
                  "a todos los pueblos.»", "respuesta": "DISCIPULOS",
         "banco": ["DISCIPULOS", "ENEMIGOS", "SOLDADOS"]},
        {"texto": "¿Qué les pidió Jesús a sus discípulos antes de irse al cielo?", "abierta": True,
         "palabras_esperadas": ["ENSEÑAR", "BAUTIZAR", "IR", "ANUNCIAR", "DISCIPULOS"],
         "respuestas_referencia": ["Que fueran por todo el mundo y enseñaran a todos los pueblos.",
                                    "Que bautizaran y enseñaran a cumplir lo que él había enseñado.",
                                    "Que anunciaran el evangelio a todas las naciones."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 28.",
               "El texto describe lo último que Jesús pidió a sus discípulos antes de subir al cielo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús envió a sus discípulos a ______ a todos los pueblos.", "respuesta": "ENSEÑAR", "banco": ["ENSEÑAR", "IGNORAR", "OLVIDAR"]},
        {"texto": "Los discípulos debían bautizar en el nombre del Padre, del Hijo y del ______.", "respuesta": "ESPIRITU SANTO", "banco": ["ESPIRITU SANTO", "PROFETA", "ANGEL"]},
        {"texto": "Jesús prometió estar con sus discípulos hasta el fin del ______.", "respuesta": "MUNDO", "banco": ["MUNDO", "DIA", "AÑO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús pidió hacer a todos los pueblos.",
               "La tercera respuesta describe hasta cuándo Jesús promete acompañarlos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús envió a sus discípulos a todos los pueblos.", "respuesta": True},
        {"texto": "Jesús pidió a sus discípulos que guardaran el secreto y no dijeran nada.", "respuesta": False},
        {"texto": "Jesús prometió estar con sus discípulos siempre, hasta el fin del mundo.", "respuesta": True},
        {"texto": "Jesús solo envió a un discípulo, no a todos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda a quiénes envió Jesús a anunciar la Buena Noticia.",
               "Si una frase dice que Jesús pidió guardar silencio, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿A quiénes envió Jesús a anunciar la Buena Noticia?",
         "opciones": ["A todos los pueblos", "Solo a los ricos", "A nadie", "Solo a los sacerdotes"], "correcta": 0},
        {"texto": "¿Qué prometió Jesús a quienes envió?",
         "opciones": ["Estar con ellos siempre", "Abandonarlos", "Olvidarlos", "Castigarlos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a quiénes envió Jesús a anunciar la Buena Noticia.",
               "Recuerda la promesa que Jesús hizo a sus discípulos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ENVIO", "definicion": "Lo que Jesús hizo antes de subir al cielo"},
        {"termino": "DISCIPULOS", "definicion": "Enviados a anunciar la Buena Noticia"},
        {"termino": "BAUTIZAR", "definicion": "Lo que debían hacer en el nombre de la Trinidad"},
        {"termino": "PUEBLOS", "definicion": "A quiénes debía llegar el mensaje"},
        {"termino": "MISION", "definicion": "Tarea que Jesús encomendó a sus discípulos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que Jesús hizo con sus discípulos antes de subir al cielo.",
               "MISION es la tarea completa, no una acción concreta como bautizar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: el envío de Jesús",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús envió a sus discípulos a todos los ______.",
         "opciones": ["pueblos", "ricos", "pocos"], "correcta": 0},
        {"texto": "Jesús prometió estar con ellos hasta el fin del ______.",
         "opciones": ["mundo", "día", "año"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a quiénes envió Jesús.",
               "Recuerda hasta cuándo prometió acompañarlos."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús envió a sus discípulos a enseñar a todos los ______.",
         "respuesta": "PUEBLOS", "banco": ["PUEBLOS", "POCOS", "NADIE"]},
    ],
    "reflexion": "¿Qué te gustaría enseñarle a otros sobre Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en a quiénes envió Jesús a anunciar la Buena Noticia.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: participo en la misión",
    "situacion": "Ya sabes que Jesús envió a sus discípulos a anunciar la Buena Noticia a todos los pueblos.",
    "items": [
        {"texto": "¿Cómo puedes tú participar hoy en esa misión?",
         "opciones": ["Contando a otros lo que aprendes de Jesús",
                      "Ayudando en actividades de mi parroquia",
                      "Viviendo como Jesús enseña",
                      "Guardando la fe solo para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no comparte nada con nadie."],
    "feedback_ok": "¡Muy bien! Así se vive hoy la misión que Jesús encomendó.",
})

# ==========================================================================
# PC11-C04 — Ser testigos de Jesús
# ==========================================================================
C = "PC11-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: ser testigos de Jesús",
    "items": [
        {"texto": "Quien cuenta lo que ha visto y vivido.", "respuesta": "TESTIGO", "banco": ["TESTIGO", "DESCONOCIDO", "EXTRAÑO"]},
        {"texto": "Lo que hacemos al contar a otros la Buena Noticia.", "respuesta": "ANUNCIAR", "banco": ["ANUNCIAR", "CALLAR", "ESCONDER"]},
        {"texto": "Lo que necesitamos para hablar de Jesús sin miedo.", "respuesta": "VALENTIA", "banco": ["VALENTIA", "MIEDO", "DUDA"]},
        {"texto": "Lo que damos con nuestras acciones, no solo con palabras.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSA", "QUEJA"]},
        {"texto": "Lo que un testigo debe decir siempre.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
        {"texto": "Lo que el Espíritu Santo nos da para ser testigos.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "MIEDO", "PEREZA"]},
    ],
    "incluir": ["TESTIGO", "ANUNCIAR"], "requisito": 4,
    "pistas": ["Piensa en quién cuenta lo que ha visto y vivido con Jesús.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: ser testigos de Jesús",
    "palabras": ["TESTIGO", "ANUNCIAR", "VALENTIA", "EJEMPLO", "VERDAD", "CONFIANZA"],
    "incluir": ["TESTIGO", "VALENTIA"], "requisito": 5,
    "pistas": ["VERDAD es de las palabras más cortas: búscala primero.",
               "CONFIANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 1,8",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 1,8 y completa: «...y me serán ______ en "
                  "Jerusalén, en toda Judea y Samaria, y hasta los confines de la tierra.»", "respuesta": "TESTIGOS",
         "banco": ["TESTIGOS", "ENEMIGOS", "EXTRAÑOS"]},
        {"texto": "¿Qué significa ser testigo de Jesús?", "abierta": True,
         "palabras_esperadas": ["CONTAR", "VIVIR", "MOSTRAR", "EJEMPLO", "ANUNCIAR"],
         "respuestas_referencia": ["Es contar con la vida y las palabras lo que Jesús hizo por nosotros.",
                                    "Es mostrar con el ejemplo lo que hemos vivido con Jesús.",
                                    "Es anunciar a otros lo que Jesús significa para nosotros."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 1.",
               "El texto describe hasta dónde debía llegar el testimonio de los discípulos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Un testigo de Jesús cuenta lo que ha ______ con él.", "respuesta": "VIVIDO", "banco": ["VIVIDO", "OLVIDADO", "ESCONDIDO"]},
        {"texto": "Ser testigo también significa dar ______ con nuestras acciones.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSAS", "QUEJAS"]},
        {"texto": "El Espíritu Santo nos da ______ para hablar de Jesús.", "respuesta": "VALENTIA", "banco": ["VALENTIA", "MIEDO", "PEREZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que cuenta un testigo de Jesús.",
               "La tercera respuesta viene del Espíritu Santo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Un testigo de Jesús cuenta lo que ha vivido con él.", "respuesta": True},
        {"texto": "Ser testigo de Jesús no tiene nada que ver con nuestras acciones.", "respuesta": False},
        {"texto": "El Espíritu Santo nos da fuerza para ser testigos.", "respuesta": True},
        {"texto": "Los testigos de Jesús deben quedarse callados siempre.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué hace un testigo de Jesús.",
               "Si una frase dice que hay que quedarse callado siempre, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué es ser testigo de Jesús?",
         "opciones": ["Contar y mostrar lo que hemos vivido con él", "Quedarse callado", "Solo escuchar", "Esconder la fe"], "correcta": 0},
        {"texto": "¿Qué nos ayuda a ser testigos valientes?",
         "opciones": ["El Espíritu Santo", "El miedo", "La pereza", "El olvido"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace un testigo de Jesús.",
               "Recuerda quién nos da fuerza para ser testigos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "TESTIGO", "definicion": "Quien cuenta lo que ha vivido"},
        {"termino": "ANUNCIAR", "definicion": "Contar a otros la Buena Noticia"},
        {"termino": "VALENTIA", "definicion": "Lo que necesitamos para hablar sin miedo"},
        {"termino": "EJEMPLO", "definicion": "Lo que damos con nuestras acciones"},
        {"termino": "VERDAD", "definicion": "Lo que un testigo debe decir siempre"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que hace y necesita un testigo de Jesús.",
               "VERDAD es lo que un testigo dice, no lo que siente."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: ser testigos",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Un testigo de Jesús ______ lo que ha vivido con él.",
         "opciones": ["cuenta", "esconde", "olvida"], "correcta": 0},
        {"texto": "El Espíritu Santo nos da ______ para ser testigos.",
         "opciones": ["valentía", "miedo", "pereza"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace un testigo de Jesús.",
               "Recuerda quién nos ayuda a ser testigos valientes."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Un testigo de Jesús cuenta y muestra lo que ha ______ con él.",
         "respuesta": "VIVIDO", "banco": ["VIVIDO", "OLVIDADO", "ESCONDIDO"]},
    ],
    "reflexion": "¿De qué te gustaría dar testimonio sobre Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en lo que cuenta un testigo de Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: soy testigo de Jesús",
    "situacion": "Ya sabes que ser testigo de Jesús es contar y mostrar con la vida lo que hemos vivido con él.",
    "items": [
        {"texto": "¿Cómo puedes ser testigo de Jesús esta semana?",
         "opciones": ["Hablando de él con respeto cuando surja el tema",
                      "Tratando bien a los demás por su ejemplo",
                      "Compartiendo lo que aprendes en la catequesis",
                      "Escondiendo que eres su amigo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que esconde la amistad con Jesús."],
    "feedback_ok": "¡Muy bien! Así se vive el testimonio de un amigo de Jesús.",
})

# ==========================================================================
# PC11-C05 — Anunciar con la vida
# ==========================================================================
C = "PC11-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: anunciar con la vida",
    "items": [
        {"texto": "Lo que damos cuando nuestras acciones muestran lo que creemos.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSA", "QUEJA"]},
        {"texto": "Lo que hacemos, más que lo que decimos.", "respuesta": "ACCIONES", "banco": ["ACCIONES", "PALABRAS", "IDEAS"]},
        {"texto": "Vivir de acuerdo con lo que se cree y se dice.", "respuesta": "COHERENCIA", "banco": ["COHERENCIA", "MENTIRA", "DUDA"]},
        {"texto": "Lo que damos al mostrar con la vida lo que creemos.", "respuesta": "TESTIMONIO", "banco": ["TESTIMONIO", "SILENCIO", "OLVIDO"]},
        {"texto": "Actuar siempre diciendo la verdad.", "respuesta": "HONESTIDAD", "banco": ["HONESTIDAD", "MENTIRA", "ENGAÑO"]},
        {"texto": "Hacer el bien a los demás sin esperar nada a cambio.", "respuesta": "BONDAD", "banco": ["BONDAD", "EGOISMO", "ENVIDIA"]},
    ],
    "incluir": ["EJEMPLO", "TESTIMONIO"], "requisito": 4,
    "pistas": ["Piensa en cómo podemos anunciar a Jesús sin decir una sola palabra.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: anunciar con la vida",
    "palabras": ["EJEMPLO", "ACCIONES", "COHERENCIA", "TESTIMONIO", "HONESTIDAD", "BONDAD"],
    "incluir": ["EJEMPLO", "COHERENCIA"], "requisito": 5,
    "pistas": ["BONDAD es de las palabras más cortas: búscala primero.",
               "HONESTIDAD y COHERENCIA son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Pedro 3,15-16",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Pedro 3,15-16 y completa: «Estén siempre preparados "
                  "para dar ______ de la esperanza que hay en ustedes.»", "respuesta": "RAZON",
         "banco": ["RAZON", "DINERO", "EXCUSAS"]},
        {"texto": "¿Cómo podemos anunciar a Jesús sin decir ni una palabra?", "abierta": True,
         "palabras_esperadas": ["EJEMPLO", "ACCIONES", "VIDA", "AMOR", "OBRAS"],
         "respuestas_referencia": ["Con nuestras acciones y el ejemplo de nuestra vida diaria.",
                                    "Viviendo con amor y haciendo el bien a los demás.",
                                    "Mostrando con nuestra forma de actuar lo que creemos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta de Pedro en el índice de tu Biblia; el capítulo es el 3.",
               "El texto habla de estar listos para explicar la esperanza que llevamos dentro."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Podemos anunciar a Jesús con nuestro ______, no solo con palabras.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "SILENCIO", "OLVIDO"]},
        {"texto": "Vivir lo que creemos se llama ______.", "respuesta": "COHERENCIA", "banco": ["COHERENCIA", "MENTIRA", "CONFUSION"]},
        {"texto": "Hacer el bien sin esperar nada a cambio es ______.", "respuesta": "BONDAD", "banco": ["BONDAD", "EGOISMO", "ENVIDIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se puede anunciar a Jesús sin hablar.",
               "La segunda respuesta describe vivir según lo que se cree."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Podemos anunciar a Jesús con nuestras acciones.", "respuesta": True},
        {"texto": "Solo se anuncia a Jesús hablando, nunca con el ejemplo.", "respuesta": False},
        {"texto": "Vivir lo que creemos se llama coherencia.", "respuesta": True},
        {"texto": "La bondad no tiene nada que ver con anunciar a Jesús.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo podemos anunciar a Jesús sin hablar.",
               "Si una frase dice que solo se anuncia hablando, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo podemos anunciar a Jesús sin hablar?",
         "opciones": ["Con el ejemplo de nuestras acciones", "Escondiéndonos", "Ignorando a los demás", "No es posible"], "correcta": 0},
        {"texto": "¿Qué es vivir con coherencia?",
         "opciones": ["Actuar según lo que creemos", "Decir una cosa y hacer otra", "Mentir a veces", "Esconder la fe"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo se anuncia a Jesús sin palabras.",
               "Recuerda qué significa vivir con coherencia."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "EJEMPLO", "definicion": "Lo que damos con nuestras acciones"},
        {"termino": "COHERENCIA", "definicion": "Vivir según lo que creemos"},
        {"termino": "TESTIMONIO", "definicion": "Mostrar con la vida lo que creemos"},
        {"termino": "HONESTIDAD", "definicion": "Decir siempre la verdad"},
        {"termino": "BONDAD", "definicion": "Hacer el bien sin esperar nada a cambio"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en distintas formas de anunciar a Jesús con la vida.",
               "HONESTIDAD tiene que ver con decir la verdad."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: anunciar con la vida",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo anunciamos a Jesús con la vida.",
    "tiempo_segundos": 45,
    "banco": ["EJEMPLO", "COHERENCIA", "BONDAD", "MENTIRA", "HONESTIDAD", "EGOISMO"],
    "correctas": ["EJEMPLO", "COHERENCIA", "BONDAD", "HONESTIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Ejemplo - Coherencia - Bondad - Honestidad.",
               "Descarta las palabras que describen actitudes contrarias a estas."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Podemos anunciar a Jesús con nuestro ______, no solo con palabras.",
         "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "SILENCIO", "OLVIDO"]},
    ],
    "reflexion": "¿Qué acción tuya podría mostrarle a otros el amor de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en cómo se anuncia a Jesús sin palabras.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: anuncio con mi vida",
    "situacion": "Ya sabes que podemos anunciar a Jesús con nuestras acciones, no solo con palabras.",
    "items": [
        {"texto": "¿Qué puedes hacer esta semana para anunciar a Jesús con tu vida?",
         "opciones": ["Tratar bien a todos aunque nadie lo note",
                      "Decir siempre la verdad",
                      "Ayudar sin esperar nada a cambio",
                      "Solo hablar de Jesús sin cambiar nada en mi vida"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta, no en una idea.",
               "Descarta la única opción que no cambia nada en la vida diaria."],
    "feedback_ok": "¡Muy bien! Así se anuncia a Jesús con el ejemplo de cada día.",
})

# ==========================================================================
# PC11-C06 — Misioneros en la familia y la escuela
# ==========================================================================
C = "PC11-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: misioneros en casa y en la escuela",
    "items": [
        {"texto": "El primer lugar donde podemos anunciar a Jesús.", "respuesta": "FAMILIA", "banco": ["FAMILIA", "DESCONOCIDOS", "EXTRAÑOS"]},
        {"texto": "Lugar donde convivimos con nuestros compañeros cada día.", "respuesta": "ESCUELA", "banco": ["ESCUELA", "PLAZA", "MERCADO"]},
        {"texto": "Quienes comparten con nosotros la escuela cada día.", "respuesta": "COMPAÑEROS", "banco": ["COMPAÑEROS", "EXTRAÑOS", "DESCONOCIDOS"]},
        {"texto": "Personas con quienes convivimos todos los días.", "respuesta": "CERCANOS", "banco": ["CERCANOS", "LEJANOS", "AUSENTES"]},
        {"texto": "Lo que damos con nuestras acciones en casa y en la escuela.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSA", "QUEJA"]},
        {"texto": "Quien lleva a Jesús a los demás con su vida diaria.", "respuesta": "MISIONERO", "banco": ["MISIONERO", "EXTRAÑO", "DESCONOCIDO"]},
    ],
    "incluir": ["FAMILIA", "MISIONERO"], "requisito": 4,
    "pistas": ["Piensa en los lugares más cercanos donde podemos anunciar a Jesús.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: misioneros en casa y en la escuela",
    "palabras": ["FAMILIA", "ESCUELA", "COMPAÑEROS", "CERCANOS", "EJEMPLO", "MISIONERO"],
    "incluir": ["FAMILIA", "ESCUELA"], "requisito": 5,
    "pistas": ["FAMILIA y ESCUELA son de las palabras más cortas: búscalas primero.",
               "COMPAÑEROS y MISIONERO son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Marcos 5,19",
    "items": [
        {"texto": "Busca en tu Biblia Católica Marcos 5,19 y completa: «Vete a tu casa, con los "
                  "tuyos, y cuéntales todo lo que el ______ ha hecho por ti.»", "respuesta": "SEÑOR",
         "banco": ["SEÑOR", "VECINO", "MAESTRO"]},
        {"texto": "¿Dónde nos pide Jesús que empecemos a anunciarlo?", "abierta": True,
         "palabras_esperadas": ["CASA", "FAMILIA", "CERCA", "ESCUELA"],
         "respuestas_referencia": ["En nuestra propia casa y familia, con quienes están cerca de nosotros.",
                                    "Con los que tenemos más cerca, como la familia y los compañeros de escuela.",
                                    "Empezando por nuestra familia y los que convivimos con nosotros cada día."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Marcos en el índice de tu Biblia; el capítulo es el 5.",
               "El texto cuenta a dónde envió Jesús al hombre que había sanado."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús pidió al hombre sanado que contara en su ______ lo que el Señor había hecho por él.", "respuesta": "CASA", "banco": ["CASA", "ESCUELA", "PLAZA"]},
        {"texto": "En la escuela, podemos ser misioneros con nuestros ______.", "respuesta": "COMPAÑEROS", "banco": ["COMPAÑEROS", "DESCONOCIDOS", "EXTRAÑOS"]},
        {"texto": "Ser misionero en casa y en la escuela es dar buen ______.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSAS", "QUEJAS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a dónde envió Jesús al hombre que sanó.",
               "La segunda respuesta son quienes comparten con nosotros la escuela."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús pidió al hombre sanado que contara en su casa lo que el Señor había hecho por él.", "respuesta": True},
        {"texto": "Solo podemos ser misioneros lejos de casa, nunca cerca.", "respuesta": False},
        {"texto": "La escuela también es un lugar donde podemos anunciar a Jesús.", "respuesta": True},
        {"texto": "Ser misionero no tiene relación con cómo tratamos a nuestra familia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda a dónde envió Jesús al hombre que sanó.",
               "Si una frase dice que solo se puede ser misionero lejos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿A dónde envió Jesús al hombre que sanó?",
         "opciones": ["A su casa, con los suyos", "Lejos, para siempre", "A quedarse con él", "A otro país"], "correcta": 0},
        {"texto": "¿Dónde podemos empezar a ser misioneros?",
         "opciones": ["En la familia y la escuela", "Solo en países lejanos", "En ningún lugar", "Solo en la iglesia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a dónde envió Jesús al hombre sanado.",
               "Recuerda los lugares más cercanos donde podemos anunciar a Jesús."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FAMILIA", "definicion": "Primer lugar para anunciar a Jesús"},
        {"termino": "ESCUELA", "definicion": "Lugar donde convivimos con compañeros"},
        {"termino": "COMPAÑEROS", "definicion": "Con quienes compartimos la escuela"},
        {"termino": "EJEMPLO", "definicion": "Lo que damos con nuestras acciones diarias"},
        {"termino": "MISIONERO", "definicion": "Quien lleva a Jesús con su vida diaria"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en los lugares más cercanos donde podemos ser misioneros.",
               "MISIONERO es la persona, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: misioneros cerca de casa",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El primer lugar para ser misioneros es nuestra ______.",
         "opciones": ["familia", "lejanía", "soledad"], "correcta": 0},
        {"texto": "En la escuela podemos dar buen ______ a nuestros compañeros.",
         "opciones": ["ejemplo", "mal ejemplo", "silencio"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el lugar más cercano donde podemos ser misioneros.",
               "Recuerda lo que podemos dar a nuestros compañeros de escuela."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús pidió al hombre sanado que contara en su ______ lo que el Señor había hecho por él.",
         "respuesta": "CASA", "banco": ["CASA", "ESCUELA", "PLAZA"]},
    ],
    "reflexion": "¿Qué puedes hacer hoy en tu casa o en tu escuela para ser misionero de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en a dónde envió Jesús al hombre que sanó.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: misionero en mi día a día",
    "situacion": "Ya sabes que Jesús nos pide anunciarlo primero en casa y en la escuela, con quienes tenemos más cerca.",
    "items": [
        {"texto": "¿Cómo puedes ser misionero esta semana en tu familia o tu escuela?",
         "opciones": ["Tratando con respeto y amor a mi familia",
                      "Ayudando a un compañero de clase",
                      "Contando en casa algo lindo que aprendí de Jesús",
                      "Ser misionero solo cuando sea grande"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción concreta y cercana, no lejana.",
               "Descarta la única opción que pospone la misión para el futuro."],
    "feedback_ok": "¡Muy bien! La misión de anunciar a Jesús empieza cerca de casa.",
})

# ==========================================================================
# ==========================================================================
# PC12 — Dios nos promete la vida eterna   (Encuentro 12, Juan 11,25-26 / Juan 14,1-3)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC12-C01 — Jesús vence a la muerte
# ==========================================================================
C = "PC12-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús vence a la muerte",
    "items": [
        {"texto": "Amigo de Jesús que murió y fue devuelto a la vida.", "respuesta": "LAZARO", "banco": ["LAZARO", "PEDRO", "JUAN"]},
        {"texto": "Lugar donde habían puesto el cuerpo de Lázaro.", "respuesta": "TUMBA", "banco": ["TUMBA", "CASA", "CAMINO"]},
        {"texto": "Lo que hizo Jesús al ver la tristeza de las hermanas de Lázaro.", "respuesta": "LLORAR", "banco": ["LLORAR", "REIR", "CALLAR"]},
        {"texto": "Volver a vivir después de haber muerto.", "respuesta": "RESUCITAR", "banco": ["RESUCITAR", "DORMIR", "OLVIDAR"]},
        {"texto": "Lo que Jesús mostró al devolver la vida a Lázaro.", "respuesta": "PODER", "banco": ["PODER", "MIEDO", "DUDA"]},
        {"texto": "Lo que Jesús le devolvió a Lázaro.", "respuesta": "VIDA", "banco": ["VIDA", "TUMBA", "TRISTEZA"]},
    ],
    "incluir": ["LAZARO", "RESUCITAR"], "requisito": 4,
    "pistas": ["Piensa en el amigo de Jesús que murió y volvió a la vida.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús vence a la muerte",
    "palabras": ["LAZARO", "TUMBA", "LLORAR", "RESUCITAR", "PODER", "VIDA"],
    "incluir": ["LAZARO", "VIDA"], "requisito": 5,
    "pistas": ["VIDA es una de las palabras más cortas: búscala primero.",
               "RESUCITAR es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 11,43-44",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 11,43-44 y completa: «¡Lázaro, sal ______!»",
         "respuesta": "FUERA", "banco": ["FUERA", "ADENTRO", "YA"]},
        {"texto": "¿Qué hizo Jesús para mostrar que tiene poder sobre la muerte?", "abierta": True,
         "palabras_esperadas": ["LAZARO", "RESUCITO", "TUMBA", "VIDA", "PODER"],
         "respuestas_referencia": ["Llamó a Lázaro, que ya había muerto, y lo devolvió a la vida.",
                                    "Resucitó a su amigo Lázaro, que llevaba varios días en la tumba.",
                                    "Mostró que su poder es más fuerte que la muerte al resucitar a Lázaro."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 11.",
               "El texto cuenta lo que Jesús gritó frente a la tumba de su amigo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Lázaro era un ______ de Jesús que había muerto.", "respuesta": "AMIGO", "banco": ["AMIGO", "EXTRAÑO", "ENEMIGO"]},
        {"texto": "Jesús ______ al ver la tristeza de Marta y María.", "respuesta": "LLORO", "banco": ["LLORO", "RIO", "CALLO"]},
        {"texto": "Jesús llamó a Lázaro y lo devolvió a la ______.", "respuesta": "VIDA", "banco": ["VIDA", "TUMBA", "TRISTEZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién era Lázaro para Jesús.",
               "La tercera respuesta es lo que Jesús le devolvió a Lázaro."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Lázaro era amigo de Jesús.", "respuesta": True},
        {"texto": "Jesús no sintió tristeza por la muerte de Lázaro.", "respuesta": False},
        {"texto": "Jesús resucitó a Lázaro después de varios días.", "respuesta": True},
        {"texto": "Jesús no tiene poder sobre la muerte.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda quién era Lázaro para Jesús.",
               "Si una frase dice que Jesús no tiene poder sobre la muerte, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hizo Jesús frente a la tumba de Lázaro?",
         "opciones": ["Lo llamó y lo resucitó", "Se fue sin hacer nada", "Se enojó", "Lo ignoró"], "correcta": 0},
        {"texto": "¿Qué mostró Jesús al resucitar a Lázaro?",
         "opciones": ["Que tiene poder sobre la muerte", "Que le teme a la muerte", "Que no le importa la vida", "Que es débil"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús hizo frente a la tumba de Lázaro.",
               "Recuerda lo que Jesús mostró al resucitarlo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "LAZARO", "definicion": "Amigo de Jesús a quien resucitó"},
        {"termino": "TUMBA", "definicion": "Lugar donde estaba el cuerpo de Lázaro"},
        {"termino": "LLORAR", "definicion": "Lo que hizo Jesús por tristeza"},
        {"termino": "PODER", "definicion": "Lo que Jesús mostró sobre la muerte"},
        {"termino": "VIDA", "definicion": "Lo que Jesús devolvió a Lázaro"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que pasó con Lázaro y con Jesús.",
               "PODER es lo que Jesús mostró, no un lugar ni una persona."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: Jesús vence a la muerte",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús llamó a ______ para devolverle la vida.",
         "opciones": ["Lázaro", "un extraño", "un soldado"], "correcta": 0},
        {"texto": "Jesús mostró su ______ sobre la muerte.",
         "opciones": ["poder", "miedo", "debilidad"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el amigo de Jesús que resucitó.",
               "Recuerda lo que Jesús mostró frente a la tumba."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús resucitó a su amigo ______.",
         "respuesta": "LAZARO", "banco": ["LAZARO", "PEDRO", "JUAN"]},
    ],
    "reflexion": "¿Qué sientes al saber que Jesús tiene poder sobre la muerte?",
    "requisito": 1,
    "pistas": ["Piensa en el amigo de Jesús que resucitó.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: confío en el poder de Jesús",
    "situacion": "Ya sabes que Jesús tiene poder sobre la muerte y devolvió la vida a Lázaro.",
    "items": [
        {"texto": "¿Qué puedes hacer cuando sientas miedo o tristeza por la muerte de alguien?",
         "opciones": ["Recordar que Jesús tiene poder sobre la muerte",
                      "Rezar pidiendo consuelo",
                      "Hablar con mi familia sobre lo que siento",
                      "Pensar que todo termina para siempre"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de fe, no de desesperanza.",
               "Descarta la única opción que dice que todo termina para siempre."],
    "feedback_ok": "¡Muy bien! Jesús nos da esperanza frente a la muerte.",
})

# ==========================================================================
# PC12-C02 — "Yo soy la resurrección y la vida"
# ==========================================================================
C = "PC12-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Yo soy la resurrección y la vida",
    "items": [
        {"texto": "Lo que Jesús dijo que él es, junto con la vida.", "respuesta": "RESURRECCION", "banco": ["RESURRECCION", "TRISTEZA", "DUDA"]},
        {"texto": "Hermana de Lázaro que habló con Jesús antes del milagro.", "respuesta": "MARTA", "banco": ["MARTA", "MARIA", "SALOME"]},
        {"texto": "Lo que Jesús pidió a Marta que hiciera.", "respuesta": "CREER", "banco": ["CREER", "DUDAR", "TEMER"]},
        {"texto": "Lo que Jesús vence con su poder.", "respuesta": "MUERTE", "banco": ["MUERTE", "VIDA", "ALEGRIA"]},
        {"texto": "Tipo de vida que Jesús promete a quien cree en él.", "respuesta": "ETERNA", "banco": ["ETERNA", "CORTA", "VACIA"]},
        {"texto": "Lo que sentimos al confiar en la promesa de Jesús.", "respuesta": "ESPERANZA", "banco": ["ESPERANZA", "TRISTEZA", "DUDA"]},
    ],
    "incluir": ["RESURRECCION", "CREER"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús dijo que él es, junto con la vida.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Yo soy la resurrección y la vida",
    "palabras": ["RESURRECCION", "MARTA", "CREER", "MUERTE", "ETERNA", "ESPERANZA"],
    "incluir": ["MARTA", "ESPERANZA"], "requisito": 5,
    "pistas": ["MARTA es de las palabras más cortas: búscala primero.",
               "RESURRECCION es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 11,25-26",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 11,25-26 y completa: «Yo soy la resurrección y la ______. "
                  "El que cree en mí, aunque muera, vivirá.»", "respuesta": "VIDA",
         "banco": ["VIDA", "LUZ", "PAZ"]},
        {"texto": "¿Qué le prometió Jesús a Marta sobre la vida eterna?", "abierta": True,
         "palabras_esperadas": ["CREER", "VIVIR", "MUERTE", "ETERNA"],
         "respuestas_referencia": ["Que quien cree en él, aunque muera, vivirá para siempre.",
                                    "Que la muerte no tiene la última palabra para quien cree en Jesús.",
                                    "Que él mismo es la resurrección y la vida para quien confía en él."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 11.",
               "El texto dice lo que Jesús es, junto con la vida."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús le dijo a Marta: «Yo soy la ______ y la vida.»", "respuesta": "RESURRECCION", "banco": ["RESURRECCION", "LUZ", "PAZ"]},
        {"texto": "Quien cree en Jesús, aunque muera, ______.", "respuesta": "VIVIRA", "banco": ["VIVIRA", "DESAPARECERA", "OLVIDARA"]},
        {"texto": "Marta le dijo a Jesús que creía que él era el ______.", "respuesta": "MESIAS", "banco": ["MESIAS", "PROFETA", "MAESTRO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús dijo que él es.",
               "La tercera respuesta es lo que Marta reconoció que era Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús dijo que él es la resurrección y la vida.", "respuesta": True},
        {"texto": "Marta no creía que Jesús pudiera ayudarla.", "respuesta": False},
        {"texto": "Quien cree en Jesús tiene la promesa de la vida eterna.", "respuesta": True},
        {"texto": "Para Jesús, la muerte es más fuerte que la vida.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Jesús dijo que él es.",
               "Si una frase dice que la muerte es más fuerte que Jesús, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué le dijo Jesús a Marta sobre sí mismo?",
         "opciones": ["Que él es la resurrección y la vida", "Que no puede ayudarla", "Que la muerte es el final", "Que no cree en la vida eterna"], "correcta": 0},
        {"texto": "¿Qué le pidió Jesús a Marta?",
         "opciones": ["Que creyera en él", "Que dudara", "Que se alejara", "Que dejara de rezar"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús dijo que él es.",
               "Recuerda lo que Jesús pidió a Marta."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "RESURRECCION", "definicion": "Lo que Jesús dijo que él es"},
        {"termino": "MARTA", "definicion": "Hermana de Lázaro que habló con Jesús"},
        {"termino": "CREER", "definicion": "Lo que Jesús pidió a Marta"},
        {"termino": "ETERNA", "definicion": "Tipo de vida que Jesús promete"},
        {"termino": "ESPERANZA", "definicion": "Lo que sentimos al confiar en Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que Jesús dijo y en lo que pidió a Marta.",
               "ESPERANZA es un sentimiento, no una persona ni una promesa."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la promesa de Jesús a Marta",
    "instruccion": "En 45 segundos, marca las palabras que describen la promesa de Jesús a Marta.",
    "tiempo_segundos": 45,
    "banco": ["RESURRECCION", "CREER", "ESPERANZA", "VIDA", "DUDA", "MIEDO"],
    "correctas": ["RESURRECCION", "CREER", "ESPERANZA", "VIDA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Resurrección - Creer - Esperanza - Vida.",
               "Descarta las palabras que describen actitudes contrarias a la fe."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús le dijo a Marta: «Yo soy la resurrección y la ______.»",
         "respuesta": "VIDA", "banco": ["VIDA", "LUZ", "PAZ"]},
    ],
    "reflexion": "¿Qué significa para ti creer que Jesús es la resurrección y la vida?",
    "requisito": 1,
    "pistas": ["Piensa en lo que Jesús dijo que él es.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo con esperanza",
    "situacion": "Ya sabes que Jesús le prometió a Marta la vida eterna a quien cree en él.",
    "items": [
        {"texto": "¿Cómo puedes vivir hoy con la esperanza que Jesús nos da?",
         "opciones": ["Confiando en Jesús en los momentos difíciles",
                      "Rezando cuando siento miedo o tristeza",
                      "Recordando que la muerte no es el final",
                      "Pensando que nada tiene sentido"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de fe, no de desesperanza.",
               "Descarta la única opción que dice que nada tiene sentido."],
    "feedback_ok": "¡Muy bien! Así se vive con la esperanza que Jesús nos regala.",
})

# ==========================================================================
# PC12-C03 — El cielo, la casa del Padre
# ==========================================================================
C = "PC12-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el cielo, la casa del Padre",
    "items": [
        {"texto": "Donde Jesús nos prepara un lugar junto al Padre.", "respuesta": "CIELO", "banco": ["CIELO", "CAMINO", "DESIERTO"]},
        {"texto": "Como llamó Jesús al cielo: la ______ del Padre.", "respuesta": "CASA", "banco": ["CASA", "CIUDAD", "TIERRA"]},
        {"texto": "A quien pertenece la casa donde Jesús nos prepara un lugar.", "respuesta": "PADRE", "banco": ["PADRE", "AMIGO", "VECINO"]},
        {"texto": "Lo que Jesús promete preparar para nosotros.", "respuesta": "LUGAR", "banco": ["LUGAR", "CAMINO", "REGALO"]},
        {"texto": "Lo que Jesús va a hacer antes de que lleguemos al cielo.", "respuesta": "PREPARAR", "banco": ["PREPARAR", "OLVIDAR", "ESCONDER"]},
        {"texto": "Palabra que usa Jesús para los muchos lugares en la casa del Padre.", "respuesta": "MORADAS", "banco": ["MORADAS", "PUERTAS", "VENTANAS"]},
    ],
    "incluir": ["CIELO", "PADRE"], "requisito": 4,
    "pistas": ["Piensa en cómo llama Jesús al cielo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el cielo, la casa del Padre",
    "palabras": ["CIELO", "CASA", "PADRE", "LUGAR", "PREPARAR", "MORADAS"],
    "incluir": ["CASA", "MORADAS"], "requisito": 5,
    "pistas": ["CASA es una de las palabras más cortas: búscala primero.",
               "PREPARAR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 14,2-3",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 14,2-3 y completa: «En la casa de mi Padre hay muchas ______.»",
         "respuesta": "MORADAS", "banco": ["MORADAS", "PUERTAS", "VENTANAS"]},
        {"texto": "¿Qué promete Jesús hacer antes de que lleguemos al cielo?", "abierta": True,
         "palabras_esperadas": ["PREPARAR", "LUGAR", "VOLVER", "LLEVAR"],
         "respuestas_referencia": ["Promete prepararnos un lugar en la casa de su Padre.",
                                    "Promete volver para llevarnos con él al cielo.",
                                    "Promete que estaremos donde él está, junto al Padre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 14.",
               "El texto habla de los muchos lugares que hay en la casa del Padre."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús llama al cielo la casa de su ______.", "respuesta": "PADRE", "banco": ["PADRE", "AMIGO", "VECINO"]},
        {"texto": "En la casa del Padre hay muchas ______.", "respuesta": "MORADAS", "banco": ["MORADAS", "PUERTAS", "VENTANAS"]},
        {"texto": "Jesús promete ______ un lugar para nosotros.", "respuesta": "PREPARAR", "banco": ["PREPARAR", "OLVIDAR", "ESCONDER"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama Jesús al cielo.",
               "La tercera respuesta es lo que Jesús hace antes de que lleguemos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús llama al cielo la casa de su Padre.", "respuesta": True},
        {"texto": "En el cielo no hay lugar para nadie más.", "respuesta": False},
        {"texto": "Jesús promete volver para llevarnos con él.", "respuesta": True},
        {"texto": "A Jesús no le importa prepararnos un lugar.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo llama Jesús al cielo.",
               "Si una frase dice que a Jesús no le importa prepararnos un lugar, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo llama Jesús al cielo?",
         "opciones": ["La casa de su Padre", "Un lugar vacío", "Un lugar lejano y solo", "Un secreto"], "correcta": 0},
        {"texto": "¿Qué promete hacer Jesús después de prepararnos un lugar?",
         "opciones": ["Volver y llevarnos con él", "Olvidarnos", "Quedarse solo", "Cerrar la puerta"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama Jesús al cielo.",
               "Recuerda lo que promete hacer Jesús después de prepararnos un lugar."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CIELO", "definicion": "Casa del Padre preparada para nosotros"},
        {"termino": "PADRE", "definicion": "A quien pertenece la casa celestial"},
        {"termino": "MORADAS", "definicion": "Los muchos lugares en la casa del Padre"},
        {"termino": "PREPARAR", "definicion": "Lo que Jesús hace antes de nuestra llegada"},
        {"termino": "VOLVER", "definicion": "Lo que Jesús promete hacer para llevarnos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que Jesús promete sobre el cielo.",
               "VOLVER es una acción futura de Jesús, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: la casa del Padre",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús llama al cielo la casa de su ______.",
         "opciones": ["Padre", "vecino", "amigo"], "correcta": 0},
        {"texto": "En esa casa hay muchas ______.",
         "opciones": ["moradas", "puertas cerradas", "habitaciones vacías"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo llama Jesús al cielo.",
               "Recuerda lo que hay en la casa del Padre."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "En la casa del Padre hay muchas ______.",
         "respuesta": "MORADAS", "banco": ["MORADAS", "PUERTAS", "VENTANAS"]},
    ],
    "reflexion": "¿Qué sientes al saber que Jesús te está preparando un lugar en el cielo?",
    "requisito": 1,
    "pistas": ["Piensa en lo que hay en la casa del Padre.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: espero la casa del Padre",
    "situacion": "Ya sabes que Jesús promete prepararnos un lugar en la casa de su Padre.",
    "items": [
        {"texto": "¿Cómo puedes vivir con la esperanza de llegar algún día a esa casa?",
         "opciones": ["Confiando en la promesa de Jesús",
                      "Viviendo con amor cada día",
                      "Rezando y agradeciendo a Dios",
                      "Pensando que el cielo no existe"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de fe, no de duda.",
               "Descarta la única opción que niega la promesa de Jesús."],
    "feedback_ok": "¡Muy bien! Así se vive esperando la casa que Jesús nos prepara.",
})

# ==========================================================================
# PC12-C04 — Vivir con esperanza
# ==========================================================================
C = "PC12-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: vivir con esperanza",
    "items": [
        {"texto": "Lo que un cristiano tiene frente a la muerte, a diferencia de quien no cree.", "respuesta": "ESPERANZA", "banco": ["ESPERANZA", "TRISTEZA", "DUDA"]},
        {"texto": "Lo que sentimos cuando perdemos a alguien que amamos.", "respuesta": "TRISTEZA", "banco": ["TRISTEZA", "ALEGRIA", "CALMA"]},
        {"texto": "Lo que Dios nos da en los momentos de tristeza.", "respuesta": "CONSUELO", "banco": ["CONSUELO", "SILENCIO", "OLVIDO"]},
        {"texto": "Lo que ponemos en la promesa de Jesús.", "respuesta": "CONFIANZA", "banco": ["CONFIANZA", "DUDA", "MIEDO"]},
        {"texto": "Lo que Jesús nos hizo sobre la vida eterna.", "respuesta": "PROMESA", "banco": ["PROMESA", "AMENAZA", "SECRETO"]},
        {"texto": "Lo que recibimos de Dios para seguir adelante.", "respuesta": "FORTALEZA", "banco": ["FORTALEZA", "DEBILIDAD", "PEREZA"]},
    ],
    "incluir": ["ESPERANZA", "CONSUELO"], "requisito": 4,
    "pistas": ["Piensa en lo que tiene un cristiano frente a la muerte.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: vivir con esperanza",
    "palabras": ["ESPERANZA", "TRISTEZA", "CONSUELO", "CONFIANZA", "PROMESA", "FORTALEZA"],
    "incluir": ["ESPERANZA", "PROMESA"], "requisito": 5,
    "pistas": ["PROMESA es una de las palabras más cortas: búscala primero.",
               "ESPERANZA y FORTALEZA son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Tesalonicenses 4,13",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Tesalonicenses 4,13 y completa: «No queremos que se entristezcan "
                  "como los que no tienen ______.»", "respuesta": "ESPERANZA",
         "banco": ["ESPERANZA", "FAMILIA", "AMIGOS"]},
        {"texto": "¿En qué se diferencia la tristeza de un cristiano de la de alguien sin fe?", "abierta": True,
         "palabras_esperadas": ["ESPERANZA", "PROMESA", "VIDA", "ETERNA"],
         "respuestas_referencia": ["El cristiano vive la tristeza con la esperanza de la vida eterna.",
                                    "El cristiano confía en la promesa de Jesús aunque también sienta dolor.",
                                    "El cristiano sabe que la muerte no es el final, gracias a la fe."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a los Tesalonicenses en el índice de tu Biblia; el capítulo es el 4.",
               "El texto compara a quienes tienen esperanza con quienes no la tienen."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo dice que no debemos entristecernos como quienes no tienen ______.", "respuesta": "ESPERANZA", "banco": ["ESPERANZA", "FAMILIA", "DINERO"]},
        {"texto": "Dios nos da ______ en los momentos difíciles.", "respuesta": "CONSUELO", "banco": ["CONSUELO", "TRISTEZA", "MIEDO"]},
        {"texto": "La fe nos da ______ para seguir adelante.", "respuesta": "FORTALEZA", "banco": ["FORTALEZA", "DEBILIDAD", "PEREZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que San Pablo dice que tienen los cristianos.",
               "La segunda respuesta es lo que Dios nos da en la tristeza."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los cristianos también sienten tristeza cuando alguien muere.", "respuesta": True},
        {"texto": "La esperanza cristiana dice que la muerte es el final de todo.", "respuesta": False},
        {"texto": "Dios nos da consuelo en los momentos de tristeza.", "respuesta": True},
        {"texto": "Nuestra fe no cambia en nada la forma de vivir la tristeza.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué tienen los cristianos frente a la muerte.",
               "Si una frase dice que la muerte es el final de todo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "Según San Pablo, ¿qué tienen los cristianos frente a la muerte?",
         "opciones": ["Esperanza", "Ninguna diferencia", "Miedo total", "Indiferencia"], "correcta": 0},
        {"texto": "¿Qué nos da Dios en los momentos de tristeza?",
         "opciones": ["Consuelo y fortaleza", "Nada", "Más tristeza", "Soledad"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que tienen los cristianos frente a la muerte.",
               "Recuerda lo que Dios nos da en la tristeza."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ESPERANZA", "definicion": "Lo que tiene un cristiano frente a la muerte"},
        {"termino": "CONSUELO", "definicion": "Lo que Dios da en la tristeza"},
        {"termino": "CONFIANZA", "definicion": "Lo que ponemos en la promesa de Jesús"},
        {"termino": "PROMESA", "definicion": "Lo que Jesús nos hizo sobre la vida eterna"},
        {"termino": "FORTALEZA", "definicion": "Lo que recibimos para seguir adelante"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en lo que sostiene a un cristiano en la tristeza.",
               "PROMESA es lo que Jesús dijo, no un sentimiento."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: vivir con esperanza",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo vive un cristiano con esperanza.",
    "tiempo_segundos": 45,
    "banco": ["ESPERANZA", "CONSUELO", "FORTALEZA", "CONFIANZA", "MIEDO", "DESANIMO"],
    "correctas": ["ESPERANZA", "CONSUELO", "FORTALEZA", "CONFIANZA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Esperanza - Consuelo - Fortaleza - Confianza.",
               "Descarta las palabras que describen actitudes contrarias a la fe."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo dice que no debemos entristecernos como quienes no tienen ______.",
         "respuesta": "ESPERANZA", "banco": ["ESPERANZA", "FAMILIA", "DINERO"]},
    ],
    "reflexion": "¿Qué te ayuda a ti a vivir con esperanza en los momentos difíciles?",
    "requisito": 1,
    "pistas": ["Piensa en lo que tienen los cristianos frente a la muerte.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo la tristeza con esperanza",
    "situacion": "Ya sabes que la fe nos da esperanza y consuelo frente a la tristeza.",
    "items": [
        {"texto": "¿Qué puedes hacer cuando estés triste por la pérdida de alguien?",
         "opciones": ["Rezar pidiendo consuelo a Dios",
                      "Recordar la promesa de la vida eterna",
                      "Hablar de lo que siento con mi familia",
                      "Pensar que nada tiene sentido"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de fe, no de desesperanza.",
               "Descarta la única opción que dice que nada tiene sentido."],
    "feedback_ok": "¡Muy bien! Así se vive la tristeza con esperanza cristiana.",
})

# ==========================================================================
# PC12-C05 — Los santos ya viven con Dios
# ==========================================================================
C = "PC12-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: los santos ya viven con Dios",
    "items": [
        {"texto": "Personas que ya viven felices junto a Dios en el cielo.", "respuesta": "SANTOS", "banco": ["SANTOS", "EXTRAÑOS", "SOLDADOS"]},
        {"texto": "Gran cantidad de gente que San Juan vio delante del trono de Dios.", "respuesta": "MULTITUD", "banco": ["MULTITUD", "PERSONA", "FAMILIA"]},
        {"texto": "Lo que los santos dan a Dios en el cielo.", "respuesta": "ALABANZA", "banco": ["ALABANZA", "QUEJA", "SILENCIO"]},
        {"texto": "Estado de felicidad plena junto a Dios.", "respuesta": "GLORIA", "banco": ["GLORIA", "TRISTEZA", "SOLEDAD"]},
        {"texto": "Lugar donde ya viven los santos.", "respuesta": "CIELO", "banco": ["CIELO", "DESIERTO", "CAMINO"]},
        {"texto": "Lo que los santos nos dejan con su vida.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSA", "QUEJA"]},
    ],
    "incluir": ["SANTOS", "GLORIA"], "requisito": 4,
    "pistas": ["Piensa en quiénes ya viven felices junto a Dios.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: los santos ya viven con Dios",
    "palabras": ["SANTOS", "MULTITUD", "ALABANZA", "GLORIA", "CIELO", "EJEMPLO"],
    "incluir": ["SANTOS", "MULTITUD"], "requisito": 5,
    "pistas": ["SANTOS y CIELO son de las palabras más cortas: búscalas primero.",
               "MULTITUD y ALABANZA son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Apocalipsis 7,9-10",
    "items": [
        {"texto": "Busca en tu Biblia Católica Apocalipsis 7,9-10 y completa: «Vi una gran ______ que nadie "
                  "podía contar, de pie delante del trono.»", "respuesta": "MULTITUD",
         "banco": ["MULTITUD", "SOLDADO", "PERSONA"]},
        {"texto": "¿Qué hacen los santos delante de Dios, según el libro del Apocalipsis?", "abierta": True,
         "palabras_esperadas": ["ALABAR", "GLORIA", "ADORAR", "DIOS"],
         "respuestas_referencia": ["Alaban a Dios y le dan gloria por siempre.",
                                    "Adoran a Dios delante de su trono, llenos de alegría.",
                                    "Cantan alabanzas a Dios porque ya viven felices con él."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro del Apocalipsis en el índice de tu Biblia; el capítulo es el 7.",
               "El texto describe una gran cantidad de gente delante del trono de Dios."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Juan vio una gran ______ delante del trono de Dios.", "respuesta": "MULTITUD", "banco": ["MULTITUD", "SOLDADO", "EJERCITO"]},
        {"texto": "Los santos dan ______ a Dios por siempre.", "respuesta": "ALABANZA", "banco": ["ALABANZA", "QUEJA", "SILENCIO"]},
        {"texto": "Los santos ya viven en la ______ de Dios.", "respuesta": "GLORIA", "banco": ["GLORIA", "TRISTEZA", "SOLEDAD"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que vio San Juan delante del trono de Dios.",
               "La tercera respuesta describe la felicidad plena de los santos."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los santos ya viven felices junto a Dios.", "respuesta": True},
        {"texto": "San Juan vio una multitud alabando a Dios.", "respuesta": True},
        {"texto": "Los santos ya no tienen relación con nosotros.", "respuesta": False},
        {"texto": "Los santos no son ejemplo para nuestra vida.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda dónde y cómo viven los santos.",
               "Si una frase dice que los santos no son ejemplo para nosotros, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué vio San Juan delante del trono de Dios?",
         "opciones": ["Una gran multitud alabando a Dios", "Un lugar vacío", "Nada", "Tristeza"], "correcta": 0},
        {"texto": "¿Qué nos dejan los santos con su vida?",
         "opciones": ["Un ejemplo a seguir", "Nada importante", "Confusión", "Miedo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que vio San Juan delante del trono de Dios.",
               "Recuerda lo que los santos nos dejan con su vida."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SANTOS", "definicion": "Quienes ya viven felices con Dios"},
        {"termino": "MULTITUD", "definicion": "Gran cantidad de gente ante el trono"},
        {"termino": "ALABANZA", "definicion": "Lo que los santos dan a Dios"},
        {"termino": "GLORIA", "definicion": "Felicidad plena junto a Dios"},
        {"termino": "EJEMPLO", "definicion": "Lo que los santos nos dejan"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en quiénes son los santos y qué hacen en el cielo.",
               "EJEMPLO es lo que los santos nos dejan con su vida, no lo que hacen en el cielo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: los santos en el cielo",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "San Juan vio una gran ______ delante del trono de Dios.",
         "opciones": ["multitud", "tristeza", "soledad"], "correcta": 0},
        {"texto": "Los santos ya viven en la ______ de Dios.",
         "opciones": ["gloria", "tristeza", "duda"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que vio San Juan.",
               "Recuerda cómo viven los santos junto a Dios."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los santos ya viven en la ______ de Dios.",
         "respuesta": "GLORIA", "banco": ["GLORIA", "TRISTEZA", "SOLEDAD"]},
    ],
    "reflexion": "¿Qué santo o persona que ya murió es un ejemplo de fe para ti?",
    "requisito": 1,
    "pistas": ["Piensa en cómo viven los santos junto a Dios.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: sigo el ejemplo de los santos",
    "situacion": "Ya sabes que los santos ya viven felices junto a Dios y nos dejan su ejemplo.",
    "items": [
        {"texto": "¿Cómo puedes seguir el ejemplo de los santos en tu vida diaria?",
         "opciones": ["Tratando de vivir con amor como ellos",
                      "Rezando y confiando en Dios",
                      "Aprendiendo sobre la vida de algún santo",
                      "Pensando que eso no tiene que ver conmigo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de fe, no de indiferencia.",
               "Descarta la única opción que dice que eso no tiene que ver contigo."],
    "feedback_ok": "¡Muy bien! Así seguimos el camino de fe de los santos.",
})

# ==========================================================================
# PC12-C06 — Caminar hacia la vida eterna
# ==========================================================================
C = "PC12-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: caminar hacia la vida eterna",
    "items": [
        {"texto": "Lo que recorremos en la vida hacia Dios.", "respuesta": "CAMINO", "banco": ["CAMINO", "MURO", "POZO"]},
        {"texto": "Lo que buscamos alcanzar al final del camino de la fe.", "respuesta": "META", "banco": ["META", "SOMBRA", "DUDA"]},
        {"texto": "Hacia dónde nos anima San Pablo a mirar, dejando atrás el pasado.", "respuesta": "ADELANTE", "banco": ["ADELANTE", "ATRAS", "LEJOS"]},
        {"texto": "Lo que Dios nos ofrece al final del camino.", "respuesta": "PREMIO", "banco": ["PREMIO", "CASTIGO", "OLVIDO"]},
        {"texto": "Seguir esforzándonos sin rendirnos.", "respuesta": "CONSTANCIA", "banco": ["CONSTANCIA", "PEREZA", "DUDA"]},
        {"texto": "Vida sin fin junto a Dios.", "respuesta": "ETERNIDAD", "banco": ["ETERNIDAD", "TRISTEZA", "SOLEDAD"]},
    ],
    "incluir": ["CAMINO", "META"], "requisito": 4,
    "pistas": ["Piensa en lo que recorremos en la vida hacia Dios.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: caminar hacia la vida eterna",
    "palabras": ["CAMINO", "META", "ADELANTE", "PREMIO", "CONSTANCIA", "ETERNIDAD"],
    "incluir": ["CAMINO", "ETERNIDAD"], "requisito": 5,
    "pistas": ["META es de las palabras más cortas: búscala primero.",
               "CONSTANCIA y ETERNIDAD son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Filipenses 3,13-14",
    "items": [
        {"texto": "Busca en tu Biblia Católica Filipenses 3,13-14 y completa: «Olvidando lo que queda atrás "
                  "y avanzando hacia lo que está ______.»", "respuesta": "ADELANTE",
         "banco": ["ADELANTE", "ATRAS", "LEJOS"]},
        {"texto": "¿Cómo nos anima San Pablo a caminar hacia la vida eterna?", "abierta": True,
         "palabras_esperadas": ["ADELANTE", "META", "CONSTANCIA", "ESFUERZO"],
         "respuestas_referencia": ["Nos anima a mirar siempre hacia adelante, sin quedarnos en el pasado.",
                                    "Nos anima a caminar con constancia hacia la meta de la vida eterna.",
                                    "Nos anima a esforzarnos cada día para alcanzar el premio de Dios."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Filipenses en el índice de tu Biblia; el capítulo es el 3.",
               "El texto habla de olvidar el pasado y avanzar hacia lo que está adelante."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo nos anima a mirar hacia ______, no hacia atrás.", "respuesta": "ADELANTE", "banco": ["ADELANTE", "ATRAS", "ABAJO"]},
        {"texto": "El premio que Dios nos ofrece es la vida ______.", "respuesta": "ETERNA", "banco": ["ETERNA", "CORTA", "VACIA"]},
        {"texto": "Para llegar a la meta se necesita ______.", "respuesta": "CONSTANCIA", "banco": ["CONSTANCIA", "PEREZA", "DUDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa hacia dónde nos anima a mirar San Pablo.",
               "La tercera respuesta es lo que se necesita para llegar a la meta."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo nos anima a mirar siempre hacia adelante.", "respuesta": True},
        {"texto": "La vida eterna no requiere ningún esfuerzo de nuestra parte.", "respuesta": False},
        {"texto": "Caminar hacia Dios es una tarea de toda la vida.", "respuesta": True},
        {"texto": "A Dios no le interesa que sigamos avanzando en la fe.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda hacia dónde nos anima a mirar San Pablo.",
               "Si una frase dice que la vida eterna no requiere esfuerzo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Hacia dónde nos anima San Pablo a mirar?",
         "opciones": ["Hacia adelante", "Hacia atrás", "A ningún lado", "Solo al pasado"], "correcta": 0},
        {"texto": "¿Qué se necesita para llegar a la meta de la vida eterna?",
         "opciones": ["Constancia y esfuerzo", "Nada", "Solo suerte", "Miedo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa hacia dónde nos anima a mirar San Pablo.",
               "Recuerda qué se necesita para llegar a la meta."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CAMINO", "definicion": "Lo que recorremos hacia Dios"},
        {"termino": "META", "definicion": "Lo que buscamos al final del camino de fe"},
        {"termino": "ADELANTE", "definicion": "Hacia dónde nos anima a mirar San Pablo"},
        {"termino": "PREMIO", "definicion": "Lo que Dios ofrece al final del camino"},
        {"termino": "CONSTANCIA", "definicion": "Seguir esforzándonos sin rendirnos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el camino de la fe y hacia dónde nos lleva.",
               "CONSTANCIA es una actitud, no un lugar ni una promesa."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: el camino hacia la vida eterna",
    "instruccion": "En 45 segundos, marca las palabras que describen el camino hacia la vida eterna.",
    "tiempo_segundos": 45,
    "banco": ["CAMINO", "META", "CONSTANCIA", "PEREZA", "DUDA", "ADELANTE"],
    "correctas": ["CAMINO", "META", "CONSTANCIA", "ADELANTE"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Camino - Meta - Constancia - Adelante.",
               "Descarta las palabras que describen actitudes contrarias a seguir avanzando."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo nos anima a mirar hacia ______, no hacia atrás.",
         "respuesta": "ADELANTE", "banco": ["ADELANTE", "ATRAS", "ABAJO"]},
    ],
    "reflexion": "¿Qué puedes hacer para seguir caminando en tu fe, paso a paso?",
    "requisito": 1,
    "pistas": ["Piensa hacia dónde nos anima a mirar San Pablo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: camino hacia Dios",
    "situacion": "Ya sabes que la vida de fe es un camino que se recorre con constancia, mirando siempre hacia adelante.",
    "items": [
        {"texto": "¿Cómo puedes seguir caminando hacia Dios cada día?",
         "opciones": ["Orando y participando en la Eucaristía",
                      "Aprendiendo más sobre mi fe",
                      "Tratando de vivir el amor de Jesús cada día",
                      "Pensando que ya llegué y no necesito seguir"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de constancia, no de conformismo.",
               "Descarta la única opción que dice que ya no hace falta seguir."],
    "feedback_ok": "¡Muy bien! Así se camina, paso a paso, hacia la vida eterna.",
})

# ==========================================================================
# ==========================================================================
# PC13 — El Espíritu Santo nos envía   (Encuentro 13, Hechos 1,8 / Juan 20,21-22)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC13-C01 — El Espíritu Santo, don de Jesús resucitado
# ==========================================================================
C = "PC13-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: don de Jesús resucitado",
    "items": [
        {"texto": "Lo primero que dijo Jesús resucitado a sus discípulos.", "respuesta": "PAZ", "banco": ["PAZ", "MIEDO", "SILENCIO"]},
        {"texto": "Gesto que hizo Jesús al dar el Espíritu Santo a sus discípulos.", "respuesta": "SOPLO", "banco": ["SOPLO", "GRITO", "LLANTO"]},
        {"texto": "Don que Jesús entregó a sus discípulos después de resucitar.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "DUDA"]},
        {"texto": "Quienes recibieron al Espíritu Santo de manos de Jesús.", "respuesta": "DISCIPULOS", "banco": ["DISCIPULOS", "EXTRAÑOS", "SOLDADOS"]},
        {"texto": "Estaban cerradas cuando Jesús se apareció a sus discípulos.", "respuesta": "PUERTAS", "banco": ["PUERTAS", "VENTANAS", "TUMBAS"]},
        {"texto": "Lo que Jesús hizo con sus discípulos, como el Padre lo había enviado a él.", "respuesta": "ENVIAR", "banco": ["ENVIAR", "ABANDONAR", "OLVIDAR"]},
    ],
    "incluir": ["PAZ", "ESPIRITU"], "requisito": 4,
    "pistas": ["Piensa en lo primero que dijo Jesús resucitado a sus discípulos.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: don de Jesús resucitado",
    "palabras": ["PAZ", "SOPLO", "ESPIRITU", "DISCIPULOS", "PUERTAS", "ENVIAR"],
    "incluir": ["PAZ", "SOPLO"], "requisito": 5,
    "pistas": ["PAZ es la palabra más corta: búscala primero.",
               "DISCIPULOS es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 20,21-22",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 20,21-22 y completa: «Sopló sobre ellos y les dijo: "
                  "Reciban el Espíritu ______.»", "respuesta": "SANTO",
         "banco": ["SANTO", "PURO", "ETERNO"]},
        {"texto": "¿Qué hizo Jesús para dar el Espíritu Santo a sus discípulos?", "abierta": True,
         "palabras_esperadas": ["SOPLO", "PAZ", "ESPIRITU", "ENVIO"],
         "respuestas_referencia": ["Sopló sobre ellos y les dijo que recibieran el Espíritu Santo.",
                                    "Les dio su paz y luego los envió con el don del Espíritu Santo.",
                                    "Se apareció a sus discípulos, les dio la paz y sopló sobre ellos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 20.",
               "El texto cuenta lo que Jesús hizo al aparecerse a sus discípulos con las puertas cerradas."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús resucitado dijo a sus discípulos: «______ a ustedes.»", "respuesta": "PAZ", "banco": ["PAZ", "MIEDO", "SILENCIO"]},
        {"texto": "Jesús sopló sobre sus discípulos y les dio el ______ Santo.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "PAN", "AGUA"]},
        {"texto": "Las ______ estaban cerradas cuando Jesús se apareció.", "respuesta": "PUERTAS", "banco": ["PUERTAS", "VENTANAS", "TUMBAS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo primero que dijo Jesús a sus discípulos.",
               "La segunda respuesta es el don que Jesús entregó."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús resucitado se apareció a sus discípulos y les dio la paz.", "respuesta": True},
        {"texto": "Jesús sopló sobre sus discípulos para darles el Espíritu Santo.", "respuesta": True},
        {"texto": "Las puertas estaban abiertas de par en par cuando Jesús llegó.", "respuesta": False},
        {"texto": "Jesús no envió a sus discípulos a ninguna misión.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo estaban las puertas cuando llegó Jesús.",
               "Si una frase dice que Jesús no envió a nadie, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué dijo Jesús primero a sus discípulos al aparecerse resucitado?",
         "opciones": ["Paz a ustedes", "Tengan miedo", "Váyanse lejos", "No digan nada"], "correcta": 0},
        {"texto": "¿Qué hizo Jesús para dar el Espíritu Santo a sus discípulos?",
         "opciones": ["Sopló sobre ellos", "Los ignoró", "Se enojó con ellos", "Los dejó solos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo primero que dijo Jesús resucitado.",
               "Recuerda el gesto que hizo Jesús para dar el Espíritu Santo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "PAZ", "definicion": "Lo primero que dijo Jesús resucitado"},
        {"termino": "SOPLO", "definicion": "Gesto de Jesús al dar el Espíritu Santo"},
        {"termino": "DISCIPULOS", "definicion": "Quienes recibieron el Espíritu Santo"},
        {"termino": "PUERTAS", "definicion": "Estaban cerradas cuando llegó Jesús"},
        {"termino": "ENVIAR", "definicion": "Lo que Jesús hizo con sus discípulos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la escena de Jesús resucitado con sus discípulos.",
               "ENVIAR es una acción de Jesús, no un objeto ni un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: Jesús da el Espíritu Santo",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús resucitado dijo a sus discípulos: «______ a ustedes.»",
         "opciones": ["paz", "miedo", "silencio"], "correcta": 0},
        {"texto": "Jesús ______ sobre sus discípulos para darles el Espíritu Santo.",
         "opciones": ["sopló", "gritó", "lloró"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo primero que dijo Jesús a sus discípulos.",
               "Recuerda el gesto que hizo Jesús para dar el Espíritu Santo."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús ______ sobre sus discípulos para darles el Espíritu Santo.",
         "respuesta": "SOPLO", "banco": ["SOPLO", "GRITO", "LLANTO"]},
    ],
    "reflexion": "¿Qué sientes al saber que Jesús te regala su propio Espíritu?",
    "requisito": 1,
    "pistas": ["Piensa en el gesto que hizo Jesús para dar el Espíritu Santo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: recibo el don del Espíritu Santo",
    "situacion": "Ya sabes que Jesús resucitado entregó a sus discípulos el don del Espíritu Santo.",
    "items": [
        {"texto": "¿Cómo puedes recibir y cuidar este don en tu vida?",
         "opciones": ["Rezando al Espíritu Santo cada día",
                      "Pidiéndole su paz cuando tengo miedo",
                      "Escuchando su voz en el silencio",
                      "Pensando que ese don no es para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de apertura al Espíritu Santo.",
               "Descarta la única opción que dice que el don no es para ti."],
    "feedback_ok": "¡Muy bien! El Espíritu Santo es un don para cada uno de nosotros.",
})

# ==========================================================================
# PC13-C02 — Recibimos fuerza para ser testigos
# ==========================================================================
C = "PC13-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: fuerza para ser testigos",
    "items": [
        {"texto": "Lo que recibimos al venir sobre nosotros el Espíritu Santo.", "respuesta": "FUERZA", "banco": ["FUERZA", "MIEDO", "DUDA"]},
        {"texto": "Lo que seremos de Jesús, según la promesa de Hechos 1,8.", "respuesta": "TESTIGOS", "banco": ["TESTIGOS", "EXTRAÑOS", "ENEMIGOS"]},
        {"texto": "Ciudad donde comenzó el testimonio de los discípulos.", "respuesta": "JERUSALEN", "banco": ["JERUSALEN", "BELEN", "NAZARET"]},
        {"texto": "Región mencionada junto a Judea en la promesa de Jesús.", "respuesta": "SAMARIA", "banco": ["SAMARIA", "GALILEA", "EGIPTO"]},
        {"texto": "Hasta dónde debía llegar el testimonio de los discípulos.", "respuesta": "CONFINES", "banco": ["CONFINES", "CENTROS", "MERCADOS"]},
        {"texto": "Quien nos da fuerza para ser testigos de Jesús.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "PEREZA"]},
    ],
    "incluir": ["FUERZA", "TESTIGOS"], "requisito": 4,
    "pistas": ["Piensa en lo que recibimos cuando viene el Espíritu Santo sobre nosotros.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: fuerza para ser testigos",
    "palabras": ["FUERZA", "TESTIGOS", "JERUSALEN", "SAMARIA", "CONFINES", "ESPIRITU"],
    "incluir": ["FUERZA", "ESPIRITU"], "requisito": 5,
    "pistas": ["FUERZA es una de las palabras más cortas: búscala primero.",
               "JERUSALEN es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 1,8",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 1,8 y completa: «...recibirán ______, porque el "
                  "Espíritu Santo vendrá sobre ustedes.»", "respuesta": "FUERZA",
         "banco": ["FUERZA", "RIQUEZA", "FAMA"]},
        {"texto": "¿Para qué nos da fuerza el Espíritu Santo, según Hechos 1,8?", "abierta": True,
         "palabras_esperadas": ["TESTIGOS", "ANUNCIAR", "MUNDO", "FUERZA"],
         "respuestas_referencia": ["Para que seamos testigos de Jesús en todas partes.",
                                    "Para anunciar a Jesús hasta los confines de la tierra.",
                                    "Para dar testimonio de Jesús con valentía en todo lugar."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 1.",
               "El texto habla de lo que recibiremos cuando venga el Espíritu Santo sobre nosotros."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo nos da ______ para ser testigos de Jesús.", "respuesta": "FUERZA", "banco": ["FUERZA", "MIEDO", "DUDA"]},
        {"texto": "Seremos testigos en Jerusalén, Judea, ______ y hasta los confines de la tierra.", "respuesta": "SAMARIA", "banco": ["SAMARIA", "GALILEA", "EGIPTO"]},
        {"texto": "El testimonio de los discípulos debía llegar hasta los ______ de la tierra.", "respuesta": "CONFINES", "banco": ["CONFINES", "CENTROS", "MERCADOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que da el Espíritu Santo a los discípulos.",
               "La tercera respuesta describe hasta dónde debía llegar el testimonio."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo nos da fuerza para ser testigos.", "respuesta": True},
        {"texto": "El testimonio de Jesús debía quedarse solo en Jerusalén.", "respuesta": False},
        {"texto": "Los discípulos recibieron la promesa de ser testigos hasta los confines de la tierra.", "respuesta": True},
        {"texto": "El Espíritu Santo no tiene relación con nuestra misión.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda para qué nos da fuerza el Espíritu Santo.",
               "Si una frase dice que el testimonio debía quedarse solo en Jerusalén, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué recibimos cuando viene el Espíritu Santo sobre nosotros?",
         "opciones": ["Fuerza para ser testigos", "Nada", "Miedo", "Confusión"], "correcta": 0},
        {"texto": "¿Hasta dónde debía llegar el testimonio de los discípulos?",
         "opciones": ["Hasta los confines de la tierra", "Solo hasta Jerusalén", "A ningún lugar", "Solo a su familia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que recibimos del Espíritu Santo.",
               "Recuerda hasta dónde debía llegar el testimonio de los discípulos."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "FUERZA", "definicion": "Lo que da el Espíritu Santo"},
        {"termino": "TESTIGOS", "definicion": "Lo que seremos de Jesús"},
        {"termino": "JERUSALEN", "definicion": "Donde comenzó el testimonio"},
        {"termino": "SAMARIA", "definicion": "Región mencionada en la promesa"},
        {"termino": "CONFINES", "definicion": "Hasta dónde debía llegar el testimonio"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la promesa de Jesús en Hechos 1,8.",
               "CONFINES describe un límite geográfico muy lejano."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la promesa de Hechos 1,8",
    "instruccion": "En 45 segundos, marca las palabras que describen la promesa de Hechos 1,8.",
    "tiempo_segundos": 45,
    "banco": ["FUERZA", "TESTIGOS", "ESPIRITU", "CONFINES", "MIEDO", "SILENCIO"],
    "correctas": ["FUERZA", "TESTIGOS", "ESPIRITU", "CONFINES"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Fuerza - Testigos - Espíritu - Confines.",
               "Descarta las palabras que describen lo contrario del testimonio valiente."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu Santo nos da ______ para ser testigos de Jesús.",
         "respuesta": "FUERZA", "banco": ["FUERZA", "RIQUEZA", "FAMA"]},
    ],
    "reflexion": "¿En qué lugares cercanos a ti puedes ser testigo de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en lo que da el Espíritu Santo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: testigo con la fuerza del Espíritu",
    "situacion": "Ya sabes que el Espíritu Santo nos da fuerza para ser testigos de Jesús en todas partes.",
    "items": [
        {"texto": "¿Cómo puedes ser testigo de Jesús esta semana?",
         "opciones": ["Hablando de Jesús con respeto cuando surja el tema",
                      "Pidiendo al Espíritu Santo que me dé valentía",
                      "Viviendo lo que aprendo en la catequesis",
                      "Esperando a ser grande para hacerlo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción posible hoy, no en el futuro.",
               "Descarta la única opción que pospone el testimonio para más adelante."],
    "feedback_ok": "¡Muy bien! El Espíritu Santo nos acompaña para ser testigos, aquí y ahora.",
})

# ==========================================================================
# PC13-C03 — Los dones del Espíritu Santo
# ==========================================================================
C = "PC13-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: los dones del Espíritu Santo",
    "items": [
        {"texto": "Don que nos ayuda a conocer y amar a Dios por encima de todo.", "respuesta": "SABIDURIA", "banco": ["SABIDURIA", "RIQUEZA", "FAMA"]},
        {"texto": "Don que nos ayuda a comprender mejor la fe.", "respuesta": "ENTENDIMIENTO", "banco": ["ENTENDIMIENTO", "OLVIDO", "CONFUSION"]},
        {"texto": "Don que nos ayuda a tomar buenas decisiones.", "respuesta": "CONSEJO", "banco": ["CONSEJO", "MIEDO", "DUDA"]},
        {"texto": "Don que nos da valentía para vivir como cristianos.", "respuesta": "FORTALEZA", "banco": ["FORTALEZA", "DEBILIDAD", "PEREZA"]},
        {"texto": "Regalos especiales que el Espíritu Santo nos da.", "respuesta": "DONES", "banco": ["DONES", "CASTIGOS", "DEBERES"]},
        {"texto": "Quien nos entrega los dones para vivir como hijos de Dios.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "DUDA"]},
    ],
    "incluir": ["DONES", "ESPIRITU"], "requisito": 4,
    "pistas": ["Piensa en los regalos especiales que el Espíritu Santo nos da.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: los dones del Espíritu Santo",
    "palabras": ["SABIDURIA", "ENTENDIMIENTO", "CONSEJO", "FORTALEZA", "DONES", "ESPIRITU"],
    "incluir": ["SABIDURIA", "FORTALEZA"], "requisito": 5,
    "pistas": ["DONES es la palabra más corta: búscala primero.",
               "ENTENDIMIENTO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Isaías 11,2-3",
    "items": [
        {"texto": "Busca en tu Biblia Católica Isaías 11,2-3 y completa: «Reposará sobre él el espíritu "
                  "del Señor: espíritu de ______ y de inteligencia.»", "respuesta": "SABIDURIA",
         "banco": ["SABIDURIA", "RIQUEZA", "PODER"]},
        {"texto": "¿Para qué nos sirven los dones del Espíritu Santo?", "abierta": True,
         "palabras_esperadas": ["VIVIR", "FE", "DECISIONES", "AMAR"],
         "respuestas_referencia": ["Para vivir mejor nuestra fe y amar más a Dios.",
                                    "Para tomar buenas decisiones y comprender lo que Dios nos pide.",
                                    "Para crecer como hijos de Dios en nuestra vida diaria."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de Isaías en el índice de tu Biblia; el capítulo es el 11.",
               "El texto describe los dones que reposan sobre quien tiene el espíritu del Señor."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los dones del Espíritu Santo nos ayudan a vivir como ______ de Dios.", "respuesta": "HIJOS", "banco": ["HIJOS", "EXTRAÑOS", "ENEMIGOS"]},
        {"texto": "El don de ______ nos ayuda a tomar buenas decisiones.", "respuesta": "CONSEJO", "banco": ["CONSEJO", "MIEDO", "DUDA"]},
        {"texto": "El don de ______ nos da valentía para vivir como cristianos.", "respuesta": "FORTALEZA", "banco": ["FORTALEZA", "DEBILIDAD", "PEREZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en para qué sirven los dones del Espíritu Santo.",
               "La tercera respuesta nos da valentía."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los dones del Espíritu Santo son regalos para vivir mejor nuestra fe.", "respuesta": True},
        {"texto": "La sabiduría nos ayuda a conocer y amar más a Dios.", "respuesta": True},
        {"texto": "El don de fortaleza nos hace débiles ante las dificultades.", "respuesta": False},
        {"texto": "Los dones del Espíritu Santo no sirven para nada en nuestra vida diaria.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda para qué sirven los dones del Espíritu Santo.",
               "Si una frase dice que esos dones no sirven de nada, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué son los dones del Espíritu Santo?",
         "opciones": ["Regalos para vivir mejor nuestra fe", "Castigos de Dios", "Cosas que no existen", "Solo para los sacerdotes"], "correcta": 0},
        {"texto": "¿Qué don nos ayuda a tomar buenas decisiones?",
         "opciones": ["Consejo", "Miedo", "Duda", "Pereza"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en qué son los dones del Espíritu Santo.",
               "Recuerda cuál de los dones ayuda a decidir bien."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SABIDURIA", "definicion": "Conocer y amar a Dios por encima de todo"},
        {"termino": "ENTENDIMIENTO", "definicion": "Comprender mejor la fe"},
        {"termino": "CONSEJO", "definicion": "Tomar buenas decisiones"},
        {"termino": "FORTALEZA", "definicion": "Valentía para vivir como cristianos"},
        {"termino": "DONES", "definicion": "Regalos que el Espíritu Santo nos da"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cada don y para qué sirve.",
               "DONES es la palabra que agrupa a todos los demás."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: los dones del Espíritu Santo",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El Espíritu Santo nos da ______ para vivir nuestra fe.",
         "opciones": ["dones", "castigos", "miedos"], "correcta": 0},
        {"texto": "El don de ______ nos ayuda a tomar buenas decisiones.",
         "opciones": ["consejo", "duda", "pereza"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que el Espíritu Santo nos regala.",
               "Recuerda cuál de los dones ayuda a decidir bien."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los dones del Espíritu Santo nos ayudan a vivir como ______ de Dios.",
         "respuesta": "HIJOS", "banco": ["HIJOS", "EXTRAÑOS", "ENEMIGOS"]},
    ],
    "reflexion": "¿Qué don del Espíritu Santo sientes que más necesitas hoy?",
    "requisito": 1,
    "pistas": ["Piensa en para qué sirven los dones del Espíritu Santo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: uso los dones del Espíritu Santo",
    "situacion": "Ya sabes que el Espíritu Santo nos da dones para vivir mejor nuestra fe.",
    "items": [
        {"texto": "¿Cómo puedes pedir y usar los dones del Espíritu Santo?",
         "opciones": ["Rezando al Espíritu Santo antes de decidir algo importante",
                      "Pidiendo su ayuda cuando tengo miedo",
                      "Escuchando su voz en la oración",
                      "Pensando que esos dones no son para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una actitud de apertura a los dones.",
               "Descarta la única opción que dice que esos dones no son para ti."],
    "feedback_ok": "¡Muy bien! Los dones del Espíritu Santo son para cada uno de nosotros.",
})

# ==========================================================================
# PC13-C04 — Los frutos del Espíritu Santo
# ==========================================================================
C = "PC13-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: los frutos del Espíritu Santo",
    "items": [
        {"texto": "El primer fruto del Espíritu Santo que menciona San Pablo.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "ENOJO"]},
        {"texto": "Fruto del Espíritu Santo que sentimos al vivir cerca de Dios.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "ENOJO"]},
        {"texto": "Fruto del Espíritu Santo que calma nuestro corazón.", "respuesta": "PAZ", "banco": ["PAZ", "MIEDO", "PRISA"]},
        {"texto": "Fruto del Espíritu Santo que nos ayuda a esperar con calma.", "respuesta": "PACIENCIA", "banco": ["PACIENCIA", "PRISA", "ENOJO"]},
        {"texto": "Fruto del Espíritu Santo que nos lleva a hacer el bien.", "respuesta": "BONDAD", "banco": ["BONDAD", "EGOISMO", "ENVIDIA"]},
        {"texto": "Señales visibles de que el Espíritu Santo vive en nosotros.", "respuesta": "FRUTOS", "banco": ["FRUTOS", "CASTIGOS", "DEBERES"]},
    ],
    "incluir": ["AMOR", "FRUTOS"], "requisito": 4,
    "pistas": ["Piensa en el primer fruto del Espíritu Santo que menciona San Pablo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: los frutos del Espíritu Santo",
    "palabras": ["AMOR", "ALEGRIA", "PAZ", "PACIENCIA", "BONDAD", "FRUTOS"],
    "incluir": ["PAZ", "BONDAD"], "requisito": 5,
    "pistas": ["AMOR y PAZ son de las palabras más cortas: búscalas primero.",
               "PACIENCIA es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Gálatas 5,22-23",
    "items": [
        {"texto": "Busca en tu Biblia Católica Gálatas 5,22-23 y completa: «El fruto del Espíritu es amor, "
                  "alegría, ______...»", "respuesta": "PAZ",
         "banco": ["PAZ", "MIEDO", "TRISTEZA"]},
        {"texto": "¿Cómo sabemos que el Espíritu Santo vive en una persona?", "abierta": True,
         "palabras_esperadas": ["FRUTOS", "AMOR", "BONDAD", "PACIENCIA"],
         "respuestas_referencia": ["Porque se ven en ella frutos como el amor, la paz y la bondad.",
                                    "Porque trata a los demás con paciencia, bondad y alegría.",
                                    "Porque su forma de vivir muestra los frutos del Espíritu Santo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Gálatas en el índice de tu Biblia; el capítulo es el 5.",
               "El texto enumera varios frutos, empezando por el amor."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El primer fruto del Espíritu Santo es el ______.", "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "ENOJO"]},
        {"texto": "La ______ nos ayuda a esperar con calma.", "respuesta": "PACIENCIA", "banco": ["PACIENCIA", "PRISA", "ENOJO"]},
        {"texto": "Los frutos del Espíritu Santo se ven en nuestra ______ diaria.", "respuesta": "VIDA", "banco": ["VIDA", "TAREA", "ESCUELA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el primer fruto que menciona San Pablo.",
               "La segunda respuesta ayuda a esperar sin desesperarse."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El amor es uno de los frutos del Espíritu Santo.", "respuesta": True},
        {"texto": "Los frutos del Espíritu Santo no se notan en nuestra vida.", "respuesta": False},
        {"texto": "La paciencia nos ayuda a esperar con calma.", "respuesta": True},
        {"texto": "La bondad no tiene relación con el Espíritu Santo.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda los frutos del Espíritu Santo mencionados por San Pablo.",
               "Si una frase dice que esos frutos no se notan, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cuál es el primer fruto del Espíritu Santo que menciona San Pablo?",
         "opciones": ["Amor", "Miedo", "Tristeza", "Enojo"], "correcta": 0},
        {"texto": "¿Dónde se ven los frutos del Espíritu Santo?",
         "opciones": ["En nuestra forma de vivir y tratar a los demás", "En ningún lugar", "Solo en la iglesia", "Solo en los adultos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el primer fruto que menciona San Pablo.",
               "Recuerda dónde se ven los frutos del Espíritu Santo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "AMOR", "definicion": "Primer fruto del Espíritu Santo"},
        {"termino": "ALEGRIA", "definicion": "Fruto que sentimos al vivir cerca de Dios"},
        {"termino": "PAZ", "definicion": "Fruto que calma nuestro corazón"},
        {"termino": "PACIENCIA", "definicion": "Fruto que nos ayuda a esperar con calma"},
        {"termino": "BONDAD", "definicion": "Fruto que nos lleva a hacer el bien"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cada fruto del Espíritu Santo y su significado.",
               "PACIENCIA es el fruto relacionado con saber esperar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: los frutos del Espíritu Santo",
    "instruccion": "En 45 segundos, marca las palabras que son frutos del Espíritu Santo.",
    "tiempo_segundos": 45,
    "banco": ["AMOR", "PAZ", "BONDAD", "PACIENCIA", "ENOJO", "EGOISMO"],
    "correctas": ["AMOR", "PAZ", "BONDAD", "PACIENCIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Amor - Paz - Bondad - Paciencia.",
               "Descarta las palabras que describen actitudes contrarias a estos frutos."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El primer fruto del Espíritu Santo es el ______.",
         "respuesta": "AMOR", "banco": ["AMOR", "MIEDO", "ENOJO"]},
    ],
    "reflexion": "¿Qué fruto del Espíritu Santo te gustaría vivir más esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en el primer fruto que menciona San Pablo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: muestro los frutos del Espíritu",
    "situacion": "Ya sabes que los frutos del Espíritu Santo se ven en cómo vivimos y tratamos a los demás.",
    "items": [
        {"texto": "¿Cómo puedes mostrar los frutos del Espíritu Santo esta semana?",
         "opciones": ["Siendo paciente con mi familia",
                      "Tratando con bondad a mis compañeros",
                      "Compartiendo la alegría de mi fe",
                      "Guardando mal humor todo el día"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes concretas, no en el mal humor.",
               "Descarta la única opción que muestra lo contrario de un fruto del Espíritu."],
    "feedback_ok": "¡Muy bien! Así se muestran los frutos del Espíritu Santo en la vida diaria.",
})

# ==========================================================================
# PC13-C05 — El Espíritu Santo guía a la Iglesia
# ==========================================================================
C = "PC13-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: el Espíritu Santo guía a la Iglesia",
    "items": [
        {"texto": "Lo que hace el Espíritu Santo con la Iglesia.", "respuesta": "GUIA", "banco": ["GUIA", "ABANDONA", "OLVIDA"]},
        {"texto": "Lo que el Espíritu Santo nos ayuda a conocer plenamente.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
        {"texto": "Comunidad de los que creen en Jesús, guiada por el Espíritu Santo.", "respuesta": "IGLESIA", "banco": ["IGLESIA", "MULTITUD", "PUEBLO"]},
        {"texto": "Lo que recorre la Iglesia guiada por el Espíritu Santo.", "respuesta": "CAMINO", "banco": ["CAMINO", "MURO", "POZO"]},
        {"texto": "Quien guía a la Iglesia hacia la verdad completa.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "DUDA"]},
        {"texto": "Lo que el Espíritu Santo da a la Iglesia para no perderse.", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "OSCURIDAD"]},
    ],
    "incluir": ["GUIA", "IGLESIA"], "requisito": 4,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con la Iglesia.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: el Espíritu Santo guía a la Iglesia",
    "palabras": ["GUIA", "VERDAD", "IGLESIA", "CAMINO", "ESPIRITU", "LUZ"],
    "incluir": ["VERDAD", "ESPIRITU"], "requisito": 5,
    "pistas": ["GUIA y LUZ son de las palabras más cortas: búscalas primero.",
               "ESPIRITU es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 16,13",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 16,13 y completa: «Cuando venga el Espíritu de la "
                  "verdad, él los guiará hasta la ______ completa.»", "respuesta": "VERDAD",
         "banco": ["VERDAD", "RIQUEZA", "FAMA"]},
        {"texto": "¿Qué hace el Espíritu Santo con la Iglesia?", "abierta": True,
         "palabras_esperadas": ["GUIA", "VERDAD", "CAMINO", "LUZ"],
         "respuestas_referencia": ["La guía hacia la verdad completa en su camino de fe.",
                                    "Le da luz para no perderse y seguir a Jesús.",
                                    "Acompaña a la Iglesia y la ayuda a conocer la verdad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 16.",
               "El texto habla de lo que hará el Espíritu de la verdad cuando venga."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "El Espíritu Santo ______ a la Iglesia en su camino.", "respuesta": "GUIA", "banco": ["GUIA", "ABANDONA", "OLVIDA"]},
        {"texto": "El Espíritu Santo nos ayuda a conocer la ______ completa.", "respuesta": "VERDAD", "banco": ["VERDAD", "MENTIRA", "DUDA"]},
        {"texto": "La Iglesia es la comunidad de quienes creen en ______.", "respuesta": "JESUS", "banco": ["JESUS", "NADIE", "OTROS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con la Iglesia.",
               "La tercera respuesta es en quien cree la Iglesia."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "El Espíritu Santo guía a la Iglesia hacia la verdad.", "respuesta": True},
        {"texto": "El Espíritu Santo abandona a la Iglesia en las dificultades.", "respuesta": False},
        {"texto": "La Iglesia camina guiada por el Espíritu Santo.", "respuesta": True},
        {"texto": "El Espíritu Santo no tiene nada que ver con la Iglesia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda quién guía a la Iglesia.",
               "Si una frase dice que el Espíritu Santo abandona a la Iglesia, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hace el Espíritu Santo con la Iglesia?",
         "opciones": ["La guía hacia la verdad", "La abandona", "La confunde", "No hace nada"], "correcta": 0},
        {"texto": "¿Qué es la Iglesia?",
         "opciones": ["La comunidad de quienes creen en Jesús", "Un edificio solamente", "Un grupo de personas sin fe", "Nada importante"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con la Iglesia.",
               "Recuerda qué es realmente la Iglesia."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "GUIA", "definicion": "Lo que hace el Espíritu Santo con la Iglesia"},
        {"termino": "VERDAD", "definicion": "Lo que el Espíritu Santo nos ayuda a conocer"},
        {"termino": "IGLESIA", "definicion": "Comunidad guiada por el Espíritu Santo"},
        {"termino": "CAMINO", "definicion": "Lo que recorre la Iglesia"},
        {"termino": "LUZ", "definicion": "Lo que el Espíritu Santo da para no perdernos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el papel del Espíritu Santo en la vida de la Iglesia.",
               "LUZ es lo que evita que la Iglesia se pierda en su camino."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: el Espíritu Santo y la Iglesia",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "El Espíritu Santo ______ a la Iglesia.",
         "opciones": ["guía", "abandona", "confunde"], "correcta": 0},
        {"texto": "El Espíritu Santo nos ayuda a conocer la ______.",
         "opciones": ["verdad", "mentira", "duda"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con la Iglesia.",
               "Recuerda lo que el Espíritu Santo nos ayuda a conocer."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "El Espíritu Santo ______ a la Iglesia en su camino.",
         "respuesta": "GUIA", "banco": ["GUIA", "ABANDONA", "OLVIDA"]},
    ],
    "reflexion": "¿Cómo sientes que el Espíritu Santo guía tu propia vida de fe?",
    "requisito": 1,
    "pistas": ["Piensa en lo que hace el Espíritu Santo con la Iglesia.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: me dejo guiar por el Espíritu",
    "situacion": "Ya sabes que el Espíritu Santo guía a la Iglesia hacia la verdad completa.",
    "items": [
        {"texto": "¿Cómo puedes dejarte guiar por el Espíritu Santo en tu vida?",
         "opciones": ["Rezando y pidiendo su luz",
                      "Escuchando la Palabra de Dios",
                      "Participando en la vida de la Iglesia",
                      "Decidiendo todo solo, sin pedir ayuda"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de apertura al Espíritu Santo.",
               "Descarta la única opción que decide todo en soledad."],
    "feedback_ok": "¡Muy bien! Así nos dejamos guiar por el Espíritu Santo.",
})

# ==========================================================================
# PC13-C06 — Enviados como Jesús fue enviado
# ==========================================================================
C = "PC13-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: enviados como Jesús",
    "items": [
        {"texto": "Como Jesús fue por el Padre, así nos envía él también.", "respuesta": "ENVIADO", "banco": ["ENVIADO", "ABANDONADO", "OLVIDADO"]},
        {"texto": "Lugar al que Jesús nos envía, como el Padre lo envió a él.", "respuesta": "MUNDO", "banco": ["MUNDO", "DESIERTO", "SILENCIO"]},
        {"texto": "Tarea que continuamos gracias al Espíritu Santo.", "respuesta": "MISION", "banco": ["MISION", "DUDA", "PEREZA"]},
        {"texto": "Lo que hacemos con la misión de Jesús, guiados por el Espíritu Santo.", "respuesta": "CONTINUAR", "banco": ["CONTINUAR", "ABANDONAR", "OLVIDAR"]},
        {"texto": "Comunidad enviada a continuar la misión de Jesús.", "respuesta": "IGLESIA", "banco": ["IGLESIA", "MULTITUD", "PUEBLO"]},
        {"texto": "Quien nos da fuerza para continuar la misión de Jesús.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "DUDA"]},
    ],
    "incluir": ["ENVIADO", "MISION"], "requisito": 4,
    "pistas": ["Piensa en cómo Jesús envía a la Iglesia, como el Padre lo envió a él.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: enviados como Jesús",
    "palabras": ["ENVIADO", "MUNDO", "MISION", "CONTINUAR", "IGLESIA", "ESPIRITU"],
    "incluir": ["MUNDO", "IGLESIA"], "requisito": 5,
    "pistas": ["MUNDO y MISION son de las palabras más cortas: búscalas primero.",
               "CONTINUAR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 17,18",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 17,18 y completa: «Como tú me enviaste al mundo, "
                  "también yo los he enviado a ______.»", "respuesta": "ELLOS",
         "banco": ["ELLOS", "NADIE", "POCOS"]},
        {"texto": "¿Qué misión continúa la Iglesia gracias al Espíritu Santo?", "abierta": True,
         "palabras_esperadas": ["MISION", "JESUS", "ANUNCIAR", "MUNDO"],
         "respuestas_referencia": ["Continúa la misión de anunciar a Jesús en el mundo entero.",
                                    "Sigue llevando el amor de Jesús a todas las personas.",
                                    "Continúa la obra de Jesús, guiada por la fuerza del Espíritu Santo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 17.",
               "El texto compara el envío de Jesús con el envío de sus discípulos."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús nos envía al ______ como el Padre lo envió a él.", "respuesta": "MUNDO", "banco": ["MUNDO", "DESIERTO", "SILENCIO"]},
        {"texto": "La Iglesia continúa la ______ de Jesús con la fuerza del Espíritu Santo.", "respuesta": "MISION", "banco": ["MISION", "DUDA", "PEREZA"]},
        {"texto": "El Espíritu Santo nos da fuerza para ______ la misión de Jesús.", "respuesta": "CONTINUAR", "banco": ["CONTINUAR", "ABANDONAR", "OLVIDAR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a dónde nos envía Jesús.",
               "La tercera respuesta es lo que hacemos con la misión de Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús envía a la Iglesia al mundo, como el Padre lo envió a él.", "respuesta": True},
        {"texto": "La misión de Jesús terminó cuando él subió al cielo.", "respuesta": False},
        {"texto": "El Espíritu Santo ayuda a la Iglesia a continuar la misión de Jesús.", "respuesta": True},
        {"texto": "Nosotros no tenemos ninguna parte en la misión de la Iglesia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda a dónde envía Jesús a la Iglesia.",
               "Si una frase dice que la misión de Jesús terminó, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿A qué nos envía Jesús, como el Padre lo envió a él?",
         "opciones": ["Al mundo", "A ningún lugar", "Solo a la iglesia", "A escondernos"], "correcta": 0},
        {"texto": "¿Quién nos da fuerza para continuar la misión de Jesús?",
         "opciones": ["El Espíritu Santo", "Nadie", "El miedo", "La duda"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en a dónde nos envía Jesús.",
               "Recuerda quién da fuerza para continuar la misión."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ENVIADO", "definicion": "Como Jesús fue por el Padre, así nos envía él"},
        {"termino": "MUNDO", "definicion": "Lugar al que Jesús nos envía"},
        {"termino": "MISION", "definicion": "Tarea que continuamos con el Espíritu Santo"},
        {"termino": "IGLESIA", "definicion": "Comunidad enviada a continuar la misión"},
        {"termino": "ESPIRITU", "definicion": "Quien nos da fuerza para la misión"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo Jesús envía a su Iglesia al mundo.",
               "ESPIRITU es quien acompaña la misión, no la misión misma."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la misión de la Iglesia",
    "instruccion": "En 45 segundos, marca las palabras que describen nuestra misión enviada por Jesús.",
    "tiempo_segundos": 45,
    "banco": ["ENVIADO", "MISION", "MUNDO", "IGLESIA", "MIEDO", "DUDA"],
    "correctas": ["ENVIADO", "MISION", "MUNDO", "IGLESIA"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Enviado - Misión - Mundo - Iglesia.",
               "Descarta las palabras que describen actitudes contrarias a la misión."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús nos envía al ______ como el Padre lo envió a él.",
         "respuesta": "MUNDO", "banco": ["MUNDO", "DESIERTO", "SILENCIO"]},
    ],
    "reflexion": "¿Cómo puedes tú continuar hoy la misión de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en a dónde nos envía Jesús.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: continúo la misión de Jesús",
    "situacion": "Ya sabes que Jesús envía a su Iglesia al mundo, con la fuerza del Espíritu Santo.",
    "items": [
        {"texto": "¿Cómo puedes ser parte de esa misión en tu vida diaria?",
         "opciones": ["Viviendo el amor de Jesús en mi familia y escuela",
                      "Compartiendo lo que aprendo de mi fe",
                      "Pidiendo al Espíritu Santo que me acompañe",
                      "Pensando que la misión es solo para los adultos"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en una acción posible para alguien de tu edad.",
               "Descarta la única opción que pospone la misión para los adultos."],
    "feedback_ok": "¡Muy bien! Así continuamos, cada día, la misión que Jesús nos confió.",
})

# ==========================================================================
# ==========================================================================
# PC14 — Iglesia sinodal: caminamos juntos   (Encuentro 14, Hechos 15,6-7.22 / Hechos 2,42)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC14-C01 — La Iglesia, Pueblo de Dios
# ==========================================================================
C = "PC14-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Iglesia, Pueblo de Dios",
    "items": [
        {"texto": "Grupo de creyentes que vive y comparte la fe junto.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "DISTANCIA", "SOLEDAD"]},
        {"texto": "Lo que los primeros cristianos escuchaban con fidelidad, según Hechos.", "respuesta": "ENSEÑANZA", "banco": ["ENSEÑANZA", "DUDA", "DISTANCIA"]},
        {"texto": "Lo que la comunidad primitiva hacía junta constantemente.", "respuesta": "ORACION", "banco": ["ORACION", "SILENCIO", "PRISA"]},
        {"texto": "Lo que la comunidad partía juntos, recordando a Jesús.", "respuesta": "PAN", "banco": ["PAN", "ORO", "AGUA"]},
        {"texto": "Como vivían los primeros cristianos, compartiendo todo.", "respuesta": "UNIDOS", "banco": ["UNIDOS", "SEPARADOS", "SOLOS"]},
        {"texto": "Como se llama a la Iglesia, caminando junto a Dios.", "respuesta": "PUEBLO", "banco": ["PUEBLO", "EJERCITO", "GRUPO"]},
    ],
    "incluir": ["COMUNIDAD", "PUEBLO"], "requisito": 4,
    "pistas": ["Piensa en cómo vivía la primera comunidad cristiana.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Iglesia, Pueblo de Dios",
    "palabras": ["COMUNIDAD", "ENSEÑANZA", "ORACION", "PAN", "UNIDOS", "PUEBLO"],
    "incluir": ["ORACION", "UNIDOS"], "requisito": 5,
    "pistas": ["PAN es la palabra más corta: búscala primero.",
               "ENSEÑANZA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 2,42",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 2,42 y completa: «Eran fieles a la enseñanza de los "
                  "apóstoles, a la ______ fraterna, a la fracción del pan y a las oraciones.»", "respuesta": "COMUNION",
         "banco": ["COMUNION", "DISTANCIA", "DUDA"]},
        {"texto": "¿Cómo vivía la primera comunidad cristiana, según Hechos 2,42?", "abierta": True,
         "palabras_esperadas": ["UNIDOS", "ORACION", "PAN", "ENSEÑANZA"],
         "respuestas_referencia": ["Vivía unida, compartiendo la enseñanza, la oración y el pan.",
                                    "Se reunía a rezar y compartir todo, como una gran familia.",
                                    "Era fiel a la enseñanza de los apóstoles y vivía en comunión."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 2.",
               "El texto describe cuatro cosas a las que era fiel la primera comunidad."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los primeros cristianos eran fieles a la ______ de los apóstoles.", "respuesta": "ENSEÑANZA", "banco": ["ENSEÑANZA", "DUDA", "DISTANCIA"]},
        {"texto": "La comunidad primitiva compartía el ______ y la oración.", "respuesta": "PAN", "banco": ["PAN", "ORO", "SILENCIO"]},
        {"texto": "La Iglesia es el ______ de Dios que camina unido.", "respuesta": "PUEBLO", "banco": ["PUEBLO", "EJERCITO", "GRUPO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que escuchaban con fidelidad los primeros cristianos.",
               "La tercera respuesta describe a la Iglesia entera."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los primeros cristianos vivían unidos, compartiendo la fe.", "respuesta": True},
        {"texto": "La primera comunidad cristiana no rezaba junta.", "respuesta": False},
        {"texto": "La Iglesia es el Pueblo de Dios que camina unido.", "respuesta": True},
        {"texto": "A los primeros cristianos no les importaba la enseñanza de los apóstoles.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo vivía la primera comunidad cristiana.",
               "Si una frase dice que no rezaban juntos, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo vivía la primera comunidad cristiana?",
         "opciones": ["Unida, compartiendo la fe y la oración", "Separada y sin comunicarse", "Sin ningún interés por Jesús", "Cada uno por su cuenta"], "correcta": 0},
        {"texto": "¿Qué es la Iglesia, según la Biblia?",
         "opciones": ["El Pueblo de Dios", "Un edificio solamente", "Un grupo cerrado", "Nada importante"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo vivía la primera comunidad cristiana.",
               "Recuerda cómo se llama a la Iglesia, como Pueblo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "COMUNIDAD", "definicion": "Grupo de creyentes que comparte la fe"},
        {"termino": "ENSEÑANZA", "definicion": "Lo que los primeros cristianos escuchaban fielmente"},
        {"termino": "PAN", "definicion": "Lo que la comunidad partía junta"},
        {"termino": "UNIDOS", "definicion": "Cómo vivían los primeros cristianos"},
        {"termino": "PUEBLO", "definicion": "Cómo se llama a la Iglesia"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la vida de la primera comunidad cristiana.",
               "PUEBLO es el nombre que recibe la Iglesia entera."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: la primera comunidad",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Los primeros cristianos vivían ______, compartiendo la fe.",
         "opciones": ["unidos", "separados", "solos"], "correcta": 0},
        {"texto": "La Iglesia es el ______ de Dios.",
         "opciones": ["Pueblo", "ejército", "grupo cerrado"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo vivía la primera comunidad cristiana.",
               "Recuerda cómo se llama a la Iglesia entera."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los primeros cristianos eran fieles a la ______ de los apóstoles.",
         "respuesta": "ENSEÑANZA", "banco": ["ENSEÑANZA", "DUDA", "DISTANCIA"]},
    ],
    "reflexion": "¿Cómo vives tú la unidad con tu comunidad de fe?",
    "requisito": 1,
    "pistas": ["Piensa en cómo vivía la primera comunidad cristiana.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo la unidad de la Iglesia",
    "situacion": "Ya sabes que los primeros cristianos vivían unidos, compartiendo la fe, la oración y el pan.",
    "items": [
        {"texto": "¿Cómo puedes vivir la unidad en tu comunidad de fe?",
         "opciones": ["Participando en la Misa con mi familia",
                      "Compartiendo lo que tengo con otros",
                      "Rezando junto a mi comunidad",
                      "Prefiriendo vivir la fe siempre solo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones que se hacen en comunidad.",
               "Descarta la única opción que prefiere vivir siempre solo."],
    "feedback_ok": "¡Muy bien! Así se vive la Iglesia como comunidad unida.",
})

# ==========================================================================
# PC14-C02 — Caminar juntos: qué es la sinodalidad
# ==========================================================================
C = "PC14-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: caminar juntos",
    "items": [
        {"texto": "Palabra que significa 'caminar juntos' en el camino de la fe.", "respuesta": "SINODO", "banco": ["SINODO", "DESIERTO", "SILENCIO"]},
        {"texto": "Lo que hace la Iglesia junta, como un solo Pueblo de Dios.", "respuesta": "CAMINAR", "banco": ["CAMINAR", "DETENERSE", "ALEJARSE"]},
        {"texto": "Junto con los ancianos, se reunieron para tratar la cuestión en Jerusalén.", "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "SOLDADOS", "EXTRAÑOS"]},
        {"texto": "Junto con los apóstoles, participaron de la reunión de Jerusalén.", "respuesta": "ANCIANOS", "banco": ["ANCIANOS", "SOLDADOS", "EXTRAÑOS"]},
        {"texto": "Lo que hicieron los apóstoles y ancianos para decidir juntos.", "respuesta": "REUNIRSE", "banco": ["REUNIRSE", "ALEJARSE", "OLVIDAR"]},
        {"texto": "Como camina la Iglesia, sin dejar a nadie atrás.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "LEJOS"]},
    ],
    "incluir": ["SINODO", "CAMINAR"], "requisito": 4,
    "pistas": ["Piensa en el significado de la palabra sínodo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: caminar juntos",
    "palabras": ["SINODO", "CAMINAR", "APOSTOLES", "ANCIANOS", "REUNIRSE", "JUNTOS"],
    "incluir": ["APOSTOLES", "JUNTOS"], "requisito": 5,
    "pistas": ["SINODO y JUNTOS son de las palabras más cortas: búscalas primero.",
               "APOSTOLES es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 15,6-7",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 15,6-7 y completa: «Los apóstoles y los ______ se "
                  "reunieron para examinar este asunto.»", "respuesta": "ANCIANOS",
         "banco": ["ANCIANOS", "SOLDADOS", "EXTRAÑOS"]},
        {"texto": "¿Qué significa que la Iglesia sea 'sinodal'?", "abierta": True,
         "palabras_esperadas": ["CAMINAR", "JUNTOS", "ESCUCHAR", "COMUNIDAD"],
         "respuestas_referencia": ["Significa que la Iglesia camina junta, escuchándose unos a otros.",
                                    "Significa que todos caminamos juntos en comunidad, sin dejar a nadie atrás.",
                                    "Significa reunirse, escuchar y decidir en comunidad, como en Jerusalén."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 15.",
               "El texto cuenta quiénes se reunieron en Jerusalén para examinar un asunto importante."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "La palabra sínodo significa caminar ______.", "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "LEJOS"]},
        {"texto": "En Jerusalén, los apóstoles y ancianos se ______ para decidir juntos.", "respuesta": "REUNIERON", "banco": ["REUNIERON", "ALEJARON", "OLVIDARON"]},
        {"texto": "La Iglesia sinodal es la Iglesia que camina en ______.", "respuesta": "COMUNIDAD", "banco": ["COMUNIDAD", "SOLEDAD", "SILENCIO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el significado de la palabra sínodo.",
               "La segunda respuesta es lo que hicieron los apóstoles y ancianos en Jerusalén."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Sínodo significa caminar juntos.", "respuesta": True},
        {"texto": "Los apóstoles decidieron todo sin reunirse con nadie.", "respuesta": False},
        {"texto": "En Jerusalén, los apóstoles y ancianos se reunieron para decidir juntos.", "respuesta": True},
        {"texto": "Una Iglesia sinodal no escucha a su comunidad.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda el significado de la palabra sínodo.",
               "Si una frase dice que los apóstoles decidieron sin reunirse, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué significa la palabra sínodo?",
         "opciones": ["Caminar juntos", "Caminar solo", "Quedarse quieto", "Alejarse de los demás"], "correcta": 0},
        {"texto": "¿Qué hicieron los apóstoles y ancianos en Jerusalén?",
         "opciones": ["Se reunieron para decidir juntos", "Se ignoraron", "Discutieron sin llegar a nada", "No les importó el tema"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en el significado de la palabra sínodo.",
               "Recuerda lo que hicieron los apóstoles y ancianos en Jerusalén."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "SINODO", "definicion": "Caminar juntos"},
        {"termino": "CAMINAR", "definicion": "Lo que hace la Iglesia unida"},
        {"termino": "APOSTOLES", "definicion": "Se reunieron con los ancianos en Jerusalén"},
        {"termino": "ANCIANOS", "definicion": "Participaron junto a los apóstoles"},
        {"termino": "JUNTOS", "definicion": "Cómo camina la Iglesia"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la reunión de Jerusalén y en su significado.",
               "JUNTOS describe la forma de caminar de toda la Iglesia."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: una Iglesia sinodal",
    "instruccion": "En 45 segundos, marca las palabras que describen una Iglesia sinodal.",
    "tiempo_segundos": 45,
    "banco": ["SINODO", "CAMINAR", "JUNTOS", "REUNIRSE", "SOLOS", "LEJOS"],
    "correctas": ["SINODO", "CAMINAR", "JUNTOS", "REUNIRSE"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Sínodo - Caminar - Juntos - Reunirse.",
               "Descarta las palabras que describen lo contrario de caminar en comunidad."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La palabra sínodo significa caminar ______.",
         "respuesta": "JUNTOS", "banco": ["JUNTOS", "SOLOS", "LEJOS"]},
    ],
    "reflexion": "¿Con quiénes caminas tú en tu comunidad de fe?",
    "requisito": 1,
    "pistas": ["Piensa en el significado de la palabra sínodo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: camino junto a mi comunidad",
    "situacion": "Ya sabes que sínodo significa caminar juntos, como lo hicieron los apóstoles y ancianos en Jerusalén.",
    "items": [
        {"texto": "¿Cómo puedes vivir el 'caminar juntos' en tu comunidad?",
         "opciones": ["Participando en las actividades de mi parroquia",
                      "Escuchando a los demás en la catequesis",
                      "Colaborando con mi grupo de catequesis",
                      "Prefiriendo hacer todo solo"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones que se hacen en comunidad.",
               "Descarta la única opción que prefiere hacer todo solo."],
    "feedback_ok": "¡Muy bien! Así se vive una Iglesia que camina junta.",
})

# ==========================================================================
# PC14-C03 — Escuchar a todos en la comunidad
# ==========================================================================
C = "PC14-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: escuchar a todos",
    "items": [
        {"texto": "Lo que hizo toda la asamblea al oír a Bernabé y Pablo.", "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "INTERRUMPIR"]},
        {"texto": "Lo que guardó la asamblea para poder escuchar.", "respuesta": "SILENCIO", "banco": ["SILENCIO", "RUIDO", "GRITOS"]},
        {"texto": "Comunidad reunida para escuchar y decidir juntos.", "respuesta": "ASAMBLEA", "banco": ["ASAMBLEA", "MULTITUD", "GRUPO"]},
        {"texto": "Junto a Pablo, contó las maravillas que Dios había hecho entre los paganos.", "respuesta": "BARNABE", "banco": ["BARNABE", "PEDRO", "JUAN"]},
        {"texto": "Junto a Bernabé, contó lo que Dios hacía entre los paganos.", "respuesta": "PABLO", "banco": ["PABLO", "PEDRO", "JUAN"]},
        {"texto": "Lo que se necesita para escuchar de verdad a los demás.", "respuesta": "ATENCION", "banco": ["ATENCION", "PRISA", "DISTRACCION"]},
    ],
    "incluir": ["ESCUCHAR", "ASAMBLEA"], "requisito": 4,
    "pistas": ["Piensa en lo que hizo la asamblea al oír a Bernabé y a Pablo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: escuchar a todos",
    "palabras": ["ESCUCHAR", "SILENCIO", "ASAMBLEA", "BARNABE", "PABLO", "ATENCION"],
    "incluir": ["SILENCIO", "ATENCION"], "requisito": 5,
    "pistas": ["PABLO es la palabra más corta: búscala primero.",
               "ATENCION es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 15,12",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 15,12 y completa: «Toda la asamblea guardó ______, "
                  "y escuchaban a Bernabé y a Pablo.»", "respuesta": "SILENCIO",
         "banco": ["SILENCIO", "RUIDO", "GRITOS"]},
        {"texto": "¿Por qué es importante escuchar a todos en la comunidad?", "abierta": True,
         "palabras_esperadas": ["ESCUCHAR", "RESPETO", "COMUNIDAD", "DECIDIR"],
         "respuestas_referencia": ["Porque escuchar a todos es una señal de respeto y de comunidad.",
                                    "Porque así se conocen mejor las necesidades de todos antes de decidir.",
                                    "Porque cada persona tiene algo valioso que aportar a la comunidad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 15.",
               "El texto describe la actitud de la asamblea al escuchar a Bernabé y a Pablo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Toda la asamblea guardó silencio para ______ a Bernabé y a Pablo.", "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "INTERRUMPIR"]},
        {"texto": "Escuchar a los demás es una señal de ______.", "respuesta": "RESPETO", "banco": ["RESPETO", "DESPRECIO", "IMPACIENCIA"]},
        {"texto": "En una Iglesia sinodal, todos tienen voz para ser ______.", "respuesta": "ESCUCHADOS", "banco": ["ESCUCHADOS", "IGNORADOS", "CALLADOS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hizo la asamblea antes de escuchar a Bernabé y a Pablo.",
               "La segunda respuesta describe una actitud de valoración hacia el otro."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Toda la asamblea guardó silencio para escuchar a Bernabé y a Pablo.", "respuesta": True},
        {"texto": "Escuchar a los demás no tiene ninguna importancia en la Iglesia.", "respuesta": False},
        {"texto": "En una comunidad sinodal, todos pueden ser escuchados.", "respuesta": True},
        {"texto": "Interrumpir a los demás es una forma de escuchar bien.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la actitud de la asamblea al escuchar a Bernabé y a Pablo.",
               "Si una frase dice que interrumpir es escuchar bien, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hizo la asamblea al escuchar a Bernabé y a Pablo?",
         "opciones": ["Guardó silencio para escuchar", "Los interrumpió", "Se fue del lugar", "No les prestó atención"], "correcta": 0},
        {"texto": "¿Qué actitud necesitamos para escuchar bien a los demás?",
         "opciones": ["Atención y respeto", "Prisa", "Indiferencia", "Enojo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la actitud de la asamblea al escuchar a Bernabé y a Pablo.",
               "Recuerda qué se necesita para escuchar de verdad."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ESCUCHAR", "definicion": "Lo que hizo la asamblea al oír a Bernabé y Pablo"},
        {"termino": "SILENCIO", "definicion": "Lo que guardó la asamblea para escuchar"},
        {"termino": "ASAMBLEA", "definicion": "Comunidad reunida para escuchar y decidir"},
        {"termino": "BARNABE", "definicion": "Contó las maravillas de Dios junto a Pablo"},
        {"termino": "ATENCION", "definicion": "Lo que se necesita para escuchar de verdad"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la escena de la asamblea escuchando a Bernabé y a Pablo.",
               "ATENCION es una actitud, no una persona ni un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: escuchar con atención",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Toda la asamblea guardó ______ para escuchar.",
         "opciones": ["silencio", "ruido", "gritos"], "correcta": 0},
        {"texto": "Escuchar a los demás es una señal de ______.",
         "opciones": ["respeto", "desprecio", "impaciencia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la actitud de la asamblea al escuchar.",
               "Recuerda qué muestra escuchar bien a los demás."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Toda la asamblea guardó silencio para ______ a Bernabé y a Pablo.",
         "respuesta": "ESCUCHAR", "banco": ["ESCUCHAR", "IGNORAR", "INTERRUMPIR"]},
    ],
    "reflexion": "¿A quién te cuesta más escuchar con atención?",
    "requisito": 1,
    "pistas": ["Piensa en la actitud de la asamblea al escuchar.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: aprendo a escuchar",
    "situacion": "Ya sabes que la asamblea de Jerusalén guardó silencio para escuchar con atención a Bernabé y a Pablo.",
    "items": [
        {"texto": "¿Cómo puedes practicar la escucha en tu comunidad?",
         "opciones": ["Prestando atención cuando otros hablan",
                      "No interrumpir a mis compañeros",
                      "Preguntando para entender mejor",
                      "Hablando siempre yo primero y sin parar"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de respeto al escuchar.",
               "Descarta la única opción que no deja hablar a nadie más."],
    "feedback_ok": "¡Muy bien! Escuchar con atención es un paso importante para caminar juntos.",
})

# ==========================================================================
# PC14-C04 — Decidir en comunión
# ==========================================================================
C = "PC14-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: decidir en comunión",
    "items": [
        {"texto": "Lo que tomaron juntos los apóstoles, los ancianos y toda la Iglesia.", "respuesta": "DECISION", "banco": ["DECISION", "DUDA", "DISTANCIA"]},
        {"texto": "Vivir y decidir unidos, como un solo cuerpo.", "respuesta": "COMUNION", "banco": ["COMUNION", "DISTANCIA", "DIVISION"]},
        {"texto": "Acuerdo al que llega una comunidad después de escuchar a todos.", "respuesta": "CONSENSO", "banco": ["CONSENSO", "PLEITO", "DESACUERDO"]},
        {"texto": "Personas enviadas para llevar la decisión de la asamblea a otras comunidades.", "respuesta": "DELEGADOS", "banco": ["DELEGADOS", "EXTRAÑOS", "SOLDADOS"]},
        {"texto": "Quien acompañó a la asamblea de Jerusalén en su decisión.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "SILENCIO"]},
        {"texto": "Documento que escribieron para comunicar la decisión de la asamblea.", "respuesta": "CARTA", "banco": ["CARTA", "ORDEN", "AMENAZA"]},
    ],
    "incluir": ["DECISION", "COMUNION"], "requisito": 4,
    "pistas": ["Piensa en lo que tomaron juntos los apóstoles, ancianos y la Iglesia.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: decidir en comunión",
    "palabras": ["DECISION", "COMUNION", "CONSENSO", "DELEGADOS", "ESPIRITU", "CARTA"],
    "incluir": ["CONSENSO", "ESPIRITU"], "requisito": 5,
    "pistas": ["CARTA es la palabra más corta: búscala primero.",
               "DELEGADOS es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 15,22.28",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 15,22.28 y completa: «Ha parecido bien al Espíritu "
                  "Santo y a ______: no imponerles más cargas que las necesarias.»", "respuesta": "NOSOTROS",
         "banco": ["NOSOTROS", "NADIE", "ELLOS"]},
        {"texto": "¿Cómo tomó la asamblea de Jerusalén su decisión?", "abierta": True,
         "palabras_esperadas": ["JUNTOS", "ESPIRITU", "ESCUCHAR", "COMUNION"],
         "respuestas_referencia": ["La tomó junta, después de escuchar a todos, guiada por el Espíritu Santo.",
                                    "Decidió en comunión, con la ayuda del Espíritu Santo.",
                                    "Escuchó a todos y luego decidió juntos, con el acompañamiento del Espíritu Santo."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 15.",
               "El texto muestra que la decisión se tomó junto con el Espíritu Santo y toda la asamblea."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los apóstoles y ancianos tomaron su ______ junto con toda la Iglesia.", "respuesta": "DECISION", "banco": ["DECISION", "DUDA", "DISTANCIA"]},
        {"texto": "La asamblea decidió con la ayuda del ______ Santo.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "SILENCIO"]},
        {"texto": "Enviaron una ______ para comunicar la decisión a las comunidades.", "respuesta": "CARTA", "banco": ["CARTA", "ORDEN", "AMENAZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quiénes participaron de la decisión de la asamblea.",
               "La tercera respuesta es cómo se comunicó la decisión."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los apóstoles y ancianos decidieron junto con toda la Iglesia.", "respuesta": True},
        {"texto": "El Espíritu Santo no tuvo ninguna parte en la decisión de la asamblea.", "respuesta": False},
        {"texto": "La asamblea envió una carta para comunicar su decisión.", "respuesta": True},
        {"texto": "En la Iglesia, las decisiones importantes se toman sin escuchar a nadie.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda quiénes participaron en la decisión de la asamblea.",
               "Si una frase dice que las decisiones se toman sin escuchar a nadie, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Quién acompañó a la asamblea de Jerusalén en su decisión?",
         "opciones": ["El Espíritu Santo", "Nadie", "El miedo", "La duda"], "correcta": 0},
        {"texto": "¿Cómo comunicaron su decisión a las demás comunidades?",
         "opciones": ["Con una carta", "Sin decir nada", "Gritando", "Escondiendo la decisión"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién acompañó la decisión de la asamblea.",
               "Recuerda cómo comunicaron la decisión a otras comunidades."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DECISION", "definicion": "Lo que tomaron juntos en la asamblea"},
        {"termino": "COMUNION", "definicion": "Vivir y decidir unidos"},
        {"termino": "CONSENSO", "definicion": "Acuerdo después de escuchar a todos"},
        {"termino": "ESPIRITU", "definicion": "Quien acompañó la decisión de la asamblea"},
        {"termino": "CARTA", "definicion": "Documento que comunicó la decisión"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en cómo se tomó y comunicó la decisión de la asamblea.",
               "CARTA es el documento, no la decisión misma."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: decidir juntos",
    "instruccion": "En 45 segundos, marca las palabras que describen cómo decidió la asamblea de Jerusalén.",
    "tiempo_segundos": 45,
    "banco": ["DECISION", "COMUNION", "ESPIRITU", "CONSENSO", "DUDA", "DISTANCIA"],
    "correctas": ["DECISION", "COMUNION", "ESPIRITU", "CONSENSO"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Decisión - Comunión - Espíritu - Consenso.",
               "Descarta las palabras que describen división o desacuerdo."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "La asamblea decidió con la ayuda del ______ Santo.",
         "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "SILENCIO"]},
    ],
    "reflexion": "¿Cómo se toman las decisiones importantes en tu familia o tu grupo?",
    "requisito": 1,
    "pistas": ["Piensa en quién acompañó la decisión de la asamblea.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: decido en comunión",
    "situacion": "Ya sabes que la asamblea de Jerusalén decidió junta, escuchando a todos y guiada por el Espíritu Santo.",
    "items": [
        {"texto": "¿Cómo puedes ayudar a decidir en comunión con tu grupo o tu familia?",
         "opciones": ["Escuchando las opiniones de los demás",
                      "Proponiendo ideas con respeto",
                      "Aceptando lo que se decide en conjunto",
                      "Queriendo decidir siempre solo, sin escuchar a nadie"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de comunión, no de imposición.",
               "Descarta la única opción que decide todo en soledad."],
    "feedback_ok": "¡Muy bien! Así se decide en comunión, como la primera Iglesia.",
})

# ==========================================================================
# PC14-C05 — Cada uno tiene un don para la comunidad
# ==========================================================================
C = "PC14-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: un don para la comunidad",
    "items": [
        {"texto": "Regalos distintos que cada persona recibe de Dios.", "respuesta": "DONES", "banco": ["DONES", "CASTIGOS", "DEBERES"]},
        {"texto": "Cómo son los dones, aunque el Espíritu que los da es el mismo.", "respuesta": "DIVERSOS", "banco": ["DIVERSOS", "IGUALES", "ESCASOS"]},
        {"texto": "Quien reparte los dones distintos a cada persona.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "DUDA"]},
        {"texto": "Para qué se dan los dones, según San Pablo.", "respuesta": "SERVICIO", "banco": ["SERVICIO", "OLVIDO", "COMPETENCIA"]},
        {"texto": "Lo que se busca con los dones: el bien de toda la comunidad.", "respuesta": "COMUN", "banco": ["COMUN", "PROPIO", "AJENO"]},
        {"texto": "Capacidades que Dios da a cada persona para ayudar a los demás.", "respuesta": "TALENTOS", "banco": ["TALENTOS", "DEFECTOS", "EXCUSAS"]},
    ],
    "incluir": ["DONES", "ESPIRITU"], "requisito": 4,
    "pistas": ["Piensa en los regalos distintos que cada persona recibe de Dios.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: un don para la comunidad",
    "palabras": ["DONES", "DIVERSOS", "ESPIRITU", "SERVICIO", "COMUN", "TALENTOS"],
    "incluir": ["DIVERSOS", "SERVICIO"], "requisito": 5,
    "pistas": ["DONES y COMUN son de las palabras más cortas: búscalas primero.",
               "SERVICIO y TALENTOS son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 12,4-7",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 12,4-7 y completa: «Hay ______ de dones, pero "
                  "un mismo Espíritu.»", "respuesta": "DIVERSIDAD",
         "banco": ["DIVERSIDAD", "IGUALDAD", "ESCASEZ"]},
        {"texto": "¿Para qué nos da Dios dones distintos a cada uno?", "abierta": True,
         "palabras_esperadas": ["SERVICIO", "COMUNIDAD", "BIEN", "AYUDAR"],
         "respuestas_referencia": ["Para que los pongamos al servicio de toda la comunidad.",
                                    "Para ayudar a los demás y construir juntos el bien común.",
                                    "Para que cada uno aporte algo distinto al bien de todos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a los Corintios en el índice de tu Biblia; el capítulo es el 12.",
               "El texto habla de la diversidad de dones y el único Espíritu que los reparte."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Hay ______ de dones, pero un mismo Espíritu.", "respuesta": "DIVERSIDAD", "banco": ["DIVERSIDAD", "IGUALDAD", "ESCASEZ"]},
        {"texto": "Los dones se dan para el ______ de toda la comunidad.", "respuesta": "BIEN", "banco": ["BIEN", "DAÑO", "OLVIDO"]},
        {"texto": "Cada persona recibe un don distinto del mismo ______.", "respuesta": "ESPIRITU", "banco": ["ESPIRITU", "MIEDO", "SILENCIO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo son los dones que da Dios.",
               "La tercera respuesta es quien reparte los dones."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Cada persona recibe un don distinto del mismo Espíritu.", "respuesta": True},
        {"texto": "Los dones sirven solo para uno mismo, no para los demás.", "respuesta": False},
        {"texto": "San Pablo dice que hay diversidad de dones.", "respuesta": True},
        {"texto": "Los dones no tienen relación con el servicio a la comunidad.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda para qué sirven los dones según San Pablo.",
               "Si una frase dice que los dones son solo para uno mismo, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Quién reparte los dones distintos a cada persona?",
         "opciones": ["El Espíritu Santo", "Nadie", "El azar", "Cada persona a sí misma"], "correcta": 0},
        {"texto": "¿Para qué sirven los dones, según San Pablo?",
         "opciones": ["Para el bien de toda la comunidad", "Solo para uno mismo", "Para nada importante", "Para competir con los demás"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en quién reparte los dones a cada persona.",
               "Recuerda para qué sirven los dones según San Pablo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "DONES", "definicion": "Regalos distintos que cada persona recibe"},
        {"termino": "DIVERSOS", "definicion": "Cómo son los dones aunque el Espíritu es el mismo"},
        {"termino": "ESPIRITU", "definicion": "Quien reparte los dones"},
        {"termino": "SERVICIO", "definicion": "Para qué se dan los dones"},
        {"termino": "COMUN", "definicion": "El bien que se busca con los dones"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el origen y el propósito de los dones.",
               "COMUN describe el bien de todos, no de uno solo."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: dones para todos",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Hay ______ de dones, pero un mismo Espíritu.",
         "opciones": ["diversidad", "igualdad", "escasez"], "correcta": 0},
        {"texto": "Los dones se dan para el ______ de la comunidad.",
         "opciones": ["bien", "daño", "olvido"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo son los dones que da Dios.",
               "Recuerda para qué se dan los dones."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los dones se dan para el ______ de toda la comunidad.",
         "respuesta": "BIEN", "banco": ["BIEN", "DAÑO", "OLVIDO"]},
    ],
    "reflexion": "¿Qué don o talento sientes que Dios te ha dado?",
    "requisito": 1,
    "pistas": ["Piensa en para qué sirven los dones.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: pongo mis dones al servicio",
    "situacion": "Ya sabes que Dios da a cada persona dones distintos para el bien de toda la comunidad.",
    "items": [
        {"texto": "¿Cómo puedes poner tus dones al servicio de los demás?",
         "opciones": ["Ayudando en algo que se me da bien",
                      "Compartiendo lo que sé con mis compañeros",
                      "Colaborando en actividades de mi parroquia",
                      "Guardando mis talentos solo para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones que benefician a otros.",
               "Descarta la única opción que guarda los talentos solo para uno mismo."],
    "feedback_ok": "¡Muy bien! Así ponemos nuestros dones al servicio de la comunidad.",
})

# ==========================================================================
# PC14-C06 — Somos Iglesia: cada uno importa
# ==========================================================================
C = "PC14-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: cada uno importa",
    "items": [
        {"texto": "Como San Pablo compara a la Iglesia: un solo ______ con muchas partes.", "respuesta": "CUERPO", "banco": ["CUERPO", "EJERCITO", "MURO"]},
        {"texto": "Cada uno de nosotros, como parte del cuerpo de la Iglesia.", "respuesta": "MIEMBROS", "banco": ["MIEMBROS", "EXTRAÑOS", "VISITANTES"]},
        {"texto": "Lo que es cada persona dentro de la comunidad, sin excepción.", "respuesta": "IMPORTANTE", "banco": ["IMPORTANTE", "IGNORADO", "OLVIDADO"]},
        {"texto": "Lo que se logra cuando cada miembro cumple su parte en el cuerpo.", "respuesta": "UNIDAD", "banco": ["UNIDAD", "DIVISION", "DISTANCIA"]},
        {"texto": "Lo que sentimos al saber que somos parte de la Iglesia.", "respuesta": "PERTENECER", "banco": ["PERTENECER", "ALEJARSE", "OLVIDAR"]},
        {"texto": "Comunidad a la que todos pertenecemos, como un solo cuerpo.", "respuesta": "IGLESIA", "banco": ["IGLESIA", "MULTITUD", "PUEBLO"]},
    ],
    "incluir": ["CUERPO", "IGLESIA"], "requisito": 4,
    "pistas": ["Piensa en cómo compara San Pablo a la Iglesia.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: cada uno importa",
    "palabras": ["CUERPO", "MIEMBROS", "IMPORTANTE", "UNIDAD", "PERTENECER", "IGLESIA"],
    "incluir": ["MIEMBROS", "UNIDAD"], "requisito": 5,
    "pistas": ["CUERPO y UNIDAD son de las palabras más cortas: búscalas primero.",
               "IMPORTANTE y PERTENECER son de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Corintios 12,12.27",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Corintios 12,12.27 y completa: «Ustedes son el ______ de "
                  "Cristo, y cada uno de ustedes es un miembro de él.»", "respuesta": "CUERPO",
         "banco": ["CUERPO", "PUEBLO", "GRUPO"]},
        {"texto": "¿Por qué cada persona es importante en la Iglesia?", "abierta": True,
         "palabras_esperadas": ["CUERPO", "MIEMBRO", "IMPORTANTE", "PARTE"],
         "respuestas_referencia": ["Porque cada persona es un miembro del cuerpo de Cristo, con su propia parte.",
                                    "Porque sin cada miembro, el cuerpo entero no funcionaría bien.",
                                    "Porque cada uno aporta algo único e importante a la comunidad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta a los Corintios en el índice de tu Biblia; el capítulo es el 12.",
               "El texto compara a la Iglesia con un cuerpo y a cada persona con un miembro."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un ______ que tiene muchas partes.", "respuesta": "CUERPO", "banco": ["CUERPO", "EJERCITO", "MURO"]},
        {"texto": "Cada uno de nosotros es un ______ de ese cuerpo.", "respuesta": "MIEMBRO", "banco": ["MIEMBRO", "EXTRAÑO", "VISITANTE"]},
        {"texto": "En la Iglesia, cada persona es ______, sin excepción.", "respuesta": "IMPORTANTE", "banco": ["IMPORTANTE", "IGNORADA", "OLVIDADA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la comparación que hace San Pablo de la Iglesia.",
               "La tercera respuesta describe el valor de cada persona."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un cuerpo que tiene muchas partes.", "respuesta": True},
        {"texto": "En la Iglesia, solo algunas personas son importantes.", "respuesta": False},
        {"texto": "Cada miembro de la Iglesia cumple una parte importante.", "respuesta": True},
        {"texto": "Pertenecer a la Iglesia no tiene ningún valor.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la comparación que hace San Pablo de la Iglesia.",
               "Si una frase dice que solo algunos son importantes, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con qué compara San Pablo a la Iglesia?",
         "opciones": ["Con un cuerpo que tiene muchas partes", "Con un edificio vacío", "Con un grupo sin sentido", "Con nada importante"], "correcta": 0},
        {"texto": "¿Qué es cada persona dentro de la Iglesia?",
         "opciones": ["Un miembro importante", "Alguien sin valor", "Un extraño", "Alguien que sobra"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la comparación que hace San Pablo de la Iglesia.",
               "Recuerda el valor de cada persona dentro de ella."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CUERPO", "definicion": "Cómo San Pablo compara a la Iglesia"},
        {"termino": "MIEMBROS", "definicion": "Cada uno de nosotros en ese cuerpo"},
        {"termino": "IMPORTANTE", "definicion": "Lo que es cada persona en la comunidad"},
        {"termino": "UNIDAD", "definicion": "Lo que se logra cuando cada uno cumple su parte"},
        {"termino": "IGLESIA", "definicion": "Comunidad a la que todos pertenecemos"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la comparación de San Pablo y en su significado.",
               "UNIDAD es el resultado de que cada miembro cumpla su parte."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: un cuerpo, muchos miembros",
    "instruccion": "En 45 segundos, marca las palabras que describen a la Iglesia como cuerpo de Cristo.",
    "tiempo_segundos": 45,
    "banco": ["CUERPO", "MIEMBROS", "IMPORTANTE", "UNIDAD", "IGNORADO", "EXTRAÑO"],
    "correctas": ["CUERPO", "MIEMBROS", "IMPORTANTE", "UNIDAD"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Cuerpo - Miembros - Importante - Unidad.",
               "Descarta las palabras que describen exclusión o indiferencia."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "San Pablo compara a la Iglesia con un ______ que tiene muchas partes.",
         "respuesta": "CUERPO", "banco": ["CUERPO", "EJERCITO", "MURO"]},
    ],
    "reflexion": "¿Qué parte crees que cumples tú dentro de tu comunidad de fe?",
    "requisito": 1,
    "pistas": ["Piensa en la comparación que hace San Pablo de la Iglesia.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: soy parte importante de la Iglesia",
    "situacion": "Ya sabes que la Iglesia es como un cuerpo, y cada persona es un miembro importante.",
    "items": [
        {"texto": "¿Cómo puedes vivir sabiendo que eres importante para tu comunidad?",
         "opciones": ["Participando activamente en mi parroquia o catequesis",
                      "Cuidando mi relación con los demás miembros",
                      "Ofreciendo mi ayuda cuando se necesita",
                      "Pensando que lo que yo hago no importa"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes que valoran tu propio aporte.",
               "Descarta la única opción que piensa que no importa."],
    "feedback_ok": "¡Muy bien! Cada uno de nosotros es una parte importante de la Iglesia.",
})

# ==========================================================================
# ==========================================================================
# PC15 — Ser luz en el mundo   (Encuentro 15, Mateo 5,14-16 / Juan 8,12)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC15-C01 — Jesús, luz del mundo
# ==========================================================================
C = "PC15-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: Jesús, luz del mundo",
    "items": [
        {"texto": "Lo que Jesús dijo que él es para el mundo.", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
        {"texto": "Lugar al que Jesús vino a traer su luz.", "respuesta": "MUNDO", "banco": ["MUNDO", "CIELO", "DESIERTO"]},
        {"texto": "Lo que no camina quien sigue a Jesús.", "respuesta": "OSCURIDAD", "banco": ["OSCURIDAD", "LUZ", "CLARIDAD"]},
        {"texto": "Lo que debemos hacer con Jesús, luz del mundo.", "respuesta": "SEGUIR", "banco": ["SEGUIR", "IGNORAR", "OLVIDAR"]},
        {"texto": "Lo que recorremos guiados por la luz de Jesús.", "respuesta": "CAMINO", "banco": ["CAMINO", "MURO", "POZO"]},
        {"texto": "Lo que tiene quien sigue a Jesús, luz del mundo.", "respuesta": "VIDA", "banco": ["VIDA", "TUMBA", "TRISTEZA"]},
    ],
    "incluir": ["LUZ", "MUNDO"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús dijo que él era para el mundo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: Jesús, luz del mundo",
    "palabras": ["LUZ", "MUNDO", "OSCURIDAD", "SEGUIR", "CAMINO", "VIDA"],
    "incluir": ["OSCURIDAD", "SEGUIR"], "requisito": 5,
    "pistas": ["LUZ y VIDA son de las palabras más cortas: búscalas primero.",
               "OSCURIDAD es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Juan 8,12",
    "items": [
        {"texto": "Busca en tu Biblia Católica Juan 8,12 y completa: «Yo soy la luz del ______. El que me "
                  "sigue no camina en la oscuridad.»", "respuesta": "MUNDO",
         "banco": ["MUNDO", "CIELO", "DESIERTO"]},
        {"texto": "¿Qué pasa con quien sigue a Jesús, luz del mundo?", "abierta": True,
         "palabras_esperadas": ["OSCURIDAD", "LUZ", "CAMINO", "VIDA"],
         "respuestas_referencia": ["No camina en la oscuridad, sino que tiene la luz de la vida.",
                                    "Recibe la luz que ilumina su camino y le da vida.",
                                    "Deja de caminar en la oscuridad y sigue el camino de Jesús."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Juan en el índice de tu Biblia; el capítulo es el 8.",
               "El texto dice qué es Jesús para el mundo y qué pasa con quien lo sigue."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús dijo: «Yo soy la ______ del mundo.»", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
        {"texto": "Quien sigue a Jesús no camina en la ______.", "respuesta": "OSCURIDAD", "banco": ["OSCURIDAD", "LUZ", "CLARIDAD"]},
        {"texto": "Jesús nos guía por el buen ______ de la vida.", "respuesta": "CAMINO", "banco": ["CAMINO", "MURO", "POZO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús dijo que era para el mundo.",
               "La segunda respuesta es lo que evita quien lo sigue."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús dijo que él es la luz del mundo.", "respuesta": True},
        {"texto": "Quien sigue a Jesús camina siempre en la oscuridad.", "respuesta": False},
        {"texto": "Seguir a Jesús es seguir la luz de la vida.", "respuesta": True},
        {"texto": "A Jesús no le importa iluminar nuestro camino.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Jesús dijo que era para el mundo.",
               "Si una frase dice que quien sigue a Jesús camina en oscuridad, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué dijo Jesús que era para el mundo?",
         "opciones": ["La luz", "La oscuridad", "El silencio", "Nada"], "correcta": 0},
        {"texto": "¿Qué pasa con quien sigue a Jesús?",
         "opciones": ["No camina en la oscuridad", "Se pierde siempre", "No tiene ayuda", "Camina solo"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que dijo Jesús que era para el mundo.",
               "Recuerda lo que pasa con quien sigue su luz."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "LUZ", "definicion": "Lo que Jesús dijo que él es"},
        {"termino": "MUNDO", "definicion": "Lugar al que Jesús trae su luz"},
        {"termino": "OSCURIDAD", "definicion": "Lo que no camina quien sigue a Jesús"},
        {"termino": "SEGUIR", "definicion": "Lo que debemos hacer con Jesús"},
        {"termino": "CAMINO", "definicion": "Lo que recorremos guiados por su luz"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la frase de Jesús sobre ser luz del mundo.",
               "CAMINO es lo que recorremos, no lo que dijo Jesús que era."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: Jesús, luz del mundo",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Jesús dijo: «Yo soy la ______ del mundo.»",
         "opciones": ["luz", "sombra", "noche"], "correcta": 0},
        {"texto": "Quien sigue a Jesús no camina en la ______.",
         "opciones": ["oscuridad", "luz", "claridad"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que dijo Jesús que era para el mundo.",
               "Recuerda lo que evita quien sigue a Jesús."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús dijo: «Yo soy la ______ del mundo.»",
         "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
    ],
    "reflexion": "¿En qué momentos sientes que Jesús ilumina tu camino?",
    "requisito": 1,
    "pistas": ["Piensa en lo que dijo Jesús que era para el mundo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: sigo la luz de Jesús",
    "situacion": "Ya sabes que Jesús es la luz del mundo y quien lo sigue no camina en la oscuridad.",
    "items": [
        {"texto": "¿Cómo puedes dejar que la luz de Jesús guíe tu vida?",
         "opciones": ["Rezando para pedir su luz",
                      "Leyendo la Biblia para conocerlo mejor",
                      "Eligiendo el bien en mis decisiones",
                      "Prefiriendo caminar solo, sin su luz"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes que buscan la luz de Jesús.",
               "Descarta la única opción que prefiere caminar sin su luz."],
    "feedback_ok": "¡Muy bien! Así dejamos que la luz de Jesús guíe nuestra vida.",
})

# ==========================================================================
# PC15-C02 — Ustedes son la luz del mundo
# ==========================================================================
C = "PC15-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: ustedes son la luz del mundo",
    "items": [
        {"texto": "Lo que Jesús dice que somos nosotros también, sus discípulos.", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
        {"texto": "Lo que no se puede esconder si está sobre un monte.", "respuesta": "CIUDAD", "banco": ["CIUDAD", "CASA", "CUEVA"]},
        {"texto": "Lugar donde una ciudad no se puede esconder.", "respuesta": "MONTE", "banco": ["MONTE", "VALLE", "POZO"]},
        {"texto": "Lo que no se puede hacer con una luz verdadera.", "respuesta": "ESCONDER", "banco": ["ESCONDER", "MOSTRAR", "ENCENDER"]},
        {"texto": "Lugar donde estamos llamados a brillar como luz.", "respuesta": "MUNDO", "banco": ["MUNDO", "CIELO", "DESIERTO"]},
        {"texto": "Lo que hace la luz que Jesús nos pide ser.", "respuesta": "BRILLAR", "banco": ["BRILLAR", "APAGARSE", "ESCONDERSE"]},
    ],
    "incluir": ["LUZ", "BRILLAR"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús dice que somos sus discípulos.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: ustedes son la luz del mundo",
    "palabras": ["LUZ", "CIUDAD", "MONTE", "ESCONDER", "MUNDO", "BRILLAR"],
    "incluir": ["CIUDAD", "MONTE"], "requisito": 5,
    "pistas": ["LUZ y MONTE son de las palabras más cortas: búscalas primero.",
               "ESCONDER es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 5,14",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 5,14 y completa: «Ustedes son la luz del mundo. No se "
                  "puede esconder una ______ situada en lo alto de un monte.»", "respuesta": "CIUDAD",
         "banco": ["CIUDAD", "CASA", "CUEVA"]},
        {"texto": "¿Qué significa que nosotros somos «la luz del mundo»?", "abierta": True,
         "palabras_esperadas": ["BRILLAR", "EJEMPLO", "MOSTRAR", "BUENO"],
         "respuestas_referencia": ["Significa que debemos mostrar con el ejemplo el bien que llevamos dentro.",
                                    "Significa brillar con nuestras acciones, sin escondernos.",
                                    "Significa que nuestra vida de fe debe ser visible para los demás."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 5.",
               "El texto compara a los discípulos con una ciudad en lo alto de un monte."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús dice: «Ustedes son la ______ del mundo.»", "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
        {"texto": "No se puede esconder una ciudad situada en lo alto de un ______.", "respuesta": "MONTE", "banco": ["MONTE", "VALLE", "POZO"]},
        {"texto": "Ser luz significa ______ con nuestro ejemplo.", "respuesta": "BRILLAR", "banco": ["BRILLAR", "ESCONDERSE", "CALLAR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús dice que somos sus discípulos.",
               "La tercera respuesta es lo que hace la luz con su ejemplo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús dice que nosotros somos la luz del mundo.", "respuesta": True},
        {"texto": "Una ciudad en lo alto de un monte se puede esconder fácilmente.", "respuesta": False},
        {"texto": "Ser luz del mundo significa brillar con el ejemplo.", "respuesta": True},
        {"texto": "A Jesús no le importa que seamos luz para los demás.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Jesús dice que somos nosotros.",
               "Si una frase dice que una ciudad en un monte se esconde fácilmente, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué dice Jesús que somos nosotros?",
         "opciones": ["La luz del mundo", "La oscuridad del mundo", "Nada importante", "Un secreto"], "correcta": 0},
        {"texto": "¿Qué no se puede esconder, según el ejemplo de Jesús?",
         "opciones": ["Una ciudad en lo alto de un monte", "Una piedra pequeña", "Un secreto", "Una sombra"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús dice que somos.",
               "Recuerda el ejemplo de la ciudad en el monte."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "LUZ", "definicion": "Lo que Jesús dice que somos"},
        {"termino": "CIUDAD", "definicion": "Lo que no se puede esconder en un monte"},
        {"termino": "MONTE", "definicion": "Lugar donde está la ciudad del ejemplo"},
        {"termino": "ESCONDER", "definicion": "Lo que no se puede hacer con la luz verdadera"},
        {"termino": "BRILLAR", "definicion": "Lo que hace la luz que Jesús nos pide ser"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el ejemplo de la ciudad sobre el monte.",
               "BRILLAR es la acción de la luz, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: ser luz del mundo",
    "instruccion": "En 45 segundos, marca las palabras del ejemplo de Jesús sobre ser luz del mundo.",
    "tiempo_segundos": 45,
    "banco": ["LUZ", "BRILLAR", "CIUDAD", "MONTE", "ESCONDER", "SOMBRA"],
    "correctas": ["LUZ", "BRILLAR", "CIUDAD", "MONTE"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Luz - Brillar - Ciudad - Monte.",
               "Descarta las palabras que describen lo contrario de brillar."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús dice: «Ustedes son la ______ del mundo.»",
         "respuesta": "LUZ", "banco": ["LUZ", "SOMBRA", "NOCHE"]},
    ],
    "reflexion": "¿Cómo puedes ser luz para las personas que están cerca de ti?",
    "requisito": 1,
    "pistas": ["Piensa en lo que Jesús dice que somos.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: brillo como luz del mundo",
    "situacion": "Ya sabes que Jesús nos llama a ser luz del mundo, como una ciudad que no se puede esconder.",
    "items": [
        {"texto": "¿Cómo puedes brillar como luz en tu día a día?",
         "opciones": ["Tratando bien a mis compañeros",
                      "Ayudando a quien lo necesita",
                      "Mostrando alegría al vivir mi fe",
                      "Escondiendo que soy amigo de Jesús"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones que muestran la luz, no que la esconden.",
               "Descarta la única opción que esconde la amistad con Jesús."],
    "feedback_ok": "¡Muy bien! Así brillamos como luz del mundo, sin escondernos.",
})

# ==========================================================================
# PC15-C03 — Una lámpara no se esconde
# ==========================================================================
C = "PC15-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: una lámpara no se esconde",
    "items": [
        {"texto": "Objeto que se enciende para dar luz.", "respuesta": "LAMPARA", "banco": ["LAMPARA", "PIEDRA", "SOMBRA"]},
        {"texto": "Lugar donde se coloca la lámpara para que ilumine bien.", "respuesta": "CANDELERO", "banco": ["CANDELERO", "CAJON", "SOTANO"]},
        {"texto": "Lo que se hace con una lámpara antes de usarla.", "respuesta": "ENCENDER", "banco": ["ENCENDER", "APAGAR", "ROMPER"]},
        {"texto": "Como no debe estar una lámpara encendida, según Jesús.", "respuesta": "ESCONDIDA", "banco": ["ESCONDIDA", "VISIBLE", "ILUMINADA"]},
        {"texto": "Lo que hace una lámpara puesta en el candelero.", "respuesta": "ILUMINAR", "banco": ["ILUMINAR", "APAGARSE", "ESCONDERSE"]},
        {"texto": "Lugar que ilumina una lámpara bien colocada.", "respuesta": "CASA", "banco": ["CASA", "CAMPO", "DESIERTO"]},
    ],
    "incluir": ["LAMPARA", "ILUMINAR"], "requisito": 4,
    "pistas": ["Piensa en el objeto que se enciende para dar luz.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: una lámpara no se esconde",
    "palabras": ["LAMPARA", "CANDELERO", "ENCENDER", "ESCONDIDA", "ILUMINAR", "CASA"],
    "incluir": ["CANDELERO", "ENCENDER"], "requisito": 5,
    "pistas": ["CASA es la palabra más corta: búscala primero.",
               "CANDELERO es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 5,15",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 5,15 y completa: «Tampoco se enciende una lámpara para "
                  "ponerla debajo de un cajón, sino sobre el ______.»", "respuesta": "CANDELERO",
         "banco": ["CANDELERO", "SUELO", "TECHO"]},
        {"texto": "¿Por qué Jesús compara nuestra vida con una lámpara encendida?", "abierta": True,
         "palabras_esperadas": ["LUZ", "ILUMINAR", "EJEMPLO", "ESCONDER"],
         "respuestas_referencia": ["Porque nuestra fe debe iluminar a los demás, no quedar escondida.",
                                    "Porque, como la lámpara, nuestro ejemplo debe alumbrar a quienes nos rodean.",
                                    "Porque una fe escondida no ayuda a nadie, como una lámpara tapada."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 5.",
               "El texto dice dónde se coloca una lámpara para que alumbre bien."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Una lámpara se enciende para ______, no para esconderla.", "respuesta": "ILUMINAR", "banco": ["ILUMINAR", "APAGAR", "ESCONDER"]},
        {"texto": "La lámpara se coloca sobre el ______ para alumbrar toda la casa.", "respuesta": "CANDELERO", "banco": ["CANDELERO", "SUELO", "CAJON"]},
        {"texto": "Nuestra vida de fe no debe quedar ______, sino visible.", "respuesta": "ESCONDIDA", "banco": ["ESCONDIDA", "ILUMINADA", "VISIBLE"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en para qué se enciende una lámpara.",
               "La segunda respuesta es dónde se coloca para alumbrar bien."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Una lámpara se enciende para iluminar, no para esconderla.", "respuesta": True},
        {"texto": "Jesús dice que debemos esconder nuestra fe como una lámpara apagada.", "respuesta": False},
        {"texto": "La lámpara se coloca en el candelero para alumbrar toda la casa.", "respuesta": True},
        {"texto": "Nuestra vida de fe no debe mostrarse a los demás.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda para qué se enciende una lámpara.",
               "Si una frase dice que debemos esconder nuestra fe, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Para qué se enciende una lámpara, según Jesús?",
         "opciones": ["Para iluminar, no para esconderla", "Para esconderla", "Para apagarla enseguida", "Para nada"], "correcta": 0},
        {"texto": "¿Dónde se coloca la lámpara para alumbrar bien?",
         "opciones": ["Sobre el candelero", "Debajo de un cajón", "En la oscuridad", "En ningún lugar"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en para qué se enciende una lámpara.",
               "Recuerda dónde se coloca para alumbrar bien."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "LAMPARA", "definicion": "Objeto que se enciende para dar luz"},
        {"termino": "CANDELERO", "definicion": "Lugar donde se coloca para iluminar bien"},
        {"termino": "ENCENDER", "definicion": "Lo que se hace con la lámpara antes de usarla"},
        {"termino": "ILUMINAR", "definicion": "Lo que hace una lámpara bien colocada"},
        {"termino": "CASA", "definicion": "Lugar que ilumina una lámpara encendida"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la comparación de Jesús sobre la lámpara.",
               "CASA es el lugar que recibe la luz, no la lámpara misma."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: la lámpara encendida",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Una lámpara se enciende para ______, no para esconderla.",
         "opciones": ["iluminar", "apagar", "esconder"], "correcta": 0},
        {"texto": "La lámpara se coloca sobre el ______ para alumbrar toda la casa.",
         "opciones": ["candelero", "suelo", "cajón"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en para qué se enciende una lámpara.",
               "Recuerda dónde se coloca para alumbrar bien."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Una lámpara se enciende para ______, no para esconderla.",
         "respuesta": "ILUMINAR", "banco": ["ILUMINAR", "APAGAR", "ESCONDER"]},
    ],
    "reflexion": "¿Qué áreas de tu vida podrías 'iluminar' más con tu ejemplo de fe?",
    "requisito": 1,
    "pistas": ["Piensa en para qué se enciende una lámpara.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: no escondo mi fe",
    "situacion": "Ya sabes que una lámpara se enciende para iluminar, no para quedar escondida.",
    "items": [
        {"texto": "¿Cómo puedes evitar 'esconder' tu fe, como esa lámpara?",
         "opciones": ["Hablando de Jesús con naturalidad",
                      "Viviendo mis valores sin miedo a que me vean",
                      "Participando abiertamente en mi comunidad de fe",
                      "Ocultando siempre que soy creyente"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes que muestran la fe, no que la esconden.",
               "Descarta la única opción que oculta siempre la fe."],
    "feedback_ok": "¡Muy bien! Así dejamos que nuestra fe ilumine, sin esconderla.",
})

# ==========================================================================
# PC15-C04 — Que brille la luz de las buenas obras
# ==========================================================================
C = "PC15-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la luz de las buenas obras",
    "items": [
        {"texto": "Acciones concretas que muestran nuestra fe a los demás.", "respuesta": "OBRAS", "banco": ["OBRAS", "EXCUSAS", "QUEJAS"]},
        {"texto": "Lo que Jesús pide que haga nuestra luz delante de los hombres.", "respuesta": "BRILLE", "banco": ["BRILLE", "APAGUE", "ESCONDA"]},
        {"texto": "Lo que hacen los demás al ver nuestras buenas obras, según Jesús.", "respuesta": "GLORIFICAR", "banco": ["GLORIFICAR", "IGNORAR", "OLVIDAR"]},
        {"texto": "A quien se glorifica cuando hacemos el bien, según Mateo 5,16.", "respuesta": "PADRE", "banco": ["PADRE", "VECINO", "MAESTRO"]},
        {"texto": "Lo que damos a otros con nuestras buenas acciones.", "respuesta": "EJEMPLO", "banco": ["EJEMPLO", "EXCUSA", "QUEJA"]},
        {"texto": "Tipo de obras que Jesús nos pide hacer brillar.", "respuesta": "BUENAS", "banco": ["BUENAS", "MALAS", "INUTILES"]},
    ],
    "incluir": ["OBRAS", "BRILLE"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús pide que hagamos brillar delante de los demás.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la luz de las buenas obras",
    "palabras": ["OBRAS", "BRILLE", "GLORIFICAR", "PADRE", "EJEMPLO", "BUENAS"],
    "incluir": ["GLORIFICAR", "PADRE"], "requisito": 5,
    "pistas": ["OBRAS y PADRE son de las palabras más cortas: búscalas primero.",
               "GLORIFICAR es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 5,16",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 5,16 y completa: «______ así su luz delante de los "
                  "hombres, para que vean sus buenas obras.»", "respuesta": "BRILLE",
         "banco": ["BRILLE", "APAGUE", "ESCONDA"]},
        {"texto": "¿Qué pasa cuando los demás ven nuestras buenas obras, según Jesús?", "abierta": True,
         "palabras_esperadas": ["GLORIFICAN", "PADRE", "DIOS", "EJEMPLO"],
         "respuestas_referencia": ["Glorifican a nuestro Padre que está en los cielos.",
                                    "Reconocen el bien y dan gracias a Dios por él.",
                                    "Ven en nosotros un ejemplo que lleva a glorificar al Padre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 5.",
               "El texto pide que nuestra luz brille para que vean nuestras buenas obras."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús pide que nuestra luz ______ delante de los demás.", "respuesta": "BRILLE", "banco": ["BRILLE", "APAGUE", "ESCONDA"]},
        {"texto": "Cuando hacemos el bien, glorificamos a nuestro ______.", "respuesta": "PADRE", "banco": ["PADRE", "VECINO", "MAESTRO"]},
        {"texto": "Nuestras buenas ______ son un ejemplo para los demás.", "respuesta": "OBRAS", "banco": ["OBRAS", "EXCUSAS", "QUEJAS"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que pide Jesús que haga nuestra luz.",
               "La segunda respuesta es a quien glorificamos con el bien."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús pide que nuestra luz brille delante de los demás.", "respuesta": True},
        {"texto": "Nuestras buenas obras no tienen ningún efecto en los demás.", "respuesta": False},
        {"texto": "Cuando hacemos el bien, glorificamos a Dios Padre.", "respuesta": True},
        {"texto": "A Jesús no le importa que hagamos buenas obras.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que Jesús pide que haga nuestra luz.",
               "Si una frase dice que nuestras obras no tienen efecto, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué pide Jesús que hagamos con nuestra luz?",
         "opciones": ["Que brille delante de los demás", "Que se esconda", "Que se apague", "Nada"], "correcta": 0},
        {"texto": "¿A quién glorificamos cuando hacemos el bien?",
         "opciones": ["Al Padre", "A nadie", "A nosotros mismos solamente", "A ningún ser"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que pide Jesús que hagamos con nuestra luz.",
               "Recuerda a quién glorificamos al hacer el bien."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "OBRAS", "definicion": "Acciones que muestran nuestra fe"},
        {"termino": "BRILLE", "definicion": "Lo que Jesús pide que haga nuestra luz"},
        {"termino": "GLORIFICAR", "definicion": "Lo que hacen los demás al ver el bien"},
        {"termino": "PADRE", "definicion": "A quien se glorifica con nuestras buenas obras"},
        {"termino": "EJEMPLO", "definicion": "Lo que damos con nuestras acciones"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el mensaje de Mateo 5,16 sobre las buenas obras.",
               "PADRE es a quien se glorifica, no la acción misma."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: dejar brillar la luz",
    "instruccion": "En 45 segundos, marca las palabras relacionadas con dejar brillar nuestra luz.",
    "tiempo_segundos": 45,
    "banco": ["OBRAS", "BRILLE", "PADRE", "GLORIFICAR", "ESCONDER", "APAGAR"],
    "correctas": ["OBRAS", "BRILLE", "PADRE", "GLORIFICAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Obras - Brille - Padre - Glorificar.",
               "Descarta las palabras que describen lo contrario de dejar brillar la luz."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús pide que nuestra luz ______ delante de los demás.",
         "respuesta": "BRILLE", "banco": ["BRILLE", "APAGUE", "ESCONDA"]},
    ],
    "reflexion": "¿Qué buena obra te gustaría hacer brillar esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en lo que pide Jesús que haga nuestra luz.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: hago brillar mi luz",
    "situacion": "Ya sabes que Jesús pide que nuestras buenas obras brillen, para glorificar al Padre.",
    "items": [
        {"texto": "¿Qué buena obra puedes hacer brillar esta semana?",
         "opciones": ["Ayudar a alguien sin que me lo pidan",
                      "Compartir lo que tengo con otros",
                      "Tratar con amor a mi familia",
                      "Guardar mis buenas acciones en secreto siempre"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones visibles, que sirven de ejemplo.",
               "Descarta la única opción que esconde siempre las buenas acciones."],
    "feedback_ok": "¡Muy bien! Así dejamos brillar nuestra luz, glorificando a Dios.",
})

# ==========================================================================
# PC15-C05 — Vencer la oscuridad con el bien
# ==========================================================================
C = "PC15-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: vencer la oscuridad con el bien",
    "items": [
        {"texto": "Lo que no debemos dejar que nos venza.", "respuesta": "MAL", "banco": ["MAL", "BIEN", "AMOR"]},
        {"texto": "Lo que San Pablo dice que debe vencer al mal.", "respuesta": "BIEN", "banco": ["BIEN", "ODIO", "MIEDO"]},
        {"texto": "Lo que hacemos con el mal cuando respondemos con el bien.", "respuesta": "VENCER", "banco": ["VENCER", "PERDER", "IGNORAR"]},
        {"texto": "Sentimiento que no vence al mal, sino que lo alimenta.", "respuesta": "ODIO", "banco": ["ODIO", "AMOR", "PAZ"]},
        {"texto": "Actitud que ayuda a vencer el mal con el bien.", "respuesta": "BONDAD", "banco": ["BONDAD", "EGOISMO", "ENVIDIA"]},
        {"texto": "Acción que vence al odio con amor.", "respuesta": "PERDON", "banco": ["PERDON", "RENCOR", "VENGANZA"]},
    ],
    "incluir": ["MAL", "BIEN"], "requisito": 4,
    "pistas": ["Piensa en lo que San Pablo dice que debe vencer al mal.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: vencer la oscuridad con el bien",
    "palabras": ["MAL", "BIEN", "VENCER", "ODIO", "BONDAD", "PERDON"],
    "incluir": ["VENCER", "BONDAD"], "requisito": 5,
    "pistas": ["MAL, BIEN y ODIO son de las palabras más cortas: búscalas primero.",
               "BONDAD es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Romanos 12,21",
    "items": [
        {"texto": "Busca en tu Biblia Católica Romanos 12,21 y completa: «No te dejes vencer por el mal; "
                  "al contrario, vence al mal con el ______.»", "respuesta": "BIEN",
         "banco": ["BIEN", "MIEDO", "SILENCIO"]},
        {"texto": "¿Cómo podemos vencer el mal, según San Pablo?", "abierta": True,
         "palabras_esperadas": ["BIEN", "BONDAD", "PERDON", "AMOR"],
         "respuestas_referencia": ["Respondiendo con bondad y amor, en lugar de con más mal.",
                                    "Perdonando y actuando con bien, aunque nos traten mal.",
                                    "Eligiendo siempre el bien, sin dejarnos llevar por el odio."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la carta a los Romanos en el índice de tu Biblia; el capítulo es el 12.",
               "El texto dice con qué debemos vencer al mal."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "San Pablo dice que no debemos dejarnos vencer por el ______.", "respuesta": "MAL", "banco": ["MAL", "BIEN", "AMOR"]},
        {"texto": "Debemos vencer al mal con el ______.", "respuesta": "BIEN", "banco": ["BIEN", "ODIO", "MIEDO"]},
        {"texto": "El ______ es una forma de vencer el mal con amor.", "respuesta": "PERDON", "banco": ["PERDON", "ODIO", "RENCOR"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que no debemos dejar que nos venza.",
               "La tercera respuesta es una acción de amor frente al daño recibido."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "San Pablo dice que debemos vencer al mal con el bien.", "respuesta": True},
        {"texto": "Responder al mal con más mal es la mejor solución.", "respuesta": False},
        {"texto": "El perdón es una forma de vencer el mal con amor.", "respuesta": True},
        {"texto": "El odio ayuda a vencer el mal.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda con qué debemos vencer el mal, según San Pablo.",
               "Si una frase dice que el odio ayuda a vencer el mal, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con qué debemos vencer al mal, según San Pablo?",
         "opciones": ["Con el bien", "Con más mal", "Con odio", "Con indiferencia"], "correcta": 0},
        {"texto": "¿Qué actitud nos ayuda a vencer el mal?",
         "opciones": ["La bondad y el perdón", "El rencor", "La venganza", "El silencio indiferente"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con qué debemos vencer el mal.",
               "Recuerda qué actitudes ayudan a vencerlo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "MAL", "definicion": "Lo que no debe vencernos"},
        {"termino": "BIEN", "definicion": "Lo que debe vencer al mal"},
        {"termino": "VENCER", "definicion": "Lo que hacemos al responder con el bien"},
        {"termino": "BONDAD", "definicion": "Actitud que ayuda a vencer el mal"},
        {"termino": "PERDON", "definicion": "Acción que vence al odio con amor"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el consejo de San Pablo sobre el mal y el bien.",
               "PERDON es una acción concreta de amor frente al daño recibido."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: vencer el mal con el bien",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "No te dejes vencer por el mal; vence al mal con el ______.",
         "opciones": ["bien", "odio", "miedo"], "correcta": 0},
        {"texto": "El ______ es una forma de vencer el mal con amor.",
         "opciones": ["perdón", "rencor", "odio"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con qué debemos vencer el mal.",
               "Recuerda qué acción vence al odio con amor."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Debemos vencer al mal con el ______.",
         "respuesta": "BIEN", "banco": ["BIEN", "ODIO", "MIEDO"]},
    ],
    "reflexion": "¿En qué situación podrías responder al mal con el bien esta semana?",
    "requisito": 1,
    "pistas": ["Piensa en con qué debemos vencer el mal.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: venzo el mal con el bien",
    "situacion": "Ya sabes que San Pablo nos pide vencer el mal con el bien, no con más mal.",
    "items": [
        {"texto": "¿Cómo puedes vencer el mal con el bien en tu vida diaria?",
         "opciones": ["Perdonando a quien me hace daño",
                      "Respondiendo con calma en vez de con enojo",
                      "Tratando con bondad aunque me traten mal",
                      "Devolviendo siempre mal por mal"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de bondad y perdón.",
               "Descarta la única opción que responde siempre con más mal."],
    "feedback_ok": "¡Muy bien! Así se vence el mal con el bien, como nos enseña San Pablo.",
})

# ==========================================================================
# PC15-C06 — Caminar en la luz
# ==========================================================================
C = "PC15-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: caminar en la luz",
    "items": [
        {"texto": "Lo que hacemos en la luz cuando vivimos como hijos de Dios.", "respuesta": "CAMINAR", "banco": ["CAMINAR", "DETENERSE", "ALEJARSE"]},
        {"texto": "Lo que tenemos unos con otros cuando caminamos en la luz.", "respuesta": "COMUNION", "banco": ["COMUNION", "DISTANCIA", "DIVISION"]},
        {"texto": "Cómo nos llama la fe a tratarnos unos a otros.", "respuesta": "HERMANOS", "banco": ["HERMANOS", "EXTRAÑOS", "ENEMIGOS"]},
        {"texto": "Lo que la sangre de Jesús nos purifica cuando caminamos en la luz.", "respuesta": "PECADO", "banco": ["PECADO", "AMOR", "BIEN"]},
        {"texto": "Lo que hace la sangre de Jesús con nuestros pecados.", "respuesta": "PURIFICA", "banco": ["PURIFICA", "ENSUCIA", "OLVIDA"]},
        {"texto": "Lo que representa vivir cerca de Dios, según San Juan.", "respuesta": "LUZ", "banco": ["LUZ", "OSCURIDAD", "SOMBRA"]},
    ],
    "incluir": ["CAMINAR", "LUZ"], "requisito": 4,
    "pistas": ["Piensa en lo que hacemos en la luz al vivir como hijos de Dios.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: caminar en la luz",
    "palabras": ["CAMINAR", "COMUNION", "HERMANOS", "PECADO", "PURIFICA", "LUZ"],
    "incluir": ["COMUNION", "HERMANOS"], "requisito": 5,
    "pistas": ["LUZ es la palabra más corta: búscala primero.",
               "PURIFICA es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: 1 Juan 1,7",
    "items": [
        {"texto": "Busca en tu Biblia Católica 1 Juan 1,7 y completa: «Si caminamos en la ______, como él "
                  "está en la luz, estamos en comunión unos con otros.»", "respuesta": "LUZ",
         "banco": ["LUZ", "OSCURIDAD", "SOMBRA"]},
        {"texto": "¿Qué significa «caminar en la luz»?", "abierta": True,
         "palabras_esperadas": ["DIOS", "BIEN", "COMUNION", "VERDAD"],
         "respuestas_referencia": ["Significa vivir cerca de Dios, eligiendo siempre el bien.",
                                    "Significa vivir en comunión con los demás, siguiendo la verdad.",
                                    "Significa vivir como hijos de Dios, en unidad con nuestros hermanos."]},
    ],
    "requisito": 2,
    "pistas": ["Busca la primera carta de Juan en el índice de tu Biblia; el capítulo es el 1.",
               "El texto dice qué logramos cuando caminamos en la luz."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Si caminamos en la luz, estamos en ______ unos con otros.", "respuesta": "COMUNION", "banco": ["COMUNION", "DISTANCIA", "DIVISION"]},
        {"texto": "Caminar en la luz es vivir cerca de ______.", "respuesta": "DIOS", "banco": ["DIOS", "NADIE", "TODOS"]},
        {"texto": "La sangre de Jesús nos ______ de todo pecado.", "respuesta": "PURIFICA", "banco": ["PURIFICA", "ENSUCIA", "OLVIDA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que logramos al caminar en la luz.",
               "La tercera respuesta es lo que hace la sangre de Jesús con el pecado."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Caminar en la luz significa vivir en comunión con los demás.", "respuesta": True},
        {"texto": "Caminar en la oscuridad nos acerca más a Dios.", "respuesta": False},
        {"texto": "La sangre de Jesús nos purifica de todo pecado.", "respuesta": True},
        {"texto": "Caminar en la luz no tiene relación con nuestra vida diaria.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué logramos al caminar en la luz.",
               "Si una frase dice que la oscuridad nos acerca a Dios, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué logramos al caminar en la luz, según San Juan?",
         "opciones": ["Estar en comunión unos con otros", "Alejarnos de todos", "Vivir en oscuridad", "Nada"], "correcta": 0},
        {"texto": "¿Qué hace la sangre de Jesús con nuestros pecados?",
         "opciones": ["Nos purifica de ellos", "Los aumenta", "No hace nada", "Los esconde"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que logramos al caminar en la luz.",
               "Recuerda lo que hace la sangre de Jesús con el pecado."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CAMINAR", "definicion": "Lo que hacemos en la luz"},
        {"termino": "COMUNION", "definicion": "Lo que tenemos unos con otros en la luz"},
        {"termino": "HERMANOS", "definicion": "Cómo nos llama la fe a tratarnos"},
        {"termino": "PECADO", "definicion": "Lo que la sangre de Jesús purifica"},
        {"termino": "LUZ", "definicion": "Lo que representa vivir cerca de Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el mensaje de 1 Juan 1,7 sobre caminar en la luz.",
               "PECADO es lo que se purifica, no lo que se vive."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: caminar en la luz",
    "instruccion": "En 45 segundos, marca las palabras que describen caminar en la luz de Dios.",
    "tiempo_segundos": 45,
    "banco": ["CAMINAR", "LUZ", "COMUNION", "HERMANOS", "OSCURIDAD", "DIVISION"],
    "correctas": ["CAMINAR", "LUZ", "COMUNION", "HERMANOS"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Caminar - Luz - Comunión - Hermanos.",
               "Descarta las palabras que describen oscuridad o división."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Si caminamos en la luz, estamos en ______ unos con otros.",
         "respuesta": "COMUNION", "banco": ["COMUNION", "DISTANCIA", "DIVISION"]},
    ],
    "reflexion": "¿Qué significa para ti caminar en la luz de Dios cada día?",
    "requisito": 1,
    "pistas": ["Piensa en lo que logramos al caminar en la luz.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: camino en la luz de Dios",
    "situacion": "Ya sabes que caminar en la luz nos une en comunión, como hermanos.",
    "items": [
        {"texto": "¿Cómo puedes caminar en la luz esta semana?",
         "opciones": ["Viviendo en paz con mi familia y amigos",
                      "Pidiendo perdón cuando me equivoco",
                      "Eligiendo siempre el bien en mis decisiones",
                      "Prefiriendo alejarme de todos"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de comunión, no de alejamiento.",
               "Descarta la única opción que se aleja de todos."],
    "feedback_ok": "¡Muy bien! Así caminamos en la luz, en comunión con los demás.",
})

# ==========================================================================
# ==========================================================================
# PC16 — Celebración final: envío misionero   (Encuentro 16, Hechos 1,8-11 / Lucas 24,50-53)
# ==========================================================================
# ==========================================================================

# ==========================================================================
# PC16-C01 — Recordamos nuestro camino de fe
# ==========================================================================
C = "PC16-C01"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: recordamos nuestro camino",
    "items": [
        {"texto": "Lo que hemos recorrido juntos durante toda la catequesis.", "respuesta": "CAMINO", "banco": ["CAMINO", "MURO", "POZO"]},
        {"texto": "Lo que hacemos al mirar hacia atrás y dar gracias por lo vivido.", "respuesta": "RECORDAR", "banco": ["RECORDAR", "OLVIDAR", "IGNORAR"]},
        {"texto": "El relato de todo lo que hemos aprendido y vivido con Dios.", "respuesta": "HISTORIA", "banco": ["HISTORIA", "SILENCIO", "DUDA"]},
        {"texto": "Lo que ha ido creciendo en nosotros encuentro tras encuentro.", "respuesta": "FE", "banco": ["FE", "DUDA", "DISTANCIA"]},
        {"texto": "Lo que hace nuestra fe cuando la cuidamos y la vivimos.", "respuesta": "CRECER", "banco": ["CRECER", "APAGARSE", "DETENERSE"]},
        {"texto": "Sentimiento que tenemos al recordar el camino recorrido con Dios.", "respuesta": "GRATITUD", "banco": ["GRATITUD", "INDIFERENCIA", "TRISTEZA"]},
    ],
    "incluir": ["CAMINO", "FE"], "requisito": 4,
    "pistas": ["Piensa en todo lo que hemos recorrido en la catequesis.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: recordamos nuestro camino",
    "palabras": ["CAMINO", "RECORDAR", "HISTORIA", "FE", "CRECER", "GRATITUD"],
    "incluir": ["RECORDAR", "GRATITUD"], "requisito": 5,
    "pistas": ["FE es la palabra más corta: búscala primero.",
               "GRATITUD es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Deuteronomio 8,2",
    "items": [
        {"texto": "Busca en tu Biblia Católica Deuteronomio 8,2 y completa: «Acuérdate de todo el ______ "
                  "que el Señor tu Dios te ha hecho recorrer.»", "respuesta": "CAMINO",
         "banco": ["CAMINO", "DESIERTO", "TIEMPO"]},
        {"texto": "¿Qué recuerdas de tu camino de fe en estos encuentros?", "abierta": True,
         "palabras_esperadas": ["APRENDI", "CRECI", "JESUS", "DIOS"],
         "respuestas_referencia": ["Recuerdo todo lo que aprendí sobre Jesús y cómo fue creciendo mi fe.",
                                    "Recuerdo momentos de oración, celebración y aprendizaje sobre Dios.",
                                    "Recuerdo cómo fui conociendo más a Jesús encuentro tras encuentro."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro del Deuteronomio en el índice de tu Biblia; el capítulo es el 8.",
               "El texto invita a recordar el camino que Dios nos ha hecho recorrer."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Hemos recorrido un ______ de fe durante toda la catequesis.", "respuesta": "CAMINO", "banco": ["CAMINO", "DESIERTO", "SILENCIO"]},
        {"texto": "Mirar hacia atrás con gratitud nos ayuda a ______ el camino recorrido.", "respuesta": "RECORDAR", "banco": ["RECORDAR", "OLVIDAR", "IGNORAR"]},
        {"texto": "Nuestra ______ ha ido creciendo encuentro tras encuentro.", "respuesta": "FE", "banco": ["FE", "DUDA", "DISTANCIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hemos recorrido en la catequesis.",
               "La segunda respuesta es lo que hacemos al mirar hacia atrás con gratitud."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Hemos recorrido un camino de fe durante toda la catequesis.", "respuesta": True},
        {"texto": "No tiene sentido recordar lo que hemos aprendido con Dios.", "respuesta": False},
        {"texto": "Nuestra fe puede crecer si la cuidamos y la vivimos.", "respuesta": True},
        {"texto": "Dar gracias por el camino recorrido no tiene ningún valor.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda todo lo que hemos vivido en la catequesis.",
               "Si una frase dice que no tiene sentido recordar, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hemos recorrido durante toda la catequesis?",
         "opciones": ["Un camino de fe", "Nada importante", "Un camino sin sentido", "Un camino solitario"], "correcta": 0},
        {"texto": "¿Qué sentimos al recordar el camino recorrido con Dios?",
         "opciones": ["Gratitud", "Indiferencia", "Aburrimiento", "Tristeza sin razón"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hemos recorrido en estos encuentros.",
               "Recuerda qué sentimos al mirar hacia atrás con fe."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "CAMINO", "definicion": "Lo que hemos recorrido en la catequesis"},
        {"termino": "RECORDAR", "definicion": "Lo que hacemos al mirar hacia atrás con gratitud"},
        {"termino": "HISTORIA", "definicion": "Relato de lo vivido con Dios"},
        {"termino": "FE", "definicion": "Lo que ha ido creciendo en nosotros"},
        {"termino": "GRATITUD", "definicion": "Lo que sentimos al recordar el camino"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en todo el camino recorrido en la catequesis.",
               "GRATITUD es un sentimiento, no una acción."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: nuestro camino de fe",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Hemos recorrido un ______ de fe en la catequesis.",
         "opciones": ["camino", "desierto", "silencio"], "correcta": 0},
        {"texto": "Recordar el camino con gratitud nos llena de ______.",
         "opciones": ["alegría", "tristeza", "indiferencia"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hemos recorrido en la catequesis.",
               "Recuerda qué sentimos al mirar hacia atrás con fe."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Hemos recorrido un ______ de fe durante toda la catequesis.",
         "respuesta": "CAMINO", "banco": ["CAMINO", "DESIERTO", "SILENCIO"]},
    ],
    "reflexion": "¿Cuál ha sido el encuentro que más recuerdas de todo este camino?",
    "requisito": 1,
    "pistas": ["Piensa en lo que hemos recorrido en la catequesis.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: agradezco mi camino de fe",
    "situacion": "Ya sabes que has recorrido un largo camino de fe durante toda la catequesis.",
    "items": [
        {"texto": "¿Cómo puedes agradecer todo lo que has aprendido en este camino?",
         "opciones": ["Dando gracias a Dios en oración",
                      "Compartiendo lo aprendido con mi familia",
                      "Recordando los momentos más importantes",
                      "Olvidando todo lo vivido apenas termine"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de gratitud, no de olvido.",
               "Descarta la única opción que olvida todo lo vivido."],
    "feedback_ok": "¡Muy bien! Así se agradece el camino de fe recorrido junto a Dios.",
})

# ==========================================================================
# PC16-C02 — La Ascensión: Jesús vuelve al Padre
# ==========================================================================
C = "PC16-C02"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la Ascensión",
    "items": [
        {"texto": "Momento en que Jesús subió al cielo junto al Padre.", "respuesta": "ASCENSION", "banco": ["ASCENSION", "TRISTEZA", "DUDA"]},
        {"texto": "Lo que Jesús dio a sus discípulos antes de subir al cielo.", "respuesta": "BENDICION", "banco": ["BENDICION", "CASTIGO", "SILENCIO"]},
        {"texto": "Lugar al que Jesús subió después de bendecir a sus discípulos.", "respuesta": "CIELO", "banco": ["CIELO", "DESIERTO", "MONTE"]},
        {"texto": "Lo que ocurrió con Jesús mientras los bendecía.", "respuesta": "ELEVADO", "banco": ["ELEVADO", "ESCONDIDO", "DORMIDO"]},
        {"texto": "Momento en que Jesús se separó de sus discípulos para volver al Padre.", "respuesta": "DESPEDIDA", "banco": ["DESPEDIDA", "ENCUENTRO", "FIESTA"]},
        {"texto": "A quien vuelve Jesús en la Ascensión.", "respuesta": "PADRE", "banco": ["PADRE", "AMIGO", "VECINO"]},
    ],
    "incluir": ["ASCENSION", "CIELO"], "requisito": 4,
    "pistas": ["Piensa en el momento en que Jesús subió al cielo.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la Ascensión",
    "palabras": ["ASCENSION", "BENDICION", "CIELO", "ELEVADO", "DESPEDIDA", "PADRE"],
    "incluir": ["BENDICION", "PADRE"], "requisito": 5,
    "pistas": ["CIELO y PADRE son de las palabras más cortas: búscalas primero.",
               "ASCENSION es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 24,50-51",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 24,50-51 y completa: «Los llevó hasta Betania y, "
                  "levantando las manos, los ______.»", "respuesta": "BENDIJO",
         "banco": ["BENDIJO", "ABANDONO", "OLVIDO"]},
        {"texto": "¿Qué hizo Jesús antes de subir al cielo?", "abierta": True,
         "palabras_esperadas": ["BENDIJO", "DISCIPULOS", "MANOS", "CIELO"],
         "respuestas_referencia": ["Bendijo a sus discípulos, levantando las manos sobre ellos.",
                                    "Los bendijo y luego fue elevado al cielo delante de ellos.",
                                    "Los reunió, los bendijo y se despidió antes de volver al Padre."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 24.",
               "El texto cuenta lo último que hizo Jesús con sus discípulos antes de subir al cielo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús ______ a sus discípulos antes de subir al cielo.", "respuesta": "BENDIJO", "banco": ["BENDIJO", "ABANDONO", "OLVIDO"]},
        {"texto": "Mientras los bendecía, Jesús fue ______ al cielo.", "respuesta": "ELEVADO", "banco": ["ELEVADO", "ESCONDIDO", "DORMIDO"]},
        {"texto": "En la Ascensión, Jesús vuelve junto a su ______.", "respuesta": "PADRE", "banco": ["PADRE", "AMIGO", "VECINO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que Jesús hizo antes de subir al cielo.",
               "La tercera respuesta es a quien vuelve Jesús."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús bendijo a sus discípulos antes de subir al cielo.", "respuesta": True},
        {"texto": "Jesús abandonó a sus discípulos sin decir nada.", "respuesta": False},
        {"texto": "En la Ascensión, Jesús vuelve junto al Padre.", "respuesta": True},
        {"texto": "La Ascensión no tiene ninguna importancia para nuestra fe.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda lo que hizo Jesús antes de subir al cielo.",
               "Si una frase dice que Jesús abandonó a sus discípulos sin decir nada, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué hizo Jesús antes de subir al cielo?",
         "opciones": ["Bendijo a sus discípulos", "Los abandonó sin decir nada", "Se enojó con ellos", "Los ignoró"], "correcta": 0},
        {"texto": "¿A quién vuelve Jesús en la Ascensión?",
         "opciones": ["Al Padre", "A nadie", "A un lugar desconocido", "A la tierra otra vez enseguida"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que hizo Jesús antes de subir al cielo.",
               "Recuerda a quién vuelve Jesús en la Ascensión."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ASCENSION", "definicion": "Momento en que Jesús sube al cielo"},
        {"termino": "BENDICION", "definicion": "Lo que Jesús dio a sus discípulos"},
        {"termino": "CIELO", "definicion": "Lugar al que Jesús subió"},
        {"termino": "ELEVADO", "definicion": "Lo que ocurrió con Jesús al bendecirlos"},
        {"termino": "PADRE", "definicion": "A quien vuelve Jesús"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la escena de la Ascensión de Jesús.",
               "PADRE es a quien vuelve Jesús, no un lugar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: la Ascensión de Jesús",
    "instruccion": "En 45 segundos, marca las palabras que describen la Ascensión de Jesús.",
    "tiempo_segundos": 45,
    "banco": ["ASCENSION", "BENDICION", "CIELO", "PADRE", "ABANDONO", "OLVIDO"],
    "correctas": ["ASCENSION", "BENDICION", "CIELO", "PADRE"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Ascensión - Bendición - Cielo - Padre.",
               "Descarta las palabras que describen abandono u olvido."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús ______ a sus discípulos antes de subir al cielo.",
         "respuesta": "BENDIJO", "banco": ["BENDIJO", "ABANDONO", "OLVIDO"]},
    ],
    "reflexion": "¿Qué sientes al saber que Jesús bendijo a sus discípulos antes de irse?",
    "requisito": 1,
    "pistas": ["Piensa en lo que hizo Jesús antes de subir al cielo.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo la bendición de Jesús",
    "situacion": "Ya sabes que Jesús bendijo a sus discípulos antes de subir al cielo junto al Padre.",
    "items": [
        {"texto": "¿Cómo puedes vivir hoy la bendición que Jesús nos dejó?",
         "opciones": ["Confiando en que Jesús está siempre con nosotros",
                      "Viviendo agradecido por su bendición",
                      "Compartiendo esa bendición con los demás",
                      "Pensando que Jesús ya no tiene nada que ver con nosotros"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de confianza y gratitud.",
               "Descarta la única opción que aleja a Jesús de nuestra vida."],
    "feedback_ok": "¡Muy bien! Jesús nos dejó su bendición antes de volver al Padre.",
})

# ==========================================================================
# PC16-C03 — La alegría de la fe recibida
# ==========================================================================
C = "PC16-C03"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: la alegría de la fe",
    "items": [
        {"texto": "Lo que sintieron los discípulos después de ver a Jesús subir al cielo.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Ciudad a la que regresaron los discípulos con gran alegría.", "respuesta": "JERUSALEN", "banco": ["JERUSALEN", "BELEN", "NAZARET"]},
        {"texto": "Lo que hicieron los discípulos antes de volver a Jerusalén.", "respuesta": "ADORAR", "banco": ["ADORAR", "IGNORAR", "OLVIDAR"]},
        {"texto": "Lo que los discípulos daban continuamente a Dios en el templo.", "respuesta": "ALABANZA", "banco": ["ALABANZA", "QUEJA", "SILENCIO"]},
        {"texto": "Lugar donde los discípulos alababan a Dios continuamente.", "respuesta": "TEMPLO", "banco": ["TEMPLO", "DESIERTO", "CAMINO"]},
        {"texto": "Sentimiento profundo de alegría por la fe recibida.", "respuesta": "GOZO", "banco": ["GOZO", "MIEDO", "DUDA"]},
    ],
    "incluir": ["ALEGRIA", "TEMPLO"], "requisito": 4,
    "pistas": ["Piensa en lo que sintieron los discípulos después de la Ascensión.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: la alegría de la fe",
    "palabras": ["ALEGRIA", "JERUSALEN", "ADORAR", "ALABANZA", "TEMPLO", "GOZO"],
    "incluir": ["JERUSALEN", "ALABANZA"], "requisito": 5,
    "pistas": ["GOZO es la palabra más corta: búscala primero.",
               "JERUSALEN es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Lucas 24,52-53",
    "items": [
        {"texto": "Busca en tu Biblia Católica Lucas 24,52-53 y completa: «Ellos, después de adorarlo, "
                  "volvieron a Jerusalén con gran ______.»", "respuesta": "ALEGRIA",
         "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "¿Por qué volvieron los discípulos a Jerusalén con alegría?", "abierta": True,
         "palabras_esperadas": ["JESUS", "BENDICION", "ESPERANZA", "FE"],
         "respuestas_referencia": ["Porque habían recibido la bendición de Jesús y la esperanza de su promesa.",
                                    "Porque sabían que Jesús estaría siempre con ellos.",
                                    "Porque su fe en Jesús les llenaba el corazón de alegría."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Lucas en el índice de tu Biblia; el capítulo es el 24.",
               "El texto describe cómo volvieron los discípulos a Jerusalén después de adorar a Jesús."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Los discípulos volvieron a Jerusalén con gran ______.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
        {"texto": "Los discípulos ______ a Jesús antes de volver a Jerusalén.", "respuesta": "ADORARON", "banco": ["ADORARON", "IGNORARON", "OLVIDARON"]},
        {"texto": "En el templo, los discípulos daban ______ a Dios continuamente.", "respuesta": "ALABANZA", "banco": ["ALABANZA", "QUEJA", "SILENCIO"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo volvieron los discípulos a Jerusalén.",
               "La tercera respuesta es lo que daban a Dios en el templo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Los discípulos volvieron a Jerusalén con gran alegría.", "respuesta": True},
        {"texto": "Los discípulos se quedaron tristes después de la Ascensión.", "respuesta": False},
        {"texto": "Los discípulos alababan a Dios continuamente en el templo.", "respuesta": True},
        {"texto": "La fe no trae ninguna alegría a quien la vive.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda cómo volvieron los discípulos a Jerusalén.",
               "Si una frase dice que se quedaron tristes, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Cómo volvieron los discípulos a Jerusalén?",
         "opciones": ["Con gran alegría", "Tristes y confundidos", "Con miedo", "Sin ningún sentimiento"], "correcta": 0},
        {"texto": "¿Qué hacían los discípulos en el templo?",
         "opciones": ["Alababan a Dios continuamente", "Se escondían", "No hacían nada", "Discutían entre ellos"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo volvieron los discípulos a Jerusalén.",
               "Recuerda lo que hacían en el templo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ALEGRIA", "definicion": "Lo que sintieron los discípulos tras la Ascensión"},
        {"termino": "JERUSALEN", "definicion": "Ciudad a la que regresaron con alegría"},
        {"termino": "ADORAR", "definicion": "Lo que hicieron antes de volver"},
        {"termino": "ALABANZA", "definicion": "Lo que daban a Dios en el templo"},
        {"termino": "TEMPLO", "definicion": "Lugar donde alababan a Dios"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la escena final del evangelio de Lucas.",
               "TEMPLO es el lugar, no la acción de alabar."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: la alegría de los discípulos",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "Los discípulos volvieron a Jerusalén con gran ______.",
         "opciones": ["alegría", "tristeza", "miedo"], "correcta": 0},
        {"texto": "En el templo, daban ______ a Dios continuamente.",
         "opciones": ["alabanza", "queja", "silencio"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en cómo volvieron los discípulos a Jerusalén.",
               "Recuerda lo que daban a Dios en el templo."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Los discípulos volvieron a Jerusalén con gran ______.",
         "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "MIEDO"]},
    ],
    "reflexion": "¿Qué te da alegría a ti de vivir tu fe en Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en cómo volvieron los discípulos a Jerusalén.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: vivo mi fe con alegría",
    "situacion": "Ya sabes que los discípulos volvieron llenos de alegría después de ver a Jesús subir al cielo.",
    "items": [
        {"texto": "¿Cómo puedes vivir tu fe con esa misma alegría?",
         "opciones": ["Participando con gusto en la Misa",
                      "Compartiendo mi alegría de fe con otros",
                      "Dando gracias a Dios cada día",
                      "Viviendo la fe como una obligación triste"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de alegría, no de obligación.",
               "Descarta la única opción que vive la fe con tristeza."],
    "feedback_ok": "¡Muy bien! Así se vive la fe: con la alegría de saber que Jesús nos acompaña.",
})

# ==========================================================================
# PC16-C04 — Enviados a anunciar el Evangelio
# ==========================================================================
C = "PC16-C04"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: enviados a anunciar",
    "items": [
        {"texto": "La Buena Noticia que estamos llamados a anunciar.", "respuesta": "EVANGELIO", "banco": ["EVANGELIO", "SECRETO", "SILENCIO"]},
        {"texto": "Lo que hacemos al compartir con otros la Buena Noticia de Jesús.", "respuesta": "ANUNCIAR", "banco": ["ANUNCIAR", "CALLAR", "ESCONDER"]},
        {"texto": "Lo que somos de Jesús cuando compartimos lo que hemos vivido con él.", "respuesta": "TESTIGOS", "banco": ["TESTIGOS", "EXTRAÑOS", "ENEMIGOS"]},
        {"texto": "Lo que ocultó a Jesús de la vista de sus discípulos al subir al cielo.", "respuesta": "NUBE", "banco": ["NUBE", "SOMBRA", "LUZ"]},
        {"texto": "Lo que Jesús hizo a sus discípulos sobre la fuerza del Espíritu Santo.", "respuesta": "PROMESA", "banco": ["PROMESA", "AMENAZA", "SECRETO"]},
        {"texto": "Tarea de anunciar el Evangelio que Jesús nos confía.", "respuesta": "MISION", "banco": ["MISION", "DUDA", "PEREZA"]},
    ],
    "incluir": ["EVANGELIO", "MISION"], "requisito": 4,
    "pistas": ["Piensa en la Buena Noticia que estamos llamados a anunciar.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: enviados a anunciar",
    "palabras": ["EVANGELIO", "ANUNCIAR", "TESTIGOS", "NUBE", "PROMESA", "MISION"],
    "incluir": ["ANUNCIAR", "TESTIGOS"], "requisito": 5,
    "pistas": ["NUBE y MISION son de las palabras más cortas: búscalas primero.",
               "EVANGELIO es la palabra más larga de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 1,8-9",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 1,8-9 y completa: «Dicho esto, fue elevado a la "
                  "vista de ellos, y una ______ lo ocultó de sus ojos.»", "respuesta": "NUBE",
         "banco": ["NUBE", "SOMBRA", "LUZ"]},
        {"texto": "¿Qué misión nos deja Jesús al subir al cielo?", "abierta": True,
         "palabras_esperadas": ["ANUNCIAR", "EVANGELIO", "TESTIGOS", "MUNDO"],
         "respuestas_referencia": ["La misión de anunciar el Evangelio y ser sus testigos en todo el mundo.",
                                    "Nos deja la tarea de compartir la Buena Noticia con los demás.",
                                    "Nos envía a anunciar lo que hemos vivido con él, hasta los confines de la tierra."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 1.",
               "El texto describe lo que ocurrió justo después de que Jesús subiera al cielo."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Estamos llamados a anunciar el ______ a todos.", "respuesta": "EVANGELIO", "banco": ["EVANGELIO", "SECRETO", "SILENCIO"]},
        {"texto": "Una ______ ocultó a Jesús de la vista de sus discípulos.", "respuesta": "NUBE", "banco": ["NUBE", "SOMBRA", "LUZ"]},
        {"texto": "Jesús nos deja la ______ de anunciar la Buena Noticia.", "respuesta": "MISION", "banco": ["MISION", "DUDA", "PEREZA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que estamos llamados a anunciar.",
               "La segunda respuesta es lo que ocultó a Jesús al subir al cielo."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Estamos llamados a anunciar el Evangelio a todos.", "respuesta": True},
        {"texto": "Una nube ocultó a Jesús de la vista de sus discípulos al subir al cielo.", "respuesta": True},
        {"texto": "La misión de anunciar el Evangelio terminó con los apóstoles.", "respuesta": False},
        {"texto": "Ser testigos de Jesús no tiene relación con el Evangelio.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda qué estamos llamados a anunciar.",
               "Si una frase dice que la misión terminó con los apóstoles, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué estamos llamados a anunciar?",
         "opciones": ["El Evangelio", "Nada importante", "Un secreto", "Solo tristeza"], "correcta": 0},
        {"texto": "¿Qué ocultó a Jesús de la vista de sus discípulos?",
         "opciones": ["Una nube", "La oscuridad", "Nada", "Un muro"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en lo que estamos llamados a anunciar.",
               "Recuerda lo que ocultó a Jesús al subir al cielo."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "EVANGELIO", "definicion": "La Buena Noticia que anunciamos"},
        {"termino": "ANUNCIAR", "definicion": "Lo que hacemos al compartir la Buena Noticia"},
        {"termino": "TESTIGOS", "definicion": "Lo que somos de Jesús"},
        {"termino": "NUBE", "definicion": "Lo que ocultó a Jesús al subir al cielo"},
        {"termino": "MISION", "definicion": "Tarea de anunciar el Evangelio"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en la escena de la Ascensión y su mensaje.",
               "NUBE es lo que ocultó a Jesús, no una tarea."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: anunciar el Evangelio",
    "instruccion": "En 45 segundos, marca las palabras que describen nuestra misión de anunciar a Jesús.",
    "tiempo_segundos": 45,
    "banco": ["EVANGELIO", "ANUNCIAR", "TESTIGOS", "MISION", "SILENCIO", "DUDA"],
    "correctas": ["EVANGELIO", "ANUNCIAR", "TESTIGOS", "MISION"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Evangelio - Anunciar - Testigos - Misión.",
               "Descarta las palabras que describen silencio o duda."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Estamos llamados a anunciar el ______ a todos.",
         "respuesta": "EVANGELIO", "banco": ["EVANGELIO", "SECRETO", "SILENCIO"]},
    ],
    "reflexion": "¿A quién te gustaría anunciarle la Buena Noticia de Jesús?",
    "requisito": 1,
    "pistas": ["Piensa en lo que estamos llamados a anunciar.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: cumplo mi misión",
    "situacion": "Ya sabes que Jesús nos deja la misión de anunciar el Evangelio y ser sus testigos.",
    "items": [
        {"texto": "¿Cómo puedes cumplir esta misión en tu vida diaria?",
         "opciones": ["Compartiendo lo que aprendí sobre Jesús",
                      "Viviendo el amor de Jesús con los demás",
                      "Invitando a otros a conocer a Jesús",
                      "Guardando la Buena Noticia solo para mí"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en acciones que comparten la Buena Noticia.",
               "Descarta la única opción que guarda la Buena Noticia solo para uno mismo."],
    "feedback_ok": "¡Muy bien! Así cumplimos la misión de anunciar el Evangelio.",
})

# ==========================================================================
# PC16-C05 — Acompañados por María, Madre de la Iglesia
# ==========================================================================
C = "PC16-C05"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: acompañados por María",
    "items": [
        {"texto": "Madre de Jesús que oraba junto a los apóstoles después de la Ascensión.", "respuesta": "MARIA", "banco": ["MARIA", "MARTA", "SALOME"]},
        {"texto": "Lo que hacían los apóstoles y María, unidos, después de la Ascensión.", "respuesta": "ORACION", "banco": ["ORACION", "SILENCIO", "PRISA"]},
        {"texto": "Como oraban los apóstoles junto a María: todos juntos y de un mismo corazón.", "respuesta": "UNANIMES", "banco": ["UNANIMES", "SEPARADOS", "DISTANTES"]},
        {"texto": "Título que recibe María también respecto de la Iglesia.", "respuesta": "MADRE", "banco": ["MADRE", "REINA LEJANA", "EXTRAÑA"]},
        {"texto": "Comunidad que camina acompañada por María, Madre de Jesús.", "respuesta": "IGLESIA", "banco": ["IGLESIA", "MULTITUD", "CIUDAD"]},
        {"texto": "Lo que hace María con la Iglesia en su camino de fe.", "respuesta": "ACOMPAÑAR", "banco": ["ACOMPAÑAR", "ABANDONAR", "IGNORAR"]},
    ],
    "incluir": ["MARIA", "IGLESIA"], "requisito": 4,
    "pistas": ["Piensa en quién oraba junto a los apóstoles después de la Ascensión.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: acompañados por María",
    "palabras": ["MARIA", "ORACION", "UNANIMES", "MADRE", "IGLESIA", "ACOMPAÑAR"],
    "incluir": ["ORACION", "MADRE"], "requisito": 5,
    "pistas": ["MARIA y MADRE son de las palabras más cortas: búscalas primero.",
               "ACOMPAÑAR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Hechos 1,14",
    "items": [
        {"texto": "Busca en tu Biblia Católica Hechos 1,14 y completa: «Todos ellos perseveraban unánimes "
                  "en la oración, junto con María, la madre de ______.»", "respuesta": "JESUS",
         "banco": ["JESUS", "PEDRO", "JUAN"]},
        {"texto": "¿Qué hacía María junto a los apóstoles después de la Ascensión?", "abierta": True,
         "palabras_esperadas": ["ORAR", "ACOMPAÑAR", "UNIDOS", "ESPERAR"],
         "respuestas_referencia": ["Oraba junto a ellos, unida en un mismo corazón, esperando al Espíritu Santo.",
                                    "Acompañaba a los apóstoles en la oración, como madre de la comunidad.",
                                    "Perseveraba en la oración junto a ellos, unánime y en comunidad."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el libro de los Hechos de los Apóstoles en el índice de tu Biblia; el capítulo es el 1.",
               "El texto describe quién oraba junto a los apóstoles después de la Ascensión."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "María oraba junto a los ______ después de la Ascensión.", "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "SOLDADOS", "EXTRAÑOS"]},
        {"texto": "Los apóstoles y María oraban ______, de un mismo corazón.", "respuesta": "UNIDOS", "banco": ["UNIDOS", "SEPARADOS", "DISTANTES"]},
        {"texto": "María es también Madre de la ______.", "respuesta": "IGLESIA", "banco": ["IGLESIA", "MULTITUD", "CIUDAD"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con quién oraba María después de la Ascensión.",
               "La tercera respuesta describe otro título de María."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "María oraba junto a los apóstoles después de la Ascensión.", "respuesta": True},
        {"texto": "María se alejó de los apóstoles después de la Ascensión.", "respuesta": False},
        {"texto": "María es también Madre de la Iglesia.", "respuesta": True},
        {"texto": "A María no le importa acompañar a la Iglesia.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda con quién oraba María después de la Ascensión.",
               "Si una frase dice que María se alejó de los apóstoles, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Con quién oraba María después de la Ascensión?",
         "opciones": ["Con los apóstoles", "Con nadie", "Sola en su casa", "Con extraños"], "correcta": 0},
        {"texto": "¿Qué título recibe María respecto de la Iglesia?",
         "opciones": ["Madre de la Iglesia", "Reina lejana", "Extraña", "Ninguno"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con quién oraba María después de la Ascensión.",
               "Recuerda el título que recibe María respecto de la Iglesia."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "MARIA", "definicion": "Madre de Jesús que oraba con los apóstoles"},
        {"termino": "ORACION", "definicion": "Lo que hacían los apóstoles y María juntos"},
        {"termino": "UNANIMES", "definicion": "Cómo oraban, de un mismo corazón"},
        {"termino": "MADRE", "definicion": "Título de María respecto de la Iglesia"},
        {"termino": "IGLESIA", "definicion": "Comunidad acompañada por María"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el papel de María en la primera comunidad.",
               "UNANIMES describe cómo oraban, no quién oraba."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "preguntas", "titulo": "Reto: María, Madre de la Iglesia",
    "instruccion": "Piensa en cada frase y elige la palabra correcta.",
    "tiempo_segundos": 45,
    "items": [
        {"texto": "María oraba junto a los ______ después de la Ascensión.",
         "opciones": ["apóstoles", "soldados", "extraños"], "correcta": 0},
        {"texto": "María es también Madre de la ______.",
         "opciones": ["Iglesia", "multitud", "ciudad"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en con quién oraba María después de la Ascensión.",
               "Recuerda el título que recibe María respecto de la Iglesia."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "María oraba junto a los ______ después de la Ascensión.",
         "respuesta": "APOSTOLES", "banco": ["APOSTOLES", "SOLDADOS", "EXTRAÑOS"]},
    ],
    "reflexion": "¿Qué sientes al saber que María también acompaña tu camino de fe?",
    "requisito": 1,
    "pistas": ["Piensa en con quién oraba María después de la Ascensión.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: pido a María que me acompañe",
    "situacion": "Ya sabes que María oraba junto a los apóstoles y es también Madre de la Iglesia.",
    "items": [
        {"texto": "¿Cómo puedes pedirle a María que te acompañe en tu camino de fe?",
         "opciones": ["Rezando el Ave María",
                      "Pidiéndole que interceda por mí",
                      "Imitando su confianza en Dios",
                      "Pensando que María no tiene nada que ver con mi fe"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en actitudes de cercanía con María.",
               "Descarta la única opción que aleja a María de tu fe."],
    "feedback_ok": "¡Muy bien! María acompaña con amor de madre nuestro camino de fe.",
})

# ==========================================================================
# PC16-C06 — Celebración final: nuestro envío misionero
# ==========================================================================
C = "PC16-C06"

_agregar(C, "A01", {
    "tipo": "crucigrama", "titulo": "Crucigrama: nuestro envío misionero",
    "items": [
        {"texto": "Lo que Jesús hace con nosotros al final de este camino de fe.", "respuesta": "ENVIO", "banco": ["ENVIO", "ABANDONO", "OLVIDO"]},
        {"texto": "Lo que Jesús promete hacer con nosotros todos los días, hasta el fin del mundo.", "respuesta": "ACOMPAÑAR", "banco": ["ACOMPAÑAR", "ABANDONAR", "IGNORAR"]},
        {"texto": "Palabra que usa Jesús al decir que estará con nosotros hasta el ______ del mundo.", "respuesta": "FIN", "banco": ["FIN", "COMIENZO", "MEDIO"]},
        {"texto": "Lo que somos llamados a ser al terminar este camino de catequesis.", "respuesta": "MISIONERO", "banco": ["MISIONERO", "EXTRAÑO", "VISITANTE"]},
        {"texto": "Lo que sentimos al celebrar todo lo aprendido y vivido.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "INDIFERENCIA"]},
        {"texto": "Lo que hacemos hoy, dando gracias por este camino de fe.", "respuesta": "CELEBRAR", "banco": ["CELEBRAR", "OLVIDAR", "IGNORAR"]},
    ],
    "incluir": ["ENVIO", "MISIONERO"], "requisito": 4,
    "pistas": ["Piensa en lo que Jesús hace con nosotros al final de este camino.",
               "Cuenta las letras de cada palabra: ese es el tamaño del espacio que ocupa en el crucigrama."],
})
_agregar(C, "A02", {
    "tipo": "sopa_letras", "titulo": "Sopa de letras: nuestro envío misionero",
    "palabras": ["ENVIO", "ACOMPAÑAR", "FIN", "MISIONERO", "ALEGRIA", "CELEBRAR"],
    "incluir": ["ACOMPAÑAR", "CELEBRAR"], "requisito": 5,
    "pistas": ["ENVIO y FIN son de las palabras más cortas: búscalas primero.",
               "ACOMPAÑAR es una de las palabras más largas de esta sopa de letras."],
})
_agregar(C, "A03", {
    "tipo": "completar", "titulo": "Práctica con la Biblia: Mateo 28,20",
    "items": [
        {"texto": "Busca en tu Biblia Católica Mateo 28,20 y completa: «Yo estoy con ustedes todos los "
                  "días, hasta el ______ del mundo.»", "respuesta": "FIN",
         "banco": ["FIN", "COMIENZO", "MEDIO"]},
        {"texto": "¿Qué significa este envío misionero al final de tu camino de fe?", "abierta": True,
         "palabras_esperadas": ["MISION", "ANUNCIAR", "ACOMPAÑAR", "TESTIGO"],
         "respuestas_referencia": ["Significa que soy enviado a anunciar a Jesús, con la certeza de que él me acompaña.",
                                    "Significa que ahora soy un misionero, testigo de todo lo vivido con Jesús.",
                                    "Significa continuar caminando con Jesús y compartiendo su amor con otros."]},
    ],
    "requisito": 2,
    "pistas": ["Busca el evangelio de Mateo en el índice de tu Biblia; el capítulo es el 28, el último.",
               "El texto es la promesa final de Jesús a sus discípulos, de acompañarlos siempre."],
})
_agregar(C, "A04", {
    "tipo": "completar", "titulo": "Completar",
    "items": [
        {"texto": "Jesús nos promete estar con nosotros todos los días, hasta el ______ del mundo.", "respuesta": "FIN", "banco": ["FIN", "COMIENZO", "MEDIO"]},
        {"texto": "Al terminar este camino, somos enviados como ______ de Jesús.", "respuesta": "MISIONEROS", "banco": ["MISIONEROS", "EXTRAÑOS", "VISITANTES"]},
        {"texto": "Hoy celebramos con ______ todo lo aprendido en este camino.", "respuesta": "ALEGRIA", "banco": ["ALEGRIA", "TRISTEZA", "INDIFERENCIA"]},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la promesa final de Jesús a sus discípulos.",
               "La segunda respuesta es lo que somos al terminar este camino."],
})
_agregar(C, "A05", {
    "tipo": "verdadero_falso", "titulo": "Verdadero o falso",
    "items": [
        {"texto": "Jesús promete acompañarnos todos los días, hasta el fin del mundo.", "respuesta": True},
        {"texto": "Al terminar la catequesis, ya no tenemos ninguna misión.", "respuesta": False},
        {"texto": "Hoy celebramos con alegría el camino de fe recorrido.", "respuesta": True},
        {"texto": "Ser misionero es una tarea solo para los adultos.", "respuesta": False},
    ],
    "requisito": 3,
    "pistas": ["Recuerda la promesa final de Jesús a sus discípulos.",
               "Si una frase dice que ya no tenemos misión, es falsa."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A06", {
    "tipo": "seleccion_multiple", "titulo": "Selección múltiple",
    "items": [
        {"texto": "¿Qué promete Jesús hasta el fin del mundo?",
         "opciones": ["Estar con nosotros", "Abandonarnos", "Olvidarnos", "Alejarse"], "correcta": 0},
        {"texto": "¿Qué somos llamados a ser al terminar este camino?",
         "opciones": ["Misioneros de Jesús", "Espectadores solamente", "Extraños a la fe", "Nada en especial"], "correcta": 0},
    ],
    "requisito": 2,
    "pistas": ["Piensa en la promesa final de Jesús a sus discípulos.",
               "Recuerda lo que somos llamados a ser al terminar este camino."],
    "feedback_ok": FEEDBACK_OK_COMPRENDISTE,
})
_agregar(C, "A07", {
    "tipo": "unir_parejas", "titulo": "Unir parejas",
    "pares": [
        {"termino": "ENVIO", "definicion": "Lo que Jesús hace con nosotros al final del camino"},
        {"termino": "ACOMPAÑAR", "definicion": "Lo que Jesús promete hacer siempre"},
        {"termino": "MISIONERO", "definicion": "Lo que somos llamados a ser"},
        {"termino": "ALEGRIA", "definicion": "Lo que sentimos al celebrar este camino"},
        {"termino": "CELEBRAR", "definicion": "Lo que hacemos hoy, dando gracias"},
    ],
    "requisito": 4,
    "pistas": ["Piensa en el mensaje final de este camino de fe.",
               "CELEBRAR es la acción de hoy, no una promesa de Jesús."],
    "feedback_ok": FEEDBACK_OK_RELACION,
})
_agregar(C, "A08", {
    "tipo": "reto", "modo": "elegir_libres", "titulo": "Reto: mi envío misionero",
    "instruccion": "En 45 segundos, marca las palabras que describen tu envío misionero de hoy.",
    "tiempo_segundos": 45,
    "banco": ["ENVIO", "MISIONERO", "ALEGRIA", "ACOMPAÑAR", "MIEDO", "DUDA"],
    "correctas": ["ENVIO", "MISIONERO", "ALEGRIA", "ACOMPAÑAR"], "minimo": 3, "requisito": 3,
    "pistas": ["El mensaje central es: Envío - Misionero - Alegría - Acompañar.",
               "Descarta las palabras que describen miedo o duda."],
})
_agregar(C, "A09", {
    "tipo": "recuperacion", "titulo": "Recuperación",
    "items": [
        {"texto": "Jesús nos promete estar con nosotros todos los días, hasta el ______ del mundo.",
         "respuesta": "FIN", "banco": ["FIN", "COMIENZO", "MEDIO"]},
    ],
    "reflexion": "¿Qué te gustaría llevar contigo de todo este camino de fe?",
    "requisito": 1,
    "pistas": ["Piensa en la promesa final de Jesús a sus discípulos.", "Repasa la actividad de completar de este tema."],
})
_agregar(C, "A10", {
    "tipo": "aplicacion", "titulo": "Aplicación: mi envío misionero",
    "situacion": "Has llegado al final de tu camino de Primera Comunión: hoy Jesús te envía como su misionero, prometiendo acompañarte siempre.",
    "items": [
        {"texto": "¿Cómo vas a vivir, de ahora en adelante, tu misión como amigo y misionero de Jesús?",
         "opciones": ["Viviendo lo que aprendí en mi familia y mi comunidad",
                      "Acercándome a Jesús en la Eucaristía",
                      "Compartiendo con otros la alegría de mi fe",
                      "Olvidando todo lo aprendido apenas termine"],
         "correctas": [0, 1, 2]},
    ],
    "requisito": 1,
    "pistas": ["Piensa en cómo seguir viviendo tu fe después de este camino.",
               "Descarta la única opción que olvida todo lo aprendido."],
    "feedback_ok": "¡Felicidades! Has completado tu camino hacia la Primera Comunión. Jesús te envía hoy "
                   "como su amigo y misionero: ¡anda y comparte su amor allí donde vayas!",
})

def siguiente_contenido_de(contenido_id):
    """Contenido que sigue en el orden general (cruza de un encuentro al
    siguiente), o None si es el último de todos — usado para invitar a
    continuar apenas se completa un tema."""
    for i, c in enumerate(CONTENIDOS):
        if c["id"] == contenido_id:
            return CONTENIDOS[i + 1] if i + 1 < len(CONTENIDOS) else None
    return None


def anterior_contenido_de(contenido_id):
    """Contenido inmediatamente anterior en el orden general (CONTENIDOS
    recorre los encuentros en orden, así que esto también cruza de un
    encuentro al anterior), o None si es el primero de todos (PC01-C01).
    Se usa para exigir que ese contenido esté completo antes de desbloquear
    este — el "camino" del itinerario se recorre en un único orden lineal,
    de principio a fin, sin poder saltar temas ni encuentros."""
    for i, c in enumerate(CONTENIDOS):
        if c["id"] == contenido_id:
            return CONTENIDOS[i - 1] if i > 0 else None
    return None
