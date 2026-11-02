import os
import math
import numpy as np
from PIL import Image

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"

# 1. Load reference DEM for tags
dem_im = Image.open(os.path.join(output_dir, "dem_tajuk_30m.tif"))
tags = dem_im.tag_v2

dem = np.array(dem_im)
slope = np.array(Image.open(os.path.join(output_dir, "slope_percent_tajuk.tif")))
b4 = np.array(Image.open(os.path.join(output_dir, "b4_tajuk_30m.tif"))).astype(np.float32)
b5 = np.array(Image.open(os.path.join(output_dir, "b5_tajuk_30m.tif"))).astype(np.float32)
b6 = np.array(Image.open(os.path.join(output_dir, "b6_tajuk_30m.tif"))).astype(np.float32)
mask = np.array(Image.open(os.path.join(output_dir, "mask_tajuk.tif"))) == 1

# Convert Landsat DN to TOA Reflectance
# MULT = 2.0E-5, ADD = -0.1, SUN_ELEV = 64.52967777 deg
sin_sun = math.sin(math.radians(64.52967777))
toa4 = (b4 * 2.0e-5 - 0.1) / sin_sun
toa5 = (b5 * 2.0e-5 - 0.1) / sin_sun
toa6 = (b6 * 2.0e-5 - 0.1) / sin_sun

denom_ndvi = toa5 + toa4
denom_ndvi[denom_ndvi == 0] = 1e-6
ndvi = np.clip((toa5 - toa4) / denom_ndvi, -1.0, 1.0)

denom_ndmi = toa5 + toa6
denom_ndmi[denom_ndmi == 0] = 1e-6
ndmi = np.clip((toa5 - toa6) / denom_ndmi, -1.0, 1.0)

valid = mask & (dem > 0)
dem_vals = dem[valid]
slope_vals = slope[valid]
ndvi_vals = ndvi[valid]
ndmi_vals = ndmi[valid]

total_pixels = len(dem_vals)
total_ha = total_pixels * 900.0 / 10000.0

# Fisher-Jenks breaks function
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

# 1. Slope (%) Score (Table 2)
# 0-8%: 1, 8-15%: 2, 15-25%: 3, 25-45%: 4, >45%: 5
score_slope = np.zeros_like(slope, dtype=np.float32)
score_slope[(slope >= 0) & (slope < 8)] = 1
score_slope[(slope >= 8) & (slope < 15)] = 2
score_slope[(slope >= 15) & (slope < 25)] = 3
score_slope[(slope >= 25) & (slope < 45)] = 4
score_slope[slope >= 45] = 5

# 2. NDVI Score (Table 2)
# >0.7: 1, 0.5-0.7: 2, 0.3-0.5: 3, 0.1-0.3: 4, <=0.1: 5
score_ndvi = np.zeros_like(ndvi, dtype=np.float32)
score_ndvi[ndvi > 0.7] = 1
score_ndvi[(ndvi > 0.5) & (ndvi <= 0.7)] = 2
score_ndvi[(ndvi > 0.3) & (ndvi <= 0.5)] = 3
score_ndvi[(ndvi > 0.1) & (ndvi <= 0.3)] = 4
score_ndvi[ndvi <= 0.1] = 5

# 3. Elevation Score (Jenks 5 classes, higher = 5)
score_elev = np.zeros_like(dem, dtype=np.float32)
score_elev[dem <= elev_breaks[0]] = 1
score_elev[(dem > elev_breaks[0]) & (dem <= elev_breaks[1])] = 2
score_elev[(dem > elev_breaks[1]) & (dem <= elev_breaks[2])] = 3
score_elev[(dem > elev_breaks[2]) & (dem <= elev_breaks[3])] = 4
score_elev[dem > elev_breaks[3]] = 5

# 4. NDMI Score (Jenks 5 classes, wetter = 5)
score_ndmi = np.zeros_like(ndmi, dtype=np.float32)
score_ndmi[ndmi <= ndmi_breaks[0]] = 1
score_ndmi[(ndmi > ndmi_breaks[0]) & (ndmi <= ndmi_breaks[1])] = 2
score_ndmi[(ndmi > ndmi_breaks[1]) & (ndmi <= ndmi_breaks[2])] = 3
score_ndmi[(ndmi > ndmi_breaks[2]) & (ndmi <= ndmi_breaks[3])] = 4
score_ndmi[ndmi > ndmi_breaks[3]] = 5

