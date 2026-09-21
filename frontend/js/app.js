// Camino a la Primera Comunión — piloto PC01
// App de una sola página (sin frameworks) que consume la API REST del
// microservicio Flask. Guarda el código del niño en localStorage (queda
// solo en su dispositivo; el servidor no guarda datos personales, solo
// ese código).

const $app = document.getElementById("app");
const $title = document.getElementById("topbar-title");
const $back = document.getElementById("btn-back");

const NOMBRE_ENCUENTRO_POR_DEFECTO = "Camino a la Primera Comunión";
const ICONOS_TIPO = {
  sopa_letras: "🔎", verdadero_falso: "✅", seleccion_multiple: "🔘",
  unir_parejas: "🔗", completar: "✏️", crucigrama: "🧩",
  recuperacion: "🔁", reto: "🏆", aplicacion: "🌍",
};
const NOMBRES_ESTADO = {
  null: "Por comenzar", NO_LOGRADO: "Por comenzar", EN_PROCESO: "En camino",
  LOGRADO: "¡Logrado!", REQUIERE_ACOMPANAMIENTO: "Pide ayuda a tu catequista",
};

function getCodigo() { return localStorage.getItem("catequesis_codigo") || ""; }
function setCodigo(c) { localStorage.setItem("catequesis_codigo", c); }

async function api(path, opts) {
  const res = await fetch(path, opts);
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: "Error de conexión." }));
    const error = new Error(err.error || "Error de conexión.");
    // Si el servidor rechazó la petición porque el contenido/actividad
    // todavía está bloqueado (ver app.py, contenido_desbloqueado), lo
    // marcamos en el propio error para que cada pantalla pueda mostrar el
    // aviso correspondiente en vez de un error genérico.
    error.bloqueado = !!err.bloqueado;
    error.requiere = err.requiere || null;
    throw error;
  }
  return res.json();
}

// -------------------------------------------------------------- router --
window.addEventListener("hashchange", route);
window.addEventListener("DOMContentLoaded", () => {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js").catch(() => {});
  }
  // Portada "Itinerario de fe": ya NO avanza sola; espera a que el niño
  // toque la pantalla para continuar.
  const $splash = document.getElementById("splash");
  if (!$splash) { route(); return; }

  // Pequeña indicación para que el niño sepa que debe tocar la pantalla
  // (se agrega por JS para no tener que tocar también el CSS/HTML).
  const $overlay = $splash.querySelector(".splash-overlay");
  if ($overlay) {
    const $toque = document.createElement("p");
    $toque.textContent = "Toca la pantalla para continuar";
    $toque.style.cssText =
      "position:relative;z-index:1;margin:14px 0 0;color:#fff;" +
      "font-family:'Fredoka',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;" +
      "font-weight:500;font-size:0.95rem;text-shadow:0 2px 8px rgba(0,0,0,0.45);" +
      "animation:catequesis-parpadeo 1.6s ease-in-out infinite;";
    $overlay.appendChild($toque);
    const $estilo = document.createElement("style");
    $estilo.textContent = "@keyframes catequesis-parpadeo{0%,100%{opacity:1}50%{opacity:0.35}}";
    document.head.appendChild($estilo);
  }

  let avanzando = false;
  const continuar = () => {
    if (avanzando) return;
    avanzando = true;
    $splash.classList.add("splash-oculto");
    setTimeout(() => $splash.remove(), 450);
    route();
  };
  $splash.addEventListener("click", continuar);
});

$back.addEventListener("click", () => history.back());

