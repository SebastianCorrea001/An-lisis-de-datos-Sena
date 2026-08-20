""" By: JUAN AVENDAÑO - JUAN CORREA 3408936 
 3137509242 --- 3122606145 
 ADSO   
"""

import glob
import os

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd


def cargar_archivos():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_files = sorted(glob.glob(os.path.join(base_dir, "*.csv")))
    xlsx_files = sorted(glob.glob(os.path.join(base_dir, "*.xlsx")))

    data_csv = []
    if csv_files:
        for archivo in csv_files:
            data_csv.append(pd.read_csv(archivo))
        concatenated_csv = pd.concat(data_csv, ignore_index=True)
    else:
        concatenated_csv = pd.DataFrame()

    data_xlsx = []
    if xlsx_files:
        for archivo in xlsx_files:
            data_xlsx.append(pd.read_excel(archivo))
        concatenated_xlsx = pd.concat(data_xlsx, ignore_index=True)
    else:
        concatenated_xlsx = pd.DataFrame()

    print("Archivos CSV concatenados:", concatenated_csv.shape[0])
    print("Archivos XLSX concatenados:", concatenated_xlsx.shape[0])
    print("-----------------------------------------------------------------")

    return concatenated_csv, concatenated_xlsx


def preparar_xlsx(concatenated_xlsx):
    if concatenated_xlsx.empty:
        return concatenated_xlsx

    for col in ["fecha", "Fecha_Venta"]:
        if col in concatenated_xlsx.columns:
            columnas = {"fecha": "fecha", "Fecha_Venta": "fecha"}
            break
    else:
        columnas = {}

    for col_origen, col_destino in {
        "fecha": "fecha",
        "Fecha_Venta": "fecha",
        "producto": "producto",
        "Producto": "producto",
        "categoria": "categoria",
        "Categoria": "categoria",
        "cantidad": "cantidad",
        "Cant": "cantidad",
        "precio_unitario": "precio_unitario",
        "Valor_Unitario": "precio_unitario",
        "vendedor": "vendedor",
        "Vendedor": "vendedor",
        "metodo_pago": "metodo_pago",
        "Pago": "metodo_pago",
    }.items():
        if col_origen in concatenated_xlsx.columns and col_destino not in concatenated_xlsx.columns:
            concatenated_xlsx[col_destino] = concatenated_xlsx[col_origen]

    if "fecha" in concatenated_xlsx.columns and "Fecha_Venta" in concatenated_xlsx.columns:
        concatenated_xlsx["fecha"] = concatenated_xlsx["fecha"].fillna(concatenated_xlsx["Fecha_Venta"])
    if "producto" in concatenated_xlsx.columns and "Producto" in concatenated_xlsx.columns:
        concatenated_xlsx["producto"] = concatenated_xlsx["producto"].fillna(concatenated_xlsx["Producto"])
    if "categoria" in concatenated_xlsx.columns and "Categoria" in concatenated_xlsx.columns:
        concatenated_xlsx["categoria"] = concatenated_xlsx["categoria"].fillna(concatenated_xlsx["Categoria"])
    if "cantidad" in concatenated_xlsx.columns and "Cant" in concatenated_xlsx.columns:
        concatenated_xlsx["cantidad"] = concatenated_xlsx["cantidad"].fillna(concatenated_xlsx["Cant"])
    if "precio_unitario" in concatenated_xlsx.columns and "Valor_Unitario" in concatenated_xlsx.columns:
        concatenated_xlsx["precio_unitario"] = concatenated_xlsx["precio_unitario"].fillna(concatenated_xlsx["Valor_Unitario"])
    if "vendedor" in concatenated_xlsx.columns and "Vendedor" in concatenated_xlsx.columns:
        concatenated_xlsx["vendedor"] = concatenated_xlsx["vendedor"].fillna(concatenated_xlsx["Vendedor"])
    if "metodo_pago" in concatenated_xlsx.columns and "Pago" in concatenated_xlsx.columns:
        concatenated_xlsx["metodo_pago"] = concatenated_xlsx["metodo_pago"].fillna(concatenated_xlsx["Pago"])

    columnas_a_eliminar = [
        "Fecha_Venta", "Producto", "Categoria", "Cant",
        "Valor_Unitario", "Vendedor", "Pago"
    ]
    columnas_a_eliminar = [c for c in columnas_a_eliminar if c in concatenated_xlsx.columns]
    if columnas_a_eliminar:
        concatenated_xlsx.drop(columns=columnas_a_eliminar, inplace=True)

    print("Columnas en XLSX:")
    print(concatenated_xlsx.columns.tolist())
    return concatenated_xlsx


