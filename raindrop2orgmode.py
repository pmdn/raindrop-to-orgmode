import pandas as pd

print('Iniciando conversión...')
# Lectura de los datos exportados en csv desde Raindrop.io
datos = pd.read_csv('bc48665c-42f0-4b0e-8669-b59def516eaa.csv')

# Concatenación/unificación de carpetas y etiquetas
etiquetas_temp = '#' + datos['folder'].str.lower() + ', ' + datos['tags'].str.lower()
etiquetas = ':' + etiquetas_temp.str.replace(', ', ':') + ':'

# Generación de las entradas en formato org mode con la siguiente estructura:
"""
** [[url][título]] :#tipo:etiqueta1:etiqueta2:
:PROPERTIES:
:CREATED: [fecha]
:END:

- Comentarios
"""
entradas = '** [[' + datos['url'] + '][' + datos['title'] + ']] ' + \
    etiquetas + '\n' + ':PROPERTIES:\n' + ':CREATED: [' + datos['created'].str[0:10] + \
    ']\n' + ':END:\n' + '\n- ' + datos['description'] + '\n'

# Escritura a txt
entradas.to_csv('MyOrgFileTemp.txt', sep=' ', index=False, header=False)

# Eliminación de las comillas dobles que se generan por cada entrada en el paso anterior
with open('MyOrgFileTemp.txt', 'r', encoding="utf8") as f, open('MyOrgFile.txt', 'w', encoding="utf8") as fo:
    for line in f:
        fo.write(line.replace('"', ''))

f.close()
fo.close()
print('Hecho!')
