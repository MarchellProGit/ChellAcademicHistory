import os
import io
import math
import json
import base64
import numpy as np
from PIL import Image, ImageDraw

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"
desktop_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"

print("--- 1. LOADING GEOSPATIAL RASTERS ---")
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

print(f"Grid dimensions: {cols} cols x {rows} rows (30m cell)")

# --- 2. SPECTRAL & AHP MODELING ---
print("--- 2. COMPUTING INDICES & AHP SCORES ---")
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

# --- 3. MULTIDIRECTIONAL HILLSHADE ---
print("--- 3. COMPUTING HILLSHADE ---")
dz_dy, dz_dx = np.gradient(dem, 30.0)
slope_rad = np.arctan(np.sqrt(dz_dx**2 + dz_dy**2))
aspect_rad = np.arctan2(-dz_dx, dz_dy)
sun_alt = np.radians(45.0)
sun_az = np.radians(315.0)
zenith_rad = np.pi/2 - sun_alt
hs_raw = np.cos(zenith_rad) * np.cos(slope_rad) + np.sin(zenith_rad) * np.sin(slope_rad) * np.cos(sun_az - aspect_rad)
hillshade = np.clip(hs_raw * 255.0, 0, 255).astype(np.float32) / 255.0
hs_mult = (0.35 + 0.65 * hillshade)[:, :, None]

# --- 4. VECTOR BOUNDARY POLYGON ---
print("--- 4. PARSING BOUNDARY VERTICES ---")
geojson_path = os.path.join(output_dir, "batas_desa_tajuk.geojson")
with open(geojson_path, "r") as f:
    geojson_data = json.load(f)
raw_coords = geojson_data["features"][0]["geometry"]["coordinates"][0]

# Pixel points for Pillow drawing
pts_px = [((x - xmin) / 30.0 * scale, (ymax - y) / 30.0 * scale) for x, y, _ in raw_coords]

# 3D points for Three.js Line (centered, normalized)
# Grid width = cols * 30 = 4020, length = rows * 30 = 7320
pts_3d = []
for x, y, _ in raw_coords:
    c = (x - xmin) / 30.0
    r = (ymax - y) / 30.0
    cr = int(round(np.clip(r, 0, rows-1)))
    cc = int(round(np.clip(c, 0, cols-1)))
    elev = float(dem[cr, cc])
    posX = round((c - cols / 2.0) * 30.0, 1)
    posZ = round((r - rows / 2.0) * 30.0, 1) # Y is up in Three.js, so Z is North-South
    pts_3d.append([posX, posZ, round(elev, 1)])

# --- 5. GENERATE 5 ULTRA-CRISP TEXTURES (BASE64) ---
print("--- 5. BAKING 5 HIGH-RESOLUTION 3D TEXTURES ---")
def bake_texture(base_rgb, border_color, halo_color, add_dusun_labels=False):
    im = Image.fromarray(base_rgb).resize((w, h), Image.BILINEAR)
    draw = ImageDraw.Draw(im)
    if halo_color:
        draw.line(pts_px, fill=halo_color, width=5)
    if border_color:
        draw.line(pts_px, fill=border_color, width=2)
    
    if add_dusun_labels:
        # Markers
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
            # Label
            draw.text((px + 10, py - 6), name, fill=(255, 255, 255))
            
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

# 1. AHP Hazard
ahp_rgb = np.zeros((rows, cols, 3), dtype=np.uint8)
ahp_rgb[~mask] = [210, 212, 205]
ahp_colors = {
    1: [26, 150, 65],
    2: [166, 217, 106],
    3: [255, 255, 115],
    4: [253, 174, 97],
    5: [215, 25, 28]
}
for k, col in ahp_colors.items():
    ahp_rgb[mask & (kl_kelas == k)] = col
ahp_blend = np.clip(ahp_rgb.astype(np.float32) * hs_mult, 0, 255).astype(np.uint8)
b64_ahp = bake_texture(ahp_blend, (0, 245, 255), (10, 25, 35), add_dusun_labels=True)
print("  - AHP Texture ready.")

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
print("  - Landsat Natural Color RGB ready.")

# 3. Landsat False Color CIR (B5, B4, B3)
nir_s = stretch_band(b5)
cir_rgb = np.clip(np.stack([nir_s, r_s, g_s], axis=-1) * 255.0, 0, 255).astype(np.uint8)
cir_dimmed = cir_rgb.copy()
cir_dimmed[~mask] = (cir_dimmed[~mask].astype(np.float32) * 0.70).astype(np.uint8)
b64_sat_cir = bake_texture(cir_dimmed, (255, 215, 0), (0, 0, 0))
print("  - Landsat False Color CIR ready.")

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
print("  - Slope Texture ready.")

# 5. Topographic Hypsometric Relief
elev_norm = np.clip((dem - 938.0) / (3066.3 - 938.0), 0.0, 1.0)
elev_r = np.clip(elev_norm * 2.2 * 255, 0, 255).astype(np.uint8)
elev_g = np.clip((1.0 - np.abs(elev_norm - 0.35) * 1.5) * 255, 0, 255).astype(np.uint8)
elev_b = np.clip((1.0 - elev_norm * 1.5) * 200, 0, 255).astype(np.uint8)
elev_rgb = np.stack([elev_r, elev_g, elev_b], axis=-1)
elev_blend = np.clip(elev_rgb.astype(np.float32) * hs_mult, 0, 255).astype(np.uint8)
b64_elev = bake_texture(elev_blend, (255, 255, 255), (0, 0, 0))
print("  - Hypsometric Texture ready.")

# --- 6. PREPARE 3D RASTER DATA ARRAYS ---
print("--- 6. PACKAGING DATA ARRAYS ---")
min_elev = float(dem.min())
max_elev = float(dem.max())

# Round values for compact JSON payload
dem_arr = [[round(float(dem[r, c]), 1) for c in range(cols)] for r in range(rows)]
slope_arr = [[round(float(slope[r, c]), 1) for c in range(cols)] for r in range(rows)]
kl_arr = [[int(kl_kelas[r, c]) for c in range(cols)] for r in range(rows)]
kl_score_arr = [[round(float(kl_cont[r, c]), 2) for c in range(cols)] for r in range(rows)]
mask_arr = [[int(mask[r, c]) for c in range(cols)] for r in range(rows)]
ndvi_arr = [[round(float(ndvi[r, c]), 2) for c in range(cols)] for r in range(rows)]