def crear_graficas(informe_final):
    if informe_final.empty:
        print("No hay datos para graficar.")
        return

    # Normalizar columnas de texto para evitar errores con NaN o datos mezclados
    for columna in ["categoria", "vendedor", "metodo_pago"]:
        if columna in informe_final.columns:
            informe_final[columna] = informe_final[columna].fillna("Sin dato").astype(str)

    os.makedirs("graficos", exist_ok=True)

    # Gráfico 1: ventas por categoría
    if "categoria" in informe_final.columns:
        ventas_categoria = informe_final.groupby("categoria", dropna=False)["cantidad"].sum().sort_values(ascending=False)
        ventas_categoria = ventas_categoria[~ventas_categoria.index.isna()]
        plt.figure(figsize=(8, 6))
        plt.bar([str(x) for x in ventas_categoria.index], ventas_categoria.values, color="steelblue")
        plt.title("Ventas por categoría")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("graficos/grafico_categoria.png", dpi=200, bbox_inches="tight")
        plt.show()

    # Gráfico 2: ventas por vendedor
    if "vendedor" in informe_final.columns:
        ventas_vendedor = informe_final.groupby("vendedor", dropna=False)["cantidad"].sum().sort_values(ascending=False)
        ventas_vendedor = ventas_vendedor[~ventas_vendedor.index.isna()]
        plt.figure(figsize=(8, 6))
        plt.bar([str(x) for x in ventas_vendedor.index], ventas_vendedor.values, color="forestgreen")
        plt.title("Ventas por vendedor")
        plt.xlabel("Vendedor")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("graficos/grafico_vendedor.png", dpi=200, bbox_inches="tight")
        plt.show()

    # Gráfico 3: métodos de pago
    if "metodo_pago" in informe_final.columns:
        metodos_pago = informe_final["metodo_pago"].fillna("Sin dato").value_counts()
        plt.figure(figsize=(7, 7))
        plt.pie(metodos_pago.values, labels=[str(x) for x in metodos_pago.index], autopct="%1.1f%%")
        plt.title("Métodos de pago")
        plt.tight_layout()
        plt.savefig("graficos/grafico_metodo_pago.png", dpi=200, bbox_inches="tight")
        plt.show()

    print("Gráficos generados:")
    print("- graficos/grafico_categoria.png")
    print("- graficos/grafico_vendedor.png")
    print("- graficos/grafico_metodo_pago.png")


if __name__ == "__main__":
    concatenated_csv, concatenated_xlsx = cargar_archivos()

    if not concatenated_xlsx.empty:
        concatenated_xlsx = preparar_xlsx(concatenated_xlsx)

    if concatenated_csv.empty and concatenated_xlsx.empty:
        raise ValueError("No se encontraron archivos CSV ni XLSX en la carpeta del proyecto.")

    informe_final = pd.concat(
        [df for df in [concatenated_csv, concatenated_xlsx] if not df.empty],
        ignore_index=True,
    )

    salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Informe_unido_sucursales.csv")
    informe_final.to_csv(salida, index=False)

    print("Archivo final generado:", salida)
    print("-----------------------------------------------------------------")
    print(informe_final.head())

    crear_graficas(informe_final)

