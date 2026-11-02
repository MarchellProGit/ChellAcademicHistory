import os
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

output_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10/output"

# Load arrays
dem = np.array(Image.open(os.path.join(output_dir, "dem_tajuk_30m.tif")))
slope = np.array(Image.open(os.path.join(output_dir, "slope_percent_tajuk.tif")))
ndvi = np.array(Image.open(os.path.join(output_dir, "ndvi_tajuk.tif")))
kl = np.array(Image.open(os.path.join(output_dir, "kerawanan_longsor_kelas.tif")))
mask = np.array(Image.open(os.path.join(output_dir, "mask_tajuk.tif"))) == 1

rows, cols = dem.shape # 244, 134

# 1. Bake Texture: Kerawanan Longsor
# Classes: 1: #1a9641, 2: #a6d96a, 3: #ffffbf, 4: #fdae61, 5: #d7191c
kl_colors = {
    0: (230, 230, 230, 100),    # Outside mask (subtle gray)
    1: (26, 150, 65, 255),      # Sangat Rendah (Green)
    2: (166, 217, 106, 255),    # Rendah (Light green)
    3: (255, 255, 191, 255),    # Sedang (Yellow)
    4: (253, 174, 97, 255),     # Tinggi (Orange)
    5: (215, 25, 28, 255)       # Sangat Tinggi (Red)
}

tex_kl = np.zeros((rows, cols, 4), dtype=np.uint8)
for val, col in kl_colors.items():
    tex_kl[kl == val] = col
tex_kl[~mask] = (220, 220, 220, 180)

im_kl = Image.fromarray(tex_kl, mode="RGBA").resize((cols * 4, rows * 4), Image.NEAREST)
draw = ImageDraw.Draw(im_kl)

# Draw pins on texture
# Points: Gedong (x=438883.7, y=9180016.3), Dukoh (x=440304.8, y=9182337.9)
xmin, ymax = 437850.0, 9183390.0
pts = [
    ("DUSUN GEDONG (Kejadian 28 Feb 2024)", 438883.7, 9180016.3),
    ("DUSUN DUKOH (Kejadian 28 Feb 2024)", 440304.8, 9182337.9)
]

for name, x, y in pts:
    px = int(round((x - xmin) / 30.0 * 4))
    py = int(round((ymax - y) / 30.0 * 4))
    # Pin marker
    r = 6
    draw.ellipse([px-r, py-r, px+r, py+r], fill=(227, 26, 28, 255), outline=(255, 255, 255, 255), width=2)
    draw.text((px + 8, py - 6), name, fill=(0, 0, 0, 255))

tex_kl_path = os.path.join(output_dir, "tex_kerawanan.png")
im_kl.save(tex_kl_path)
print("Saved tex_kerawanan.png")

# 2. Elevation array for 3D mesh
# Normalize elevation relative to base (938m)
min_e = float(dem[mask].min())
max_e = float(dem[mask].max())
dem_clean = dem.copy()
dem_clean[~mask] = min_e # Flatten outside

# Normalize z values in grid coordinate space
# Terrain physical dimensions: cols * 30m = 4020m, rows * 30m = 7320m
z_data = [[round(float(dem_clean[r, c]), 1) for c in range(cols)] for r in range(rows)]

