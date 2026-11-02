import os
import math
import numpy as np
from osgeo import gdal

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"
tajuk_shp = os.path.join(output_dir, "batas_desa_tajuk.shp").replace("\\", "/")
pts_shp = os.path.join(output_dir, "titik_longsor_bpbd.shp").replace("\\", "/")
dem_out = os.path.join(output_dir, "dem_tajuk_30m.tif").replace("\\", "/")
slope_out = os.path.join(output_dir, "slope_percent_tajuk.tif").replace("\\", "/")
b4_out = os.path.join(output_dir, "b4_tajuk_30m.tif").replace("\\", "/")
b5_out = os.path.join(output_dir, "b5_tajuk_30m.tif").replace("\\", "/")
b6_out = os.path.join(output_dir, "b6_tajuk_30m.tif").replace("\\", "/")
mask_out = os.path.join(output_dir, "mask_tajuk.tif").replace("\\", "/")

ndvi_out = os.path.join(output_dir, "ndvi_tajuk.tif").replace("\\", "/")
ndmi_out = os.path.join(output_dir, "ndmi_tajuk.tif").replace("\\", "/")

score_slope_out = os.path.join(output_dir, "score_slope.tif").replace("\\", "/")
score_ndvi_out = os.path.join(output_dir, "score_ndvi.tif").replace("\\", "/")
score_elev_out = os.path.join(output_dir, "score_elevation.tif").replace("\\", "/")
score_ndmi_out = os.path.join(output_dir, "score_ndmi.tif").replace("\\", "/")

kl_continuous_out = os.path.join(output_dir, "kerawanan_longsor_continuous.tif").replace("\\", "/")
kl_classified_out = os.path.join(output_dir, "kerawanan_longsor_kelas.tif").replace("\\", "/")

ds_ref = gdal.Open(dem_out)
cols = ds_ref.RasterXSize
rows = ds_ref.RasterYSize
gt = ds_ref.GetGeoTransform()
proj = ds_ref.GetProjection()

ds_mask = gdal.Open(mask_out)
mask_arr = ds_mask.GetRasterBand(1).ReadAsArray() == 1

