# Camino a la Primera Comunión — piloto PC01 a PC16

Prototipo funcional (no de producción) del microservicio de formación y
reforzamiento catequético descrito en el documento maestro: una API
REST en Flask que sirve el contenido de dieciséis encuentros —
**PC01 — "Dios nos creó por amor"**, **PC02 — "Jesús es nuestro amigo"**,
**PC03 — "Dios nos habla en la Biblia"**, **PC04 — "La familia de Jesús:
la Iglesia"**, **PC05 — "El Bautismo: somos hijos de Dios"**, **PC06 —
"La Eucaristía: Jesús se queda con nosotros"**, **PC07 — "El Espíritu
Santo nos da fuerza"**, **PC08 — "Jesús nos enseña a amar a todos"**,
**PC09 — "Aprendemos a rezar con Jesús"**, **PC10 — "María, la Madre de
Jesús y Madre nuestra"**, **PC11 — "Somos amigos y misioneros de
Jesús"**, **PC12 — "Dios nos promete la vida eterna"**, **PC13 — "El
Espíritu Santo nos envía"**, **PC14 — "Iglesia sinodal: caminamos
juntos"**, **PC15 — "Ser luz en el mundo"** y **PC16 — "Celebración
final: envío misionero"** — y aplica el motor de reforzamiento, más una
interfaz web instalable (PWA) que un niño puede usar desde el navegador o
desde el ícono en su teléfono.

## Qué incluye este piloto

- **Contenido real** (no plantilla) para dieciséis encuentros completos:
  - **PC01 — Dios nos creó por amor** (Génesis 1,26-31): 6 contenidos
    (PC01-C01 a PC01-C06).
  - **PC02 — Jesús es nuestro amigo** (Marcos 10,13-16): 6 contenidos
    (PC02-C01 a PC02-C06).
  - **PC03 — Dios nos habla en la Biblia** (2 Timoteo 3,14-17 / Lucas
    24,13-35): 6 contenidos (PC03-C01 a PC03-C06).
  - **PC04 — La familia de Jesús: la Iglesia** (Hechos 2,42-47): 6
    contenidos (PC04-C01 a PC04-C06).
  - **PC05 — El Bautismo: somos hijos de Dios** (Mateo 28,18-20 / Juan
    3,5): 6 contenidos (PC05-C01 a PC05-C06).
  - **PC06 — La Eucaristía: Jesús se queda con nosotros** (Lucas
    22,19-20 / Juan 6,51): 6 contenidos (PC06-C01 a PC06-C06).
  - **PC07 — El Espíritu Santo nos da fuerza** (Hechos 2,1-4): 6
    contenidos (PC07-C01 a PC07-C06).
  - **PC08 — Jesús nos enseña a amar a todos** (Lucas 10,25-37): 6
    contenidos (PC08-C01 a PC08-C06).
  - **PC09 — Aprendemos a rezar con Jesús** (Mateo 6,5-13): 6 contenidos
    (PC09-C01 a PC09-C06).
  - **PC10 — María, la Madre de Jesús y Madre nuestra** (Lucas 1,26-38 /
    Juan 19,25-27): 6 contenidos (PC10-C01 a PC10-C06).
  - **PC11 — Somos amigos y misioneros de Jesús** (Juan 15,15-17 / Mateo
    28,19-20): 6 contenidos (PC11-C01 a PC11-C06).
  - **PC12 — Dios nos promete la vida eterna** (Juan 11,25-26 / Juan
    14,1-3): 6 contenidos (PC12-C01 a PC12-C06).
  - **PC13 — El Espíritu Santo nos envía** (Hechos 1,8 / Juan 20,21-22):
    6 contenidos (PC13-C01 a PC13-C06).
  - **PC14 — Iglesia sinodal: caminamos juntos** (Hechos 15,6-7.22 /
    Hechos 2,42): 6 contenidos (PC14-C01 a PC14-C06).
  - **PC15 — Ser luz en el mundo** (Mateo 5,14-16 / Juan 8,12): 6
    contenidos (PC15-C01 a PC15-C06).
  - **PC16 — Celebración final: envío misionero** (Hechos 1,8-11 / Lucas
    24,50-53): 6 contenidos (PC16-C01 a PC16-C06), el cierre del
    itinerario completo.

  > **Nota sobre PC11 a PC16**: a diferencia de PC01-PC10, para estos
  > seis encuentros solo se recibieron los títulos (sin documento
  > maestro detallado por contenido). Las citas bíblicas, objetivos y el
  > contenido pedagógico de cada actividad se redactaron desde cero,
  > siguiendo el mismo estilo, estructura y nivel que los encuentros
  > anteriores. Conviene que la formadora los revise y los compare con
  > su propio material antes de usarlos con los niños.

  Cada contenido tiene **10 actividades** — **960 actividades en
  total** (60 por encuentro): crucigrama, sopa de letras, práctica con
  la Biblia, completar, verdadero/falso, selección múltiple, unir
  parejas, reto, recuperación y aplicación (una situación de la vida
  real con varias respuestas válidas, no solo una).
