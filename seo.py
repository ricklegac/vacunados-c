import pandas as pd 
datos=pd.read_csv("/home/rick/Downloads/vacunados.csv",sep=';',warn_bad_lines=False,header=0);
descripcion=datos['descripcion_vacuna'].value_counts(ascending=True)
print(type(datos))
print("CANTIDAD DE VACUNAS APLICADA POR TIPO DE VACUNA ASCENDENTEMENTE:")
descripcion=descripcion.reset_index()
descripcion.rename(columns={'index': 'Vacunas', 'descripcion_vacuna': 'Cantidad'}, inplace=True)
print(descripcion)
descripcion.groupby(['Vacunas']).sum().plot(kind='pie', y='Cantidad', figsize=(10,10))