function route() {
  const hash = location.hash.replace(/^#\/?/, "");
  const [ruta, param] = hash.split("/");

  if (!getCodigo()) return pantallaLogin();

  if (!ruta || ruta === "home") return pantallaEncuentros();
  if (ruta === "encuentro" && param) return pantallaEncuentro(param);
  if (ruta === "contenido" && param) return pantallaContenido(param);
  if (ruta === "actividad" && param) return pantallaActividad(param);
  if (ruta === "celebracion-final") return pantallaCelebracionFinal();
  return pantallaEncuentros();
}

function irA(hash) { location.hash = hash; }

// ---------------------------------------------- avisos de "no puedes avanzar" --
// Pantalla completa: cuando se llega bloqueado a un encuentro/contenido/
// actividad por URL directa (o por un enlace guardado), en vez de mostrar
// su contenido.
function pantallaBloqueada(mensaje) {
  $app.innerHTML = `
    <section class="pantalla pantalla-bloqueada">
      <p class="bloqueo-icono">🔒</p>
      <h1>Todavía no puedes entrar aquí</h1>
      <p class="mensaje">${mensaje}</p>
      <button type="button" class="btn-primario" id="btn-bloqueo-volver">Volver al inicio</button>
    </section>`;
  document.getElementById("btn-bloqueo-volver").addEventListener("click", () => irA("#/home"));
}

// Aviso corto: cuando se toca una tarjeta bloqueada dentro de una lista
// (sin navegar a otra pantalla), para no sacar al niño de donde estaba.
function mostrarAviso(mensaje) {
  let $aviso = document.getElementById("aviso-bloqueo");
  if (!$aviso) {
    $aviso = document.createElement("div");
    $aviso.id = "aviso-bloqueo";
    $aviso.className = "aviso-bloqueo";
    $app.prepend($aviso);
  }
  $aviso.innerHTML = `🔒 ${mensaje}`;
  $aviso.classList.remove("aviso-oculto");
  $aviso.scrollIntoView({ behavior: "smooth", block: "start" });
  clearTimeout($aviso._temporizador);
  $aviso._temporizador = setTimeout(() => $aviso.classList.add("aviso-oculto"), 3800);
}

function mensajeBloqueo(requiere) {
  return requiere
    ? `No puedes avanzar todavía: primero debes completar todas las actividades de «${requiere.titulo}».`
    : "No puedes avanzar todavía: primero debes completar el contenido anterior.";
}

// -------------------------------------------------------------- login --
function pantallaLogin() {
  $back.hidden = true;
  $title.textContent = NOMBRE_ENCUENTRO_POR_DEFECTO;
  const tpl = document.getElementById("tpl-login");
  $app.innerHTML = "";
  $app.appendChild(tpl.content.cloneNode(true));

  const input = document.getElementById("input-codigo");
  const entrar = () => {
    const val = input.value.trim();
    if (!val) { input.focus(); return; }
    setCodigo(val);
    irA("#/home");
    route();
  };
  document.getElementById("btn-entrar").addEventListener("click", entrar);
  input.addEventListener("keydown", (e) => { if (e.key === "Enter") entrar(); });
}

// ---------------------------------------------------- selección de encuentro --
async function pantallaEncuentros() {
  $back.hidden = true;
  $title.textContent = NOMBRE_ENCUENTRO_POR_DEFECTO;
  $app.innerHTML = '<p class="cargando">Cargando…</p>';

  try {
    const data = await api(`/api/encuentros?nino=${encodeURIComponent(getCodigo())}`);
    const { encuentros } = data;
    const caminoCompleto = encuentros.length > 0 && encuentros.every(
      (e) => e.total_actividades > 0 && e.logradas === e.total_actividades
    );

    $app.innerHTML = `
      <section class="pantalla">
        <h1>${NOMBRE_ENCUENTRO_POR_DEFECTO}</h1>
        <p class="subtitulo">${encuentros.length} encuentros</p>
        ${caminoCompleto ? `
          <button type="button" class="aviso-camino-completo" id="btn-ver-celebracion">
            <span class="titulo">🎉 ¡Completaste todo el camino!</span>
            <span class="subtitulo-aviso">Toca aquí para ver tu celebración final</span>
          </button>` : ""}
        <div class="lista-tarjetas" id="lista-encuentros"></div>
      </section>`;

    if (caminoCompleto) {
      document.getElementById("btn-ver-celebracion")
        .addEventListener("click", () => irA("#/celebracion-final"));
    }

    const $lista = document.getElementById("lista-encuentros");
    encuentros.forEach((e, i) => {
      const completo = e.total_actividades > 0 && e.logradas === e.total_actividades;
      const bloqueado = e.desbloqueado === false;
      const btn = document.createElement("button");
      btn.className = "tarjeta" + (bloqueado ? " tarjeta-bloqueada" : "");
      btn.innerHTML = `
        <span class="num">${bloqueado ? "🔒" : i + 1}</span>
        <span class="info">
          <span class="titulo">${e.titulo}</span>
          <span class="subinfo">${e.texto_biblico} · ${e.logradas}/${e.total_actividades} actividades logradas</span>
        </span>
        <span class="badge badge-${completo ? "LOGRADO" : (e.logradas > 0 ? "EN_PROCESO" : "NO_LOGRADO")}">
          ${completo ? "¡Completo!" : (e.logradas > 0 ? "En camino" : "Por comenzar")}
        </span>`;
      btn.addEventListener("click", () => {
        if (bloqueado) { mostrarAviso(mensajeBloqueo(e.requiere)); return; }
        irA(`#/encuentro/${e.id}`);
      });
      $lista.appendChild(btn);
    });
  } catch (e) {
    $app.innerHTML = `<p class="vacio">${e.message}</p>`;
  }
}

// --------------------------------------------------------------- encuentro --
async function pantallaEncuentro(encuentroId) {
  $back.hidden = false;
  $app.innerHTML = '<p class="cargando">Cargando…</p>';

  try {
    const data = await api(`/api/encuentro/${encuentroId}?nino=${encodeURIComponent(getCodigo())}`);
    if (data.encuentro_desbloqueado === false) {
      $title.textContent = data.encuentro.titulo;
      pantallaBloqueada(mensajeBloqueo(data.requiere));
      return;
    }
    const { encuentro, contenidos } = data;
    $title.textContent = encuentro.titulo;

    const totalLogrado = contenidos.filter((c) => c.estado === "LOGRADO").length;

    $app.innerHTML = `
      <section class="pantalla">
        <h1>${encuentro.titulo}</h1>
        <p class="subtitulo">${encuentro.texto_biblico} · ${contenidos.length} temas</p>
        <div class="barra-progreso"><div style="width:${(totalLogrado / contenidos.length) * 100}%"></div></div>
        <div class="lista-tarjetas" id="lista-contenidos"></div>
      </section>`;

    const $lista = document.getElementById("lista-contenidos");
    contenidos.forEach((c, i) => {
      const bloqueado = c.desbloqueado === false;
      const btn = document.createElement("button");
      btn.className = "tarjeta" + (bloqueado ? " tarjeta-bloqueada" : "");
      btn.innerHTML = `
        <span class="num">${bloqueado ? "🔒" : i + 1}</span>
        <span class="info">
          <span class="titulo">${c.titulo}</span>
          <span class="subinfo">${c.logradas}/${c.total_actividades} actividades logradas</span>
        </span>
        <span class="badge badge-${c.estado}">${NOMBRES_ESTADO[c.estado]}</span>`;
      btn.addEventListener("click", () => {
        if (bloqueado) { mostrarAviso(mensajeBloqueo(c.requiere)); return; }
        irA(`#/contenido/${c.id}`);
      });
      $lista.appendChild(btn);
    });
  } catch (e) {
    if (e.bloqueado) { pantallaBloqueada(mensajeBloqueo(e.requiere)); return; }
    $app.innerHTML = `<p class="vacio">${e.message}</p>`;
  }
}

// ---------------------------------------------------------- contenido --
async function pantallaContenido(contenidoId) {
  $back.hidden = false;
  $app.innerHTML = '<p class="cargando">Cargando…</p>';

  try {
    const data = await api(`/api/contenido/${contenidoId}/actividades?nino=${encodeURIComponent(getCodigo())}`);
    $title.textContent = data.titulo;

    $app.innerHTML = `<section class="pantalla"><div class="lista-tarjetas" id="lista-act"></div></section>`;
    const $lista = document.getElementById("lista-act");
    data.actividades.forEach((a, i) => {
      const btn = document.createElement("button");
      btn.className = "tarjeta";
      btn.innerHTML = `
        <span class="num">${ICONOS_TIPO[a.tipo] || "•"}</span>
        <span class="info">
          <span class="titulo">${a.titulo}</span>
          <span class="subinfo">${a.intentos > 0 ? `${a.intentos} intento(s)` : "Sin comenzar"}</span>
        </span>
        <span class="badge badge-${a.estado}">${NOMBRES_ESTADO[a.estado]}</span>`;
      btn.addEventListener("click", () => irA(`#/actividad/${a.id}`));
      $lista.appendChild(btn);
    });
  } catch (e) {
    if (e.bloqueado) { pantallaBloqueada(mensajeBloqueo(e.requiere)); return; }
    $app.innerHTML = `<p class="vacio">${e.message}</p>`;
  }
}

// ---------------------------------------------------------- actividad --
async function pantallaActividad(actividadId) {
  $back.hidden = false;
  $app.innerHTML = '<p class="cargando">Cargando…</p>';

  let actividad;
  try {
    actividad = await api(`/api/actividad/${actividadId}?nino=${encodeURIComponent(getCodigo())}`);
  } catch (e) {
    if (e.bloqueado) { pantallaBloqueada(mensajeBloqueo(e.requiere)); return; }
    $app.innerHTML = `<p class="vacio">${e.message}</p>`;
    return;
  }
  $title.textContent = actividad.titulo;

  const estadoInteraccion = {
    seleccionMultiple: [], vf: [], parejas: [], completar: [], sopaEncontradas: [], retoChips: [], crucigrama: [],
  };

  $app.innerHTML = `
    <section class="pantalla">
      <h2 class="actividad-titulo">${ICONOS_TIPO[actividad.tipo] || ""} ${actividad.titulo}</h2>
      ${actividad.instruccion ? `<p class="situacion">${actividad.instruccion}</p>` : ""}
      ${actividad.situacion ? `<p class="situacion">${actividad.situacion}</p>` : ""}
      <div id="cuerpo-actividad"></div>
      ${actividad.reflexion ? `<p class="reflexion">💭 Para conversar: ${actividad.reflexion}</p>` : ""}
      <button id="btn-comprobar" class="btn-primario">Comprobar</button>
      <div id="panel-feedback"></div>
    </section>`;

  const $cuerpo = document.getElementById("cuerpo-actividad");
  const $feedback = document.getElementById("panel-feedback");
  const $comprobar = document.getElementById("btn-comprobar");

  renderCuerpo(actividad, $cuerpo, estadoInteraccion);

  $comprobar.addEventListener("click", async () => {
    const respuestas = recolectarRespuestas(actividad, estadoInteraccion);
    $comprobar.disabled = true;
    try {
      const r = await api(`/api/actividad/${actividadId}/responder`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nino: getCodigo(), respuestas }),
      });
      mostrarFeedback(r, $feedback, actividad);
      if (r.logrado) {
        $comprobar.textContent = "¡Listo! Volver al tema";
        $comprobar.onclick = () => irA(`#/contenido/${actividad.contenido_id}`);
        $comprobar.disabled = false;
      } else {
        $comprobar.disabled = false;
      }
    } catch (e) {
      $feedback.innerHTML = `<div class="panel-feedback"><p class="mensaje">${e.message}</p></div>`;
      $comprobar.disabled = false;
    }
  });
}

