# 📄 MASTER PROMPT UNTUK AI CLAUDE: PENYUSUNAN MANUSKRIP JURNAL ILMIAH
### Proyek: Pemodelan Spasial Kerawanan Tanah Longsor Multi-Kriteria (6 Parameter Komprehensif) Desa Tajuk, Lereng Gunung Merbabu

> **Petunjuk Penggunaan:**  
> Salin (*copy-paste*) seluruh isi dokumen ini ke Claude (Claude 3.5 Sonnet / Opus). Dokumen ini telah distrukturkan sedemikian rupa sehingga Claude memiliki seluruh konteks penelitian, data numerik eksak, landasan geodinamika, dan aturan penulisan jurnal akademik terindeks (SINTA 1/2 / Scopus Q1/Q2) tanpa halusinasi data.

---

```markdown
<system_prompt>
Anda adalah Peneliti Senior di bidang Sains Informasi Geografis, Penginderaan Jauh, dan Geomorfologi Kebencanaan (Senior Geospatial Scientist & Academic Peer Reviewer). Anda berpengalaman menulis dan menelaah artikel ilmiah untuk jurnal terindeks SINTA 1/2 dan Scopus (Q1/Q2) seperti *Geomorphology*, *Catena*, *Natural Hazards*, dan *Journal of Mountain Science*.

Tugas Anda adalah membantu menyusun, menyempurnakan, dan menarasikan naskah jurnal penelitian spasial tingkat desa secara mendalam, berbasis bukti, dan memenuhi kaidah penulisan ilmiah standar IMRaD (Introduction, Methods, Results, and Discussion).

### ATURAN BAHASA & KUALITAS (ACADEMIC ANTI-SLOP RULES):
1. **Larang Keras Klise AI:** DILARANG menggunakan kata-kata hampa atau berbunga-bunga seperti: "merupakan bukti nyata", "menyelami", "tapestry", "tak terbantahkan", "di era modern ini", "seiring berjalannya waktu", "tidak dapat dipungkiri", "merupakan langkah awal yang krusial", atau "menawarkan wawasan mendalam".
2. **Karakter Narasi:** Gunakan kalimat efektif, aktif-pasif terukur, berbobot ilmiah, logis, dan selalu merujuk pada data numerik (persentase, luas ha, skor, koefisien $r$, dan rasio konsistensi $CR$).
3. **Kepatuhan Data:** JANGAN PERNAH mengarang atau mengira-ngira angka baru. Seluruh angka HARUS mengikuti Master Dataset yang tercantum di bawah ini.
4. **Bahasa:** Bahasa Indonesia baku akademik formal (atau Bahasa Inggris akademik jika diminta).
</system_prompt>

<master_dataset>
## 1. IDENTITAS WILAYAH & DATA DASAR
- **Lokasi Penelitian:** Desa Tajuk, Kecamatan Getasan, Kabupaten Semarang, Provinsi Jawa Tengah.
- **Letak Geomorfologis:** Kaki hingga lereng atas bagian utara-barat laut Gunung Merbabu.
- **Batas Administrasi:** Data Vektor Peta Rupa Bumi Indonesia (RBI) Skala 1:25.000 (Badan Informasi Geospasial / LapakGIS Kab. Semarang).
- **Dimensi Grid Raster:** 134 kolom x 244 baris (32.696 piksel grid seluler 30 m x 30 m pada proyeksi UTM Zona 49S, WGS 84 / EPSG:32749).
- **Luas Total Wilayah Raster Analisis:** 2.942,64 hektare (Area tangkapan lereng mikro Desa Tajuk hingga puncak Merbabu).
- **Rentang Elevasi (DEMNAS 30m):** Minimum = 933,6 m dpl (Kaki lereng utara batas Getasan); Maksimum = 3.085,4 m dpl (Flank kaldera puncak Gunung Merbabu).

## 2. INTEGRASI DATA VEKTOR TOPOGRAFI & ADMINISTRASI (RBI 1:25.000)
1. **Jaringan Hidrologi & Alur Debris (51 Ruas Vektor):**
   - Meliputi Kali Gandu (alur utama banjir bandang debris flow 28 Feb 2024), Kali Nanggulak, Kali Jurang, dan Kali Jetak.
   - Mengalir dari igir-igir curam hulu Merbabu menuju dataran undak permukiman kaki lereng.
2. **Jaringan Jalan Desa (39 Ruas Vektor):**
   - Menghubungkan 18 dusun dan sentra produksi pertanian sayuran terasering dengan jalur utama Kopeng-Getasan.
3. **Toponimi 18 Dusun (Sebaran Pemukiman & Titik Kritis):**
   - *Dusun Gedong* (Elevasi 1.630,4 m dpl, Titik Bencana Longsor Terasering 28 Feb 2024).
   - *Dusun Dukuh* (Elevasi 1.080,8 m dpl, Titik Jembatan Tertimbun Aliran Rombakan Debris Flow 28 Feb 2024).
   - *Dusun Ngaduman* (Elevasi 1.677,9 - 1.737,0 m dpl, Dusun Tertinggi di Jawa Tengah).
   - *Dusun Tajuk* (Elevasi 1.071,6 m dpl, Pusat Balai Desa dan Administrasi Pemerintahan).
   - *Dusun Lainnya:* Pulihan (1.145 m), Sokowolu (1.183 m), Cingklok (1.181 m), Jabu (1.127 m), Krikisan (1.040 m), Ngroto (1.066 m), Banaran (968 m), Kaliajeng (999 m), Puyang (1.095 m), Tajul (1.324 m).

## 3. CITRA PENGINDERAAN JAUH LANDSAT 9 OLI-2
- **Waktu Akuisisi:** 24 September 2026 (Kondisi bebas awan di atas Desa Tajuk).
- **Koreksi Radiometrik:** BOA Surface Reflectance.
- **Indeks Vegetasi (NDVI):** Min = 0,181 | Max = 0,790 | Rata-rata = 0,512.
- **Indeks Kelembapan Kanopi (NDMI):** Min = -0,149 | Max = 0,490 | Rata-rata = 0,146.
- **Korelasi Pearson ($r$) NDVI vs NDMI:** 0,917.

## 4. PEMODELAN MULTIKRITERIA AHP KOMPREHENSIF (6 PARAMETER)
Sesuai rekomendasi Badan Nasional Penanggulangan Bencana (BNPB Perka No. 2/2012) dan Pusat Vulkanologi dan Mitigasi Bencana Geologi (PVMBG), model mengintegrasikan 6 parameter penyebab longsor:

### Matriks Perbandingan Berpasangan (Pairwise Comparison Matrix - Saaty 1980):
| Parameter | Kemiringan Lereng | Tutupan Lahan (LULC) | Curah Hujan Orografis | Pedologi Jenis Tanah | Elevasi Topografi | Kelembapan NDMI | Bobot Prioritas ($W$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kemiringan Lereng** | 1 | 2 | 2 | 3 | 4 | 5 | **0,32 (32%)** |
| **Tutupan Lahan (LULC)** | 1/2 | 1 | 2 | 2 | 3 | 4 | **0,22 (22%)** |
| **Curah Hujan Orografis** | 1/2 | 1/2 | 1 | 2 | 3 | 3 | **0,18 (18%)** |
| **Pedologi Jenis Tanah** | 1/3 | 1/2 | 1/2 | 1 | 2 | 3 | **0,14 (14%)** |
| **Elevasi Topografi** | 1/4 | 1/3 | 1/3 | 1/2 | 1 | 2 | **0,09 (9%)** |
| **Kelembapan NDMI** | 1/5 | 1/4 | 1/3 | 1/3 | 1/2 | 1 | **0,05 (5%)** |

### Uji Rasio Konsistensi (Consistency Ratio):
- **Nilai Eigen Terbesar ($\lambda_{\max}$):** 6,150
- **Indeks Konsistensi ($CI$):** $CI = rac{\lambda_{\max} - n}{n - 1} = rac{6,150 - 6}{5} = 0,030$
- **Indeks Acak ($RI$, $n=6$):** 1,24
- **Rasio Konsistensi ($CR$):** $CR = rac{CI}{RI} = rac{0,030}{1,24} = \mathbf{0,024} < \mathbf{0,10}$  
  *(Matriks dinyatakan sangat konsisten, logis, dan sahih secara matematis).*

### Persamaan Matematis Kerawanan Longsor 6-Parameter ($KL_{6P}$):
$$KL_{6P} = 0{,}32 	imes S_{	ext{slope}} + 0{,}22 	imes S_{	ext{LULC}} + 0{,}18 	imes S_{	ext{rain}} + 0{,}14 	imes S_{	ext{soil}} + 0{,}09 	imes S_{	ext{elev}} + 0{,}05 	imes S_{	ext{NDMI}}$$

## 5. SKORING DAN KLASIFIKASI PARAMETER
1. **Kemiringan Lereng (Bobot 32%):**
   - 0 – 15% (Landai): Skor 1
   - 15 – 25% (Agak Curam): Skor 2
   - 25 – 40% (Curam): Skor 3
   - 40 – 60% (Sangat Curam): Skor 4
   - > 60% (Terjal Ekstrem): Skor 5
2. **Tutupan Lahan LULC (Bobot 22%):**
   - Hutan Lindung Taman Nasional Gunung Merbabu: Skor 1 (Luas: 2.621,58 Ha / 80,18%)
   - Permukiman Penduduk: Skor 4 (Luas: 52,35 Ha / 1,60%)
   - Ladang Sayur Terasering Intensif: Skor 5 (Luas: 269,93 Ha / 8,26%)
3. **Curah Hujan Orografis (Bobot 18%):**
   - 2.400 – 2.800 mm/tahun (Zona Kaki Lereng): Skor 3
   - 2.800 – 3.200 mm/tahun (Zona Lereng Tengah): Skor 4
   - > 3.200 mm/tahun (Zona Puncak Kaldera): Skor 5
4. **Pedologi Jenis Tanah (Bobot 14%):**
   - Latosol Coklat Kemerahan (Kaki Lereng Bawah): Skor 2 (Permeabilitas sedang, kohesi lempung)
   - Andosol Coklat Gembur (Lereng Tengah): Skor 4 (Sangat peka erosi dan jenuh air)
   - Regosol Pasir Vulkanik Lepas (Puncak Curam): Skor 5 (Struktur remah lepas tanpa kohesi)
5. **Elevasi Topografi (Bobot 9%):**
   - 933 – 1.300 m dpl: Skor 1
   - 1.300 – 1.700 m dpl: Skor 2
   - 1.700 – 2.100 m dpl: Skor 3
   - 2.100 – 2.500 m dpl: Skor 4
   - 2.500 – 3.085 m dpl: Skor 5
6. **Kelembapan Kanopi NDMI (Bobot 5%):**
   - < 0,05: Skor 1
   - 0,05 – 0,15: Skor 2
   - 0,15 – 0,25: Skor 3
   - 0,25 – 0,35: Skor 4
   - > 0,35: Skor 5

## 6. HASIL DISTRIBUSI SPASIAL KELAS KERAWANAN (MODEL 6-PARAMETER)
| Kelas Kerawanan | Rentang Skor Komposit | Luas (Hektare) | Persentase Wilayah (%) | Karakteristik Spasial & Rekomendasi |
| :--- | :---: | :---: | :---: | :--- |
| **Kelas 1 (Sangat Rendah)** | < 2,00 | 527,22 ha | 17,92% | Morfologi datar di kaki lereng utara (Dusun Tajuk, Krikisan, Banaran). Zona aman pengembangan permukiman. |
| **Kelas 2 (Rendah)** | 2,00 – 2,80 | 983,70 ha | 33,43% | Kaki lereng landai perkebunan rakyat dan permukiman (Dusun Dukuh, Pulihan, Sokowolu). |
| **Kelas 3 (Sedang)** | 2,80 – 3,60 | 1.113,93 ha | 37,85% | **Zona Dominan Terluas:** Terasering pertanian sayuran lereng tengah (Dusun Gedong, Ngaduman). Rawan ketidakstabilan lokal saat jenuh air. |
| **Kelas 4 (Tinggi)** | 3,60 – 4,40 | 317,79 ha | 10,80% | Tebing terjal (>40%) lereng atas, tanah andosol-regosol, curah hujan >3.000 mm/th. Hulu luncuran material debris flow. |
| **Kelas 5 (Sangat Tinggi)** | $\ge$ 4,40 | 0,00 ha | 0,00% | Tebing cadas batuan andesit masif puncak tanpa penutup tanah lepas. |
| **Total Wilayah Analisis** | - | **2.942,64 ha** | **100,00%** | **Fokus mitigasi terpusat pada alur konektivitas hidraulik lereng-sungai.** |

## 7. ANALISIS GEOMORFOLOGI KRITIS: VALIDASI BENCANA 28 FEBRUARI 2024
1. **Ketidakstabilan Lereng In-Situ (Dusun Gedong):**
   - Terletak pada elevasi 1.630 m dpl, kemiringan lereng 20,3%, tutupan lahan ladang sayur terasering (skor 5), tanah andosol gembur (skor 4).
   - Model 6-parameter mengklasifikasikan wilayah ini pada skor komposit 3,12 (Kelas Sedang mendekati Tinggi).
   - Longsor terpicu oleh kenaikan muka air tanah pori (*pore water pressure*) akibat curah hujan lebat berkepanjangan pada tanah andosol gembur yang diolah secara intensif tanpa vegetasi berakar tunjang dalam.
2. **Aliran Rombakan / Debris Flow (Dusun Dukuh):**
   - Tapak jembatan Dukuh berada di elevasi 1.080 m dpl pada kemiringan lereng 9,0% (Kelas Rendah, skor 2,11).
   - Tertutupnya jembatan oleh material tebal lumpur, batu andesit, dan kayu membuktikan fenomena **aliran rombakan (*debris flow*)** yang terangkut melalui alur Kali Gandu sepanjang 2,8 km dari tebing rawan tinggi di hulu lereng Gunung Merbabu.
   - Mengonfirmasi pentingnya pemodelan konektivitas hidraulik lereng-ke-sungai (*slope-channel coupling*) dalam mitigasi kebencanaan gunungapi aktif.
</master_dataset>

<instruction_prompts>
Berikut adalah perintah-perintah yang dapat Anda minta untuk saya kerjakan berdasarkan Master Dataset di atas:

### Perintah 1: Susun Bab Pendahuluan (Introduction)
"Berdasarkan <system_prompt> dan <master_dataset>, buatkan draf Bab 1 Pendahuluan secara komprehensif, menguraikan latar belakang geomorfologi vulkanik Merbabu, urgensi integrasi 6 parameter (Slope, LULC, Curah Hujan, Pedologi, Elevasi, NDMI), gap penelitian sebelumnya (kegagalan membedakan longsor in-situ vs debris flow), dan tujuan studi."

### Perintah 2: Susun Bab Metodologi (Methods)
"Susun Bab 2 Metode Penelitian lengkap dengan: (a) Deskripsi wilayah studi dan data vektor RBI 1:25.000; (b) Alur kerja SIG dan ekstraksi spektral Landsat 9; (c) Formulasi matematis AHP 6-parameter lengkap dengan Matriks Saaty dan pembuktian CR = 0,024; (d) Klasifikasi skoring multikriteria."

### Perintah 3: Susun Bab Hasil dan Pembahasan (Results & Discussion)
"Susun Bab 3 Hasil dan Pembahasan secara mendalam, sertakan tabel distribusi luas 6 parameter, analisis spasial sebaran kerawanan di 18 dusun, dan pembahasan geomorfologi komparatif antara longsor translasi Dusun Gedong vs debris flow Jembatan Dukuh."

### Perintah 4: Susun Rekomendasi Kebijakan & Kesimpulan
"Susun Bab 4 Kesimpulan dan Rekomendasi Kebijakan Mitigasi Terapan untuk BPBD Kabupaten Semarang dan Pemerintah Desa Tajuk, mencakup zonasi tata ruang, rekayasa drainase terasering, dan peringatan dini berbasis curah hujan orografis."
</instruction_prompts>
```
