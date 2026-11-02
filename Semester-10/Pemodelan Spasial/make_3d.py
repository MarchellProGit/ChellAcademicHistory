import os
import json
import math
import numpy as np
from PIL import Image, ImageDraw

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"

dem = np.array(Image.open(os.path.join(output_dir, "dem_tajuk_30m.tif")))
slope = np.array(Image.open(os.path.join(output_dir, "slope_percent_tajuk.tif")))
b4 = np.array(Image.open(os.path.join(output_dir, "b4_tajuk_30m.tif"))).astype(np.float32)
b5 = np.array(Image.open(os.path.join(output_dir, "b5_tajuk_30m.tif"))).astype(np.float32)
b6 = np.array(Image.open(os.path.join(output_dir, "b6_tajuk_30m.tif"))).astype(np.float32)
mask = np.array(Image.open(os.path.join(output_dir, "mask_tajuk.tif"))) == 1

rows, cols = dem.shape # 244, 134

# TOA
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

elev_breaks = [1299.8, 1684.8, 2097.6, 2530.6, 3066.3]
ndmi_breaks = [0.0294, 0.1149, 0.1954, 0.2840, 0.4897]

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

kl_continuous = 0.517 * score_slope + 0.226 * score_ndvi + 0.134 * score_elev + 0.123 * score_ndmi

kl_classified = np.zeros_like(kl_continuous, dtype=np.uint8)
kl_classified[(kl_continuous >= 1.0) & (kl_continuous < 1.8)] = 1
kl_classified[(kl_continuous >= 1.8) & (kl_continuous < 2.6)] = 2
kl_classified[(kl_continuous >= 2.6) & (kl_continuous < 3.4)] = 3
kl_classified[(kl_continuous >= 3.4) & (kl_continuous < 4.2)] = 4
kl_classified[kl_continuous >= 4.2] = 5

# 1. Bake Texture (PNG)
kl_colors = {
    0: (230, 230, 230, 80),
    1: (26, 150, 65, 255),      # Green
    2: (166, 217, 106, 255),    # Light Green
    3: (255, 255, 191, 255),    # Yellow
    4: (253, 174, 97, 255),     # Orange
    5: (215, 25, 28, 255)       # Red
}
tex_kl = np.zeros((rows, cols, 4), dtype=np.uint8)
for val, col in kl_colors.items():
    tex_kl[kl_classified == val] = col
tex_kl[~valid] = (220, 220, 220, 180)

im_kl = Image.fromarray(tex_kl, mode="RGBA").resize((cols * 4, rows * 4), Image.NEAREST)
draw = ImageDraw.Draw(im_kl)

xmin, ymax = 437850.0, 9183390.0
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
print("Saved tex_kerawanan.png")

# 2. Elevation array for 3D
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
            <b>Luas Wilayah:</b> 1.021,14 ha<br>
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
            Klik Kiri + Geser: Putar Rotasi 3D<br>
            Scroll: Zoom In / Out<br>
            Klik Kanan + Geser: Pan (Geser Kamera)
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
