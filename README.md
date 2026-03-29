# ⚽ FC Barcelona Scouting Analytics: UCL 25/26

> **"No es solo un Dashboard. Es una herramienta de Scouting 100% automatizada." 🚀**

Este repositorio contiene el código fuente, los datasets y el archivo de Power BI correspondientes a mi proyecto de **Sports Data Analytics End-to-End**. El objetivo de este proyecto es auditar el rendimiento ofensivo y táctico del FC Barcelona durante la presente edición de la UEFA Champions League, transformando datos web crudos en un Dashboard Ejecutivo interactivo.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Extracción de Datos:** `undetected-chromedriver`, `selenium`, `re` (RegEx)
* **Transformación (ETL):** `pandas`, `io.StringIO`
* **Visualización & Modelado:** Power BI, DAX
* **Diseño UI:** Canva

---

## 🏗️ Arquitectura del Proyecto (End-to-End)

El verdadero reto de este proyecto reside en el "Back-End" técnico, dividido en tres fases principales:

### 1. Web Scraping & Data Engineering (Python)
Para automatizar la ingesta de datos desde **FBref**, desarrollé un script de extracción robusto:
* **Bypass de Anti-Bots:** Implementación de `undetected_chromedriver` configurado en modo seguro (`--disable-gpu`, `--no-sandbox`) para negociar y evadir las protecciones de Cloudflare.
* **Procesamiento de HTML:** Extracción del `page_source` y limpieza inicial con expresiones regulares para habilitar la lectura de tablas ocultas.
* **Transformación con Pandas:** * Aplanamiento de cabeceras de múltiples niveles (`MultiIndex`).
  * Eliminación de filas agregadas (`Squad Total`, `Opponent Total`) que ensucian la muestra.
  * Cruce de tablas (`pd.merge`) entre las estadísticas generales (*Standard Stats*) y los minutos de juego (*Playing Time*), eliminando columnas duplicadas mediante la intersección de *sets*.
* **Output:** Generación automática de un dataset maestro limpio listo para ingesta.

### 2. Modelado de Datos y Lógica de Negocio (DAX)
Ya en Power BI, se desarrollaron medidas personalizadas para elevar los números brutos a *insights* analíticos:
* **Positional Impact:** Sobrescritura de la taxonomía original de FBref mediante funciones lógicas condicionales (`SWITCH`). Esto asegura que perfiles como Lamine Yamal o Raphinha sean evaluados por su rol táctico real (*Forwards*) y no por etiquetas desfasadas del proveedor de datos.
* **Performance Matrix:** Creación de métricas normalizadas cruzando el Volumen de Juego (Minutos) y la Eficiencia (G+A per 90 min) para alimentar los gráficos de dispersión.

### 3. Diseño Visual y UX/UI
Desarrollo de una interfaz inmersiva que respeta la identidad corporativa del club (Blaugrana y Dorado).
* Implementación de **Bookmarks** (estado de sesión) para el reseteo de filtros (Botón "Reset Filters").
* Uso de segmentaciones dinámicas y menús interactivos con estados *hover* para una navegación fluida por posiciones y nacionalidades.

---

## 🏆 Insights Destacados

* **Top Attacking Contributors:** Fermín López lidera la producción ofensiva global con **6 goles y 4 asistencias**, demostrando una eficiencia letal en la competición europea.
* **Squad Age Profile:** La distribución de minutos revela el impacto estructural de *La Masia*. El bloque de jugadores Sub-21 acumula una cuota de minutos inusual para un aspirante a la Champions League, sosteniendo el sistema del equipo.

---

## 📂 Estructura del Repositorio

```text
├── scraper_fbref.py                  # Script principal de extracción y limpieza
├── barca_ucl_stats_automated.csv     # Dataset final generado por el script
├── FC_Barcelona_Dashboard.pbix       # Archivo original de Power BI
└── README.md                         # Documentación del proyecto