- **Pantalla de selección de encuentro**: al entrar, el niño ve los
  encuentros disponibles con su progreso (`GET /api/encuentros`) y elige
  cuál seguir. Al terminar todas las actividades del último contenido de
  un encuentro, la app invita automáticamente a continuar con el primer
  contenido del siguiente encuentro (PC01-C06 → PC02-C01 → ... →
  PC15-C06 → PC16-C01), sin que el niño tenga que volver a elegir
  manualmente.
- **Bloqueo de avance (gating)**: no se puede pasar al contenido
  siguiente si no se completaron (lograron) todas las actividades del
  contenido actual. Si el niño intenta saltarse contenido sin haber
  aprobado sus actividades, la app muestra una advertencia explicando
  que primero debe completar las actividades del contenido actual —
  nunca permite el salto en silencio.
- **Animación final del camino**: al completar la última actividad del
  último contenido (PC16-C06-A10, "Celebración final"), en vez del aviso
  genérico de "encuentro completado" aparece una animación de cierre: un
  camino ilustrado donde va apareciendo, encuentro por encuentro, la
  figura de un niño que recorre y supera los 16 encuentros, hasta llegar
  a un altar con Jesús, que los recibe con los brazos abiertos y una
  frase de felicitación por haber completado el camino hacia la Primera
  Comunión. También se puede volver a ver después desde un banner en la
  pantalla de encuentros ("¡Completaste todo el camino!"), una vez que
  todo el itinerario está logrado.
- **Portada con San Charbel**: al abrir la app aparece una portada de
  bienvenida con la imagen de San Charbel durante unos 2 segundos, y
  continúa de inmediato a la pantalla normal (login o lista de
  encuentros, según corresponda). En el resto de las pantallas, la misma
  imagen aparece pequeña, como un ícono redondo, en el encabezado (arriba
  a la izquierda), en todas las páginas. Ver más detalles en la sección
  "Imagen de San Charbel" más abajo.
- **Crucigrama real**: no es una lista de espacios para rellenar, sino una
  cuadrícula donde las palabras se cruzan entre sí por letras compartidas
  (como un crucigrama de verdad), con pistas numeradas en horizontal y
  vertical. El trazado se calcula automáticamente a partir de las palabras
  y sus definiciones — no hay que diseñar la cuadrícula a mano por contenido.
- **Motor de reforzamiento** fiel a las reglas del documento: 1er error →
  retroalimentación y nuevo intento; 2do → pista; 3er → pista más
  específica; 4to → se muestra la respuesta con explicación; 5to en
  adelante → `REQUIERE_ACOMPAÑAMIENTO` (se sugiere pedir ayuda al
  catequista). Un acierto con ayuda igual cuenta como logrado, tal como
  especifica el modelo.
- **Estados** por actividad y por contenido (`NO_LOGRADO`, `EN_PROCESO`,
  `LOGRADO`, `REQUIERE_ACOMPAÑAMIENTO`), sin nota numérica.
- **Registro de progreso** en SQLite, separado del contenido (igual que
  describe el modelo), identificando al niño solo por un código que le
  asigna el catequista — sin nombre completo, correo ni datos personales.
  Cada intento queda asociado al encuentro (PC01 a PC10) al que pertenece
  su actividad.
- **Interfaz web instalable (PWA)**: `manifest.json` + `service worker`,
  para que se pueda "instalar" desde el navegador tanto en computadora
  como en teléfono, sin pasar por tiendas de aplicaciones.

## Nota sobre "Práctica con la Biblia" (actividad A03)

La actividad A03 se llamaba originalmente "palabra por número": el niño
debía asociar palabras con números de una lista de vocabulario. Esa lista
numerada nunca se mostraba en pantalla (solo se revelaba como pista después
de 2 intentos fallidos), así que era imposible de resolver desde el
principio.

Siguiendo el documento maestro (donde esta actividad se sustituyó en
toda la formación, no solo en un complemento aparte), A03 es ahora
**"Práctica con la Biblia"** en los **96 contenidos** de los dieciséis
encuentros: el niño busca en su propia Biblia la cita indicada y completa
la palabra que falta en el versículo (con un banco de palabras para
ayudarse), y luego responde una pregunta abierta de reflexión sobre lo
leído. Cada contenido usa una **cita bíblica distinta**, relacionada con su
contenido específico, para que la práctica no se sienta repetitiva.

