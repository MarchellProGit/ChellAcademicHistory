import os
import sys
import math
import numpy as np
from osgeo import gdal, ogr, osr

# Paths
base_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"
code_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10"
output_dir = os.path.join(code_dir, "output").replace("\\", "/")
os.makedirs(output_dir, exist_ok=True)

admin_shp = os.path.join(base_dir, "[LapakGIS.com] KAB. SEMARANG/ADMINISTRASIDESA_AR_25K.shp").replace("\\", "/")
topo_shp = os.path.join(base_dir, "[LapakGIS.com] KAB. SEMARANG/TOPONIMI_PT_25K.shp").replace("\\", "/")
dem_tif = os.path.join(base_dir, "DEMNAS_1408-52_v1.0.tif").replace("\\", "/")
landsat_dir = os.path.join(base_dir, "LC08_L1TP_120065_20261002_20261002_02_RT").replace("\\", "/")

b4_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B4.TIF").replace("\\", "/")
b5_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B5.TIF").replace("\\", "/")
b6_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B6.TIF").replace("\\", "/")

target_crs_epsg = 32749  # WGS 84 / UTM zone 49S

print("--- Step 1: Extract Batas Desa Tajuk ---")
from qgis.core import (
    QgsVectorLayer, QgsFeature, QgsGeometry, QgsProject,
    QgsCoordinateReferenceSystem, QgsCoordinateTransform,
    QgsVectorFileWriter, QgsField
)
from PyQt5.QtCore import QVariant

layer_admin = QgsVectorLayer(admin_shp, "AdminDesa", "ogr")
feat_tajuk = layer_admin.getFeature(65)
geom_tajuk = feat_tajuk.geometry()

# Reproject to EPSG:32749
src_crs = layer_admin.crs()
dst_crs = QgsCoordinateReferenceSystem("EPSG:32749")
ct = QgsCoordinateTransform(src_crs, dst_crs, QgsProject.instance())
geom_tajuk_utm = QgsGeometry(geom_tajuk)
geom_tajuk_utm.transform(ct)

# Calculate area in ha
area_m2 = geom_tajuk_utm.area()
area_ha = area_m2 / 10000.0
print(f"Luas Desa Tajuk: {area_ha:.2f} ha ({area_m2:.2f} m2)")

# Save batas desa tajuk to GPKG and SHP
tajuk_shp = os.path.join(output_dir, "batas_desa_tajuk.shp").replace("\\", "/")
tajuk_gpkg = os.path.join(output_dir, "batas_desa_tajuk.gpkg").replace("\\", "/")

from qgis.core import QgsFields
fields = QgsFields()
fields.append(QgsField("NAMOBJ", QVariant.String))
fields.append(QgsField("WADMKC", QVariant.String))
fields.append(QgsField("WADMKK", QVariant.String))
fields.append(QgsField("LUAS_HA", QVariant.Double))

writer = QgsVectorFileWriter(
    tajuk_shp, "UTF-8", fields, geom_tajuk_utm.wkbType(), dst_crs, "ESRI Shapefile"
)
out_f = QgsFeature(fields)
out_f.setGeometry(geom_tajuk_utm)
out_f["NAMOBJ"] = "Desa Tajuk"
out_f["WADMKC"] = "Getasan"
out_f["WADMKK"] = "Kabupaten Semarang"
out_f["LUAS_HA"] = round(area_ha, 2)
writer.addFeature(out_f)
del writer

# Save GPKG as well
writer_gpkg = QgsVectorFileWriter(
    tajuk_gpkg, "UTF-8", fields, geom_tajuk_utm.wkbType(), dst_crs, "GPKG"
)
writer_gpkg.addFeature(out_f)
del writer_gpkg

print("Batas Desa Tajuk saved!")

# Step 1b: Save Titik Validasi BPBD (Dusun Gedong & Dusun Dukoh)
print("--- Step 1b: Save Titik Validasi BPBD ---")
pts_shp = os.path.join(output_dir, "titik_longsor_bpbd.shp").replace("\\", "/")
pt_fields = QgsFields()
pt_fields.append(QgsField("Dusun", QVariant.String))
pt_fields.append(QgsField("Kejadian", QVariant.String))
pt_fields.append(QgsField("Tanggal", QVariant.String))
pt_fields.append(QgsField("Sumber", QVariant.String))

pt_writer = QgsVectorFileWriter(
    pts_shp, "UTF-8", pt_fields, 1, dst_crs, "ESRI Shapefile" # 1 = Point
)

from qgis.core import QgsPointXY
# Dusun Gedong
f_gedong = QgsFeature(pt_fields)
pt_gedong = ct.transform(QgsPointXY(110.446445, -7.416926))
f_gedong.setGeometry(QgsGeometry.fromPointXY(pt_gedong))
f_gedong["Dusun"] = "Dusun Gedong"
f_gedong["Kejadian"] = "Longsor menutup jalan dan menimpa rumah warga"
f_gedong["Tanggal"] = "28 Februari 2024"
f_gedong["Sumber"] = "BPBD Jawa Tengah"
pt_writer.addFeature(f_gedong)

# Dusun Dukoh
f_dukoh = QgsFeature(pt_fields)
pt_dukoh = ct.transform(QgsPointXY(110.459283, -7.395905))
f_dukoh.setGeometry(QgsGeometry.fromPointXY(pt_dukoh))
f_dukoh["Dusun"] = "Dusun Dukoh"
f_dukoh["Kejadian"] = "Akses jembatan tertutup material tanah, batu, pasir, dan kayu"
f_dukoh["Tanggal"] = "28 Februari 2024"
f_dukoh["Sumber"] = "BPBD Jawa Tengah"
pt_writer.addFeature(f_dukoh)
del pt_writer
print("Titik validasi saved!")
