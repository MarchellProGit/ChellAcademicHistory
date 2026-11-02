import os
import math
import json
import numpy as np
from osgeo import gdal
from PIL import Image, ImageDraw

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"
desktop_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"
code_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10"

# Open reference DEM
dem_path = os.path.join(output_dir, "dem_tajuk_30m.tif")
ds_ref = gdal.Open(dem_path)
cols = ds_ref.RasterXSize
rows = ds_ref.RasterYSize
gt = ds_ref.GetGeoTransform()
proj = ds_ref.GetProjection()

dem = ds_ref.GetRasterBand(1).ReadAsArray().astype(np.float32)
slope = gdal.Open(os.path.join(output_dir, "slope_percent_tajuk.tif")).GetRasterBand(1).ReadAsArray().astype(np.float32)
b4 = gdal.Open(os.path.join(output_dir, "b4_tajuk_30m.tif")).GetRasterBand(1).ReadAsArray().astype(np.float32)
b5 = gdal.Open(os.path.join(output_dir, "b5_tajuk_30m.tif")).GetRasterBand(1).ReadAsArray().astype(np.float32)
b6 = gdal.Open(os.path.join(output_dir, "b6_tajuk_30m.tif")).GetRasterBand(1).ReadAsArray().astype(np.float32)
mask = gdal.Open(os.path.join(output_dir, "mask_tajuk.tif")).GetRasterBand(1).ReadAsArray() == 1

# TOA Reflectance
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

# Natural breaks function
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

# Scores (1 to 5)
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

score_elev = np.zeros_like(dem, dtype=np.float32)
score_elev[dem <= elev_breaks[0]] = 1
score_elev[(dem > elev_breaks[0]) & (dem <= elev_breaks[1])] = 2
score_elev[(dem > elev_breaks[1]) & (dem <= elev_breaks[2])] = 3
score_elev[(dem > elev_breaks[2]) & (dem <= elev_breaks[3])] = 4
score_elev[dem > elev_breaks[3]] = 5

score_ndmi = np.zeros_like(ndmi, dtype=np.float32)
score_ndmi[ndmi <= ndmi_breaks[0]] = 1
score_ndmi[(ndmi > ndmi_breaks[0]) & (ndmi <= ndmi_breaks[1])] = 2
score_ndmi[(ndmi > ndmi_breaks[1]) & (ndmi <= ndmi_breaks[2])] = 3
score_ndmi[(ndmi > ndmi_breaks[2]) & (ndmi <= ndmi_breaks[3])] = 4
score_ndmi[ndmi > ndmi_breaks[3]] = 5

kl_continuous = (
    0.517 * score_slope +
    0.226 * score_ndvi +
    0.134 * score_elev +
    0.123 * score_ndmi
)

kl_classified = np.zeros_like(kl_continuous, dtype=np.uint8)
kl_classified[(kl_continuous >= 1.0) & (kl_continuous < 1.8)] = 1
kl_classified[(kl_continuous >= 1.8) & (kl_continuous < 2.6)] = 2
kl_classified[(kl_continuous >= 2.6) & (kl_continuous < 3.4)] = 3
kl_classified[(kl_continuous >= 3.4) & (kl_continuous < 4.2)] = 4
kl_classified[kl_continuous >= 4.2] = 5

# Function to save GeoTIFF via GDAL
drv = gdal.GetDriverByName("GTiff")
def save_gdal(filename, arr, dtype, nodata_val):
    ds = drv.Create(os.path.join(output_dir, filename), cols, rows, 1, dtype)
    ds.SetGeoTransform(gt)
    ds.SetProjection(proj)
    band = ds.GetRasterBand(1)
    out_arr = arr.copy()
    if dtype == gdal.GDT_Byte:
        out_arr[~valid] = 0
        band.WriteArray(out_arr.astype(np.uint8))
        band.SetNoDataValue(0)
    else:
        out_arr[~valid] = nodata_val
        band.WriteArray(out_arr.astype(np.float32))
        band.SetNoDataValue(nodata_val)
    ds.FlushCache()
    ds = None
    print(f"Saved GeoTIFF: {filename}")

save_gdal("ndvi_tajuk.tif", ndvi, gdal.GDT_Float32, -9999.0)
save_gdal("ndmi_tajuk.tif", ndmi, gdal.GDT_Float32, -9999.0)
save_gdal("score_slope.tif", score_slope, gdal.GDT_Byte, 0)
save_gdal("score_ndvi.tif", score_ndvi, gdal.GDT_Byte, 0)
save_gdal("score_elev.tif", score_elev, gdal.GDT_Byte, 0)
save_gdal("score_ndmi.tif", score_ndmi, gdal.GDT_Byte, 0)
save_gdal("kerawanan_longsor_continuous.tif", kl_continuous, gdal.GDT_Float32, -9999.0)
save_gdal("kerawanan_longsor_kelas.tif", kl_classified, gdal.GDT_Byte, 0)