function mostrarFeedback(r, $feedback, actividad) {
  const clase = r.logrado ? "ok" : (r.estado_actividad === "REQUIERE_ACOMPANAMIENTO" ? "acompanamiento" : "");
  let extra = "";
  if (r.pista) extra += `<p class="pista">💡 Pista: ${r.pista}</p>`;
  if (r.respuesta_correcta) extra += `<p class="respuesta">Respuesta: ${formatearRespuesta(actividad, r.respuesta_correcta)}</p>`;

  // Si con esta actividad se completaron TODAS las del contenido (no solo
  // esta), se invita de una vez a seguir con el siguiente tema. Si además
  // era el último contenido de todo el itinerario (PC16-C06, los 16
  // encuentros), en vez del aviso genérico se invita a ver la animación
  // final del camino (ver camino_completo en app.py).
  let bannerContenido = "";
  if (r.logrado && r.camino_completo) {
    bannerContenido = `
      <div class="panel-contenido-logrado">
        <p class="mensaje">🎉 ¡Felicidades! Terminaste «${r.contenido_titulo}» y completaste todo tu camino hacia la Primera Comunión.</p>
        <button type="button" class="btn-primario" id="btn-siguiente-contenido">Ver mi celebración final</button>
      </div>`;
  } else if (r.logrado && r.contenido_completo) {
    bannerContenido = r.siguiente_contenido
      ? `<div class="panel-contenido-logrado">
           <p class="mensaje">🎉 ¡Felicidades! Terminaste las actividades de «${r.contenido_titulo}».</p>
           <button type="button" class="btn-primario" id="btn-siguiente-contenido">Continuar a: ${r.siguiente_contenido.titulo}</button>
         </div>`
      : `<div class="panel-contenido-logrado">
           <p class="mensaje">🎉 ¡Felicidades! Terminaste las actividades de «${r.contenido_titulo}» y completaste todo el encuentro.</p>
           <button type="button" class="btn-primario" id="btn-siguiente-contenido">Volver al inicio</button>
         </div>`;
  }

  $feedback.innerHTML = `
    <div class="panel-feedback ${clase}">
      <p class="mensaje">${r.mensaje}</p>
      <p class="subinfo">Aciertos: ${r.aciertos}/${r.total} · Necesitas: ${r.requisito}/${r.total}</p>
      ${extra}
    </div>
    ${bannerContenido}`;

  const $btnSiguiente = document.getElementById("btn-siguiente-contenido");
  if ($btnSiguiente) {
    $btnSiguiente.addEventListener("click", () => {
      if (r.camino_completo) { irA("#/celebracion-final"); return; }
      irA(r.siguiente_contenido ? `#/contenido/${r.siguiente_contenido.id}` : "#/home");
    });
  }
}