# Weighted Overlay: KL = 0.517*Slope + 0.226*NDVI + 0.134*Elev + 0.123*NDMI
kl_continuous = (
    0.517 * score_slope +
    0.226 * score_ndvi +
    0.134 * score_elev +
    0.123 * score_ndmi
)

# Classify into 5 classes:
# 1.0 - 1.8: Sangat Rendah (1)
# 1.8 - 2.6: Rendah (2)
# 2.6 - 3.4: Sedang (3)
# 3.4 - 4.2: Tinggi (4)
# 4.2 - 5.0: Sangat Tinggi (5)
kl_classified = np.zeros_like(kl_continuous, dtype=np.uint8)
kl_classified[(kl_continuous >= 1.0) & (kl_continuous < 1.8)] = 1
kl_classified[(kl_continuous >= 1.8) & (kl_continuous < 2.6)] = 2
kl_classified[(kl_continuous >= 2.6) & (kl_continuous < 3.4)] = 3
kl_classified[(kl_continuous >= 3.4) & (kl_continuous < 4.2)] = 4
kl_classified[kl_continuous >= 4.2] = 5

# Apply mask for outputs
def save_tiff(name, arr, dtype=np.float32, nodata=-9999.0):
    out = arr.copy().astype(dtype)
    if dtype == np.uint8:
        out[~valid] = 0
    else:
        out[~valid] = nodata
    im = Image.fromarray(out)
    im.save(os.path.join(output_dir, name), tiffinfo=tags)

save_tiff("ndvi_tajuk.tif", ndvi)
save_tiff("ndmi_tajuk.tif", ndmi)
save_tiff("score_slope.tif", score_slope, np.uint8)
save_tiff("score_ndvi.tif", score_ndvi, np.uint8)
save_tiff("score_elev.tif", score_elev, np.uint8)
save_tiff("score_ndmi.tif", score_ndmi, np.uint8)
save_tiff("kerawanan_longsor_continuous.tif", kl_continuous)
save_tiff("kerawanan_longsor_kelas.tif", kl_classified, np.uint8)

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

kl_vals = kl_classified[valid]
kl_counts = [
    int(np.sum(kl_vals == 1)),
    int(np.sum(kl_vals == 2)),
    int(np.sum(kl_vals == 3)),
    int(np.sum(kl_vals == 4)),
    int(np.sum(kl_vals == 5))
]
kl_labels = ["Sangat Rendah", "Rendah", "Sedang", "Tinggi", "Sangat Tinggi"]

print("="*60)
print("HASIL ANALISIS LENGKAP PEMODELAN KERAWANAN LONGSOR DESA TAJUK")
print("="*60)
print(f"Luas Total Desa Tajuk: {total_ha:.2f} ha ({total_pixels} piksel 30m x 30m)")
print(f"Ketinggian: Min = {min_elev:.1f} m, Max = {max_elev:.1f} m, Mean = {mean_elev:.1f} m")
print(f"Jenks Kelas Ketinggian (m): {[round(b, 1) for b in elev_breaks]}")
print(f"Jenks Kelas NDMI: {[round(b, 4) for b in ndmi_breaks]}")

print("\nTabel 5. Sebaran Kemiringan Lereng:")
for lab, count in zip(slope_labels, slope_counts):
    ha = count * 900.0 / 10000.0
    pct = count / total_pixels * 100.0
    print(f"  {lab:22s}: {ha:8.2f} ha ({pct:5.2f}%)")

print("\nTabel 6. Statistik NDVI & NDMI:")
print(f"  NDVI: Min = {min_ndvi:.3f}, Max = {max_ndvi:.3f}, Mean = {mean_ndvi:.3f}")
print(f"  NDMI: Min = {min_ndmi:.3f}, Max = {max_ndmi:.3f}, Mean = {mean_ndmi:.3f}")
print(f"  Korelasi Pearson (r): {r_pearson:.3f}")

