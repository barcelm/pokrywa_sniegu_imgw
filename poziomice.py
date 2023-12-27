from qgis.core import QgsRasterLayer, QgsProject, QgsVectorLayer
import processing
from datetime import date

data = date.today().strftime("%Y_%m_%d")
path = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/mapy/poziomice/'
input = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/mapy/raster/'

result = processing.run("gdal:contour", {
    'INPUT': input + data + '_interpolacja.tif',
    'BAND': 1,
    'INTERVAL': 5,
    'FIELD_NAME': 'opad',
    'CREATE_3D': False,
    'IGNORE_NODATA': False,
    'NODATA': None,
    'OFFSET': 0,
    'EXTRA': '',
    'OUTPUT': path + data + '_poziomice.shp'
})

output_layer = QgsVectorLayer(result['OUTPUT'], 'Poziomice')

style_path = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/warstwy/poziomice.qml'
output_layer.loadNamedStyle(style_path)

if output_layer.isValid():
    QgsProject.instance().addMapLayer(output_layer)
    print('Warstwa została wczytana')
else:
    print('Wystąpił problem podczas wczytywania warstwy')