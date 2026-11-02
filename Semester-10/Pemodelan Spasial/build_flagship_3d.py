import os
import io
import math
import json
import base64
import numpy as np
from PIL import Image, ImageDraw

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"
repo_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/PemodelanSpasial-DesaTajuk"
sem10_web_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/web"
desktop_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"

print("--- 1. LOADING DATA RASTERS ---")
dem = np.array(Image.open(os.path.join(output_dir, "dem_tajuk_30m.tif"))).astype(np.float32)
slope = np.array(Image.open(os.path.join(output_dir, "slope_percent_tajuk.tif"))).astype(np.float32)
b2 = np.array(Image.open(os.path.join(output_dir, "b2_tajuk_30m.tif"))).astype(np.float32)
b3 = np.array(Image.open(os.path.join(output_dir, "b3_tajuk_30m.tif"))).astype(np.float32)
b4 = np.array(Image.open(os.path.join(output_dir, "b4_tajuk_30m.tif"))).astype(np.float32)
b5 = np.array(Image.open(os.path.join(output_dir, "b5_tajuk_30m.tif"))).astype(np.float32)
b6 = np.array(Image.open(os.path.join(output_dir, "b6_tajuk_30m.tif"))).astype(np.float32)
mask = np.array(Image.open(os.path.join(output_dir, "mask_tajuk.tif"))) == 1

rows, cols = dem.shape # 244, 134
scale = 4
w, h = cols * scale, rows * scale
xmin, ymax = 437850.0, 9183390.0

# 2. Computations
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

score_slope = np.zeros_like(slope, dtype=np.float32)
score_slope[(slope >= 0) & (slope < 8)] = 1
score_slope[(slope >= 8) & (slope < 15)] = 2
score_slope[(slope >= 15) & (slope < 25)] = 3
score_slope[(slope >= 25) & (slope < 45)] = 4
score_slope[slope >= 45] = 5

score_ndvi = np.zeros_like(ndvi, dtype=np.float32)
score_ndvi[ndvi > 0.7] = 1
score_ndvi[(ndvi > 0.5) & (ndvi <= 0.7)] = 2
score_ndvi[(ndvi > 0.3) & (ndvi <= 0.5)] = 3
score_ndvi[(ndvi > 0.1) & (ndvi <= 0.3)] = 4
score_ndvi[ndvi <= 0.1] = 5

elev_breaks = [1299.8, 1684.8, 2097.6, 2530.6, 3066.3]
score_elev = np.zeros_like(dem, dtype=np.float32)
score_elev[dem <= elev_breaks[0]] = 1
score_elev[(dem > elev_breaks[0]) & (dem <= elev_breaks[1])] = 2
score_elev[(dem > elev_breaks[1]) & (dem <= elev_breaks[2])] = 3
score_elev[(dem > elev_breaks[2]) & (dem <= elev_breaks[3])] = 4
score_elev[dem > elev_breaks[3]] = 5

ndmi_breaks = [0.0294, 0.1149, 0.1954, 0.2840, 0.4897]
score_ndmi = np.zeros_like(ndmi, dtype=np.float32)
score_ndmi[ndmi <= ndmi_breaks[0]] = 1
score_ndmi[(ndmi > ndmi_breaks[0]) & (ndmi <= ndmi_breaks[1])] = 2
score_ndmi[(ndmi > ndmi_breaks[1]) & (ndmi <= ndmi_breaks[2])] = 3
score_ndmi[(ndmi > ndmi_breaks[2]) & (ndmi <= ndmi_breaks[3])] = 4
score_ndmi[ndmi > ndmi_breaks[3]] = 5

kl_cont = 0.517 * score_slope + 0.226 * score_ndvi + 0.134 * score_elev + 0.123 * score_ndmi
kl_kelas = np.zeros_like(kl_cont, dtype=np.uint8)
kl_kelas[(kl_cont >= 1.0) & (kl_cont < 1.8)] = 1
kl_kelas[(kl_cont >= 1.8) & (kl_cont < 2.6)] = 2
kl_kelas[(kl_cont >= 2.6) & (kl_cont < 3.4)] = 3
kl_kelas[(kl_cont >= 3.4) & (kl_cont < 4.2)] = 4
kl_kelas[kl_cont >= 4.2] = 5