// ---------------------------------------------------- celebración final --
// Animación de cierre: un camino con los 16 encuentros recorridos, un niño
// que se suma en cada uno, hasta llegar a un altar donde Jesús los recibe
// con los brazos abiertos. Se llega aquí al terminar la última actividad
// del último contenido (PC16-C06) — ver camino_completo — o, después, desde
// el aviso que queda en la pantalla de inicio una vez completado todo.
async function pantallaCelebracionFinal() {
  $back.hidden = false;
  $app.innerHTML = '<p class="cargando">Cargando…</p>';

  try {
    const data = await api(`/api/encuentros?nino=${encodeURIComponent(getCodigo())}`);
    const { encuentros } = data;
    const caminoCompleto = encuentros.length > 0 && encuentros.every(
      (e) => e.total_actividades > 0 && e.logradas === e.total_actividades
    );
    if (!caminoCompleto) { irA("#/home"); return; }

    $title.textContent = "¡Felicidades!";
    $app.innerHTML = `
      <section class="pantalla pantalla-celebracion">
        <h1>Tu camino a la Primera Comunión</h1>
        <div class="celebracion-escena">
          <svg class="celebracion-svg" viewBox="0 0 320 600" preserveAspectRatio="xMidYMid meet">
            <path id="camino-path" class="camino-linea"
              d="M36 580 C 130 540, 250 520, 180 470 C 110 420, 24 410, 86 360
                 C 148 310, 268 300, 208 250 C 158 210, 66 206, 118 166
                 C 150 142, 188 134, 202 126" />
            <g id="grupo-altar-pos" transform="translate(202,80) scale(1.5)">
              <g id="grupo-altar" class="altar-grupo">
                <circle class="jesus-halo" cx="0" cy="-27" r="13"></circle>
                <path d="M -10 -6 C -10 -18 10 -18 10 -6 L 13 22 L -13 22 Z"
                      fill="#EAF1F7" stroke="var(--azul-claro)" stroke-width="1.3"></path>
                <circle cx="0" cy="-16" r="6.5" fill="var(--crema)" stroke="var(--azul)" stroke-width="1.2"></circle>
                <path d="M -10 -4 C -20 2 -24 14 -22 22" fill="none" stroke="var(--azul-claro)" stroke-width="3" stroke-linecap="round"></path>
                <path d="M 10 -4 C 20 2 24 14 22 22" fill="none" stroke="var(--azul-claro)" stroke-width="3" stroke-linecap="round"></path>
                <rect x="-26" y="24" width="52" height="10" rx="2" fill="var(--dorado)"></rect>
                <rect x="-2" y="6" width="4" height="16" fill="var(--dorado-claro)"></rect>
                <rect x="-20" y="2" width="4" height="12" fill="var(--rojo)"></rect>
                <rect x="16" y="2" width="4" height="12" fill="var(--rojo)"></rect>
              </g>
            </g>
          </svg>
          <div class="celebracion-confeti" id="confeti"></div>
          <div class="celebracion-texto" id="texto-final">
            <p class="celebracion-mensaje">🎉 ¡Lo lograste!</p>
            <p class="celebracion-submensaje">
              Recorriste los ${encuentros.length} encuentros de tu camino a la Primera Comunión.
              Jesús te recibe hoy con los brazos abiertos, como su amigo y misionero.
            </p>
          </div>
        </div>
        <button type="button" class="btn-primario celebracion-boton" id="btn-celebracion-volver">Volver al inicio</button>
      </section>`;

    animarCaminoCelebracion(encuentros.length);

    document.getElementById("btn-celebracion-volver").addEventListener("click", () => irA("#/home"));
  } catch (e) {
    $app.innerHTML = `<p class="vacio">${e.message}</p>`;
  }
}