En la app, esta actividad reutiliza el mismo tipo `completar` ya probado
en el resto de las actividades (un ítem cerrado con respuesta única + un
ítem abierto evaluado solo por participación), en vez de construir una
mecánica de búsqueda nueva — el mismo criterio de "reutilizar el motor ya
probado" que ya se venía aplicando en el resto del piloto.

## Filtro de respuestas abiertas (ítems "abierta")

Los ítems `"abierta": True` (la pregunta de reflexión de "Práctica con la
Biblia", y algunos de "Recuperación") no tienen una única respuesta
correcta. Por defecto el motor los daría por logrados con que el niño
escriba algo — pero eso por sí solo no distingue una reflexión sincera de
una respuesta que contradice el tema, ni de una que simplemente no tiene
nada que ver con lo que se preguntó. Hay dos mecanismos, en `app.py`
(función `_evaluar_item_abierto`), que corrigen esto:

1. **`content.PALABRAS_ALERTA`** (en `content.py`, junto a los
   `FEEDBACK_*`): una lista de palabras que claramente contradicen el
   mensaje catequético (odiar, pegar, mentir, robar, etc.). Si la
   respuesta contiene alguna, no cuenta como lograda y el niño recibe
   `content.FEEDBACK_ALERTA` en vez del mensaje genérico. Ejemplo:
   responder "odiar" a "¿qué nos manda Jesús?".

2. **`"palabras_esperadas"`** (opcional, en el propio ítem dentro de
   `content.py`): cuando la pregunta tiene una dirección correcta clara
   según la cita bíblica o la situación planteada, el ítem declara una
   lista de palabras esperadas (por ejemplo, para "¿qué significa que la
   tierra sea del Señor, para el cuidado que le debemos?": `CUIDAR,
   RESPETAR, PROTEGER, LIMPIAR, CREACION`) y la respuesta debe contener
   al menos una — si no, no cuenta como lograda y el niño recibe
   `content.FEEDBACK_FUERA_DE_TEMA`. De las **104 preguntas abiertas**
   que hay en total (las 96 de "Práctica con la Biblia", una por
   contenido, más 8 de "Recuperación" repartidas entre los dieciséis
   encuentros), **102 tienen `palabras_esperadas`**; las 2 restantes
   ("¿cuándo has sentido que Jesús es tu amigo?" y "¿qué podrías decirle
   a Jesús antes de dormir?") son genuinamente personales y se dejan sin
   esta lista a propósito, para no rechazar respuestas honestas y
   variadas que no puedan anticiparse con palabras clave.

La respuesta de la API incluye `"alerta_contenido"` y `"fuera_de_tema"`
(booleanos) para que ambos casos queden visibles en el registro de
progreso del catequista.

Ambos son filtros simples por palabra (no un modelo de lenguaje): no
captan paráfrasis ni ironías, y pueden dar algún falso positivo o
negativo ocasional (una respuesta que mencione "pelear" para decir que
*no* hay que pelear; o una respuesta correcta que use un sinónimo que no
esté en la lista). Ampliarlos o afinarlos es cuestión de editar
`PALABRAS_ALERTA` o el campo `"palabras_esperadas"` del ítem en
`content.py`, sin tocar la lógica de `app.py`.

### Tercer nivel: similitud semántica (paráfrasis)

Aun con `palabras_esperadas` bien afinado, va a seguir apareciendo el
mismo problema de fondo: un niño responde **bien**, pero con palabras que
no anticipamos al escribir el contenido — por ejemplo, "Dios Vivo" para
"¿Cómo llama san Pablo a la Iglesia?" es literalmente correcto (1 Timoteo
3,15: *"la Iglesia del Dios vivo"*), pero si "VIVO" no estaba en la lista,
el filtro de palabras lo rechaza igual que rechazaría "hacer incendios".
Ampliar listas a mano solo pospone el problema para la siguiente
respuesta imprevista.

Por eso se agregó un tercer nivel, en `nlp_eval.py`: cuando
`palabras_esperadas` **no** encuentra ninguna coincidencia, en vez de
rechazar la respuesta de una vez, se compara su **significado** con una
lista de 2-3 `"respuestas_referencia"` (frases de ejemplo correctas, ya
agregadas en `content.py` a los mismos 66 ítems que tienen
`palabras_esperadas`) usando un modelo preentrenado de "sentence
embeddings" (`paraphrase-multilingual-MiniLM-L12-v2`, multilingüe,
incluye español). Si el parecido de significado supera el umbral
`nlp_eval.UMBRAL_SIMILITUD` (0.55 de partida), la respuesta se acepta
aunque no comparta ninguna palabra clave con las previstas.

Esto **no es** un modelo entrenado a la medida con tus datos (para eso
hace falta un historial real de respuestas revisadas por un catequista,
que todavía no existe) — es un modelo genérico ya entrenado por terceros
para "entender" si dos frases dicen lo mismo, sin que nadie tenga que
etiquetar nada. Si en el futuro se junta suficiente historial real,
tiene sentido dar el salto a un modelo entrenado a la medida (por
ejemplo, reutilizando el mismo enfoque BETO/RoBERTa-es de tu clasificador
pastoral).

**Diseño a prueba de fallos, muy importante:** si la librería
`sentence-transformers` no está instalada, o el modelo no se puede
descargar (por ejemplo, el servidor arrancó sin conexión a internet la
primera vez), `nlp_eval` lo detecta, avisa una sola vez en el log y la
app sigue funcionando exactamente igual que antes, evaluando solo con
`palabras_esperadas` — nunca se cae por esto. Este comportamiento de
respaldo sí se probó a fondo durante el desarrollo (ver nota de instalación
más abajo); lo que **no** se pudo probar en el entorno donde se escribió
este código fue el modelo real funcionando, porque ese entorno de
desarrollo no tenía acceso a internet hacia huggingface.co (de donde se
descarga el modelo) — una restricción de red de ese entorno específico,
no del código. Tu servidor real debería tener acceso a internet normal,
así que debería funcionar sin problema, pero **conviene probarlo ahí**
antes de confiar en él del todo:

1. **Instalación**: `requirements.txt` ya incluye `sentence-transformers`
   y una versión de `torch` (la librería de la que depende) fijada a su
   variante **solo para CPU** — la que instala `pip` por defecto trae
   soporte para GPU (CUDA) y pesa varios GB de más, inútiles en un
   servidor sin GPU. Con `pip install -r requirements.txt` ya debería
   instalarse la versión correcta; si tu servidor sí tiene GPU y quieres
   aprovecharla, edita `requirements.txt` como se explica en sus propios
   comentarios.
2. **Primera descarga del modelo**: la primera vez que arranques el
   servidor (`python app.py`) y llegue una respuesta abierta que necesite
   este nivel, se descargan automáticamente unos cientos de MB del
   modelo — asegúrate de tener conexión a internet en ese momento. Las
   veces siguientes ya queda en caché local y no vuelve a descargarse.
3. **Calibrar el umbral**: `UMBRAL_SIMILITUD = 0.55` en `nlp_eval.py` es
   un punto de partida razonable, no un valor validado con respuestas
   reales. Si notas que acepta respuestas que no debería (muy permisivo),
   súbelo un poco (por ejemplo a 0.6-0.65); si sigue rechazando
   paráfrasis correctas (muy estricto), bájalo (por ejemplo a 0.45-0.5).
   Una forma simple de calibrar: agrega temporalmente un `print` en
   `similitud_maxima()` que muestre el puntaje de cada respuesta real que
   vayan escribiendo los niños, y ajusta el número con esos datos.
4. Puedes seguir usando la app con total normalidad aunque decidas NO
   instalar `sentence-transformers` en absoluto — simplemente te quedas
   en los dos primeros niveles (`PALABRAS_ALERTA` + `palabras_esperadas`).

## Nota sobre algunas actividades de PC02

El documento maestro de PC02 describe algunas actividades de "reto" y
"aplicación" como tareas abiertas (escribir una oración propia de dos o
tres frases, realizar una acción durante la semana y contarla luego).
Para reutilizar el mismo motor ya probado en PC01 (en vez de construir un
tipo de actividad nuevo solo para estos casos puntuales), esas se
adaptaron al mecanismo de "elegir entre varias opciones válidas" que ya
usan el resto de actividades — por ejemplo, en vez de escribir una
oración libre, el niño elige entre varias oraciones breves y apropiadas.
El contenido pedagógico (la situación, el tema, el criterio de logro) se
mantuvo fiel al documento; lo que cambió fue únicamente el mecanismo de
interacción en pantalla.

## Imagen de San Charbel

La app muestra una imagen de San Charbel en dos lugares:

- **Portada de bienvenida** (`#splash` en `index.html`): a pantalla
  completa, se muestra apenas se abre la app y desaparece sola con una
  transición suave luego de `DURACION_SPLASH_MS` (2000 ms, en
  `frontend/js/app.js`), continuando de inmediato a la pantalla que
  corresponda (login o lista de encuentros).
- **Encabezado pequeño** (`.topbar-logo` en `index.html`/`style.css`):
  un ícono redondo pequeño arriba a la izquierda, fijo en la barra
  superior (`.topbar-inner`) que ya aparece en todas las pantallas
  después de la portada, gracias a que la app es de una sola página y
  esa barra es parte del "cascarón" común a todas las vistas.

Los archivos de imagen viven en `frontend/icons/`:

- `san-charbel-splash.png` (500×585) — versión para la portada.
- `san-charbel-header.png` (160×187) — versión recortada/pequeña para
  el encabezado.

**Para cambiar la imagen**, reemplaza esos dos archivos por otra versión
(conservando esos nombres, o actualizando las referencias en
`index.html`) y sube en 1 el número de versión del service worker
(`CACHE` en `frontend/sw.js`, por ejemplo de `"catequesis-pc01-v3"` a
`"catequesis-pc01-v4"`) — si no se sube ese número, los teléfonos que ya
instalaron la app como PWA pueden seguir viendo la imagen anterior desde
su caché offline hasta que se actualice solos.

## Cómo probarlo

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Abre `http://localhost:5000` en el navegador. Vas a ver primero la portada
con San Charbel (unos 2 segundos) y luego la pantalla de entrada: escribe
cualquier código (por ejemplo `PRUEBA-1`) para entrar — no hace falta
registro. Vas a ver luego la pantalla con los dieciséis encuentros
disponibles (PC01 a PC16); elige uno para ver sus 6 contenidos (no se
puede pasar a un contenido siguiente sin haber completado las
actividades del actual). Al terminar la última actividad del último
contenido (PC16-C06-A10) aparece la animación final del camino. Para
probarlo desde el teléfono, ambos
dispositivos deben estar en la misma red Wi-Fi: usa
`http://<IP-de-tu-computadora>:5000` en el navegador del teléfono, y desde
ahí "Agregar a pantalla de inicio" para instalarlo como app.

Para reiniciar el progreso de prueba, simplemente borra
`backend/catequesis.db` (se vuelve a crear solo).

## Despliegue en producción (VPS con Easypanel)

El proyecto ya incluye un `Dockerfile` (en la raíz) listo para desplegarlo
en un VPS con Easypanel — el mismo patrón "App a partir de Dockerfile"
que se usa para Evolution API — con `gunicorn` como servidor de
producción en vez del servidor de pruebas de Flask. Para el paso a paso
completo (subir el proyecto, crear la app en Easypanel, dominio y HTTPS
—indispensable para que la PWA se pueda instalar en el celular—,
volúmenes persistentes para no perder el progreso de los niños ni volver
a descargar el modelo de IA en cada redeploy, y mantenimiento del día a
día), ver la **"Guía de despliegue en VPS"** que acompaña este proyecto.

## Estructura del proyecto

```
Dockerfile       Imagen de producción (gunicorn) para desplegar en el VPS
.dockerignore    Archivos que no se copian a la imagen (catequesis.db, caché, etc.)
backend/
  app.py         API REST + servidor de la interfaz web
  content.py     Base de conocimiento de PC01 a PC16 (96 contenidos, 960 actividades)
  motor.py       Motor de formación + reforzamiento (reglas del modelo)
  db.py          Persistencia del progreso (SQLite), separada del contenido
  nlp_eval.py    Similitud semántica para respuestas abiertas (opcional, con respaldo seguro)
  requirements.txt
frontend/
  index.html, css/, js/app.js     Interfaz web (sin frameworks)
  manifest.json, sw.js            Configuración PWA
  icons/                          Íconos de la app instalada + imágenes de San Charbel
```

## Próximos pasos para escalarlo (según el plan ya conversado)

1. **Validar con niños reales** este piloto completo de PC01 a PC16 (ya
   completos, 960 actividades en total, con bloqueo de avance y la
   animación final ya incorporados) antes de invertir más tiempo en
   ajustes adicionales.
2. **Revisar el contenido de PC11 a PC16** contra el material propio de
   la formadora, ya que estos seis encuentros se redactaron sin un
   documento maestro detallado (ver nota en "Qué incluye este piloto").
3. **Migrar de SQLite a PostgreSQL** cuando el proyecto pase a producción
   con varios grupos de catequesis usándolo a la vez.
4. **Desplegar con Docker** en tu Easypanel/VPS, junto a Evolution API,
   como ya está planteado en el documento maestro.
5. **Conectar con tu bot de WhatsApp (n8n)** para avisar a los padres
   cuando su hijo complete un encuentro, o cuando complete el camino
   completo (los 16 encuentros).