# Multidirectional hillshade
dz_dy, dz_dx = np.gradient(dem, 30.0)
slope_rad = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2))
aspect_rad = np.arctan2(-dz_dx, dz_dy)
sun_alt = np.radians(45.0)
sun_az = np.radians(315.0)
zenith_rad = np.pi/2 - sun_alt
hs_raw = np.cos(zenith_rad) * np.cos(slope_rad) + np.sin(zenith_rad) * np.sin(slope_rad) * np.cos(sun_az - aspect_rad)
hillshade = np.clip(hs_raw * 255.0, 0, 255).astype(np.float32) / 255.0
hs_mult = (0.35 + 0.65 * hillshade)[:, :, None]

# GeoJSON boundary
with open(os.path.join(output_dir, "batas_desa_tajuk.geojson"), "r") as f:
    geojson_data = json.load(f)
raw_coords = geojson_data["features"][0]["geometry"]["coordinates"][0]
pts_px = [((x - xmin) / 30.0 * scale, (ymax - y) / 30.0 * scale) for x, y, _ in raw_coords]

pts_3d = []
for x, y, _ in raw_coords:
    c = (x - xmin) / 30.0
    r = (ymax - y) / 30.0
    cr = int(round(np.clip(r, 0, rows-1)))
    cc = int(round(np.clip(c, 0, cols-1)))
    elev = float(dem[cr, cc])
    posX = round((c - cols / 2.0) * 30.0, 1)
    posZ = round((r - rows / 2.0) * 30.0, 1)
    pts_3d.append([posX, posZ, round(elev, 1)])

# Bake Textures Function
def bake_texture(base_rgb, border_color, halo_color, add_dusun_labels=False):
    im = Image.fromarray(base_rgb).resize((w, h), Image.BILINEAR)
    draw = ImageDraw.Draw(im)
    if halo_color:
        draw.line(pts_px, fill=halo_color, width=5)
    if border_color:
        draw.line(pts_px, fill=border_color, width=2)
    
    if add_dusun_labels:
        pois = [
            ("DUSUN GEDONG (Titik Longsor)", 438883.7, 9180016.3, (220, 20, 60)),
            ("DUSUN DUKOH (Jembatan Tertimbun)", 440304.8, 9182337.9, (0, 150, 255)),
            ("PUNCAK MERBABU (3.066 m)", 439800.0, 9176350.0, (255, 215, 0)),
            ("DUSUN NGADUMAN", 439600.0, 9179500.0, (50, 205, 50))
        ]
        for name, x, y, col in pois:
            px = int(round((x - xmin) / 30.0 * scale))
            py = int(round((ymax - y) / 30.0 * scale))
            r = 6
            draw.ellipse([px-r-1, py-r-1, px+r+1, py+r+1], fill=(0,0,0))
            draw.ellipse([px-r, py-r, px+r, py+r], fill=col)
            draw.text((px + 10, py - 6), name, fill=(255, 255, 255))
            
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

# 1. AHP Hazard
ahp_rgb = np.zeros((rows, cols, 3), dtype=np.uint8)
ahp_rgb[~mask] = [210, 212, 205]
colors = {
    1: [26, 150, 65],
    2: [166, 217, 106],
    3: [255, 255, 115],
    4: [253, 174, 97],
    5: [215, 25, 28]
}
for k, col in colors.items():
    ahp_rgb[mask & (kl_kelas == k)] = col
ahp_blend = np.clip(ahp_rgb.astype(np.float32) * hs_mult, 0, 255).astype(np.uint8)
b64_ahp = bake_texture(ahp_blend, (0, 245, 255), (10, 25, 35), add_dusun_labels=True)

# 2. Landsat Natural RGB
def stretch_band(b):
    p2, p98 = np.percentile(b, (2, 98))
    norm = np.clip((b - p2) / (p98 - p2 + 1e-6), 0.0, 1.0)
    return np.power(norm, 0.85)