function animarCaminoCelebracion(totalEncuentros) {
  const $path = document.getElementById("camino-path");
  const $svg = document.querySelector(".celebracion-svg");
  const $altarPos = document.getElementById("grupo-altar-pos");
  const $altarGlow = document.getElementById("grupo-altar");
  const $confeti = document.getElementById("confeti");
  const $texto = document.getElementById("texto-final");
  if (!$path || !$svg) return;

  const COLORES = ["var(--azul-claro)", "var(--verde)", "var(--rojo)", "var(--dorado)"];
  const largo = $path.getTotalLength();
  const pasoMs = 240; // separación entre la aparición de cada niño
  const svgNS = "http://www.w3.org/2000/svg";
  // Tamaño del niño (1.4x la figura base). Se calcula así, en vez de usar un
  // atributo transform="scale(...)" en el mismo <g> que además anima su
  // "transform" por CSS (ver .nino-camino), porque en SVG un atributo
  // transform y una animación/transición CSS de la propiedad "transform" en
  // el MISMO elemento compiten entre sí y la CSS termina "ganando" y
  // reemplazando el atributo — el niño (y, con el mismo problema, el altar)
  // aparecía encogido en la esquina superior izquierda en vez de en su
  // punto del camino. La solución: un <g> exterior solo con la posición
  // (atributo, sin CSS que la toque) y un <g> interior solo con la
  // animación CSS (sin atributo transform propio).
  const s = 1.4;

  // Un punto por encuentro, repartidos a lo largo del camino (dejando el
  // último tramo libre para el altar, que ya está dibujado en el extremo).
  for (let i = 0; i < totalEncuentros; i++) {
    const fraccion = (i + 0.5) / totalEncuentros;
    const punto = $path.getPointAtLength(largo * fraccion * 0.94);
    const color = COLORES[i % COLORES.length];

    const marca = document.createElementNS(svgNS, "circle");
    marca.setAttribute("class", "camino-punto");
    marca.setAttribute("cx", punto.x);
    marca.setAttribute("cy", punto.y);
    marca.setAttribute("r", "3.6");
    $svg.insertBefore(marca, $altarPos);

    const ninoPos = document.createElementNS(svgNS, "g");
    ninoPos.setAttribute("transform", `translate(${punto.x},${punto.y - 11})`);
    const nino = document.createElementNS(svgNS, "g");
    nino.setAttribute("class", "nino-camino");
    nino.style.animationDelay = `${i * pasoMs}ms`;
    nino.innerHTML = `
      <path d="M ${-4.5 * s} ${3 * s} C ${-4.5 * s} ${-3 * s} ${4.5 * s} ${-3 * s} ${4.5 * s} ${3 * s}
               L ${5.5 * s} ${10 * s} L ${-5.5 * s} ${10 * s} Z" fill="${color}"></path>
      <circle class="nino-cabeza" cx="0" cy="${-1 * s}" r="${3.4 * s}"></circle>`;
    ninoPos.appendChild(nino);
    $svg.insertBefore(ninoPos, $altarPos);
  }

  const finCaminoMs = totalEncuentros * pasoMs + 550;

  setTimeout(() => {
    if ($altarGlow) $altarGlow.classList.add("brillo");
    const $halo = document.querySelector(".jesus-halo");
    if ($halo) $halo.classList.add("pulso");
  }, finCaminoMs);
  setTimeout(() => {
    if ($texto) $texto.classList.add("visible");
    lanzarConfeti($confeti);
  }, finCaminoMs + 450);
}

function lanzarConfeti($contenedor) {
  if (!$contenedor) return;
  const COLORES = ["var(--dorado)", "var(--rojo)", "var(--verde)", "var(--azul-claro)", "var(--dorado-claro)"];
  for (let i = 0; i < 26; i++) {
    const pieza = document.createElement("span");
    pieza.className = "pieza-confeti";
    pieza.style.left = `${Math.random() * 100}%`;
    pieza.style.background = COLORES[i % COLORES.length];
    pieza.style.animationDuration = `${1.6 + Math.random() * 1.2}s`;
    pieza.style.animationDelay = `${Math.random() * 0.6}s`;
    $contenedor.appendChild(pieza);
  }
}

function formatearRespuesta(actividad, resp) {
  if (actividad.tipo === "verdadero_falso") return resp.map((b) => (b ? "Verdadero" : "Falso")).join(" · ");
  if (actividad.tipo === "unir_parejas") return resp.map((p) => `${p.termino} → ${p.definicion}`).join(" · ");
  return Array.isArray(resp) ? resp.join(", ") : String(resp);
}

