import os
import sys
import math
import numpy as np
from osgeo import gdal, ogr, osr

# Enable GDAL exceptions
gdal.UseExceptions()

# Paths
base_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"
code_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10"
output_dir = os.path.join(code_dir, "output").replace("\\", "/")
os.makedirs(output_dir, exist_ok=True)

admin_shp = os.path.join(base_dir, "[LapakGIS.com] KAB. SEMARANG/ADMINISTRASIDESA_AR_25K.shp").replace("\\", "/")
dem_tif = os.path.join(base_dir, "DEMNAS_1408-52_v1.0.tif").replace("\\", "/")
landsat_dir = os.path.join(base_dir, "LC08_L1TP_120065_20261002_20261002_02_RT").replace("\\", "/")

b4_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B4.TIF").replace("\\", "/")
b5_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B5.TIF").replace("\\", "/")
b6_tif = os.path.join(landsat_dir, "LC08_L1TP_120065_20261002_20261002_02_RT_B6.TIF").replace("\\", "/")

tajuk_shp = os.path.join(output_dir, "batas_desa_tajuk.shp").replace("\\", "/")
pts_shp = os.path.join(output_dir, "titik_longsor_bpbd.shp").replace("\\", "/")

print("=== 1. PREPARING EXTENT & WARPING RASTERS ===")
from qgis.core import (
    QgsVectorLayer, QgsRasterLayer, QgsProject, QgsCoordinateReferenceSystem,
    QgsCoordinateTransform, QgsPointXY, QgsClassificationJenks,
    QgsColorRampShader, QgsRasterShader, QgsSingleBandPseudoColorRenderer,
    QgsPalettedRasterRenderer, QgsSymbol, QgsSingleSymbolRenderer,
    QgsSimpleLineSymbolLayer, QgsMarkerSymbol, QgsPalLayerSettings,
    QgsVectorLayerSimpleLabeling, QgsTextFormat, QgsTextBufferSettings
)
from PyQt5.QtGui import QColor, QFont

layer_tajuk = QgsVectorLayer(tajuk_shp, "Batas Desa Tajuk", "ogr")
extent = layer_tajuk.extent()
xmin = math.floor(extent.xMinimum() / 30.0) * 30.0
ymin = math.floor(extent.yMinimum() / 30.0) * 30.0
xmax = math.ceil(extent.xMaximum() / 30.0) * 30.0
ymax = math.ceil(extent.yMaximum() / 30.0) * 30.0
output_bounds = [xmin, ymin, xmax, ymax]
print(f"Target Extent (EPSG:32749): {output_bounds}")

dem_out = os.path.join(output_dir, "dem_tajuk_30m.tif").replace("\\", "/")
slope_out = os.path.join(output_dir, "slope_percent_tajuk.tif").replace("\\", "/")
b4_out = os.path.join(output_dir, "b4_tajuk_30m.tif").replace("\\", "/")
b5_out = os.path.join(output_dir, "b5_tajuk_30m.tif").replace("\\", "/")
b6_out = os.path.join(output_dir, "b6_tajuk_30m.tif").replace("\\", "/")

ndvi_out = os.path.join(output_dir, "ndvi_tajuk.tif").replace("\\", "/")
ndmi_out = os.path.join(output_dir, "ndmi_tajuk.tif").replace("\\", "/")

score_slope_out = os.path.join(output_dir, "score_slope.tif").replace("\\", "/")
score_ndvi_out = os.path.join(output_dir, "score_ndvi.tif").replace("\\", "/")
score_ndmi_out = os.path.join(output_dir, "score_ndmi.tif").replace("\\", "/")
score_elev_out = os.path.join(output_dir, "score_elevation.tif").replace("\\", "/")

kl_continuous_out = os.path.join(output_dir, "kerawanan_longsor_continuous.tif").replace("\\", "/")
kl_classified_out = os.path.join(output_dir, "kerawanan_longsor_kelas.tif").replace("\\", "/")

