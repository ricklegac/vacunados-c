import pandas as pd 
import numpy as np
import perfplot
import os
import cv2
import matplotlib.image as mpimg
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
import matplotlib.dates as dates
datos=pd.read_csv("/home/rick/Downloads/vacunados.csv",sep=';',warn_bad_lines=False,header=0);
descripcion=datos['descripcion_vacuna'].value_counts(ascending=True)
print(type(datos))
print("CANTIDAD DE VACUNAS APLICADA POR TIPO DE VACUNA ASCENDENTEMENTE:")
descripcion=descripcion.reset_index()
descripcion.rename(columns={'index': 'Vacunas', 'descripcion_vacuna': 'Cantidad'}, inplace=True)
print(descripcion)
cantidad_vacunados = datos.shape[0]
print('cantidad de vacunados hasta la fecha: ',cantidad_vacunados)
'''
perfplot.save(
    "out.jpg",
    setup=lambda n: pd.DataFrame(np.arange(n * 3).reshape(n, 3)),
    n_range=[2**k for k in range(5)],
    kernels=[
        lambda datos: len(datos.index),
        lambda datos: datos.shape[0],
        lambda datos: datos[datos.columns[0]].count(),
    ],
    labels=["len(df.index)", "df.shape[0]", "df[df.columns[0]].count()"],
    xlabel="Cantidad de vacunados",
)'''
descripcion.groupby(['Vacunas']).sum().plot(kind='pie', y='Cantidad', figsize=(10,10))
plt.style.use('seaborn')

''' Cantidad de vacunados por dia '''
datos['fecha_aplicacion']=pd.to_datetime(datos['fecha_aplicacion'])
counts_fechas = datos.groupby(['fecha_aplicacion']).count().sort_values(['establecimiento'],ascending=False).head(100)
counts_fechas = counts_fechas.drop(["nombre","apellido","cedula","descripcion_vacuna","actualizado_al",'dosis'],axis=1)
counts_fechas.rename(columns={'establecimiento':'Cantidad'},inplace=True)
img = mpimg.imread('vacunatorio covid 2020.jpg')



imgplot = plt.imshow(img)
plt.show()

im = cv2.imread('vacunatorio covid 2020.jpg')
im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
plt.show()
'''
datos_fecha = datos['fecha_aplicacion']
datos_cantidad_fecha = counts_fechas['establecimiento']

fechas= counts_fechas.set_index('nombre')
fechas.plot(x_compat=True)
locator.MAXTICKS = 100
plt.gca().xaxis.set_major_locator(dates.DayLocator())
plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%d\n\n%a'))
plt.gca().invert_xaxis()
plt.gcf().autofmt_xdate(rotation=0, ha="center")
'''
#order_establecimientos = datos.sort_values(['establecimiento']).head(10)
counts_establecimientos = datos.groupby(['establecimiento']).count()
count_sorted_establecimiento = counts_establecimientos.sort_values(['nombre'],ascending=False)
count_sorted_establecimiento  = count_sorted_establecimiento .drop(["nombre","apellido","cedula","descripcion_vacuna","actualizado_al",'dosis'],axis=1)
count_sorted_establecimiento.rename(columns={'fecha_aplicacion':'Cantidad'},inplace=True)

counts_dosis = datos.groupby(['dosis']).count()
count_sorted_dosis= counts_dosis.sort_values(['nombre'],ascending=False)


