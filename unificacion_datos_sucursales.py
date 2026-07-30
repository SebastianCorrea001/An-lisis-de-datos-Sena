""" By: JUAN AVENDAÑO - JUAN CORREA 3408936 
 3137509242 --- 3122606145 
 ADSO 
"""

import pandas as pd
import glob  
import openpyxl

csv_files = glob.glob("*.csv")

xlsx_files = glob.glob("*.xlsx")

concatenated_csv = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
concatenated_xlsx = pd.concat([pd.read_excel(f) for f in xlsx_files], ignore_index=True)

print("Archivos CSV concatenados:", concatenated_csv.shape[0])
print("Archivos XLSX concatenados:", concatenated_xlsx.shape[0])

print("-----------------------------------------------------------------")


"""Imprime los nombres de las columnas de cada DataFrame para verificar que coinciden"""
print("Columnas en CSV:", concatenated_csv.columns.tolist())
print("Columnas en XLSX:", concatenated_xlsx)

concatenated_xlsx['fecha'] = concatenated_xlsx['fecha'].fillna(concatenated_xlsx['Fecha_Venta'])
concatenated_xlsx['producto'] = concatenated_xlsx['producto'].fillna(concatenated_xlsx['Producto'])
concatenated_xlsx['categoria'] = concatenated_xlsx['categoria'].fillna(concatenated_xlsx['Categoria'])
concatenated_xlsx['cantidad'] = concatenated_xlsx['cantidad'].fillna(concatenated_xlsx['Cant'])
concatenated_xlsx['precio_unitario'] = concatenated_xlsx['precio_unitario'].fillna(concatenated_xlsx['Valor_Unitario'])
concatenated_xlsx['vendedor'] = concatenated_xlsx['vendedor'].fillna(concatenated_xlsx['Vendedor'])
concatenated_xlsx['metodo_pago'] = concatenated_xlsx['metodo_pago'].fillna(concatenated_xlsx['Pago'])
""" print("Columnas en XLSX:", concatenated_xlsx)
 """

""" 
concatenated_xlsx['procedencia'] =  

 """
concatenated_xlsx.drop(columns=['Fecha_Venta', 'Producto', 'Categoria', 'Cant', 'Valor_Unitario', 'Vendedor', 'Pago'], inplace=True)
print("Columnas en XLSX:", concatenated_xlsx)


informe_final = pd.concat([concatenated_csv, concatenated_xlsx], ignore_index=True)
informe_final = informe_final.to_csv('Informe_unido_sucursales', index=False)