# Warp DEMNAS (with explicit srcSRS='EPSG:4326')
print("Warping DEMNAS...")
gdal.Warp(
    dem_out, dem_tif,
    options=gdal.WarpOptions(
        format="GTiff",
        srcSRS="EPSG:4326",
        dstSRS="EPSG:32749",
        outputBounds=output_bounds,
        xRes=30.0,
        yRes=30.0,
        resampleAlg="bilinear",
        dstNodata=-9999.0
    )
)

# Warp Landsat Bands B4, B5, B6
print("Warping Landsat Bands...")
landsat_opts = gdal.WarpOptions(
    format="GTiff",
    dstSRS="EPSG:32749",
    outputBounds=output_bounds,
    xRes=30.0,
    yRes=30.0,
    resampleAlg="bilinear",
    dstNodata=0.0
)
gdal.Warp(b4_out, b4_tif, options=landsat_opts)
gdal.Warp(b5_out, b5_tif, options=landsat_opts)
gdal.Warp(b6_out, b6_tif, options=landsat_opts)

# Rasterize Mask of Desa Tajuk
mask_out = os.path.join(output_dir, "mask_tajuk.tif").replace("\\", "/")
drv = gdal.GetDriverByName("GTiff")
ds_ref = gdal.Open(dem_out)
cols = ds_ref.RasterXSize
rows = ds_ref.RasterYSize
gt = ds_ref.GetGeoTransform()
proj = ds_ref.GetProjection()

ds_mask = drv.Create(mask_out, cols, rows, 1, gdal.GDT_Byte)
ds_mask.SetGeoTransform(gt)
ds_mask.SetProjection(proj)
band_mask = ds_mask.GetRasterBand(1)
band_mask.Fill(0)
band_mask.SetNoDataValue(0)

ds_poly = ogr.Open(tajuk_shp)
lyr_poly = ds_poly.GetLayer()
gdal.RasterizeLayer(ds_mask, [1], lyr_poly, burn_values=[1])
ds_mask.FlushCache()
mask_arr = band_mask.ReadAsArray() == 1
ds_mask = None
ds_poly = None

# Calculate Slope (%)
print("Calculating Slope (%)...")
gdal.DEMProcessing(slope_out, dem_out, "slope", slopeFormat="percent")