r_s = stretch_band(b4)
g_s = stretch_band(b3)
b_s = stretch_band(b2)
sat_rgb = np.clip(np.stack([r_s, g_s, b_s], axis=-1) * 255.0, 0, 255).astype(np.uint8)
sat_dimmed = sat_rgb.copy()
sat_dimmed[~mask] = (sat_dimmed[~mask].astype(np.float32) * 0.70).astype(np.uint8)
b64_sat_rgb = bake_texture(sat_dimmed, (255, 255, 255), (0, 0, 0))

# 3. Landsat False Color CIR (B5, B4, B3)
nir_s = stretch_band(b5)
cir_rgb = np.clip(np.stack([nir_s, r_s, g_s], axis=-1) * 255.0, 0, 255).astype(np.uint8)
cir_dimmed = cir_rgb.copy()
cir_dimmed[~mask] = (cir_dimmed[~mask].astype(np.float32) * 0.70).astype(np.uint8)
b64_sat_cir = bake_texture(cir_dimmed, (255, 215, 0), (0, 0, 0))

# 4. Slope %
slope_rgb = np.zeros((rows, cols, 3), dtype=np.uint8)
slope_rgb[~mask] = [210, 212, 205]
slope_cols = {
    1: [43, 131, 186],
    2: [171, 221, 164],
    3: [255, 255, 191],
    4: [253, 174, 97],
    5: [215, 25, 28]
}
for k, col in slope_cols.items():
    slope_rgb[mask & (score_slope == k)] = col
slope_blend = np.clip(slope_rgb.astype(np.float32) * hs_mult, 0, 255).astype(np.uint8)
b64_slope = bake_texture(slope_blend, (0, 245, 255), (10, 25, 35))

# 5. Hypsometric Elevation
elev_norm = np.clip((dem - 938.0) / (3066.3 - 938.0), 0.0, 1.0)
elev_r = np.clip(elev_norm * 2.2 * 255, 0, 255).astype(np.uint8)
elev_g = np.clip((1.0 - np.abs(elev_norm - 0.35) * 1.5) * 255, 0, 255).astype(np.uint8)
elev_b = np.clip((1.0 - elev_norm * 1.5) * 200, 0, 255).astype(np.uint8)
elev_rgb = np.stack([elev_r, elev_g, elev_b], axis=-1)
elev_blend = np.clip(elev_rgb.astype(np.float32) * hs_mult, 0, 255).astype(np.uint8)
b64_elev = bake_texture(elev_blend, (255, 255, 255), (0, 0, 0))

# Data Arrays
min_elev = float(dem.min())
max_elev = float(dem.max())
dem_arr = [[round(float(dem[r, c]), 1) for c in range(cols)] for r in range(rows)]
slope_arr = [[round(float(slope[r, c]), 1) for c in range(cols)] for r in range(rows)]
kl_arr = [[int(kl_kelas[r, c]) for c in range(cols)] for r in range(rows)]
kl_score_arr = [[round(float(kl_cont[r, c]), 2) for c in range(cols)] for r in range(rows)]
mask_arr = [[int(mask[r, c]) for c in range(cols)] for r in range(rows)]
ndvi_arr = [[round(float(ndvi[r, c]), 2) for c in range(cols)] for r in range(rows)]

flow_pts_raw = [
    (439300.0, 9177500.0, 2450.0),
    (439050.0, 9178800.0, 1950.0),
    (438900.0, 9179800.0, 1680.0),
    (439300.0, 9180700.0, 1450.0),
    (439850.0, 9181600.0, 1250.0),
    (440304.8, 9182337.9, 1084.1)
]
flow_pts_3d = []
for x, y, z in flow_pts_raw:
    c = (x - xmin) / 30.0
    r = (ymax - y) / 30.0
    posX = round((c - cols / 2.0) * 30.0, 1)
    posZ = round((r - rows / 2.0) * 30.0, 1)
    flow_pts_3d.append([posX, posZ, z])

with open(os.path.join(output_dir, "three.min.js"), "r", encoding="utf-8") as f:
    three_js_code = f.read()
with open(os.path.join(output_dir, "OrbitControls.js"), "r", encoding="utf-8") as f:
    orbit_controls_code = f.read()

# Load taste html template
print("--- 3. COMPILING TASTE SKILL WEBGL DASHBOARD ---")
