from qgis.core import QgsRasterLayer, QgsProject
import processing
from datetime import date
data = date.today().strftime("%Y_%m_%d")

save_path = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/mapy/raster/interpolacja.tif'
path = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/mapy/raster/'
result = processing.run("qgis:tininterpolation", {'INTERPOLATION_DATA':'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/warstwy/stacje_do_interpolacji.shp::~::0::~::10::~::1',
'METHOD':0,
'EXTENT':'201786.675200000,556131.688300000,303794.700400000,587396.391900000 [EPSG:2180]',
'PIXEL_SIZE':1000,
'OUTPUT':path+data+'_interpolacja.tif'})

output_layer = QgsRasterLayer(result['OUTPUT'], 'Interpolation Result')

style_path = 'S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/warstwy/interpolacja.qml'
output_layer.loadNamedStyle(style_path)

if output_layer.isValid():
    QgsProject.instance().addMapLayer(output_layer)
    print('Warstwa została wczytana')
else:
    print('Wystąpił problem podczas wczytywania warstwy')