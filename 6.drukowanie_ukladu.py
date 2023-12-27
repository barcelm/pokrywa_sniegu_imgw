from qgis.core import QgsProject, QgsLayout, QgsLayoutExporter
from datetime import date

project_path = "S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/4.Mapa_pokrywy_snieznej.qgz"
data = date.today().strftime("%Y_%m_%d")

output_folder = "S:/RP/RPC Hydrologia/DYREKTOR_TECHNICZNY/2024/METEO-opady/Mapa_pokrywy_sniegu/mapy/"

layout_name = "pokrywa_sniegu"

project = QgsProject.instance()
project.read(project_path)

layout_manager = project.layoutManager()


if layout_manager.layoutByName(layout_name) is None:
    print("Układ o nazwie '{}' nie istnieje w projekcie.".format(layout_name))
else:
    layout = layout_manager.layoutByName(layout_name)

    output_file = "{}/{}_{}.png".format(output_folder, data, layout_name)

    exporter = QgsLayoutExporter(layout)

    export_settings = QgsLayoutExporter.ImageExportSettings()
    export_settings.dpi = 300
    export_settings.imageWidth = 1000
    export_settings.imageHeight = 1000
    export_settings.imageDpi = 300
    

    exporter.exportToImage(output_file, export_settings)

    print("Utworzono plik {} w folderze {}".format(output_file, output_folder))


###usuwanie
raster_layer_name = "Interpolation Result"
raster_layer = QgsProject.instance().mapLayersByName(raster_layer_name)
if len(raster_layer) > 0:
    QgsProject.instance().removeMapLayer(raster_layer[0])
    print(f"Warstwa rastrowa {raster_layer_name} została usunięta")
else:
    print(f"Warstwa rastrowa {raster_layer_name} nie istnieje w projekcie")


vector_layer_name = "Poziomice"
vector_layer = QgsProject.instance().mapLayersByName(vector_layer_name)
if len(vector_layer) > 0:
    QgsProject.instance().removeMapLayer(vector_layer[0])
    print(f"Warstwa wektorowa {vector_layer_name} została usunięta")
else:
    print(f"Warstwa wektorowa {vector_layer_name} nie istnieje w projekcie")