import os
import zipfile
import xml.etree.ElementTree as ET

code_dir = r"C:/Users/HP VICTUS 15/Documents/CODE/1_Academic_Coursework/ChellAcademicHistory/Semester-10"
desktop_dir = r"C:/Users/HP VICTUS 15/Desktop/Study/SEMESTER 10/PEMODELAN SPASIAL"
output_dir = os.path.join(code_dir, "output").replace("\\", "/")

# XML Template for the full QGIS project
qgs_content = f"""<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis projectname="Pemodelan Kerawanan Longsor Desa Tajuk" saveDateTime="2026-10-26T23:10:00" version="3.28.3-Firenze" saveUserFull="Marchell" saveUser="HP VICTUS 15">
  <homePath path=""/>
  <title>Pemodelan Spasial Kerawanan Longsor Desa Tajuk</title>
  <transaction mode="Disabled"/>
  <projectFlags set=""/>
  <projectCrs>
    <spatialrefsys nativeFormat="Wkt">
      <wkt>PROJCRS["WGS 84 / UTM zone 49S",BASEGEOGCRS["WGS 84",ENSEMBLE["World Geodetic System 1984 ensemble",MEMBER["World Geodetic System 1984 (Transit)"],MEMBER["World Geodetic System 1984 (G730)"],MEMBER["World Geodetic System 1984 (G873)"],MEMBER["World Geodetic System 1984 (G1150)"],MEMBER["World Geodetic System 1984 (G1674)"],MEMBER["World Geodetic System 1984 (G1762)"],MEMBER["World Geodetic System 1984 (G2139)"],ELLIPSOID["WGS 84",6378137,298.257223563,LENGTHUNIT["metre",1]],ENSEMBLEACCURACY[2.0]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433]],ID["EPSG",4326]],CONVERSION["UTM zone 49S",METHOD["Transverse Mercator",ID["EPSG",9807]],PARAMETER["Latitude of natural origin",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8801]],PARAMETER["Longitude of natural origin",111,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8802]],PARAMETER["Scale factor at natural origin",0.9996,SCALEUNIT["unity",1],ID["EPSG",8805]],PARAMETER["False easting",500000,LENGTHUNIT["metre",1],ID["EPSG",8806]],PARAMETER["False northing",10000000,LENGTHUNIT["metre",1],ID["EPSG",8807]]],CS[Cartesian,2],AXIS["(E)",east,ORDER[1],LENGTHUNIT["metre",1]],AXIS["(N)",north,ORDER[2],LENGTHUNIT["metre",1]],USAGE[SCOPE["Engineering survey, topographic mapping."],AREA["Between 108°E and 114°E, southern hemisphere between 80°S and equator, onshore and offshore. Australia. Indonesia."],BBOX[-80,108,0,114]],ID["EPSG",32749]]</wkt>
      <proj4>+proj=utm +zone=49 +south +datum=WGS84 +units=m +no_defs</proj4>
      <srsid>3199</srsid>
      <srid>32749</srid>
      <authid>EPSG:32749</authid>
      <description>WGS 84 / UTM zone 49S</description>
      <projectionacronym>utm</projectionacronym>
      <ellipsoidacronym>EPSG:7030</ellipsoidacronym>
      <geographicflag>false</geographicflag>
    </spatialrefsys>
  </projectCrs>
  <layer-tree-group>
    <customproperties>
      <Option/>
    </customproperties>
    <layer-tree-layer checked="Qt::Checked" name="Titik Validasi BPBD" providerKey="ogr" expanded="1" id="titik_bpbd_layer" source="{output_dir}/titik_longsor_bpbd.shp">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Checked" name="Batas Administrasi Desa Tajuk" providerKey="ogr" expanded="1" id="batas_tajuk_layer" source="{output_dir}/batas_desa_tajuk.shp">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Checked" name="Peta Kerawanan Longsor (AHP)" providerKey="gdal" expanded="1" id="kl_layer" source="{output_dir}/kerawanan_longsor_kelas.tif">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Unchecked" name="Kemiringan Lereng (%)" providerKey="gdal" expanded="0" id="slope_layer" source="{output_dir}/slope_percent_tajuk.tif">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Unchecked" name="NDVI (Kerapatan Vegetasi)" providerKey="gdal" expanded="0" id="ndvi_layer" source="{output_dir}/ndvi_tajuk.tif">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Unchecked" name="NDMI (Kelembapan Permukaan)" providerKey="gdal" expanded="0" id="ndmi_layer" source="{output_dir}/ndmi_tajuk.tif">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <layer-tree-layer checked="Qt::Checked" name="DEM Elevasi (30m)" providerKey="gdal" expanded="1" id="dem_layer" source="{output_dir}/dem_tajuk_30m.tif">
      <customproperties><Option/></customproperties>
    </layer-tree-layer>
    <custom-order enabled="0">
      <item>titik_bpbd_layer</item>
      <item>batas_tajuk_layer</item>
      <item>kl_layer</item>
      <item>slope_layer</item>
      <item>ndvi_layer</item>
      <item>ndmi_layer</item>
      <item>dem_layer</item>
    </custom-order>
  </layer-tree-group>
  <mapcanvas annotationsVisible="1" name="theMapCanvas">
    <units>meters</units>
    <extent>
      <xmin>437500.0</xmin>
      <ymin>9175500.0</ymin>
      <xmax>442200.0</xmax>
      <ymax>9183800.0</ymax>
    </extent>
    <rotation>0</rotation>
    <destinationsrs>
      <spatialrefsys nativeFormat="Wkt">
        <wkt>PROJCRS["WGS 84 / UTM zone 49S",BASEGEOGCRS["WGS 84",ENSEMBLE["World Geodetic System 1984 ensemble",MEMBER["World Geodetic System 1984 (Transit)"],MEMBER["World Geodetic System 1984 (G730)"],MEMBER["World Geodetic System 1984 (G873)"],MEMBER["World Geodetic System 1984 (G1150)"],MEMBER["World Geodetic System 1984 (G1674)"],MEMBER["World Geodetic System 1984 (G1762)"],MEMBER["World Geodetic System 1984 (G2139)"],ELLIPSOID["WGS 84",6378137,298.257223563,LENGTHUNIT["metre",1]],ENSEMBLEACCURACY[2.0]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433]],ID["EPSG",4326]],CONVERSION["UTM zone 49S",METHOD["Transverse Mercator",ID["EPSG",9807]],PARAMETER["Latitude of natural origin",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8801]],PARAMETER["Longitude of natural origin",111,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8802]],PARAMETER["Scale factor at natural origin",0.9996,SCALEUNIT["unity",1],ID["EPSG",8805]],PARAMETER["False easting",500000,LENGTHUNIT["metre",1],ID["EPSG",8806]],PARAMETER["False northing",10000000,LENGTHUNIT["metre",1],ID["EPSG",8807]]],CS[Cartesian,2],AXIS["(E)",east,ORDER[1],LENGTHUNIT["metre",1]],AXIS["(N)",north,ORDER[2],LENGTHUNIT["metre",1]],USAGE[SCOPE["Engineering survey, topographic mapping."],AREA["Between 108°E and 114°E, southern hemisphere between 80°S and equator, onshore and offshore. Australia. Indonesia."],BBOX[-80,108,0,114]],ID["EPSG",32749]]</wkt>
        <proj4>+proj=utm +zone=49 +south +datum=WGS84 +units=m +no_defs</proj4>
        <srsid>3199</srsid>
        <srid>32749</srid>
        <authid>EPSG:32749</authid>
        <description>WGS 84 / UTM zone 49S</description>
      </spatialrefsys>
    </destinationsrs>
  </mapcanvas>
  <projectLayers>
    <!-- TITIK BPBD -->
    <maplayer type="vector" id="titik_bpbd_layer" name="Titik Validasi BPBD">
      <datasource>{output_dir}/titik_longsor_bpbd.shp</datasource>
      <renderer-v2 type="singleSymbol" symbollevels="0">
        <symbols>
          <symbol type="marker" name="0" alpha="1">
            <layer class="SimpleMarker" enabled="1" pass="0">
              <Option type="Map">
                <Option value="0" type="QString" name="angle"/>
                <Option value="227,26,28,255" type="QString" name="color"/>
                <Option value="triangle" type="QString" name="name"/>
                <Option value="0,0" type="QString" name="offset"/>
                <Option value="255,255,255,255" type="QString" name="outline_color"/>
                <Option value="solid" type="QString" name="outline_style"/>
                <Option value="0.8" type="QString" name="outline_width"/>
                <Option value="5.5" type="QString" name="size"/>
              </Option>
            </layer>
          </symbol>
        </symbols>
      </renderer-v2>
      <labeling type="simple">
        <settings calloutType="simple">
          <text-style fontBold="1" fontItalic="0" fontLetterSpacing="0" fontPointSize="10" fontSize="10" fontUnderline="0" fontWordSpacing="0" textColor="0,0,0,255" namedStyle="Bold" fontFamily="Arial">
            <text-buffer bufferColor="255,255,255,255" bufferDraw="1" bufferSize="1.5"/>
          </text-style>
          <rule-labels fieldName="Dusun"/>
        </settings>
      </labeling>
    </maplayer>

    <!-- BATAS DESA TAJUK -->
    <maplayer type="vector" id="batas_tajuk_layer" name="Batas Administrasi Desa Tajuk">
      <datasource>{output_dir}/batas_desa_tajuk.shp</datasource>
      <renderer-v2 type="singleSymbol" symbollevels="0">
        <symbols>
          <symbol type="fill" name="0" alpha="1">
            <layer class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option value="0,0,0,255" type="QString" name="line_color"/>
                <Option value="solid" type="QString" name="line_style"/>
                <Option value="1.0" type="QString" name="line_width"/>
              </Option>
            </layer>
          </symbol>
        </symbols>
      </renderer-v2>
    </maplayer>

    <!-- KERAWANAN LONGSOR PALETTED -->
    <maplayer type="raster" id="kl_layer" name="Peta Kerawanan Longsor (AHP)">
      <datasource>{output_dir}/kerawanan_longsor_kelas.tif</datasource>
      <rasterrenderer band="1" opacity="1" type="paletted">
        <colorPalette>
          <paletteEntry color="#1a9641" label="Sangat Rendah (1.0–1.8) [46.7 ha / 4.6%]" value="1"/>
          <paletteEntry color="#a6d96a" label="Rendah (1.8–2.6) [191.8 ha / 18.8%]" value="2"/>
          <paletteEntry color="#ffffbf" label="Sedang (2.6–3.4) [421.5 ha / 41.3%]" value="3"/>
          <paletteEntry color="#fdae61" label="Tinggi (3.4–4.2) [346.5 ha / 33.9%]" value="4"/>
          <paletteEntry color="#d7191c" label="Sangat Tinggi (4.2–5.0) [14.7 ha / 1.4%]" value="5"/>
        </colorPalette>
      </rasterrenderer>
    </maplayer>

    <!-- KEMIRINGAN LERENG -->
    <maplayer type="raster" id="slope_layer" name="Kemiringan Lereng (%)">
      <datasource>{output_dir}/slope_percent_tajuk.tif</datasource>
      <rasterrenderer band="1" opacity="1" type="singlebandpseudocolor">
        <rastershader>
          <colorrampshader colorRampType="INTERPOLATED" clip="0">
            <item color="#2b83ba" label="0% (Datar)" value="0"/>
            <item color="#abdda4" label="15% (Landai)" value="15"/>
            <item color="#ffffbf" label="25% (Agak Curam)" value="25"/>
            <item color="#fdae61" label="45% (Curam)" value="45"/>
            <item color="#d7191c" label=">80% (Sangat Curam)" value="80"/>
          </colorrampshader>
        </rastershader>
      </rasterrenderer>
    </maplayer>

    <!-- NDVI -->
    <maplayer type="raster" id="ndvi_layer" name="NDVI (Kerapatan Vegetasi)">
      <datasource>{output_dir}/ndvi_tajuk.tif</datasource>
      <rasterrenderer band="1" opacity="1" type="singlebandpseudocolor">
        <rastershader>
          <colorrampshader colorRampType="INTERPOLATED" clip="0">
            <item color="#a6611a" label="Lahan Terbuka (<0.1)" value="0.1"/>
            <item color="#dfc27d" label="Jarang (0.1–0.3)" value="0.3"/>
            <item color="#f5f5f5" label="Sedang (0.3–0.5)" value="0.5"/>
            <item color="#80cdc1" label="Rapat (0.5–0.7)" value="0.7"/>
            <item color="#018571" label="Sangat Rapat (>0.7)" value="0.85"/>
          </colorrampshader>
        </rastershader>
      </rasterrenderer>
    </maplayer>

    <!-- NDMI -->
    <maplayer type="raster" id="ndmi_layer" name="NDMI (Kelembapan Permukaan)">
      <datasource>{output_dir}/ndmi_tajuk.tif</datasource>
      <rasterrenderer band="1" opacity="1" type="singlebandpseudocolor">
        <rastershader>
          <colorrampshader colorRampType="INTERPOLATED" clip="0">
            <item color="#f7fbff" label="Kering (-0.15)" value="-0.15"/>
            <item color="#6baed6" label="Sedang (0.15)" value="0.15"/>
            <item color="#08306b" label="Sangat Lembap (0.49)" value="0.49"/>
          </colorrampshader>
        </rastershader>
      </rasterrenderer>
    </maplayer>

    <!-- DEM ELEVASI -->
    <maplayer type="raster" id="dem_layer" name="DEM Elevasi (30m)">
      <datasource>{output_dir}/dem_tajuk_30m.tif</datasource>
      <rasterrenderer band="1" opacity="1" type="singlebandpseudocolor">
        <rastershader>
          <colorrampshader colorRampType="INTERPOLATED" clip="0">
            <item color="#31a354" label="938 m" value="938"/>
            <item color="#fed976" label="1500 m" value="1500"/>
            <item color="#fd8d3c" label="2200 m" value="2200"/>
            <item color="#7a0177" label="3066 m" value="3066"/>
          </colorrampshader>
        </rastershader>
      </rasterrenderer>
    </maplayer>
  </projectLayers>
  <ElevationProperties>
    <terrainProvider type="raster">
      <TerrainProvider layer="dem_layer" scale="1" offset="0"/>
    </terrainProvider>
  </ElevationProperties>
</qgis>
"""

# Save PROJECT AKHIR.qgs in code_dir and desktop_dir
qgs_path_code = os.path.join(code_dir, "PROJECT AKHIR.qgs")
qgs_path_desktop = os.path.join(desktop_dir, "PROJECT AKHIR.qgs")

with open(qgs_path_code, "w", encoding="utf-8") as f:
    f.write(qgs_content)
with open(qgs_path_desktop, "w", encoding="utf-8") as f:
    f.write(qgs_content)

# Zip into PROJECT AKHIR.qgz
for target_dir in [code_dir, desktop_dir]:
    qgz_path = os.path.join(target_dir, "PROJECT AKHIR.qgz")
    with zipfile.ZipFile(qgz_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("PROJECT AKHIR.qgs", qgs_content)

print(f"Created styled QGIS Project:")
print(f"  {qgs_path_code}")
print(f"  {qgs_path_desktop}")