# 2. Bake 3D Texture (PNG)
kl_colors = {
    0: (230, 230, 230, 80),
    1: (26, 150, 65, 255),
    2: (166, 217, 106, 255),
    3: (255, 255, 191, 255),
    4: (253, 174, 97, 255),
    5: (215, 25, 28, 255)
}
tex_kl = np.zeros((rows, cols, 4), dtype=np.uint8)
for val, col in kl_colors.items():
    tex_kl[kl_classified == val] = col
tex_kl[~valid] = (220, 220, 220, 180)

im_kl = Image.fromarray(tex_kl, mode="RGBA").resize((cols * 4, rows * 4), Image.NEAREST)
draw = ImageDraw.Draw(im_kl)

xmin, ymax = gt[0], gt[3]
pts = [
    ("DUSUN GEDONG", 438883.7, 9180016.3),
    ("DUSUN DUKOH", 440304.8, 9182337.9)
]

for name, x, y in pts:
    px = int(round((x - xmin) / 30.0 * 4))
    py = int(round((ymax - y) / 30.0 * 4))
    r = 7
    draw.ellipse([px-r, py-r, px+r, py+r], fill=(227, 26, 28, 255), outline=(255, 255, 255, 255), width=2)
    draw.text((px + 10, py - 6), name, fill=(0, 0, 0, 255))

tex_path = os.path.join(output_dir, "tex_kerawanan.png")
im_kl.save(tex_path)
print("Saved 3D texture: tex_kerawanan.png")