print("\nTabel 7. Luas Kelas Kerawanan Longsor:")
for lab, count in zip(kl_labels, kl_counts):
    ha = count * 900.0 / 10000.0
    pct = count / total_pixels * 100.0
    print(f"  {lab:22s}: {ha:8.2f} ha ({pct:5.2f}%)")

high_ha = (kl_counts[3] + kl_counts[4]) * 900.0 / 10000.0
high_pct = (kl_counts[3] + kl_counts[4]) / total_pixels * 100.0
print(f"\nTotal Area Rawan (Tinggi + Sangat Tinggi): {high_ha:.2f} ha ({high_pct:.2f}%)")

# Sample at BPBD points
# Extent origin: xmin = 437850.0, ymax = 9183390.0, res = 30.0
# Pixel col = (x - xmin)/30, row = (ymax - y)/30
xmin = 437850.0
ymax = 9183390.0

points = [
    ("Dusun Gedong", 438883.7, 9180016.3),
    ("Dusun Dukoh", 440304.8, 9182337.9)
]

print("\nValidasi Titik BPBD:")
val_records = []
for name, x, y in points:
    c = int(round((x - xmin) / 30.0))
    r = int(round((ymax - y) / 30.0))
    v_class = int(kl_classified[r, c])
    v_score = float(kl_continuous[r, c])
    v_slope = float(slope[r, c])
    v_elev = float(dem[r, c])
    v_ndvi = float(ndvi[r, c])
    v_ndmi = float(ndmi[r, c])
    label_class = kl_labels[v_class - 1]
    val_records.append((name, label_class, v_score, v_slope, v_elev, v_ndvi, v_ndmi))
    print(f"  {name}: Kelas = {label_class} (Skor = {v_score:.2f}, Lereng = {v_slope:.1f}%, Elevasi = {v_elev:.1f} m, NDVI = {v_ndvi:.2f}, NDMI = {v_ndmi:.2f})")

# Write text report
report_path = os.path.join(output_dir, "hasil_analisis_jurnal.txt")
with open(report_path, "w", encoding="utf-8") as f:
    f.write(f"Luas Wilayah Kajian Desa Tajuk: {total_ha:.2f} ha ({total_pixels} piksel)\n")
    f.write(f"Rentang Elevasi: {min_elev:.1f} - {max_elev:.1f} m (Rata-rata: {mean_elev:.1f} m)\n")
    f.write(f"Batas Kelas Ketinggian Jenks: {[round(b, 1) for b in elev_breaks]}\n")
    f.write(f"Batas Kelas NDMI Jenks: {[round(b, 4) for b in ndmi_breaks]}\n\n")
    
    f.write("Tabel 5. Sebaran Kelas Kemiringan Lereng:\n")
    for lab, count in zip(slope_labels, slope_counts):
        f.write(f"{lab}: {count*900/10000:.2f} ha ({count/total_pixels*100:.2f}%)\n")
    
    f.write(f"\nTabel 6. Statistik NDVI & NDMI:\n")
    f.write(f"NDVI: Min={min_ndvi:.3f}, Max={max_ndvi:.3f}, Mean={mean_ndvi:.3f}\n")
    f.write(f"NDMI: Min={min_ndmi:.3f}, Max={max_ndmi:.3f}, Mean={mean_ndmi:.3f}\n")
    f.write(f"Koefisien Korelasi Pearson (r): {r_pearson:.3f}\n\n")
    
    f.write("Tabel 7. Luas Kelas Kerawanan Longsor Desa Tajuk:\n")
    for lab, count in zip(kl_labels, kl_counts):
        f.write(f"{lab}: {count*900/10000:.2f} ha ({count/total_pixels*100:.2f}%)\n")
    
    f.write(f"\nTotal Kelas Tinggi & Sangat Tinggi: {high_ha:.2f} ha ({high_pct:.2f}%)\n\n")
    
    f.write("Validasi dengan Titik Kejadian BPBD (28 Februari 2024):\n")
    for name, c_name, score, sl, el, nd, nm in val_records:
        f.write(f"{name}: Kelas {c_name} (Skor {score:.2f}, Lereng {sl:.1f}%, Elevasi {el:.1f} m, NDVI {nd:.2f}, NDMI {nm:.2f})\n")

print(f"\nSummary successfully written to: {report_path}")