# 3D Debris Flow stream path (Hulu lereng curam Merbabu -> Gedong -> Lembah -> Dukoh)
flow_pts_raw = [
    (439300.0, 9177500.0, 2450.0),
    (439050.0, 9178800.0, 1950.0),
    (438900.0, 9179800.0, 1680.0),
    (439300.0, 9180700.0, 1450.0),
    (439850.0, 9181600.0, 1250.0),
    (440304.8, 9182337.9, 1084.1) # Jembatan Dukoh
]
flow_pts_3d = []
for x, y, z in flow_pts_raw:
    c = (x - xmin) / 30.0
    r = (ymax - y) / 30.0
    posX = round((c - cols / 2.0) * 30.0, 1)
    posZ = round((r - rows / 2.0) * 30.0, 1)
    flow_pts_3d.append([posX, posZ, z])

print("Data arrays packaged successfully.")

# Read local three.js files for inline or fallback embedding
three_js_code = ""
orbit_controls_code = ""
with open(os.path.join(output_dir, "three.min.js"), "r", encoding="utf-8") as f:
    three_js_code = f.read()
with open(os.path.join(output_dir, "OrbitControls.js"), "r", encoding="utf-8") as f:
    orbit_controls_code = f.read()

print("Three.js libraries read from local cache.")

# --- 7. COMPOSE COMPREHENSIVE 3D HTML VIEWER ---
print("--- 7. GENERATING INTERACTIVE 3D WEBGL APPLICATION ---")