# 3. Generate HTML 3D Viewer
min_e = float(dem[valid].min())
max_e = float(dem[valid].max())
dem_clean = dem.copy()
dem_clean[~valid] = min_e
z_data = [[round(float(dem_clean[r, c]), 1) for c in range(cols)] for r in range(rows)]

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Model 3D Kerawanan Longsor Desa Tajuk - Gunung Merbabu</title>
    <style>
        body {{ margin: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #fff; }}
        #canvas-container {{ width: 100vw; height: 100vh; display: block; }}
        #ui-panel {{
            position: absolute; top: 16px; left: 16px; z-index: 100;
            background: rgba(15, 23, 42, 0.90); backdrop-filter: blur(10px);
            padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.12);
            max-width: 330px; box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }}
        h2 {{ margin: 0 0 4px 0; font-size: 16px; font-weight: 700; color: #38bdf8; }}
        p.subtitle {{ margin: 0 0 12px 0; font-size: 12px; color: #94a3b8; line-height: 1.4; }}
        .control-group {{ margin-bottom: 12px; }}
        label {{ font-size: 12px; font-weight: 600; display: block; margin-bottom: 5px; color: #e2e8f0; }}
        input[type=range] {{ width: 100%; cursor: pointer; accent-color: #38bdf8; }}
        .stats-badge {{ background: rgba(255,255,255,0.06); padding: 8px 10px; border-radius: 6px; font-size: 11px; margin-bottom: 12px; line-height: 1.6; border-left: 3px solid #38bdf8; }}
        .legend {{ margin-top: 10px; font-size: 11px; }}
        .legend-item {{ display: flex; align-items: center; margin-bottom: 4px; }}
        .legend-color {{ width: 14px; height: 14px; border-radius: 3px; margin-right: 8px; flex-shrink: 0; border: 1px solid rgba(0,0,0,0.2); }}
        .help-text {{ font-size: 11px; color: #64748b; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px; margin-top: 12px; line-height: 1.5; }}
        .btn {{
            background: #0284c7; color: white; border: none; padding: 6px 12px; border-radius: 6px;
            font-size: 11px; cursor: pointer; font-weight: 600; margin-right: 6px; margin-top: 4px;
        }}
        .btn:hover {{ background: #0369a1; }}
    </style>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="ui-panel">
        <h2>Model Topografi 3D Desa Tajuk</h2>
        <p class="subtitle">Kecamatan Getasan, Kabupaten Semarang<br>Lereng Gunung Merbabu</p>
        
        <div class="stats-badge">
            <b>Elevasi:</b> {min_e:.0f} m – {max_e:.0f} m dpl<br>
            <b>Luas Wilayah:</b> {total_ha:.2f} ha (1.021 ha)<br>
            <b>Area Rawan (Tinggi+Sangat Tinggi):</b> 361,17 ha (35,37%)
        </div>

        <div class="control-group">
            <label for="exaggeration">Vertikal Exaggeration: <span id="exag-val">1.5x</span></label>
            <input type="range" id="exaggeration" min="0.5" max="3.0" step="0.1" value="1.5">
        </div>

        <div class="control-group">
            <button class="btn" onclick="resetView()">Reset Kamera</button>
            <button class="btn" onclick="toggleWireframe()">Wireframe</button>
        </div>

        <div class="legend">
            <label>Tingkat Kerawanan Longsor (AHP):</label>
            <div class="legend-item"><div class="legend-color" style="background:#1a9641;"></div>Sangat Rendah (4,57%)</div>
            <div class="legend-item"><div class="legend-color" style="background:#a6d96a;"></div>Rendah (18,78%)</div>
            <div class="legend-item"><div class="legend-color" style="background:#ffffbf;"></div>Sedang (41,27%)</div>
            <div class="legend-item"><div class="legend-color" style="background:#fdae61;"></div>Tinggi (33,93%)</div>
            <div class="legend-item"><div class="legend-color" style="background:#d7191c;"></div>Sangat Tinggi (1,44%)</div>
        </div>

        <div class="help-text">
            🖱️ <b>Klik Kiri + Drag:</b> Putar Rotasi 3D<br>
            🖱️ <b>Scroll:</b> Zoom In / Out<br>
            🖱️ <b>Klik Kanan + Drag:</b> Geser (Pan)
        </div>
    </div>

    <div id="canvas-container"></div>

    <script>
        const rows = {rows};
        const cols = {cols};
        const zData = {json.dumps(z_data)};
        const minZ = {min_e};
        const maxZ = {max_e};

        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 50000);
        camera.position.set(0, -3600, 3200);

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxPolarAngle = Math.PI / 2.05;

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xfff5e6, 0.9);
        dirLight.position.set(2000, 3000, 4500);
        dirLight.castShadow = true;
        scene.add(dirLight);

        // Terrain Geometry
        const terrainWidth = cols * 30;
        const terrainHeight = rows * 30;
        const geometry = new THREE.PlaneGeometry(terrainWidth, terrainHeight, cols - 1, rows - 1);

        let verticalScale = 1.5;
        const pos = geometry.attributes.position;

        function updateTerrainZ() {{
            let idx = 0;
            for (let r = 0; r < rows; r++) {{
                for (let c = 0; c < cols; c++) {{
                    const z = (zData[r][c] - minZ) * verticalScale;
                    pos.setZ(idx, z);
                    idx++;
                }}
            }}
            pos.needsUpdate = true;
            geometry.computeVertexNormals();
        }}
        updateTerrainZ();

        const textureLoader = new THREE.TextureLoader();
        const texture = textureLoader.load('tex_kerawanan.png');
        texture.magFilter = THREE.LinearFilter;
        texture.minFilter = THREE.LinearFilter;

        const material = new THREE.MeshStandardMaterial({{
            map: texture,
            roughness: 0.65,
            metalness: 0.05,
            side: THREE.DoubleSide
        }});

        const terrainMesh = new THREE.Mesh(geometry, material);
        scene.add(terrainMesh);

        function createPin(name, xMeter, yMeter, zElev, colorHex) {{
            const group = new THREE.Group();
            const z = (zElev - minZ) * verticalScale;

            const rodGeo = new THREE.CylinderGeometry(12, 12, 180, 16);
            const rodMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
            const rod = new THREE.Mesh(rodGeo, rodMat);
            rod.rotation.x = Math.PI / 2;
            rod.position.set(0, 0, 90);
            group.add(rod);

            const headGeo = new THREE.SphereGeometry(50, 24, 24);
            const headMat = new THREE.MeshStandardMaterial({{ color: colorHex, roughness: 0.2 }});
            const head = new THREE.Mesh(headGeo, headMat);
            head.position.set(0, 0, 200);
            group.add(head);

            group.position.set(xMeter, yMeter, z);
            scene.add(group);
            return group;
        }}

        const midX = 439860.0;
        const midY = 9179730.0;
        const pinGedong = createPin("Dusun Gedong", 438883.7 - midX, 9180016.3 - midY, 1656.1, 0xe11d48);
        const pinDukoh = createPin("Dusun Dukoh", 440304.8 - midX, 9182337.9 - midY, 1084.1, 0x0284c7);

        document.getElementById('exaggeration').addEventListener('input', function(e) {{
            verticalScale = parseFloat(e.target.value);
            document.getElementById('exag-val').innerText = verticalScale.toFixed(1) + 'x';
            updateTerrainZ();
            pinGedong.position.z = (1656.1 - minZ) * verticalScale;
            pinDukoh.position.z = (1084.1 - minZ) * verticalScale;
        }});

        function resetView() {{
            camera.position.set(0, -3600, 3200);
            controls.target.set(0, 0, 400);
            controls.update();
        }}

        function toggleWireframe() {{
            material.wireframe = !material.wireframe;
        }}

        window.addEventListener('resize', onWindowResize, false);
        function onWindowResize() {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }}

        function animate() {{
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }}
        resetView();
        animate();
    </script>
</body>
</html>
"""

html_path = os.path.join(output_dir, "peta_3d_tajuk.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated 3D HTML Viewer: {html_path}")