// -------------------------------------------------- render por tipo --
function renderCuerpo(actividad, $cuerpo, estado) {
  const tipo = actividad.tipo;
  if (tipo === "verdadero_falso") return renderVF(actividad, $cuerpo, estado);
  if (tipo === "seleccion_multiple" || tipo === "aplicacion") return renderSM(actividad, $cuerpo, estado);
  if (tipo === "unir_parejas") return renderUP(actividad, $cuerpo, estado);
  if (tipo === "crucigrama") return renderCrucigrama(actividad, $cuerpo, estado);
  if (tipo === "completar" || tipo === "recuperacion") return renderCO(actividad, $cuerpo, estado);
  if (tipo === "sopa_letras") return renderSL(actividad, $cuerpo, estado);
  if (tipo === "reto") return renderReto(actividad, $cuerpo, estado);
}

function recolectarRespuestas(actividad, estado) {
  const tipo = actividad.tipo;
  if (tipo === "verdadero_falso") return estado.vf;
  if (tipo === "seleccion_multiple" || tipo === "aplicacion") return estado.seleccionMultiple;
  if (tipo === "unir_parejas") return estado.parejas;
  if (tipo === "crucigrama") return estado.crucigrama;
  if (tipo === "completar" || tipo === "recuperacion") return estado.completar;
  if (tipo === "sopa_letras") return estado.sopaEncontradas;
  if (tipo === "reto") return actividad.modo === "preguntas" ? estado.seleccionMultiple : estado.retoChips;
}

function renderVF(actividad, $cuerpo, estado) {
  estado.vf = actividad.items.map(() => null);
  $cuerpo.innerHTML = actividad.items.map((it, i) => `
    <div class="item-pregunta">
      <p class="texto">${it.texto}</p>
      <div class="vf-botones" data-idx="${i}">
        <button class="vf-boton" data-val="true">Verdadero</button>
        <button class="vf-boton" data-val="false">Falso</button>
      </div>
    </div>`).join("");

  $cuerpo.querySelectorAll(".vf-botones").forEach((grupo) => {
    const idx = Number(grupo.dataset.idx);
    grupo.querySelectorAll(".vf-boton").forEach((btn) => {
      btn.addEventListener("click", () => {
        grupo.querySelectorAll(".vf-boton").forEach((b) => b.classList.remove("seleccionada"));
        btn.classList.add("seleccionada");
        estado.vf[idx] = btn.dataset.val === "true";
      });
    });
  });
}

function renderSM(actividad, $cuerpo, estado) {
  estado.seleccionMultiple = actividad.items.map(() => -1);
  $cuerpo.innerHTML = actividad.items.map((it, i) => `
    <div class="item-pregunta">
      <p class="texto">${it.texto}</p>
      <div class="opciones" data-idx="${i}">
        ${it.opciones.map((op, j) => `<button class="opcion" data-val="${j}">${op}</button>`).join("")}
      </div>
    </div>`).join("");

  $cuerpo.querySelectorAll(".opciones").forEach((grupo) => {
    const idx = Number(grupo.dataset.idx);
    grupo.querySelectorAll(".opcion").forEach((btn) => {
      btn.addEventListener("click", () => {
        grupo.querySelectorAll(".opcion").forEach((b) => b.classList.remove("seleccionada"));
        btn.classList.add("seleccionada");
        estado.seleccionMultiple[idx] = Number(btn.dataset.val);
      });
    });
  });
}

function renderUP(actividad, $cuerpo, estado) {
  estado.parejas = [];
  const terminos = mezclar(actividad.terminos.map((t, i) => ({ t, i })));
  const definiciones = mezclar(actividad.definiciones.map((d, i) => ({ d, i })));
  let seleccionTermino = null, seleccionDef = null;
  const emparejados = new Set();

  $cuerpo.innerHTML = `
    <div class="parejas-cols">
      <div class="parejas-col" id="col-terminos"></div>
      <div class="parejas-col" id="col-defs"></div>
    </div>
    <div class="parejas-lista" id="lista-parejas">Aún no has unido ninguna pareja.</div>`;

  const $colT = document.getElementById("col-terminos");
  const $colD = document.getElementById("col-defs");
  const $lista = document.getElementById("lista-parejas");

  terminos.forEach(({ t, i }) => {
    const b = document.createElement("button");
    b.className = "pareja-item"; b.textContent = t; b.dataset.i = i;
    b.addEventListener("click", () => {
      if (b.classList.contains("emparejada")) return;
      $colT.querySelectorAll(".pareja-item").forEach((x) => x.classList.remove("seleccionada"));
      b.classList.add("seleccionada");
      seleccionTermino = { el: b, texto: t };
      intentarEmparejar();
    });
    $colT.appendChild(b);
  });

  definiciones.forEach(({ d, i }) => {
    const b = document.createElement("button");
    b.className = "pareja-item"; b.textContent = d; b.dataset.i = i;
    b.addEventListener("click", () => {
      if (b.classList.contains("emparejada")) return;
      $colD.querySelectorAll(".pareja-item").forEach((x) => x.classList.remove("seleccionada"));
      b.classList.add("seleccionada");
      seleccionDef = { el: b, texto: d };
      intentarEmparejar();
    });
    $colD.appendChild(b);
  });

  function intentarEmparejar() {
    if (!seleccionTermino || !seleccionDef) return;
    seleccionTermino.el.classList.add("emparejada");
    seleccionDef.el.classList.add("emparejada");
    seleccionTermino.el.classList.remove("seleccionada");
    seleccionDef.el.classList.remove("seleccionada");
    estado.parejas.push({ termino: seleccionTermino.texto, definicion: seleccionDef.texto });
    $lista.textContent = estado.parejas.map((p) => `${p.termino} → ${p.definicion}`).join(" · ");
    seleccionTermino = null; seleccionDef = null;
  }
}