# 3. HTML 3D Viewer template with Three.js (CDN)
html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Model 3D Kerawanan Longsor Desa Tajuk - Gunung Merbabu</title>
    <style>
        body {{ margin: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1a1a1a; color: #fff; }}
        #canvas-container {{ width: 100vw; height: 100vh; display: block; }}
        #ui-panel {{
            position: absolute; top: 16px; left: 16px; z-index: 100;
            background: rgba(20, 25, 35, 0.88); backdrop-filter: blur(8px);
            padding: 18px 22px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.15);
            max-width: 320px; box-shadow: 0 8px 32px rgba(0,0,0,0.5);
        }}
        h2 {{ margin: 0 0 6px 0; font-size: 17px; font-weight: 700; color: #4ade80; }}
        p.subtitle {{ margin: 0 0 14px 0; font-size: 12px; color: #cbd5e1; }}
        .control-group {{ margin-bottom: 12px; }}
        label {{ font-size: 12px; font-weight: 600; display: block; margin-bottom: 4px; color: #e2e8f0; }}
        input[type=range] {{ width: 100%; cursor: pointer; accent-color: #4ade80; }}
        .stats-badge {{ background: rgba(255,255,255,0.08); padding: 8px 10px; border-radius: 6px; font-size: 11px; margin-bottom: 12px; line-height: 1.5; }}
        .legend {{ margin-top: 10px; font-size: 11px; }}
        .legend-item {{ display: flex; align-items: center; margin-bottom: 4px; }}
        .legend-color {{ width: 14px; height: 14px; border-radius: 3px; margin-right: 8px; flex-shrink: 0; }}
        .help-text {{ font-size: 11px; color: #94a3b8; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px; margin-top: 12px; }}
        .btn {{
            background: #2563eb; color: white; border: none; padding: 6px 12px; border-radius: 6px;
            font-size: 11px; cursor: pointer; font-weight: 600; margin-right: 6px; margin-top: 4px;
        }}
        .btn:hover {{ background: #1d4ed8; }}
    </style>
    <!-- Three.js and OrbitControls from CDN -->
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="ui-panel">
        <h2>Visualisasi 3D Kerawanan Longsor</h2>
        <p class="subtitle">Desa Tajuk, Kec. Getasan, Kab. Semarang<br>(Lereng Gunung Merbabu)</p>
        
        <div class="stats-badge">
            <b>Elevasi:</b> {min_e:.0f} m – {max_e:.0f} m dpl<br>
            <b>Luas Desa:</b> {total_ha:.2f} ha (1.021 ha)<br>
            <b>Area Rawan Tinggi & Sangat Tinggi:</b> 361,17 ha (35,37%)
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
            🖱️ <b>Klik Kiri + Geser:</b> Putar 3D Scene<br>
            🖱️ <b>Scroll:</b> Zoom In / Zoom Out<br>
            🖱️ <b>Klik Kanan + Geser:</b> Geser (Pan)
        </div>
    </div>

    <div id="canvas-container"></div>

    <script>
        const rows = {rows};
        const cols = {cols};
        const zData = {json.dumps(z_data)};
        const minZ = {min_e};
        const maxZ = {max_e};

        // Scene setup
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x141824);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 50000);
        camera.position.set(0, -3500, 3200);

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

        const dirLight = new THREE.DirectionalLight(0xfffaed, 0.8);
        dirLight.position.set(2000, 3000, 4000);
        dirLight.castShadow = true;
        scene.add(dirLight);

        // Terrain Geometry
        const terrainWidth = cols * 30;  // in meters (~4020 m)
        const terrainHeight = rows * 30; // in meters (~7320 m)
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

        // Load Texture
        const textureLoader = new THREE.TextureLoader();
        const texture = textureLoader.load('tex_kerawanan.png');
        texture.magFilter = THREE.LinearFilter;
        texture.minFilter = THREE.LinearFilter;

        const material = new THREE.MeshStandardMaterial({{
            map: texture,
            roughness: 0.7,
            metalness: 0.1,
            side: THREE.DoubleSide
        }});

        const terrainMesh = new THREE.Mesh(geometry, material);
        // PlaneGeometry defaults in XY, orient it so Z is elevation
        terrainMesh.position.set(0, 0, 0);
        scene.add(terrainMesh);

        // Add 3D Pin Markers for Dusun Gedong and Dukoh
        function createPin(name, xMeter, yMeter, zElev, colorHex) {{
            const group = new THREE.Group();
            const z = (zElev - minZ) * verticalScale;

            // Pin rod
            const rodGeo = new THREE.CylinderGeometry(15, 15, 200, 16);
            const rodMat = new THREE.MeshBasicMaterial({{ color: 0xffffff }});
            const rod = new THREE.Mesh(rodGeo, rodMat);
            rod.rotation.x = Math.PI / 2;
            rod.position.set(0, 0, 100);
            group.add(rod);

            // Pin head
            const headGeo = new THREE.SphereGeometry(60, 24, 24);
            const headMat = new THREE.MeshStandardMaterial({{ color: colorHex, roughness: 0.3 }});
            const head = new THREE.Mesh(headGeo, headMat);
            head.position.set(0, 0, 220);
            group.add(head);

            group.position.set(xMeter, yMeter, z);
            scene.add(group);
            return group;
        }}

        // Center origin coordinates:
        // xmin=437850, xmax=441870, midX = 439860
        // ymin=9176070, ymax=9183390, midY = 9179730
        const midX = 439860.0;
        const midY = 9179730.0;

        const pinGedong = createPin("Dusun Gedong", 438883.7 - midX, 9180016.3 - midY, 1656.1, 0xe11d48);
        const pinDukoh = createPin("Dusun Dukoh", 440304.8 - midX, 9182337.9 - midY, 1084.1, 0x2563eb);

        // UI Controls
        document.getElementById('exaggeration').addEventListener('input', function(e) {{
            verticalScale = parseFloat(e.target.value);
            document.getElementById('exag-val').innerText = verticalScale.toFixed(1) + 'x';
            updateTerrainZ();
            pinGedong.position.z = (1656.1 - minZ) * verticalScale;
            pinDukoh.position.z = (1084.1 - minZ) * verticalScale;
        }});

        function resetView() {{
            camera.position.set(0, -3500, 3200);
            controls.target.set(0, 0, 500);
            controls.update();
        }}

        function toggleWireframe() {{
            material.wireframe = !material.wireframe;
        }}

        // Window resize
        window.addEventListener('resize', onWindowResize, false);
        function onWindowResize() {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }}

        // Render loop
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

print(f"Interactive 3D WebGL Viewer generated successfully: {html_path}")