# Read arrays
dem_arr = gdal.Open(dem_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
slope_arr = gdal.Open(slope_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b4_arr = gdal.Open(b4_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b5_arr = gdal.Open(b5_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b6_arr = gdal.Open(b6_out).GetRasterBand(1).ReadAsArray().astype(np.float32)

# Convert Landsat DN to TOA Reflectance
# MULT = 2.0E-5, ADD = -0.1, SUN_ELEV = 64.52967777 deg
sin_sun = math.sin(math.radians(64.52967777))
toa4 = (b4_arr * 2.0e-5 - 0.1) / sin_sun
toa5 = (b5_arr * 2.0e-5 - 0.1) / sin_sun
toa6 = (b6_arr * 2.0e-5 - 0.1) / sin_sun

# Compute NDVI & NDMI
denom_ndvi = toa5 + toa4
denom_ndvi[denom_ndvi == 0] = 1e-6
ndvi_arr = (toa5 - toa4) / denom_ndvi
ndvi_arr = np.clip(ndvi_arr, -1.0, 1.0)

denom_ndmi = toa5 + toa6
denom_ndmi[denom_ndmi == 0] = 1e-6
ndmi_arr = (toa5 - toa6) / denom_ndmi
ndmi_arr = np.clip(ndmi_arr, -1.0, 1.0)

def save_raster(filename, data, dtype=gdal.GDT_Float32, nodata=-9999.0):
    ds = drv.Create(filename, cols, rows, 1, dtype)
    ds.SetGeoTransform(gt)
    ds.SetProjection(proj)
    b = ds.GetRasterBand(1)
    out_data = data.copy()
    out_data[~mask_arr] = nodata
    b.WriteArray(out_data)
    b.SetNoDataValue(nodata)
    ds.FlushCache()
    ds = None

save_raster(ndvi_out, ndvi_arr)
save_raster(ndmi_out, ndmi_arr)

# Valid pixels inside Tajuk
valid_mask = mask_arr & (dem_arr > 0)
dem_vals = dem_arr[valid_mask]
slope_vals = slope_arr[valid_mask]
ndvi_vals = ndvi_arr[valid_mask]
ndmi_vals = ndmi_arr[valid_mask]

total_valid_pixels = len(dem_vals)
total_area_ha = total_valid_pixels * 900.0 / 10000.0
print(f"Total Pixels Valid: {total_valid_pixels} (~{total_area_ha:.2f} ha)")

# Natural Breaks (Jenks)
jenks = QgsClassificationJenks()
sample_elev = list(float(x) for x in np.random.choice(dem_vals, min(len(dem_vals), 5000), replace=False))
res_elev = jenks.classes(sample_elev, 5)
elev_breaks = [r.upperBound() for r in res_elev]
print(f"Elevation Jenks Breaks: {[round(b, 1) for b in elev_breaks]}")

sample_ndmi = list(float(x) for x in np.random.choice(ndmi_vals, min(len(ndmi_vals), 5000), replace=False))
res_ndmi = jenks.classes(sample_ndmi, 5)
ndmi_breaks = [r.upperBound() for r in res_ndmi]
print(f"NDMI Jenks Breaks: {[round(b, 4) for b in ndmi_breaks]}")

# --- Scoring Parameters ---
# 1. Slope (%) (Table 2)
score_slope = np.zeros_like(slope_arr, dtype=np.float32)
score_slope[(slope_arr >= 0) & (slope_arr < 8)] = 1
score_slope[(slope_arr >= 8) & (slope_arr < 15)] = 2
score_slope[(slope_arr >= 15) & (slope_arr < 25)] = 3
score_slope[(slope_arr >= 25) & (slope_arr < 45)] = 4
score_slope[slope_arr >= 45] = 5

# 2. NDVI (Table 2: >0.7:1, 0.5-0.7:2, 0.3-0.5:3, 0.1-0.3:4, <=0.1:5)
score_ndvi = np.zeros_like(ndvi_arr, dtype=np.float32)
score_ndvi[ndvi_arr > 0.7] = 1
score_ndvi[(ndvi_arr > 0.5) & (ndvi_arr <= 0.7)] = 2
score_ndvi[(ndvi_arr > 0.3) & (ndvi_arr <= 0.5)] = 3
score_ndvi[(ndvi_arr > 0.1) & (ndvi_arr <= 0.3)] = 4
score_ndvi[ndvi_arr <= 0.1] = 5

# 3. Elevation (Higher = 5)
score_elev = np.zeros_like(dem_arr, dtype=np.float32)
score_elev[dem_arr <= elev_breaks[0]] = 1
score_elev[(dem_arr > elev_breaks[0]) & (dem_arr <= elev_breaks[1])] = 2
score_elev[(dem_arr > elev_breaks[1]) & (dem_arr <= elev_breaks[2])] = 3
score_elev[(dem_arr > elev_breaks[2]) & (dem_arr <= elev_breaks[3])] = 4
score_elev[dem_arr > elev_breaks[3]] = 5

# 4. NDMI (Higher = wetter = 5)
score_ndmi = np.zeros_like(ndmi_arr, dtype=np.float32)
score_ndmi[ndmi_arr <= ndmi_breaks[0]] = 1
score_ndmi[(ndmi_arr > ndmi_breaks[0]) & (ndmi_arr <= ndmi_breaks[1])] = 2
score_ndmi[(ndmi_arr > ndmi_breaks[1]) & (ndmi_arr <= ndmi_breaks[2])] = 3
score_ndmi[(ndmi_arr > ndmi_breaks[2]) & (ndmi_arr <= ndmi_breaks[3])] = 4
score_ndmi[ndmi_arr > ndmi_breaks[3]] = 5

save_raster(score_slope_out, score_slope, gdal.GDT_Byte, 0)
save_raster(score_ndvi_out, score_ndvi, gdal.GDT_Byte, 0)
save_raster(score_elev_out, score_elev, gdal.GDT_Byte, 0)
save_raster(score_ndmi_out, score_ndmi, gdal.GDT_Byte, 0)

# --- Weighted Overlay ---
kl_continuous = (
    0.517 * score_slope +
    0.226 * score_ndvi +
    0.134 * score_elev +
    0.123 * score_ndmi
)
save_raster(kl_continuous_out, kl_continuous)

# Classified Kerawanan (1 to 5)
kl_classified = np.zeros_like(kl_continuous, dtype=np.uint8)
kl_classified[(kl_continuous >= 1.0) & (kl_continuous < 1.8)] = 1
kl_classified[(kl_continuous >= 1.8) & (kl_continuous < 2.6)] = 2
kl_classified[(kl_continuous >= 2.6) & (kl_continuous < 3.4)] = 3
kl_classified[(kl_continuous >= 3.4) & (kl_continuous < 4.2)] = 4
kl_classified[kl_continuous >= 4.2] = 5

save_raster(kl_classified_out, kl_classified, gdal.GDT_Byte, 0)
print("All rasters calculated and saved!")

# --- STATISTICAL REPORT ---
min_elev = float(np.min(dem_vals))
max_elev = float(np.max(dem_vals))
mean_elev = float(np.mean(dem_vals))

slope_counts = [
    int(np.sum((slope_vals >= 0) & (slope_vals < 8))),
    int(np.sum((slope_vals >= 8) & (slope_vals < 15))),
    int(np.sum((slope_vals >= 15) & (slope_vals < 25))),
    int(np.sum((slope_vals >= 25) & (slope_vals < 45))),
    int(np.sum(slope_vals >= 45))
]
slope_labels = ["0–8 (Datar)", "8–15 (Landai)", "15–25 (Agak Curam)", "25–45 (Curam)", "> 45 (Sangat Curam)"]

min_ndvi = float(np.min(ndvi_vals))
max_ndvi = float(np.max(ndvi_vals))
mean_ndvi = float(np.mean(ndvi_vals))

min_ndmi = float(np.min(ndmi_vals))
max_ndmi = float(np.max(ndmi_vals))
mean_ndmi = float(np.mean(ndmi_vals))
r_pearson = float(np.corrcoef(ndvi_vals, ndmi_vals)[0, 1])

kl_vals = kl_classified[valid_mask]
kl_counts = [
    int(np.sum(kl_vals == 1)),
    int(np.sum(kl_vals == 2)),
    int(np.sum(kl_vals == 3)),
    int(np.sum(kl_vals == 4)),
    int(np.sum(kl_vals == 5))
]
kl_labels = ["Sangat Rendah", "Rendah", "Sedang", "Tinggi", "Sangat Tinggi"]

print("\n=== TABEL 5: SEBARAN LERENG ===")
for lab, count in zip(slope_labels, slope_counts):
    print(f"{lab}: {count*900/10000:.2f} ha ({count/total_valid_pixels*100:.2f}%)")

print("\n=== TABEL 6: STATISTIK NDVI & NDMI ===")
print(f"NDVI: Min={min_ndvi:.3f}, Max={max_ndvi:.3f}, Mean={mean_ndvi:.3f}")
print(f"NDMI: Min={min_ndmi:.3f}, Max={max_ndmi:.3f}, Mean={mean_ndmi:.3f}")
print(f"Pearson r={r_pearson:.3f}")

print("\n=== TABEL 7: KELAS KERAWANAN LONGSOR ===")
for lab, count in zip(kl_labels, kl_counts):
    print(f"{lab}: {count*900/10000:.2f} ha ({count/total_valid_pixels*100:.2f}%)")

high_ha = (kl_counts[3] + kl_counts[4]) * 900.0 / 10000.0
high_pct = (kl_counts[3] + kl_counts[4]) / total_valid_pixels * 100.0
print(f"Total Tinggi & Sangat Tinggi: {high_ha:.2f} ha ({high_pct:.2f}%)")

# Validation Points
layer_pts = QgsVectorLayer(pts_shp, "Titik BPBD", "ogr")
inv_gt = gdal.InvGeoTransform(gt)
val_info = []
for feat in layer_pts.getFeatures():
    dusun = feat["Dusun"]
    pt = feat.geometry().asPoint()
    px, py = gdal.ApplyGeoTransform(inv_gt, pt.x(), pt.y())
    px = int(round(px))
    py = int(round(py))
    v_class = int(kl_classified[py, px])
    v_score = float(kl_continuous[py, px])
    v_slope = float(slope_arr[py, px])
    v_elev = float(dem_arr[py, px])
    v_ndvi = float(ndvi_arr[py, px])
    val_info.append({
        "dusun": dusun,
        "class": kl_labels[v_class - 1],
        "score": v_score,
        "slope": v_slope,
        "elev": v_elev,
        "ndvi": v_ndvi
    })
    print(f"Validasi {dusun}: Kelas {kl_labels[v_class - 1]} (Skor {v_score:.2f}, Lereng {v_slope:.1f}%, Elev {v_elev:.1f}m)")

# Save statistics file
stats_file = os.path.join(output_dir, "hasil_analisis_jurnal.txt").replace("\\", "/")
with open(stats_file, "w", encoding="utf-8") as f:
    f.write(f"Luas Desa Tajuk: {total_area_ha:.2f} ha\n")
    f.write(f"Elevasi: {min_elev:.1f} - {max_elev:.1f} m (Rata-rata: {mean_elev:.1f} m)\n\n")
    f.write("Tabel 5. Sebaran Kemiringan Lereng:\n")
    for lab, c in zip(slope_labels, slope_counts):
        f.write(f"{lab}: {c*900/10000:.2f} ha ({c/total_valid_pixels*100:.2f}%)\n")
    f.write("\nTabel 6. Statistik NDVI & NDMI:\n")
    f.write(f"NDVI: Min={min_ndvi:.3f}, Max={max_ndvi:.3f}, Mean={mean_ndvi:.3f}\n")
    f.write(f"NDMI: Min={min_ndmi:.3f}, Max={max_ndmi:.3f}, Mean={mean_ndmi:.3f}\n")
    f.write(f"Pearson r={r_pearson:.3f}\n\n")
    f.write("Tabel 7. Luas Kelas Kerawanan Longsor:\n")
    for lab, c in zip(kl_labels, kl_counts):
        f.write(f"{lab}: {c*900/10000:.2f} ha ({c/total_valid_pixels*100:.2f}%)\n")
    f.write(f"Total Tinggi & Sangat Tinggi: {high_ha:.2f} ha ({high_pct:.2f}%)\n\n")
    f.write("Validasi BPBD:\n")
    for v in val_info:
        f.write(f"{v['dusun']}: Kelas {v['class']} (Skor {v['score']:.2f}, Lereng {v['slope']:.1f}%, Elevasi {v['elev']:.1f}m)\n")

print(f"\nStats report saved to: {stats_file}")

# --- 2. ADD & STYLE LAYERS IN ACTIVE QGIS PROJECT ---
print("\n=== ADDING & STYLING LAYERS IN QGIS PROJECT ===")
project = QgsProject.instance()
project.setCrs(QgsCoordinateReferenceSystem("EPSG:32749"))

# Clear old layers if any
project.removeAllMapLayers()

# A. Add Classified Landslide Susceptibility Layer
rlayer_kl = QgsRasterLayer(kl_classified_out, "Peta Kerawanan Longsor (AHP)")
if rlayer_kl.isValid():
    # Paletted renderer
    classes = [
        QgsPalettedRasterRenderer.Class(1, QColor("#1a9641"), "Sangat Rendah (1.0–1.8)"),
        QgsPalettedRasterRenderer.Class(2, QColor("#a6d96a"), "Rendah (1.8–2.6)"),
        QgsPalettedRasterRenderer.Class(3, QColor("#ffffbf"), "Sedang (2.6–3.4)"),
        QgsPalettedRasterRenderer.Class(4, QColor("#fdae61"), "Tinggi (3.4–4.2)"),
        QgsPalettedRasterRenderer.Class(5, QColor("#d7191c"), "Sangat Tinggi (4.2–5.0)")
    ]
    renderer_kl = QgsPalettedRasterRenderer(rlayer_kl.dataProvider(), 1, classes)
    rlayer_kl.setRenderer(renderer_kl)
    rlayer_kl.triggerRepaint()
    project.addMapLayer(rlayer_kl)
    print("Added: Peta Kerawanan Longsor (AHP)")

# B. Add Slope Layer
rlayer_slope = QgsRasterLayer(slope_out, "Kemiringan Lereng (%)")
if rlayer_slope.isValid():
    shader = QgsRasterShader()
    ramp = QgsColorRampShader()
    ramp.setColorRampType(QgsColorRampShader.Interpolated)
    items = [
        QgsColorRampShader.ColorRampItem(0, QColor("#2b83ba"), "0%"),
        QgsColorRampShader.ColorRampItem(15, QColor("#abdda4"), "15%"),
        QgsColorRampShader.ColorRampItem(25, QColor("#ffffbf"), "25%"),
        QgsColorRampShader.ColorRampItem(45, QColor("#fdae61"), "45%"),
        QgsColorRampShader.ColorRampItem(80, QColor("#d7191c"), ">80%")
    ]
    ramp.setColorRampItemList(items)
    shader.setRasterShaderFunction(ramp)
    renderer_slope = QgsSingleBandPseudoColorRenderer(rlayer_slope.dataProvider(), 1, shader)
    rlayer_slope.setRenderer(renderer_slope)
    rlayer_slope.triggerRepaint()
    project.addMapLayer(rlayer_slope)
    print("Added: Kemiringan Lereng (%)")

# C. Add NDVI Layer
rlayer_ndvi = QgsRasterLayer(ndvi_out, "NDVI (Vegetasi)")
if rlayer_ndvi.isValid():
    shader = QgsRasterShader()
    ramp = QgsColorRampShader()
    ramp.setColorRampType(QgsColorRampShader.Interpolated)
    items = [
        QgsColorRampShader.ColorRampItem(-0.2, QColor("#a6611a"), "Lahan Terbuka (<0.1)"),
        QgsColorRampShader.ColorRampItem(0.2, QColor("#dfc27d"), "Jarang (0.1–0.3)"),
        QgsColorRampShader.ColorRampItem(0.4, QColor("#f5f5f5"), "Sedang (0.3–0.5)"),
        QgsColorRampShader.ColorRampItem(0.6, QColor("#80cdc1"), "Rapat (0.5–0.7)"),
        QgsColorRampShader.ColorRampItem(0.85, QColor("#018571"), "Sangat Rapat (>0.7)")
    ]
    ramp.setColorRampItemList(items)
    shader.setRasterShaderFunction(ramp)
    rlayer_ndvi.setRenderer(QgsSingleBandPseudoColorRenderer(rlayer_ndvi.dataProvider(), 1, shader))
    rlayer_ndvi.triggerRepaint()
    project.addMapLayer(rlayer_ndvi)
    print("Added: NDVI (Vegetasi)")

# D. Add NDMI Layer
rlayer_ndmi = QgsRasterLayer(ndmi_out, "NDMI (Kelembapan)")
if rlayer_ndmi.isValid():
    shader = QgsRasterShader()
    ramp = QgsColorRampShader()
    ramp.setColorRampType(QgsColorRampShader.Interpolated)
    items = [
        QgsColorRampShader.ColorRampItem(min_ndmi, QColor("#f7fbff"), "Kering"),
        QgsColorRampShader.ColorRampItem(mean_ndmi, QColor("#6baed6"), "Sedang"),
        QgsColorRampShader.ColorRampItem(max_ndmi, QColor("#08306b"), "Sangat Lembap")
    ]
    ramp.setColorRampItemList(items)
    shader.setRasterShaderFunction(ramp)
    rlayer_ndmi.setRenderer(QgsSingleBandPseudoColorRenderer(rlayer_ndmi.dataProvider(), 1, shader))
    rlayer_ndmi.triggerRepaint()
    project.addMapLayer(rlayer_ndmi)
    print("Added: NDMI (Kelembapan)")

# E. Add DEM Layer
rlayer_dem = QgsRasterLayer(dem_out, "DEM Elevasi (30m)")
if rlayer_dem.isValid():
    shader = QgsRasterShader()
    ramp = QgsColorRampShader()
    ramp.setColorRampType(QgsColorRampShader.Interpolated)
    items = [
        QgsColorRampShader.ColorRampItem(min_elev, QColor("#31a354"), f"{int(min_elev)} m"),
        QgsColorRampShader.ColorRampItem(1500, QColor("#fed976"), "1500 m"),
        QgsColorRampShader.ColorRampItem(2200, QColor("#fd8d3c"), "2200 m"),
        QgsColorRampShader.ColorRampItem(max_elev, QColor("#7a0177"), f"{int(max_elev)} m")
    ]
    ramp.setColorRampItemList(items)
    shader.setRasterShaderFunction(ramp)
    rlayer_dem.setRenderer(QgsSingleBandPseudoColorRenderer(rlayer_dem.dataProvider(), 1, shader))
    rlayer_dem.triggerRepaint()
    project.addMapLayer(rlayer_dem)
    print("Added: DEM Elevasi (30m)")

# F. Add Batas Desa Tajuk (Vector Boundary)
vlayer_tajuk = QgsVectorLayer(tajuk_shp, "Batas Administrasi Desa Tajuk", "ogr")
if vlayer_tajuk.isValid():
    # Outline only (black thick border)
    sym = QgsSymbol.defaultSymbol(vlayer_tajuk.geometryType())
    sym.symbolLayer(0).setStrokeColor(QColor("#000000"))
    sym.symbolLayer(0).setStrokeWidth(0.8)
    sym.symbolLayer(0).setFillColor(QColor(0, 0, 0, 0)) # transparent fill
    vlayer_tajuk.setRenderer(QgsSingleSymbolRenderer(sym))
    vlayer_tajuk.triggerRepaint()
    project.addMapLayer(vlayer_tajuk)
    print("Added: Batas Administrasi Desa Tajuk")

# G. Add Titik Validasi BPBD (Points with labels)
vlayer_pts = QgsVectorLayer(pts_shp, "Titik Kejadian Longsor (BPBD)", "ogr")
if vlayer_pts.isValid():
    sym = QgsMarkerSymbol.createSimple({
        "name": "triangle",
        "color": "#e31a1c",
        "size": "5.0",
        "outline_color": "#ffffff",
        "outline_width": "0.8"
    })
    vlayer_pts.setRenderer(QgsSingleSymbolRenderer(sym))
    
    # Labeling
    lbl_settings = QgsPalLayerSettings()
    lbl_settings.fieldName = "Dusun"
    text_format = QgsTextFormat()
    text_format.setFont(QFont("Arial", 10, QFont.Bold))
    text_format.setColor(QColor("#000000"))
    
    buf = QgsTextBufferSettings()
    buf.setEnabled(True)
    buf.setSize(1.2)
    buf.setColor(QColor("#ffffff"))
    text_format.setBuffer(buf)
    
    lbl_settings.setFormat(text_format)
    vlayer_pts.setLabeling(QgsVectorLayerSimpleLabeling(lbl_settings))
    vlayer_pts.setLabelsEnabled(True)
    vlayer_pts.triggerRepaint()
    project.addMapLayer(vlayer_pts)
    print("Added: Titik Kejadian Longsor (BPBD)")

# Set active layer to Kerawanan Longsor
from qgis.utils import iface
if iface:
    iface.setActiveLayer(rlayer_kl)
    iface.mapCanvas().setExtent(layer_tajuk.extent())
    iface.mapCanvas().refresh()

# Save QGIS project
project.write()
print("QGIS Project saved successfully!")
