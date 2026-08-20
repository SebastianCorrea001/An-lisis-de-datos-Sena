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

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/conciliacion-ventas-sucursales.git](https://github.com/tu-usuario/conciliacion-ventas-sucursales.git)
   cd conciliacion-ventas-sucursales