function renderCO(actividad, $cuerpo, estado) {
  estado.completar = actividad.items.map(() => "");
  $cuerpo.innerHTML = actividad.items.map((it, i) => `
    <div class="item-pregunta">
      <p class="texto">${it.texto}</p>
      ${it.abierta
        ? `<textarea class="input-completar input-abierta" data-idx="${i}" rows="3" placeholder="Escribe tu respuesta con tus propias palabras"></textarea>`
        : `<input type="text" class="input-completar" data-idx="${i}" placeholder="Escribe tu respuesta" />`}
      ${it.banco && it.banco.length ? `<div class="chips" data-idx="${i}">
        ${it.banco.map((op) => `<button type="button" class="chip" data-val="${op}">${op}</button>`).join("")}
      </div>` : ""}
    </div>`).join("");

  $cuerpo.querySelectorAll(".input-completar").forEach((input) => {
    const idx = Number(input.dataset.idx);
    input.addEventListener("input", () => { estado.completar[idx] = input.value; });
  });

  $cuerpo.querySelectorAll(".chips").forEach((grupo) => {
    const idx = Number(grupo.dataset.idx);
    const input = $cuerpo.querySelector(`.input-completar[data-idx="${idx}"]`);
    grupo.querySelectorAll(".chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        grupo.querySelectorAll(".chip").forEach((c) => c.classList.remove("seleccionada"));
        chip.classList.add("seleccionada");
        input.value = chip.dataset.val;
        estado.completar[idx] = chip.dataset.val;
      });
    });
  });
}

function renderCrucigrama(actividad, $cuerpo, estado) {
  const { filas, columnas, palabras } = actividad;
  estado.crucigrama = palabras.map(() => "");

  const numeroPorCelda = {};
  const celdasActivas = new Set();
  palabras.forEach((p) => {
    numeroPorCelda[`${p.fila},${p.columna}`] = p.num;
    const dr = p.direccion === "V" ? 1 : 0, dc = p.direccion === "V" ? 0 : 1;
    for (let i = 0; i < p.longitud; i++) {
      celdasActivas.add(`${p.fila + dr * i},${p.columna + dc * i}`);
    }
  });

  $cuerpo.innerHTML = "";
  const $grid = document.createElement("div");
  $grid.className = "cruci-grid";
  $grid.style.gridTemplateColumns = `repeat(${columnas}, 28px)`;

  const inputPorCelda = {};
  for (let r = 0; r < filas; r++) {
    for (let c = 0; c < columnas; c++) {
      const key = `${r},${c}`;
      const $cel = document.createElement("div");
      if (!celdasActivas.has(key)) {
        $cel.className = "cruci-celda cruci-bloqueada";
        $grid.appendChild($cel);
        continue;
      }
      $cel.className = "cruci-celda";
      if (numeroPorCelda[key]) {
        const $num = document.createElement("span");
        $num.className = "cruci-num";
        $num.textContent = numeroPorCelda[key];
        $cel.appendChild($num);
      }
      const $input = document.createElement("input");
      $input.maxLength = 1;
      $input.autocomplete = "off";
      $input.className = "cruci-input";
      $cel.appendChild($input);
      inputPorCelda[key] = $input;
      $grid.appendChild($cel);
    }
  }

  const inputsPorPalabra = palabras.map((p) => {
    const dr = p.direccion === "V" ? 1 : 0, dc = p.direccion === "V" ? 0 : 1;
    const inputs = [];
    for (let i = 0; i < p.longitud; i++) {
      inputs.push(inputPorCelda[`${p.fila + dr * i},${p.columna + dc * i}`]);
    }
    return inputs;
  });

  function actualizarRespuestas() {
    estado.crucigrama = inputsPorPalabra.map((inputs) => inputs.map((inp) => inp.value || "").join(""));
  }

  Object.values(inputPorCelda).forEach(($input) => {
    $input.addEventListener("input", () => {
      $input.value = $input.value.toUpperCase().slice(-1);
      actualizarRespuestas();
    });
  });

  $cuerpo.appendChild($grid);

  const horizontales = palabras.filter((p) => p.direccion === "H").sort((a, b) => a.num - b.num);
  const verticales = palabras.filter((p) => p.direccion === "V").sort((a, b) => a.num - b.num);
  const $claves = document.createElement("div");
  $claves.className = "cruci-claves";
  $claves.innerHTML = `
    ${horizontales.length ? `<p class="cruci-claves-titulo">Horizontales</p>
      <ol>${horizontales.map((p) => `<li><b>${p.num}.</b> ${p.clave}</li>`).join("")}</ol>` : ""}
    ${verticales.length ? `<p class="cruci-claves-titulo">Verticales</p>
      <ol>${verticales.map((p) => `<li><b>${p.num}.</b> ${p.clave}</li>`).join("")}</ol>` : ""}`;
  $cuerpo.appendChild($claves);
}