html_code = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Model Topografi 3D & Kerawanan Longsor Desa Tajuk - Gunung Merbabu</title>
    <style>
        :root {{
            --bg-glass: rgba(15, 23, 42, 0.88);
            --border-glass: rgba(255, 255, 255, 0.12);
            --accent: #38bdf8;
            --accent-hover: #0284c7;
            --text-light: #f8fafc;
            --text-dim: #94a3b8;
        }}
        * {{ box-sizing: border-box; }}
        body, html {{
            margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #0b1120; color: var(--text-light); user-select: none;
        }}
        #canvas-container {{ width: 100vw; height: 100vh; display: block; position: absolute; top: 0; left: 0; z-index: 1; }}

        /* HUD & Panels */
        .glass-panel {{
            background: var(--bg-glass);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid var(--border-glass);
            border-radius: 14px;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55);
            z-index: 10;
            color: var(--text-light);
        }}

        #main-dashboard {{
            position: absolute; top: 18px; left: 18px;
            width: 360px; max-height: calc(100vh - 36px);
            display: flex; flex-direction: column;
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        #main-dashboard.minimized {{
            transform: translateX(-380px);
        }}
        .panel-header {{
            padding: 16px 20px 12px; border-bottom: 1px solid var(--border-glass);
            display: flex; justify-content: space-between; align-items: flex-start;
        }}
        .panel-title {{ margin: 0; font-size: 15px; font-weight: 700; color: #38bdf8; letter-spacing: 0.3px; }}
        .panel-subtitle {{ margin: 3px 0 0; font-size: 11px; color: var(--text-dim); line-height: 1.4; }}
        
        .toggle-btn {{
            background: rgba(255,255,255,0.08); border: 1px solid var(--border-glass);
            color: #fff; border-radius: 8px; width: 28px; height: 28px;
            cursor: pointer; display: flex; align-items: center; justify-content: center;
            font-size: 14px; transition: all 0.2s;
        }}
        .toggle-btn:hover {{ background: rgba(56, 189, 248, 0.25); border-color: var(--accent); }}

        #btn-reopen {{
            position: absolute; top: 18px; left: 18px; z-index: 9;
            padding: 10px 14px; font-size: 12px; font-weight: 600;
            cursor: pointer; display: none; align-items: center; gap: 8px;
        }}

        .panel-content {{
            padding: 16px 20px; overflow-y: auto; flex: 1;
        }}
        .panel-content::-webkit-scrollbar {{ width: 5px; }}
        .panel-content::-webkit-scrollbar-thumb {{ background: rgba(255,255,255,0.2); border-radius: 4px; }}

        .section-label {{
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.8px; color: #38bdf8; margin: 14px 0 8px;
            display: flex; align-items: center; gap: 6px;
        }}
        .section-label:first-child {{ margin-top: 0; }}

        /* Layer Selector Grid */
        .layer-grid {{
            display: grid; grid-template-columns: 1fr 1fr; gap: 6px; margin-bottom: 12px;
        }}
        .layer-btn {{
            background: rgba(255,255,255,0.05); border: 1px solid var(--border-glass);
            color: #e2e8f0; border-radius: 8px; padding: 8px 10px;
            font-size: 11px; font-weight: 600; cursor: pointer; text-align: left;
            display: flex; align-items: center; gap: 6px; transition: all 0.2s;
        }}
        .layer-btn:hover {{ background: rgba(255,255,255,0.12); }}
        .layer-btn.active {{
            background: rgba(2, 132, 199, 0.35); border-color: #38bdf8; color: #38bdf8;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }}

        /* Slider Controls */
        .control-row {{ margin-bottom: 12px; }}
        .slider-label {{
            display: flex; justify-content: space-between; font-size: 11px;
            color: #cbd5e1; margin-bottom: 5px; font-weight: 500;
        }}
        .slider-label span.val {{ color: #38bdf8; font-weight: 700; }}
        input[type=range] {{
            width: 100%; height: 5px; border-radius: 4px;
            background: rgba(255,255,255,0.15); outline: none;
            -webkit-appearance: none; cursor: pointer; accent-color: #38bdf8;
        }}

        /* Button Grid */
        .btn-group {{
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 12px;
        }}
        .action-btn {{
            background: rgba(255,255,255,0.06); border: 1px solid var(--border-glass);
            color: #f1f5f9; padding: 7px 8px; border-radius: 6px;
            font-size: 10.5px; font-weight: 600; cursor: pointer; text-align: center;
            transition: all 0.2s; display: flex; align-items: center; justify-content: center; gap: 4px;
        }}
        .action-btn:hover {{ background: rgba(56, 189, 248, 0.2); border-color: #38bdf8; }}
        .action-btn.active {{ background: #0284c7; border-color: #38bdf8; }}

        /* Legend */
        .legend-card {{
            background: rgba(0,0,0,0.25); border: 1px solid var(--border-glass);
            border-radius: 8px; padding: 10px 12px; font-size: 11px; margin-top: 10px;
        }}
        .legend-item {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 5px; }}
        .legend-item:last-child {{ margin-bottom: 0; }}
        .legend-left {{ display: flex; align-items: center; gap: 8px; }}
        .color-dot {{ width: 12px; height: 12px; border-radius: 3px; flex-shrink: 0; border: 1px solid rgba(0,0,0,0.2); }}

        /* Inspector / Inspector Card */
        #inspector-badge {{
            position: absolute; bottom: 20px; right: 20px; z-index: 10;
            padding: 14px 18px; width: 310px; font-size: 11px; line-height: 1.5;
        }}
        .badge-title {{ font-weight: 700; color: #38bdf8; font-size: 12px; margin-bottom: 4px; display: flex; align-items: center; gap: 6px; }}
        .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4px 12px; margin-top: 6px; }}
        .stat-row {{ display: flex; justify-content: space-between; }}
        .stat-name {{ color: var(--text-dim); }}
        .stat-val {{ font-weight: 600; color: #f8fafc; }}

        /* Compass HUD */
        #compass-widget {{
            position: absolute; top: 18px; right: 18px; z-index: 10;
            width: 46px; height: 46px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: transform 0.2s;
        }}
        #compass-arrow {{
            width: 24px; height: 24px; transition: transform 0.1s linear;
        }}

        /* Modal Card for Pin Details */
        #pin-modal {{
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0.9);
            width: 440px; max-width: 90vw; padding: 22px 26px; z-index: 100;
            opacity: 0; pointer-events: none; transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        #pin-modal.visible {{
            transform: translate(-50%, -50%) scale(1);
            opacity: 1; pointer-events: auto;
        }}
        .modal-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
        .modal-title {{ margin: 0; font-size: 16px; font-weight: 700; color: #38bdf8; }}
        .modal-close {{ background: none; border: none; color: #cbd5e1; font-size: 20px; cursor: pointer; }}
        .modal-body {{ font-size: 12px; line-height: 1.6; color: #e2e8f0; }}

        /* Instructions Toast */
        #help-toast {{
            position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%);
            padding: 8px 18px; font-size: 11px; z-index: 5;
            background: rgba(15, 23, 42, 0.75); border: 1px solid var(--border-glass);
            border-radius: 20px; color: #94a3b8; pointer-events: none; text-align: center;
        }}
    </style>

    <!-- INLINE THREE.JS ENGINE (100% OFFLINE, ZERO EXTERNAL DEPENDENCIES) -->
    <script>
        {three_js_code}
    </script>
    <script>
        {orbit_controls_code}
    </script>
</head>
<body>

    <!-- 3D WebGL Canvas Container -->
    <div id="canvas-container"></div>

    <!-- Re-open Dashboard Button -->
    <button id="btn-reopen" class="glass-panel" onclick="toggleDashboard()">
        ☰ Panel Kontrol 3D
    </button>

    <!-- Compass HUD -->
    <div id="compass-widget" class="glass-panel" onclick="resetNorth()" title="Klik untuk Reset Arah Utara">
        <svg id="compass-arrow" viewBox="0 0 100 100">
            <polygon points="50,10 65,50 50,42" fill="#ef4444" />
            <polygon points="50,10 35,50 50,42" fill="#dc2626" />
            <polygon points="50,90 65,50 50,42" fill="#cbd5e1" />
            <polygon points="50,90 35,50 50,42" fill="#94a3b8" />
            <circle cx="50" cy="50" r="5" fill="#38bdf8" />
            <text x="50" y="24" font-size="14" font-weight="bold" fill="#ef4444" text-anchor="middle">U</text>
        </svg>
    </div>

    <!-- Main Glassmorphism Dashboard -->
    <div id="main-dashboard" class="glass-panel">
        <div class="panel-header">
            <div>
                <h1 class="panel-title">Model Digital 3D Desa Tajuk</h1>
                <p class="panel-subtitle">Kecamatan Getasan, Kabupaten Semarang<br>Lereng Utara Gunung Merbabu</p>
            </div>
            <button class="toggle-btn" onclick="toggleDashboard()" title="Tutup Panel">✕</button>
        </div>

        <div class="panel-content">
            <!-- 1. Lapisan Peta Tematik (Multi-Texture) -->
            <div class="section-label">🗺️ Pilihan Lapisan 3D</div>
            <div class="layer-grid">
                <button id="btn-layer-ahp" class="layer-btn active" onclick="switchLayer('ahp')">
                    🛡️ Kerawanan AHP
                </button>
                <button id="btn-layer-sat" class="layer-btn" onclick="switchLayer('sat_rgb')">
                    🛰️ Citra Satelit RGB
                </button>
                <button id="btn-layer-cir" class="layer-btn" onclick="switchLayer('sat_cir')">
                    🌿 Inframerah (CIR)
                </button>
                <button id="btn-layer-elev" class="layer-btn" onclick="switchLayer('elev')">
                    ⛰️ Relif Elevasi
                </button>
                <button id="btn-layer-slope" class="layer-btn" onclick="switchLayer('slope')" style="grid-column: span 2;">
                    📐 Peta Kemiringan Lereng (%)
                </button>
            </div>

            <!-- 2. Kontrol Terrain & Sudut Pandang -->
            <div class="section-label">⚙️ Pengaturan Topografi & Cahaya</div>
            <div class="control-row">
                <div class="slider-label">
                    <span>Eksagerasi Vertikal (Tinggi)</span>
                    <span id="lbl-exag" class="val">1.5x</span>
                </div>
                <input type="range" id="slider-exag" min="0.5" max="3.0" step="0.1" value="1.5" oninput="setExaggeration(this.value)">
            </div>

            <div class="control-row">
                <div class="slider-label">
                    <span>Sudut Matahari (Pencahayaan)</span>
                    <span id="lbl-sun" class="val">315° (Barat Laut)</span>
                </div>
                <input type="range" id="slider-sun" min="0" max="360" step="5" value="315" oninput="setSunAngle(this.value)">
            </div>

            <div class="control-row">
                <div class="slider-label">
                    <span>Intensitas Cahaya Terang</span>
                    <span id="lbl-light" class="val">100%</span>
                </div>
                <input type="range" id="slider-light" min="0.4" max="1.6" step="0.05" value="1.0" oninput="setLightIntensity(this.value)">
            </div>

            <!-- 3. Kamera & Fitur Interaktif -->
            <div class="section-label">🎥 Sudut Kamera & Presets</div>
            <div class="btn-group">
                <button class="action-btn" onclick="setPresetView('iso')">🌐 3D Isometrik</button>
                <button class="action-btn" onclick="setPresetView('top')">🦅 2D Nadir</button>
                <button class="action-btn" onclick="setPresetView('valley')">⬆️ Lembah Bawah</button>
                <button class="action-btn" onclick="setPresetView('summit')">⬇️ Dari Puncak</button>
                <button class="action-btn" onclick="flyToPoint('gedong')">🔴 Dusun Gedong</button>
                <button class="action-btn" onclick="flyToPoint('dukoh')">🔵 Dusun Dukoh</button>
            </div>

            <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                <button id="btn-tour" class="action-btn" style="flex: 1; padding: 9px;" onclick="toggleCinematicTour()">
                    ▶️ Tur Sinematik 3D
                </button>
                <button class="action-btn" style="flex: 1; padding: 9px;" onclick="toggleWireframe()">
                    🕸️ Wireframe
                </button>
            </div>

            <div style="display: flex; gap: 8px;">
                <button class="action-btn" style="flex: 1; padding: 9px; background: rgba(56, 189, 248, 0.2); border-color: #38bdf8;" onclick="takeScreenshot()">
                    📸 Tangkap Gambar HD
                </button>
            </div>

            <!-- 4. Legenda Interaktif -->
            <div class="section-label">📋 Legenda Lapisan Aktif</div>
            <div id="legend-box" class="legend-card">
                <!-- Dynamically updated -->
            </div>
        </div>
    </div>

    <!-- Inspector Badge (Bottom Right) -->
    <div id="inspector-badge" class="glass-panel">
        <div class="badge-title">
            <span>📍 Inspektor Medan 3D</span>
            <span style="font-size: 10px; color: #94a3b8; font-weight: normal; margin-left: auto;">(Klik di peta)</span>
        </div>
        <div id="badge-content">
            <div class="stat-grid">
                <div class="stat-row"><span class="stat-name">Elevasi:</span><span id="insp-elev" class="stat-val">1.629 m dpl</span></div>
                <div class="stat-row"><span class="stat-name">Kemiringan:</span><span id="insp-slope" class="stat-val">28.4% (Curam)</span></div>
                <div class="stat-row"><span class="stat-name">Kerawanan:</span><span id="insp-hazard" class="stat-val" style="color:#fdae61;">Tinggi (3.6)</span></div>
                <div class="stat-row"><span class="stat-name">Vegetasi (NDVI):</span><span id="insp-ndvi" class="stat-val">0.54</span></div>
                <div class="stat-row" style="grid-column: span 2;"><span class="stat-name">Koordinat:</span><span id="insp-coords" class="stat-val">439200 mE, 9179500 mN</span></div>
            </div>
        </div>
    </div>

    <!-- Modal Card for Detailed Inspection -->
    <div id="pin-modal" class="glass-panel">
        <div class="modal-header">
            <h2 id="modal-title" class="modal-title">Dusun Gedong</h2>
            <button class="modal-close" onclick="closeModal()">✕</button>
        </div>
        <div id="modal-body" class="modal-body">
            <!-- Modal details dynamically loaded -->
        </div>
    </div>

    <!-- Help Toast -->
    <div id="help-toast">
        🖱️ <b>Klik Kiri + Geser:</b> Putar 360° | <b>Scroll:</b> Zoom | <b>Klik Kanan:</b> Geser Peta | <b>Klik Objek:</b> Detail Informasi
    </div>

    <!-- SCRIPT APPLICATION LOGIC -->
    <script>
        // Data Payloads
        const rows = {rows};
        const cols = {cols};
        const minZ = {min_elev};
        const maxZ = {max_elev};
        const demData = {json.dumps(dem_arr)};
        const slopeData = {json.dumps(slope_arr)};
        const klData = {json.dumps(kl_arr)};
        const klScoreData = {json.dumps(kl_score_arr)};
        const maskData = {json.dumps(mask_arr)};
        const ndviData = {json.dumps(ndvi_arr)};
        const border3D = {json.dumps(pts_3d)};
        const debrisPath = {json.dumps(flow_pts_3d)};

        const textures = {{
            ahp: '{b64_ahp}',
            sat_rgb: '{b64_sat_rgb}',
            sat_cir: '{b64_sat_cir}',
            slope: '{b64_slope}',
            elev: '{b64_elev}'
        }};

        // Three.js Core
        let scene, camera, renderer, controls;
        let terrainMesh, terrainGeo, terrainMat;
        let skirtMesh;
        let borderLine, debrisLine;
        let dirLight, ambientLight, hemiLight;
        let verticalScale = 1.5;
        let isTourActive = false;
        let tourAngle = 0;
        let pins = [];
        let loadedTextures = {{}};
        let currentLayer = 'ahp';

        const terrainWidth = cols * 30.0;
        const terrainHeight = rows * 30.0;
        const xmin = 437850.0;
        const ymax = 9183390.0;

        init();
        animate();

        function init() {{
            const container = document.getElementById('canvas-container');

            // Scene & Fog
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x0a0f1d);
            scene.fog = new THREE.FogExp2(0x0a0f1d, 0.00008);

            // Camera
            camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 10, 80000);
            camera.position.set(-2800, 3600, 4800);

            // Renderer
            renderer = new THREE.WebGLRenderer({{ antialias: true, preserveDrawingBuffer: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.shadowMap.enabled = true;
            renderer.shadowMap.type = THREE.PCFSoftShadowMap;
            renderer.toneMapping = THREE.ACESFilmicToneMapping;
            renderer.toneMappingExposure = 1.1;
            container.appendChild(renderer.domElement);

            // Controls
            controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.maxPolarAngle = Math.PI / 2.05;
            controls.target.set(0, 700, 0);

            // Lighting Setup
            ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
            scene.add(ambientLight);

            hemiLight = new THREE.HemisphereLight(0xdbeafe, 0x1e293b, 0.45);
            hemiLight.position.set(0, 5000, 0);
            scene.add(hemiLight);

            dirLight = new THREE.DirectionalLight(0xfff7ed, 0.95);
            dirLight.castShadow = true;
            dirLight.shadow.mapSize.width = 2048;
            dirLight.shadow.mapSize.height = 2048;
            dirLight.shadow.camera.near = 500;
            dirLight.shadow.camera.far = 15000;
            const d = 4500;
            dirLight.shadow.camera.left = -d;
            dirLight.shadow.camera.right = d;
            dirLight.shadow.camera.top = d;
            dirLight.shadow.camera.bottom = -d;
            updateSunPosition(315);
            scene.add(dirLight);

            // Preload Textures (From Base64)
            const texLoader = new THREE.TextureLoader();
            for (let key in textures) {{
                const tex = texLoader.load(textures[key]);
                tex.generateMipmaps = true;
                tex.minFilter = THREE.LinearMipmapLinearFilter;
                tex.magFilter = THREE.LinearFilter;
                loadedTextures[key] = tex;
            }}

            // Build Topographic Terrain Mesh
            buildTerrainGeometry();

            // Build Solid Diorama Pedestal (Skirt)
            buildSkirtGeometry();

            // Build 3D Administrative Boundary Line
            buildBoundaryLine();

            // Build Debris Flow 3D Trajectory
            buildDebrisFlowLine();

            // Build 3D Markers & Beacons
            buildPOIMarkers();

            // Raycaster Picker
            setupRaycaster();

            // Resize listener
            window.addEventListener('resize', onWindowResize, false);

            // Initial Legend
            updateLegend('ahp');
        }}

        function buildTerrainGeometry() {{
            terrainGeo = new THREE.PlaneGeometry(terrainWidth, terrainHeight, cols - 1, rows - 1);
            // Rotate so X is horizontal, Z is depth (North-South), Y is UP elevation
            terrainGeo.rotateX(-Math.PI / 2);

            updateTerrainHeights();

            terrainMat = new THREE.MeshStandardMaterial({{
                map: loadedTextures['ahp'],
                roughness: 0.7,
                metalness: 0.05,
                flatShading: false,
                side: THREE.FrontSide
            }});

            terrainMesh = new THREE.Mesh(terrainGeo, terrainMat);
            terrainMesh.receiveShadow = true;
            terrainMesh.castShadow = true;
            scene.add(terrainMesh);
        }}

        function updateTerrainHeights() {{
            const pos = terrainGeo.attributes.position;
            let idx = 0;
            // PlaneGeometry vertices row by row
            for (let r = 0; r < rows; r++) {{
                for (let c = 0; c < cols; c++) {{
                    const zElev = demData[r][c];
                    const y = (zElev - minZ) * verticalScale;
                    pos.setY(idx, y);
                    idx++;
                }}
            }}
            pos.needsUpdate = true;
            terrainGeo.computeVertexNormals();
        }}

        function buildSkirtGeometry() {{
            // Build the 4 side walls (pedestal) around the terrain
            const baseLevel = -200;
            const skirtPositions = [];

            // Helper to push a quad (2 triangles)
            function pushQuad(p1, p2, p3, p4) {{
                skirtPositions.push(...p1, ...p2, ...p4);
                skirtPositions.push(...p2, ...p3, ...p4);
            }}

            // 1. North Wall (r = 0, c = 0..cols-1)
            for (let c = 0; c < cols - 1; c++) {{
                const x1 = (c - cols / 2.0) * 30.0;
                const x2 = ((c + 1) - cols / 2.0) * 30.0;
                const z = (-rows / 2.0) * 30.0;
                const y1 = (demData[0][c] - minZ) * verticalScale;
                const y2 = (demData[0][c + 1] - minZ) * verticalScale;

                pushQuad([x1, y1, z], [x2, y2, z], [x2, baseLevel, z], [x1, baseLevel, z]);
            }}

            // 2. South Wall (r = rows-1, c = 0..cols-1)
            for (let c = 0; c < cols - 1; c++) {{
                const x1 = (c - cols / 2.0) * 30.0;
                const x2 = ((c + 1) - cols / 2.0) * 30.0;
                const z = (rows / 2.0) * 30.0;
                const y1 = (demData[rows - 1][c] - minZ) * verticalScale;
                const y2 = (demData[rows - 1][c + 1] - minZ) * verticalScale;

                pushQuad([x2, y2, z], [x1, y1, z], [x1, baseLevel, z], [x2, baseLevel, z]);
            }}

            // 3. West Wall (c = 0, r = 0..rows-1)
            for (let r = 0; r < rows - 1; r++) {{
                const x = (-cols / 2.0) * 30.0;
                const z1 = (r - rows / 2.0) * 30.0;
                const z2 = ((r + 1) - rows / 2.0) * 30.0;
                const y1 = (demData[r][0] - minZ) * verticalScale;
                const y2 = (demData[r + 1][0] - minZ) * verticalScale;

                pushQuad([x, y2, z2], [x, y1, z1], [x, baseLevel, z1], [x, baseLevel, z2]);
            }}

            // 4. East Wall (c = cols-1, r = 0..rows-1)
            for (let r = 0; r < rows - 1; r++) {{
                const x = (cols / 2.0) * 30.0;
                const z1 = (r - rows / 2.0) * 30.0;
                const z2 = ((r + 1) - rows / 2.0) * 30.0;
                const y1 = (demData[r][cols - 1] - minZ) * verticalScale;
                const y2 = (demData[r + 1][cols - 1] - minZ) * verticalScale;

                pushQuad([x, y1, z1], [x, y2, z2], [x, baseLevel, z2], [x, baseLevel, z1]);
            }}

            const skirtGeo = new THREE.BufferGeometry();
            skirtGeo.setAttribute('position', new THREE.Float32BufferAttribute(skirtPositions, 3));
            skirtGeo.computeVertexNormals();

            const skirtMat = new THREE.MeshStandardMaterial({{
                color: 0x111827,
                roughness: 0.85,
                metalness: 0.1,
                side: THREE.DoubleSide
            }});

            if (skirtMesh) scene.remove(skirtMesh);
            skirtMesh = new THREE.Mesh(skirtGeo, skirtMat);
            skirtMesh.receiveShadow = true;
            scene.add(skirtMesh);
        }}

        function buildBoundaryLine() {{
            const linePositions = [];
            for (let i = 0; i < border3D.length; i++) {{
                const p = border3D[i];
                const y = (p[2] - minZ) * verticalScale + 12.0; // slightly above terrain
                linePositions.push(p[0], y, p[1]);
            }}

            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
            const mat = new THREE.LineBasicMaterial({{ color: 0x00f5ff, linewidth: 3 }});
            borderLine = new THREE.Line(geo, mat);
            scene.add(borderLine);
        }}

        function buildDebrisFlowLine() {{
            const flowPositions = [];
            for (let i = 0; i < debrisPath.length; i++) {{
                const p = debrisPath[i];
                const y = (p[2] - minZ) * verticalScale + 18.0;
                flowPositions.push(p[0], y, p[1]);
            }}
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.Float32BufferAttribute(flowPositions, 3));
            const mat = new THREE.LineDashedMaterial({{
                color: 0xf59e0b,
                linewidth: 3,
                scale: 1,
                dashSize: 80,
                gapSize: 40
            }});
            debrisLine = new THREE.Line(geo, mat);
            debrisLine.computeLineDistances();
            scene.add(debrisLine);
        }}

        function buildPOIMarkers() {{
            const poiData = [
                {{
                    id: 'gedong',
                    name: 'Dusun Gedong',
                    sub: 'Lokasi Longsor 28 Feb 2024',
                    x: 438883.7, y: 9180016.3, elev: 1656.1,
                    color: 0xef4444,
                    desc: 'Kejadian tanah longsor menimpa 1 rumah warga dan menutup akses jalan dusun. Lereng terasering agak curam (20.3%) dengan ketidakstabilan lereng lokal akibat jenuh air hujan lebat.'
                }},
                {{
                    id: 'dukoh',
                    name: 'Dusun Dukoh',
                    sub: 'Jembatan Tertimbun Aliran Debris',
                    x: 440304.8, y: 9182337.9, elev: 1084.1,
                    color: 0x0284c7,
                    desc: 'Akses jembatan tertutup timbunan lumpur, batu, pasir, dan gelondongan kayu. Merupakan fenomena <b>aliran rombakan (debris flow)</b> yang terbawa arus sungai dari tebing curam hulu Gunung Merbabu, bukan kegagalan lereng di tapak jembatan.'
                }},
                {{
                    id: 'merbabu',
                    name: 'Puncak Gunung Merbabu',
                    sub: 'Elevasi 3.066 m dpl',
                    x: 439800.0, y: 9176350.0, elev: 3066.3,
                    color: 0xf59e0b,
                    desc: 'Puncak batas selatan wilayah administrasi Desa Tajuk. Bertopografi sangat curam (>45%) dengan batuan vulkanik andesitik dan semak sub-alpin.'
                }},
                {{
                    id: 'ngaduman',
                    name: 'Dusun Ngaduman',
                    sub: 'Dusun Tertinggi (1.737 m dpl)',
                    x: 439600.0, y: 9179500.0, elev: 1737.0,
                    color: 0x10b981,
                    desc: 'Salah satu perkampungan tertinggi di lereng Merbabu dalam wilayah Desa Tajuk dengan lahan pertanian terasering kentang dan sayuran dataran tinggi.'
                }}
            ];

            poiData.forEach(poi => {{
                const group = new THREE.Group();
                const c = (poi.x - xmin) / 30.0;
                const r = (ymax - poi.y) / 30.0;
                const posX = (c - cols / 2.0) * 30.0;
                const posZ = (r - rows / 2.0) * 30.0;
                const posY = (poi.elev - minZ) * verticalScale;

                // Glowing Beacon Sphere
                const sphereGeo = new THREE.SphereGeometry(45, 16, 16);
                const sphereMat = new THREE.MeshStandardMaterial({{
                    color: poi.color,
                    emissive: poi.color,
                    emissiveIntensity: 0.6,
                    roughness: 0.2
                }});
                const sphere = new THREE.Mesh(sphereGeo, sphereMat);
                sphere.position.y = 120;
                group.add(sphere);

                // Stem Rod
                const stemGeo = new THREE.CylinderGeometry(8, 8, 120, 8);
                const stemMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
                const stem = new THREE.Mesh(stemGeo, stemMat);
                stem.position.y = 60;
                group.add(stem);

                // Ground Ring
                const ringGeo = new THREE.RingGeometry(30, 65, 32);
                ringGeo.rotateX(-Math.PI / 2);
                const ringMat = new THREE.MeshBasicMaterial({{
                    color: poi.color,
                    side: THREE.DoubleSide,
                    transparent: true,
                    opacity: 0.7
                }});
                const ring = new THREE.Mesh(ringGeo, ringMat);
                ring.position.y = 5;
                group.add(ring);

                group.position.set(posX, posY, posZ);
                group.userData = poi;
                scene.add(group);
                pins.push({{ group, sphere, ring, data: poi }});
            }});
        }}

        function setupRaycaster() {{
            const raycaster = new THREE.Raycaster();
            const mouse = new THREE.Vector2();

            window.addEventListener('click', function(event) {{
                // Ignore if clicking on UI
                if (event.target.closest('#main-dashboard') || event.target.closest('#pin-modal') || event.target.closest('#compass-widget')) return;

                mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
                mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

                raycaster.setFromCamera(mouse, camera);

                // Check POI pins first
                const pinObjects = pins.map(p => p.sphere);
                const pinIntersects = raycaster.intersectObjects(pinObjects);
                if (pinIntersects.length > 0) {{
                    const clickedPin = pins.find(p => p.sphere === pinIntersects[0].object);
                    if (clickedPin) {{
                        openModal(clickedPin.data);
                        return;
                    }}
                }}

                // Check Terrain
                const terrainIntersects = raycaster.intersectObject(terrainMesh);
                if (terrainIntersects.length > 0) {{
                    const hit = terrainIntersects[0].point;
                    const c = (hit.x / 30.0) + (cols / 2.0);
                    const r = (hit.z / 30.0) + (rows / 2.0);

                    const cr = Math.min(Math.max(Math.round(r), 0), rows - 1);
                    const cc = Math.min(Math.max(Math.round(c), 0), cols - 1);

                    const utmX = Math.round(xmin + cc * 30.0);
                    const utmY = Math.round(ymax - cr * 30.0);
                    const elev = demData[cr][cc];
                    const slp = slopeData[cr][cc];
                    const klK = klData[cr][cc];
                    const klS = klScoreData[cr][cc];
                    const ndviVal = ndviData[cr][cc];
                    const isInside = maskData[cr][cc] === 1;

                    const hazardNames = ['-', 'Sangat Rendah', 'Rendah', 'Sedang', 'Tinggi', 'Sangat Tinggi'];
                    const hazardColors = ['#94a3b8', '#1a9641', '#a6d96a', '#eab308', '#fdae61', '#ef4444'];

                    document.getElementById('insp-elev').innerText = elev.toFixed(1) + ' m dpl';
                    document.getElementById('insp-slope').innerText = slp.toFixed(1) + '%';
                    const hSpan = document.getElementById('insp-hazard');
                    hSpan.innerText = isInside ? `${{hazardNames[klK]}} (${{klS.toFixed(2)}})` : 'Luar Batas Tajuk';
                    hSpan.style.color = isInside ? hazardColors[klK] : '#94a3b8';
                    document.getElementById('insp-ndvi').innerText = ndviVal.toFixed(2);
                    document.getElementById('insp-coords').innerText = `${{utmX}} mE, ${{utmY}} mN`;
                }}
            }});
        }}

        // Layer Switching
        function switchLayer(layerKey) {{
            if (!loadedTextures[layerKey]) return;
            currentLayer = layerKey;
            terrainMat.map = loadedTextures[layerKey];
            terrainMat.needsUpdate = true;

            document.querySelectorAll('.layer-grid .layer-btn').forEach(btn => btn.classList.remove('active'));
            const activeBtn = document.getElementById('btn-layer-' + (layerKey === 'sat_rgb' ? 'sat' : (layerKey === 'sat_cir' ? 'cir' : layerKey)));
            if (activeBtn) activeBtn.classList.add('active');

            updateLegend(layerKey);
        }}

        function updateLegend(layerKey) {{
            const box = document.getElementById('legend-box');
            if (layerKey === 'ahp') {{
                box.innerHTML = `
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#1a9641;"></div>Sangat Rendah</div><b>4,57%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#a6d96a;"></div>Rendah</div><b>18,78%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#ffff73;"></div>Sedang (Dominan)</div><b>41,27%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#fdae61;"></div>Tinggi</div><b>33,93%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#d7191c;"></div>Sangat Tinggi</div><b>1,44%</b></div>
                `;
            }} else if (layerKey === 'slope') {{
                box.innerHTML = `
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#2b83ba;"></div>0–8% (Datar)</div><b>4,60%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#abdda4;"></div>8–15% (Landai)</div><b>15,04%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#ffffbf;"></div>15–25% (Agak Curam)</div><b>23,33%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#fdae61;"></div>25–45% (Curam)</div><b>30,62%</b></div>
                    <div class="legend-item"><div class="legend-left"><div class="color-dot" style="background:#d7191c;"></div>>45% (Sangat Curam)</div><b>26,35%</b></div>
                `;
            }} else if (layerKey === 'sat_rgb') {{
                box.innerHTML = `
                    <div style="font-size:11px; line-height:1.5;">
                        <b>Landsat 9 OLI-2:</b> Komposit Natural True Color (Band 4-3-2). Menampilkan kondisi tutupan lahan nyata, sawah terasering, serta pemukiman warga lereng Merbabu.
                    </div>
                `;
            }} else if (layerKey === 'sat_cir') {{
                box.innerHTML = `
                    <div style="font-size:11px; line-height:1.5;">
                        <b>False Color Inframerah (5-4-3):</b> Vegetasi sehat memantulkan NIR tinggi (merah tua/krimson), lahan terbuka/bangunan tampak abu-abu kebiruan.
                    </div>
                `;
            }} else if (layerKey === 'elev') {{
                box.innerHTML = `
                    <div style="font-size:11px; line-height:1.5;">
                        <b>Hipsometrik DEM:</b> Rentang elevasi 938 m dpl (lembah utara, hijau) hingga 3.066 m dpl (puncak Merbabu, abu-abu cadas).
                    </div>
                `;
            }}
        }}

        // Exaggeration Slider
        function setExaggeration(val) {{
            verticalScale = parseFloat(val);
            document.getElementById('lbl-exag').innerText = verticalScale.toFixed(1) + 'x';
            updateTerrainHeights();
            buildSkirtGeometry();

            // Update boundary line
            const linePositions = [];
            for (let i = 0; i < border3D.length; i++) {{
                const p = border3D[i];
                const y = (p[2] - minZ) * verticalScale + 12.0;
                linePositions.push(p[0], y, p[1]);
            }}
            borderLine.geometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
            borderLine.geometry.attributes.position.needsUpdate = true;

            // Update pins
            pins.forEach(pin => {{
                pin.group.position.y = (pin.data.elev - minZ) * verticalScale;
            }});
        }}

        // Lighting Controls
        function setSunAngle(deg) {{
            document.getElementById('lbl-sun').innerText = deg + '°';
            updateSunPosition(parseFloat(deg));
        }}
        function updateSunPosition(deg) {{
            const rad = THREE.MathUtils.degToRad(deg);
            const dist = 6000;
            dirLight.position.set(Math.sin(rad) * dist, 4800, Math.cos(rad) * dist);
        }}
        function setLightIntensity(val) {{
            document.getElementById('lbl-light').innerText = Math.round(val * 100) + '%';
            ambientLight.intensity = 0.75 * val;
            dirLight.intensity = 0.95 * val;
        }}

        // Camera Presets
        function setPresetView(type) {{
            isTourActive = false;
            document.getElementById('btn-tour').innerText = '▶️ Tur Sinematik 3D';
            document.getElementById('btn-tour').classList.remove('active');

            if (type === 'iso') {{
                camera.position.set(-2800, 3600, 4800);
                controls.target.set(0, 700, 0);
            }} else if (type === 'top') {{
                camera.position.set(0, 8500, 50);
                controls.target.set(0, 600, 0);
            }} else if (type === 'valley') {{
                camera.position.set(0, 1800, -5400);
                controls.target.set(0, 1400, 1000);
            }} else if (type === 'summit') {{
                camera.position.set(0, 4600, 4800);
                controls.target.set(0, 1100, -2000);
            }}
            controls.update();
        }}

        function flyToPoint(id) {{
            const pin = pins.find(p => p.data.id === id);
            if (!pin) return;
            const p = pin.group.position;
            camera.position.set(p.x + 800, p.y + 700, p.z + 1200);
            controls.target.set(p.x, p.y + 60, p.z);
            controls.update();
            openModal(pin.data);
        }}

        function resetNorth() {{
            const r = Math.sqrt(camera.position.x * camera.position.x + camera.position.z * camera.position.z);
            camera.position.x = 0;
            camera.position.z = r;
            controls.target.set(0, 700, 0);
            controls.update();
        }}

        // Tur Sinematik
        function toggleCinematicTour() {{
            isTourActive = !isTourActive;
            const btn = document.getElementById('btn-tour');
            if (isTourActive) {{
                btn.innerText = '⏸️ Hentikan Tur';
                btn.classList.add('active');
            }} else {{
                btn.innerText = '▶️ Tur Sinematik 3D';
                btn.classList.remove('active');
            }}
        }}

        function toggleWireframe() {{
            terrainMat.wireframe = !terrainMat.wireframe;
        }}

        function toggleDashboard() {{
            const dash = document.getElementById('main-dashboard');
            const reopen = document.getElementById('btn-reopen');
            dash.classList.toggle('minimized');
            reopen.style.display = dash.classList.contains('minimized') ? 'flex' : 'none';
        }}

        // Modal Card
        function openModal(data) {{
            document.getElementById('modal-title').innerText = data.name;
            document.getElementById('modal-body').innerHTML = `
                <div style="font-weight:600; color:#38bdf8; margin-bottom:8px;">${{data.sub}}</div>
                <div style="background:rgba(255,255,255,0.06); padding:10px 12px; border-radius:8px; margin-bottom:10px;">
                    <b>Elevasi:</b> ${{data.elev.toFixed(1)}} m dpl<br>
                    <b>Koordinat UTM:</b> ${{data.x.toFixed(1)}} mE, ${{data.y.toFixed(1)}} mN
                </div>
                <p style="margin:0;">${{data.desc}}</p>
            `;
            document.getElementById('pin-modal').classList.add('visible');
        }}
        function closeModal() {{
            document.getElementById('pin-modal').classList.remove('visible');
        }}

        // Screenshot Export
        function takeScreenshot() {{
            renderer.render(scene, camera);
            const dataURL = renderer.domElement.toDataURL('image/png');
            const link = document.createElement('a');
            link.download = 'Model_3D_Desa_Tajuk_Merbabu.png';
            link.href = dataURL;
            link.click();
        }}

        function onWindowResize() {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }}

        // Animation Loop
        function animate(timestamp) {{
            requestAnimationFrame(animate);

            // Compass rotation
            const dir = new THREE.Vector3();
            camera.getWorldDirection(dir);
            const heading = Math.atan2(dir.x, dir.z);
            document.getElementById('compass-arrow').style.transform = `rotate(${{-heading * (180 / Math.PI)}}deg)`;

            // Beacon pulsing
            const t = timestamp ? timestamp * 0.003 : 0;
            pins.forEach(pin => {{
                const s = 1.0 + 0.15 * Math.sin(t * 2);
                pin.sphere.scale.set(s, s, s);
                const rs = 1.0 + 0.25 * Math.sin(t * 2.5);
                pin.ring.scale.set(rs, rs, rs);
            }});

            // Debris flow animation
            if (debrisLine) {{
                debrisLine.material.dashSize = 80;
                debrisLine.material.gapSize = 40;
            }}

            // Cinematic tour rotation
            if (isTourActive) {{
                tourAngle += 0.0035;
                const radius = 5400;
                camera.position.x = Math.sin(tourAngle) * radius;
                camera.position.z = Math.cos(tourAngle) * radius;
                camera.position.y = 2800 + Math.sin(tourAngle * 2) * 600;
                controls.target.set(0, 900, 0);
            }}

            controls.update();
            renderer.render(scene, camera);
        }}
    </script>
</body>
</html>
"""

html_dest = os.path.join(output_dir, "peta_3d_tajuk.html")
with open(html_dest, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"Generated standalone 3D Viewer: {html_dest} ({os.path.getsize(html_dest)} bytes)")

# Sync to Desktop study folder
desktop_html = os.path.join(desktop_dir, "peta_3d_tajuk.html")
with open(desktop_html, "w", encoding="utf-8") as f:
    f.write(html_code)
print(f"Synced to Desktop: {desktop_html}")

# Copy three.min.js and OrbitControls.js to desktop folder
import shutil
shutil.copy2(os.path.join(output_dir, "three.min.js"), os.path.join(desktop_dir, "three.min.js"))
shutil.copy2(os.path.join(output_dir, "OrbitControls.js"), os.path.join(desktop_dir, "OrbitControls.js"))
print("Synced Three.js dependencies to Desktop folder.")