dem_arr = ds_ref.GetRasterBand(1).ReadAsArray().astype(np.float32)
slope_arr = gdal.Open(slope_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b4_arr = gdal.Open(b4_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b5_arr = gdal.Open(b5_out).GetRasterBand(1).ReadAsArray().astype(np.float32)
b6_arr = gdal.Open(b6_out).GetRasterBand(1).ReadAsArray().astype(np.float32)

sin_sun = math.sin(math.radians(64.52967777))
toa4 = (b4_arr * 2.0e-5 - 0.1) / sin_sun
toa5 = (b5_arr * 2.0e-5 - 0.1) / sin_sun
toa6 = (b6_arr * 2.0e-5 - 0.1) / sin_sun

denom_ndvi = toa5 + toa4
denom_ndvi[denom_ndvi == 0] = 1e-6
ndvi_arr = np.clip((toa5 - toa4) / denom_ndvi, -1.0, 1.0)

denom_ndmi = toa5 + toa6
denom_ndmi[denom_ndmi == 0] = 1e-6
ndmi_arr = np.clip((toa5 - toa6) / denom_ndmi, -1.0, 1.0)

drv = gdal.GetDriverByName("GTiff")
def save_raster(filename, data, dtype=gdal.GDT_Float32, nodata=-9999.0):
    ds = drv.Create(filename, cols, rows, 1, dtype)
    ds.SetGeoTransform(gt)
    ds.SetProjection(proj)
    b = ds.GetRasterBand(1)
    out_data = data.copy()
    if dtype == gdal.GDT_Byte:
        out_data[~mask_arr] = 0
        b.WriteArray(out_data.astype(np.uint8))
        b.SetNoDataValue(0)
    else:
        out_data[~mask_arr] = nodata
        b.WriteArray(out_data.astype(np.float32))
        b.SetNoDataValue(nodata)
    ds.FlushCache()
    ds = None

save_raster(ndvi_out, ndvi_arr)
save_raster(ndmi_out, ndmi_arr)

valid_mask = mask_arr & (dem_arr > 0)
dem_vals = dem_arr[valid_mask]
slope_vals = slope_arr[valid_mask]
ndvi_vals = ndvi_arr[valid_mask]
ndmi_vals = ndmi_arr[valid_mask]

total_valid_pixels = len(dem_vals)
total_area_ha = total_valid_pixels * 900.0 / 10000.0

def jenks_breaks(data, n_classes=5):
    data = np.sort(data)
    n = len(data)
    sample = np.interp(np.linspace(0, n-1, 150), np.arange(n), data)
    m = len(sample)
    mat1 = np.zeros((m + 1, n_classes + 1))
    mat2 = np.zeros((m + 1, n_classes + 1))
    for i in range(1, n_classes + 1):
        mat1[1][i] = 1
        mat2[1][i] = 0
        for j in range(2, m + 1):
            mat2[j][i] = float('inf')
    v = 0.0
    for l in range(2, m + 1):
        s1 = 0.0
        s2 = 0.0
        w = 0.0
        for m_idx in range(1, l + 1):
            i3 = l - m_idx + 1
            val = float(sample[i3 - 1])
            s2 += val * val
            s1 += val
            w += 1
            v = s2 - (s1 * s1) / w
            i4 = i3 - 1
            if i4 != 0:
                for j in range(2, n_classes + 1):
                    if mat2[l][j] >= (v + mat2[i4][j - 1]):
                        mat1[l][j] = i3
                        mat2[l][j] = v + mat2[i4][j - 1]
        mat1[l][1] = 1
        mat2[l][1] = v
    k = m
    kclass = [0.0] * (n_classes + 1)
    kclass[n_classes] = float(sample[-1])
    kclass[0] = float(sample[0])
    countNum = n_classes
    while countNum >= 2:
        id_idx = int(mat1[k][countNum]) - 2
        kclass[countNum - 1] = float(sample[id_idx])
        k = int(mat1[k][countNum] - 1)
        countNum -= 1
    return kclass[1:]

elev_breaks = jenks_breaks(dem_vals, 5)
ndmi_breaks = jenks_breaks(ndmi_vals, 5)

# 1. Slope (%)
score_slope = np.zeros_like(slope_arr, dtype=np.float32)
score_slope[(slope_arr >= 0) & (slope_arr < 8)] = 1
score_slope[(slope_arr >= 8) & (slope_arr < 15)] = 2
score_slope[(slope_arr >= 15) & (slope_arr < 25)] = 3
score_slope[(slope_arr >= 25) & (slope_arr < 45)] = 4
score_slope[slope_arr >= 45] = 5

# 2. NDVI
score_ndvi = np.zeros_like(ndvi_arr, dtype=np.float32)
score_ndvi[ndvi_arr > 0.7] = 1
score_ndvi[(ndvi_arr > 0.5) & (ndvi_arr <= 0.7)] = 2
score_ndvi[(ndvi_arr > 0.3) & (ndvi_arr <= 0.5)] = 3
score_ndvi[(ndvi_arr > 0.1) & (ndvi_arr <= 0.3)] = 4
score_ndvi[ndvi_arr <= 0.1] = 5

# 3. Elevation
score_elev = np.zeros_like(dem_arr, dtype=np.float32)
score_elev[dem_arr <= elev_breaks[0]] = 1
score_elev[(dem_arr > elev_breaks[0]) & (dem_arr <= elev_breaks[1])] = 2
score_elev[(dem_arr > elev_breaks[1]) & (dem_arr <= elev_breaks[2])] = 3
score_elev[(dem_arr > elev_breaks[2]) & (dem_arr <= elev_breaks[3])] = 4
score_elev[dem_arr > elev_breaks[3]] = 5

# 4. NDMI
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

# Weighted Overlay
kl_continuous = (
    0.517 * score_slope +
    0.226 * score_ndvi +
    0.134 * score_elev +
    0.123 * score_ndmi
)
save_raster(kl_continuous_out, kl_continuous)

kl_classified = np.zeros_like(kl_continuous, dtype=np.uint8)
kl_classified[(kl_continuous >= 1.0) & (kl_continuous < 1.8)] = 1
kl_classified[(kl_continuous >= 1.8) & (kl_continuous < 2.6)] = 2
kl_classified[(kl_continuous >= 2.6) & (kl_continuous < 3.4)] = 3
kl_classified[(kl_continuous >= 3.4) & (kl_continuous < 4.2)] = 4
kl_classified[kl_continuous >= 4.2] = 5

save_raster(kl_classified_out, kl_classified, gdal.GDT_Byte, 0)

# Statistics
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

print(f"LUAS_TOTAL_HA: {total_area_ha:.2f}")
print(f"ELEV_MIN: {min_elev:.1f}")
print(f"ELEV_MAX: {max_elev:.1f}")
print(f"ELEV_MEAN: {mean_elev:.1f}")
print(f"ELEV_BREAKS: {[round(b, 1) for b in elev_breaks]}")
print(f"NDMI_BREAKS: {[round(b, 4) for b in ndmi_breaks]}")

print("TABEL_SLOPE:")
for lab, count in zip(slope_labels, slope_counts):
    print(f"  {lab}|{count*900/10000:.2f}|{count/total_valid_pixels*100:.2f}")

print(f"NDVI_MIN: {min_ndvi:.3f}")
print(f"NDVI_MAX: {max_ndvi:.3f}")
print(f"NDVI_MEAN: {mean_ndvi:.3f}")
print(f"NDMI_MIN: {min_ndmi:.3f}")
print(f"NDMI_MAX: {max_ndmi:.3f}")
print(f"NDMI_MEAN: {mean_ndmi:.3f}")
print(f"PEARSON_R: {r_pearson:.3f}")

print("TABEL_KL:")
for lab, count in zip(kl_labels, kl_counts):
    print(f"  {lab}|{count*900/10000:.2f}|{count/total_valid_pixels*100:.2f}")

high_ha = (kl_counts[3] + kl_counts[4]) * 900.0 / 10000.0
high_pct = (kl_counts[3] + kl_counts[4]) / total_valid_pixels * 100.0
print(f"TOTAL_HIGH_HA: {high_ha:.2f}")
print(f"TOTAL_HIGH_PCT: {high_pct:.2f}")

# Validation points
from qgis.core import QgsVectorLayer
layer_pts = QgsVectorLayer(pts_shp, "Titik BPBD", "ogr")
inv_gt = gdal.InvGeoTransform(gt)
print("VALIDASI_BPBD:")
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
    print(f"  {dusun}|{kl_labels[v_class - 1]}|{v_score:.2f}|{v_slope:.1f}|{v_elev:.1f}")

# Save to stats file
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
    f.write(f"Pearson r: {r_pearson:.3f}\n\n")
    f.write("Tabel 7. Luas Kelas Kerawanan Longsor:\n")
    for lab, c in zip(kl_labels, kl_counts):
        f.write(f"{lab}: {c*900/10000:.2f} ha ({c/total_valid_pixels*100:.2f}%)\n")
    f.write(f"Total Tinggi & Sangat Tinggi: {high_ha:.2f} ha ({high_pct:.2f}%)\n")

print("FINISHED_CALCULATION_SUCCESSFULLY")