function renderSL(actividad, $cuerpo, estado) {
  estado.sopaEncontradas = [];
  const grid = actividad.grid;
  const tam = grid.length;
  let inicio = null;

  $cuerpo.innerHTML = `
    <div class="sopa-grid" id="sopa-grid" style="grid-template-columns:repeat(${tam}, 26px)"></div>
    <p class="subinfo">Toca la primera letra de una palabra y luego la última (en línea recta).</p>
    <div class="sopa-lista-palabras" id="sopa-palabras">
      ${actividad.palabras.map((p) => `<span data-p="${normaliza(p)}">${p}</span>`).join("")}
    </div>`;

  const $grid = document.getElementById("sopa-grid");
  for (let r = 0; r < tam; r++) {
    for (let c = 0; c < tam; c++) {
      const cel = document.createElement("div");
      cel.className = "sopa-celda";
      cel.textContent = grid[r][c];
      cel.dataset.r = r; cel.dataset.c = c;
      cel.addEventListener("click", () => onClickCelda(cel));
      $grid.appendChild(cel);
    }
  }

  function onClickCelda(cel) {
    if (cel.classList.contains("encontrada")) return;
    if (!inicio) {
      limpiarSeleccion();
      inicio = cel;
      cel.classList.add("seleccionada");
      return;
    }
    const r0 = Number(inicio.dataset.r), c0 = Number(inicio.dataset.c);
    const r1 = Number(cel.dataset.r), c1 = Number(cel.dataset.c);
    const celdas = extraerLinea(r0, c0, r1, c1);
    if (celdas) {
      celdas.forEach((cc) => cc.classList.add("seleccionada"));
      const palabra = celdas.map((cc) => cc.textContent).join("");
      const palabraInv = celdas.map((cc) => cc.textContent).join("").split("").reverse().join("");
      const match = actividad.palabras.find((p) => normaliza(p) === palabra || normaliza(p) === palabraInv);
      if (match && !estado.sopaEncontradas.includes(match)) {
        estado.sopaEncontradas.push(match);
        celdas.forEach((cc) => { cc.classList.remove("seleccionada"); cc.classList.add("encontrada"); });
        const $chip = document.querySelector(`#sopa-palabras span[data-p="${normaliza(match)}"]`);
        if ($chip) $chip.classList.add("encontrada");
      } else {
        setTimeout(limpiarSeleccion, 300);
      }
    } else {
      limpiarSeleccion();
    }
    inicio = null;
  }

  function limpiarSeleccion() {
    $grid.querySelectorAll(".sopa-celda.seleccionada").forEach((c) => c.classList.remove("seleccionada"));
  }

  function extraerLinea(r0, c0, r1, c1) {
    if (r0 !== r1 && c0 !== c1) return null; // solo horizontal o vertical
    const celdas = [];
    const dr = Math.sign(r1 - r0), dc = Math.sign(c1 - c0);
    const pasos = Math.max(Math.abs(r1 - r0), Math.abs(c1 - c0));
    for (let i = 0; i <= pasos; i++) {
      const r = r0 + dr * i, c = c0 + dc * i;
      const el = $grid.querySelector(`.sopa-celda[data-r="${r}"][data-c="${c}"]`);
      if (!el) return null;
      celdas.push(el);
    }
    return celdas;
  }
}

function renderReto(actividad, $cuerpo, estado) {
  const timerHtml = `<p class="cronometro" id="cronometro">⏱ ${actividad.tiempo_segundos}s</p>`;

  if (actividad.modo === "preguntas") {
    $cuerpo.innerHTML = timerHtml;
    const $sub = document.createElement("div");
    $cuerpo.appendChild($sub);
    renderSM(actividad, $sub, estado);
  } else {
    estado.retoChips = [];
    $cuerpo.innerHTML = `
      ${timerHtml}
      <div class="chips chips-grande" id="reto-chips">
        ${actividad.banco.map((op) => `<button type="button" class="chip" data-val="${op}">${op}</button>`).join("")}
      </div>
      <p class="subinfo">Selecciona al menos ${actividad.minimo} ${actividad.minimo === 1 ? "opción" : "opciones"}.</p>`;

    $cuerpo.querySelectorAll("#reto-chips .chip").forEach((chip) => {
      chip.addEventListener("click", () => {
        const val = chip.dataset.val;
        chip.classList.toggle("seleccionada");
        if (chip.classList.contains("seleccionada")) {
          estado.retoChips.push(val);
        } else {
          estado.retoChips = estado.retoChips.filter((v) => v !== val);
        }
      });
    });
  }

  iniciarCronometro(actividad.tiempo_segundos);
}

function iniciarCronometro(segundos) {
  const $el = document.getElementById("cronometro");
  if (!$el) return;
  let restante = segundos;
  const id = setInterval(() => {
    restante -= 1;
    if (!document.getElementById("cronometro")) { clearInterval(id); return; }
    if (restante <= 0) {
      document.getElementById("cronometro").textContent = "⏱ ¡Tiempo! Puedes seguir igual.";
      clearInterval(id);
    } else {
      document.getElementById("cronometro").textContent = `⏱ ${restante}s`;
    }
  }, 1000);
}

// ------------------------------------------------------------- utils --
function mezclar(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function normaliza(s) {
  return s.normalize("NFKD").replace(/[̀-ͯ]/g, "").toUpperCase();
}
