readme_content = """# Sistema de Conciliación y Análisis de Ventas Sucursales

**Desarrollado por:** Juan Avendaño & Juan Correa  
**Programa:** Análisis y Desarrollo de Software (ADSO)  
**Ficha:** 3408936  
**Contacto:** 3137509242 | 3122606145  

---

## 1. Descripción del Proyecto

El **Sistema de Conciliación y Análisis de Ventas Sucursales** es un script automatizado en Python diseñado para unificar, consolidar y analizar datos transaccionales provenientes de diversas fuentes (archivos `.csv` y `.xlsx`) generados por distintas sucursales.

### Características principales:
* **Lectura Automática de Datos:** Detecta e ingiere todos los archivos `.csv` y `.xlsx` ubicados en el directorio del proyecto sin necesidad de especificar rutas dinámicas manualmente.
* **Estandarización y Limpieza (Data Munging):** Homogeniza nombres de columnas con inconsistencias sintácticas (ej. `Fecha_Venta` frente a `fecha`, `Valor_Unitario` frente a `precio_unitario`, `Pago` frente a `metodo_pago`).
* **Consolidación Unificada:** Fusiona las estructuras procesadas generando un reporte centralizado denominado `Informe_unido_sucursales.csv`.
* **Visualización Automática de Indicadores clave (KPIs):** Genera visualizaciones gráficas almacenadas en formato PNG dentro de la carpeta `graficos/`:
  * Ventas acumuladas por categoría de producto (Gráfico de barras).
  * Rendimiento comercial por vendedor (Gráfico de barras).
  * Distribución porcentual por método de pago (Gráfico circular/Pie chart).

---

## 2. Instrucciones de Instalación

### Requisitos Previos
* **Python 3.8+** instalado en el sistema.
* Entorno con soporte para interfaces gráficas GUI (Tkinter) para la renderización dinámica de gráficos mediante Matplotlib (`TkAgg`).

### Pasos de Instalación

## 3. docs: cómo ejecutar el proyecto

1. **Ubicación de archivos de entrada:**
   Coloca todos los archivos de datos (`.csv` y/o `.xlsx`) de las sucursales dentro de la misma carpeta donde se encuentra el script `unificacion_datos_sucursales.py`.

2. **Ejecutar el script:**
   Abre la consola o terminal en la ruta del proyecto y ejecuta:
   ```bash
   python unificacion_datos_sucursales.py

## 4. docs: resultados y hallazgos[cite: 1]

A partir de la ejecución del script y el procesamiento de los datos recolectados de las sucursales, se consolidó la información en un reporte estructurado y se generaron indicadores visuales para el análisis del negocio[cite: 1].

### Resumen de Entregables e Indicadores Generados

| Elemento / Archivo | Tipo / Formato | Descripción / Hallazgo Principal |
| :--- | :--- | :--- |
| **`Informe_unido_sucursales.csv`** | CSV Consolidado | Archivo maestro que unifica la totalidad de los datos dispersos en archivos `.csv` y `.xlsx`, estandarizando los nombres de columnas a `fecha`, `producto`, `categoria`, `cantidad`, `precio_unitario`, `vendedor` y `metodo_pago`[cite: 1]. |
| **`grafico_categoria.png`** | Gráfico de Barras | Refleja el total de unidades vendidas clasificadas por categoría de producto, lo que permite identificar rápidamente las líneas de negocio con mayor demanda[cite: 1]. |
| **`grafico_vendedor.png`** | Gráfico de Barras | Compara el volumen total de productos vendidos por cada asesor comercial, facilitando la evaluación del desempeño de ventas por ejecutivo[cite: 1]. |
| **`grafico_metodo_pago.png`** | Gráfico Circular (Pie) | Muestra la distribución porcentual de los canales de pago elegidos por los clientes (efectivo, tarjeta, transferencia, etc.)[cite: 1]. |

---

## 5. docs: conclusion final[cite: 1]

La implementación de este script automatizado aporta valor operativo y estratégico en la gestión de información comercial de las sucursales[cite: 1]:

- **Homologación Automática:** Se resuelve el problema técnico derivado de las diferencias en el formateo de datos y nombres de encabezados entre sedes (`Fecha_Venta` vs `fecha`, `Cant` vs `cantidad`, etc.), eliminando la necesidad de intervenciones manuales[cite: 1].
- **Agilidad en el Análisis:** La generación automática de archivos visuales en la carpeta `graficos/` permite a la directiva interpretar patrones de consumo y rendimiento comercial de forma ágil y precisa[cite: 1].
- **Robustez del Código:** El manejo centralizado de excepciones y la imputación/normalización de valores nulos garantizan que la consolidación de datos sea confiable e ininterrumpida[cite: 1].

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/conciliacion-ventas-sucursales.git](https://github.com/tu-usuario/conciliacion-ventas-sucursales.git)
   cd conciliacion-ventas-sucursales