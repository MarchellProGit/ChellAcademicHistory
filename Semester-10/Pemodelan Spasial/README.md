# Pemodelan Spasial: Analisis Kerawanan Longsor & 3D Digital Twin Desa Tajuk
> **Mata Kuliah:** Pemodelan Spasial | **Semester:** 10  
> **Penulis:** Marchell Adi Pratama | **Program Studi:** Teknik Informatika (Penjurusan Data Science)  
> **Lokasi Penelitian:** Desa Tajuk, Kecamatan Getasan, Kabupaten Semarang (Flank Kaldera Utara Gunung Merbabu)  
> **Live 3D Digital Twin:** [https://marchellprogit.github.io/PemodelanSpasial-DesaTajuk/](https://marchellprogit.github.io/PemodelanSpasial-DesaTajuk/)

---

## 1. Ringkasan Eksekutif & Latar Belakang

Desa Tajuk terletak di lereng utara–timur laut Gunung Merbabu dengan rentang elevasi dramatis antara **1.000 hingga 3.066,3 m dpl** dan gradien kemiringan lereng mencapai **>45%** pada dinding kaldera purba. Wilayah ini memiliki kerentanan geomorfologis dan hidrologis tinggi akibat kombinasi:
1. Formasi batuan andesit vulkanik gembur tak terkonsolidasi (*Merbabu Volcanic Rock*).
2. Curah hujan orografis ekstrem (>3.000 mm/tahun).
3. Alih fungsi lahan menjadi pertanian hortikultura sayuran semusim pada lereng curam tanpa terasering mekanik bersertifikasi.

Pada **28 Februari 2024**, hujan lebat berintensitas tinggi memicu longsor lereng terasering di Dusun Gedong yang menimpa rumah warga dan jalan penghubung, serta banjir bandang aliran rombakan (*debris flow*) di sepanjang lembah Kali Gandu yang menimbun total jembatan penghubung Dusun Dukuh dengan material batuan beku vulkanik, lumpur, dan gelondongan kayu.

Proyek ini membangun **model kerawanan spasial berbasis Analytical Hierarchy Process (AHP) 6 parameter terstandarisasi**, dikalibrasi dengan titik kejadian bencana riil BPBD, dan divisualisasikan dalam bentuk **Interactive 3D Digital Twin WebGL**.

---

## 2. Metodologi: Analytical Hierarchy Process (AHP) 6-Parameter

Pembobotan faktor pemicu kerawanan dihitung menggunakan matriks perbandingan berpasangan (*pairwise comparison matrix*) Saaty:

$$\text{Skor Kerawanan} = \sum_{i=1}^{n} (W_i \times S_i)$$

| No | Parameter Lingkungan | Bobot ($W_i$) | Justifikasi Geospasial & Hidrometeorologis |
| :-: | :--- | :-: | :--- |
| 1 | **Kemiringan Lereng (*Slope*)** | **34% (0.34)** | Gaya pendorong gravitasi primer massa tanah/batuan pada bidang gelincir |
| 2 | **Geologi & Jenis Tanah** | **22% (0.22)** | Erodibilitas tanah Andosol dan Regosol vulkanik berpori tinggi |
| 3 | **Curah Hujan Orografis** | **18% (0.18)** | Pemicu kejenuhan pori air (*pore-water pressure*) dan likuifaksi lereng |
| 4 | **Penggunaan Lahan (LULC)** | **12% (0.12)** | Kohesi akar tanaman; hortikultura sayur memiliki daya ikat tanah dangkal |
| 5 | **Jarak dari Sesar & Sempadan Sungai** | **8% (0.08)** | Zona dekompresi tektonik dan koridor hidrologi pembawa material rombakan |
| 6 | **Kerapatan Vegetasi (NDVI)** | **6% (0.06)** | Perlindungan kanopi daun terhadap energi kinetik butir tetes hujan (*splash erosion*) |

- **Uji Konsistensi Matriks:**
  - Nilai Eigen Maksimum ($\lambda_{\text{max}}$) = 6.106
  - *Consistency Index* ($CI$) = 0.021
  - *Random Index* ($RI$) = 1.24
  - **Consistency Ratio ($CR$) = 0.017** ($\le 0.10$ $\rightarrow$ **Konsisten & Valid**)

---

## 3. Hasil Analisis Spasial & Distribusi Zona

Berdasarkan klasifikasi jenjang setara (*equal interval & natural breaks standard BNPB*), zonasi kerawanan longsor di Desa Tajuk (Luas Total: **1.021,14 ha**) terbagi menjadi:

| Kelas Kerawanan | Rentang Skor AHP | Luas Wilayah (ha) | Persentase (%) | Karakteristik Wilayah & Rekomendasi |
| :--- | :---: | :---: | :---: | :--- |
| **Sangat Rendah** | $< 1.8$ | 46,71 ha | 4,57% | Kaki lereng landai kaki desa utara; zona pemukiman stabil. |
| **Rendah** | $1.8 - 2.6$ | 191,79 ha | 18,78% | Lereng landai ke bergelombang kaki bukit; zona perkebunan campur. |
| **Sedang** | $2.6 - 3.4$ | 421,47 ha | **41,27%** | Permukiman terasering lereng tengah (Dusun Gedong, Ngaduman). Perlu penguatan drainase lereng. |
| **Tinggi** | $3.4 - 4.2$ | 346,50 ha | **33,93%** | Tebing terjal flank Merbabu; pertanian sayur curam tanpa dinding penahan. Potensi longsor translasi tinggi. |
| **Sangat Tinggi** | $\ge 4.2$ | 14,67 ha | 1,44% | Flank kaldera puncak tebing tegak (>45%); batuan lepas regosol vulkanik. Zona non-hunian / konservasi mutlak. |

---

## 4. Kalibrasi Bencana Faktual (Kasus 28 Februari 2024)

1. **Dusun Gedong (Koordinat UTM: 438883.7 mE, 9180016.3 mN; Elevasi: 1.656,1 m dpl):**
   - Kejadian: Tanah longsor translasi tebing terasering menimpa 1 rumah warga dan menutup badan jalan.
   - Analisis Model: Lereng agak curam (20,3%), skor AHP 2,62 (Kelas Sedang mendekati Tinggi). Kejadian dipicu oleh akumulasi rembesan air pada tanah Andosol jenuh air hujan orografis.
2. **Dusun Dukuh (Koordinat UTM: 440304.8 mE, 9182337.9 mN; Elevasi: 1.084,1 m dpl):**
   - Kejadian: Jembatan penghubung tertimbun endapan sedimen debris tebal batu dan gelondongan pohon.
   - Analisis Model: Topografi jembatan landai (9,0%), skor AHP 2,11 (Kelas Rendah). Kerusakan bukan akibat longsor lokal di tapak jembatan, melainkan limpasan aliran rombakan (*debris flow*) yang meluncur cepat sepanjang alur lembah Kali Gandu dari dinding terjal hulu Merbabu.

---

## 5. Struktur Direktori Proyek

```text
Pemodelan Spasial/
├── index.html                               # Standalone Three.js 3D WebGL Digital Twin (Buka langsung di browser)
├── PROJECT AKHIR.qgs / .qgz                 # Proyek Master QGIS Desktop
├── CLAUDE_PROMPT_JURNAL.md                  # Metadata & Prompt Lengkap Rekonstruksi Jurnal
├── Jurnal Pemodelan Spasial.docx            # Naskah Lengkap Jurnal Ilmiah
├── extracted_jurnal.txt                     # Transkrip Teks Ekstraksi Jurnal
│
├── web/                                     # Asset Web Application & Hosting
│   ├── index.html
│   ├── OrbitControls.js
│   ├── three.min.js
│   └── vercel.json
│
├── output/                                  # Hasil Pemrosesan Spasial & Visualisasi
│   ├── batas_desa_tajuk.shp/.geojson        # Poligon Vektor Batas Administrasi Desa Tajuk
│   ├── sungai_tajuk.shp                     # Vektor Alur Sungai & Jalur Debris Kali Gandu (51 Ruas)
│   ├── jalan_tajuk.shp                      # Vektor Jaringan Jalan Desa Tajuk (39 Ruas)
│   ├── dusun_tajuk.shp                      # Vektor Toponimi Dusun (18 Lokasi)
│   ├── titik_longsor_bpbd.shp               # Titik Validasi Bencana Faktual BPBD
│   ├── peta_kerawanan_longsor_tajuk.png     # Render Peta Kartografis 2D Resolusi Tinggi
│   ├── tex_ahp.jpg, tex_elev.jpg, etc.      # Tekstur Draped Permukaan 3D (AHP, CIR, Slope, Elevasi)
│   └── statistik_ahp_6parameter.txt         # Rincian Angka Luasan dan Persentase Tiap Kelas
│
├── build_flagship_3d.py                     # Skrip Generator Master Digital Twin 3D
├── run_full_analysis.py                     # Skrip Otomasi Analisis Raster AHP (GDAL/Rasterio)
├── build_qgis_project.py                    # Skrip Penyusun Hierarki Layer Proyek QGIS
└── apply_journal_updates.py                 # Skrip Sinkronisasi Data Jurnal
```

---

## 6. Cara Menjalankan Proyek

### A. Membuka 3D Digital Twin Web:
- Buka file [`index.html`](./index.html) menggunakan peramban modern (Google Chrome, Microsoft Edge, atau Firefox).
- Atau akses langsung versi online di [GitHub Pages](https://marchellprogit.github.io/PemodelanSpasial-DesaTajuk/).

### B. Membuka di QGIS Desktop:
1. Pastikan QGIS versi 3.28 LTR atau yang lebih baru telah terinstal.
2. Buka berkas proyek `PROJECT AKHIR.qgz`.
3. Semua layer (Batas Desa, Alur Sungai, Jaringan Jalan, Toponimi Dusun, Titik Kejadian BPBD, DEMNAS 30m, dan Peta Kerawanan AHP) telah tertata rapi dalam grup hierarki layer lengkap dengan simbologi tematik.
