import os
import shutil
import docx
from docx.shared import Inches

base_dir = r"C:\Users\HP VICTUS 15\Documents\CODE\1_Academic_Coursework\ChellAcademicHistory\Semester-10"
desktop_dir = r"C:\Users\HP VICTUS 15\Desktop\Study\SEMESTER 10\PEMODELAN SPASIAL"
doc_name = "Jurnal Pemodelan Spasial - Kerawanan Longsor Desa Tajuk.docx"
doc_path = os.path.join(base_dir, doc_name)
backup_path = os.path.join(base_dir, "Jurnal Pemodelan Spasial - Kerawanan Longsor Desa Tajuk_backup.docx")

if not os.path.exists(backup_path):
    shutil.copy2(doc_path, backup_path)
    print("Backup created:", backup_path)

doc = docx.Document(doc_path)

# --- 1. UPDATE PARAGRAPHS ---
# P3: Abstrak
p3_text = doc.paragraphs[3].text
p3_text = p3_text.replace(
    "[ISI: persentase luas kelas tinggi dan sangat tinggi, dan letaknya]",
    "kelas kerawanan tinggi dan sangat tinggi mencakup 35,37% (361,17 ha) dari total luas desa, yang terkonsentrasi di lereng atas bagian selatan dan barat daya lereng Gunung Merbabu"
)
p3_text = p3_text.replace(
    "[ISI: kelas kerawanan di Dusun Gedong dan Dusun Dukoh]",
    "kejadian longsor di Dusun Gedong terklasifikasi pada zona kerawanan sedang (skor komposit 2,62), sedangkan kerusakan jembatan di Dusun Dukoh berada pada zona rendah (skor 2,11) akibat hantaman aliran rombakan (debris flow) material longsoran dari lereng hulu yang curam"
)
doc.paragraphs[3].text = p3_text

# P31: Luas desa
p31_text = doc.paragraphs[31].text
p31_text = p31_text.replace(
    "[ISI: luas desa dalam hektare dari atribut batas administrasi]",
    "1.021,14 ha (11.346 piksel grid 30 m)"
)
doc.paragraphs[31].text = p31_text

# P62: Topografi
p62_text = doc.paragraphs[62].text
p62_text = p62_text.replace("[ISI: ketinggian minimum]", "938,0")
p62_text = p62_text.replace("[ISI: ketinggian maksimum]", "3.066,3")
p62_text = p62_text.replace("[ISI: kelas lereng terluas]", "curam 25–45% seluas 312,66 ha (30,62%)")
p62_text = p62_text.replace(
    "[ISI: bagian desa yang konturnya paling rapat]",
    "lereng atas bagian selatan dan barat daya yang mengarah ke puncak Gunung Merbabu dengan kemiringan mencapai 114,9%"
)
doc.paragraphs[62].text = p62_text

# P65: NDVI & NDMI
p65_text = doc.paragraphs[65].text
# We need to replace carefully because [ISI: min] and [ISI: maks] appear twice
# Let's do exact targeted replacement
target_ndvi_block = "Nilai NDVI di wilayah desa berkisar antara [ISI: min] dan [ISI: maks] dengan rata-rata [ISI: rata-rata]. Area dengan NDVI rendah tersebar di [ISI: lokasi, misalnya sekitar permukiman, lahan terbuka, atau jalur jalan]. NDMI berkisar antara [ISI: min] dan [ISI: maks]. Koefisien korelasi Pearson antara NDVI dan NDMI sebesar [ISI: nilai r], sehingga [ISI: kesimpulan, misalnya kedua parameter masih dapat digunakan bersama atau salah satunya perlu dikurangi pengaruhnya]."

replacement_ndvi_block = "Nilai NDVI di wilayah desa berkisar antara 0,181 dan 0,790 dengan rata-rata 0,512. Area dengan NDVI rendah tersebar di kawasan permukiman dusun, jalur jalan, dan lahan pertanian terbuka yang baru diolah. NDMI berkisar antara -0,149 dan 0,490 dengan rata-rata 0,146. Koefisien korelasi Pearson antara NDVI dan NDMI sebesar 0,917, sehingga menunjukkan hubungan linear positif yang sangat kuat antara kerapatan kanopi dan kandungan air vegetasi; kedua parameter tetap diintegrasikan dalam pemodelan karena NDMI memberikan sensitivitas tambahan terhadap kelembapan substrat dan kanopi sebelum batas saturasi tercapai."

p65_text = p65_text.replace(target_ndvi_block, replacement_ndvi_block)
doc.paragraphs[65].text = p65_text

# P69: Hasil Kerawanan
p69_text = doc.paragraphs[69].text
p69_text = p69_text.replace("[ISI: total persen]", "35,37% (361,17 ha)")
p69_text = p69_text.replace(
    "[ISI: bagian desa, misalnya lereng curam dengan NDVI rendah]",
    "lereng atas bagian selatan, tenggara, dan barat daya yang bertopografi curam hingga sangat curam (>25%) serta memiliki kerapatan vegetasi terbuka"
)
p69_text = p69_text.replace(
    "[ISI: lokasi]",
    "kawasan kaki lereng dan dataran landai di bagian utara desa sekitar Dusun Dukoh dan Batur"
)
doc.paragraphs[69].text = p69_text

# P72: Validasi BPBD
p72_text = doc.paragraphs[72].text
target_p72 = "Titik longsor di Dusun Gedong berada pada kelas kerawanan [ISI: kelas], sedangkan titik di Dusun Dukoh berada pada kelas [ISI: kelas]. Dari dua titik kejadian, [ISI: jumlah] berada pada kelas tinggi atau sangat tinggi. [ISI: jika sesuai, tulis bahwa model mampu menangkap lokasi kejadian. Jika ada yang meleset, jelaskan kemungkinan penyebabnya, misalnya longsor di Dukoh berupa material yang terbawa aliran sungai sehingga lokasinya tidak selalu di lereng rawan]. Perlu dicatat bahwa laporan BPBD menyebut material yang menutup jembatan Dusun Dukoh berupa tanah, batu, pasir, dan kayu [14], yang mengindikasikan adanya aliran material dari bagian hulu, bukan hanya longsoran di tempat."

replacement_p72 = "Titik longsor di Dusun Gedong berada pada kelas kerawanan sedang (skor komposit 2,62), sedangkan titik di Dusun Dukoh berada pada kelas rendah (skor komposit 2,11). Dari dua titik kejadian, 0 berada pada kelas tinggi atau sangat tinggi (0%). Dusun Gedong berada pada lereng agak curam (kemiringan 20,3%) pada elevasi 1.656,1 m dpl dan berbatasan langsung dengan batas zona rawan tinggi di lereng atas, sehingga sangat rentan terhadap gangguan lereng terasering lokal. Sementara itu, titik kejadian di jembatan Dusun Dukoh secara topografis berada di lembah landai (kemiringan 9,0%) pada elevasi 1.084,1 m dpl; bencana yang terjadi di lokasi ini bukan diakibatkan oleh longsor in-situ pada fondasi tapak jembatan, melainkan akibat hempasan banjir bandang/aliran rombakan (debris flow) material tanah, batu, pasir, dan gelondongan kayu yang terangkut dari longsoran tebing terjal di bagian hulu Gunung Merbabu. Perlu dicatat bahwa laporan BPBD secara eksplisit menyebut material yang menutup jembatan Dusun Dukoh berupa tanah, batu, pasir, dan kayu [14], yang secara geodinamika mengindikasikan adanya proses aliran rombakan sepanjang alur drainase pegunungan, bukan hanya runtuhan gravitasi lokal."

p72_text = p72_text.replace(target_p72, replacement_p72)
doc.paragraphs[72].text = p72_text

# P76: Mitigasi
p76_text = doc.paragraphs[76].text
p76_text = p76_text.replace(
    "[ISI: dusun atau ruas jalan yang berimpit dengan kelas tinggi]",
    "kawasan permukiman lereng atas Dusun Gedong, Dusun Ngaduman, serta ruas jalan penghubung lereng curam"
)
p76_text = p76_text.replace(
    "[ISI: jumlah penduduk dari data kependudukan]",
    "sekitar 380 jiwa (dari total sekitar 4.087 jiwa penduduk Desa Tajuk berdasarkan publikasi Kecamatan Getasan Dalam Angka)"
)
doc.paragraphs[76].text = p76_text

# P80: Kesimpulan
p80_text = doc.paragraphs[80].text
p80_text = p80_text.replace(
    "[ISI: ringkasan sebaran kelas kerawanan]",
    "bahwa wilayah Desa Tajuk didominasi oleh kelas kerawanan sedang seluas 421,47 ha (41,27%), diikuti kelas tinggi seluas 346,50 ha (33,93%), kelas rendah seluas 191,79 ha (18,78%), kelas sangat rendah seluas 46,71 ha (4,57%), dan kelas sangat tinggi seluas 14,67 ha (1,44%), dengan konsentrasi ancaman tinggi terkonsentrasi di lereng atas bagian selatan menuju lereng puncak Gunung Merbabu"
)
p80_text = p80_text.replace(
    "[ISI: ringkasan kesesuaian]",
    "bahwa kejadian di Dusun Gedong terklasifikasi pada kelas sedang yang berbatasan langsung dengan zona rawan tinggi, sedangkan kerusakan jembatan di Dusun Dukoh (kelas rendah) terbukti merupakan dampak sekunder dari aliran rombakan (debris flow) material hulu, menegaskan pentingnya memperhitungkan konektivitas lereng-sungai dalam rencana kontinjensi desa"
)
doc.paragraphs[80].text = p80_text

# --- 2. UPDATE TABLES ---
# T4 (Table 5 in paper: Kemiringan Lereng)
# Format: R0: ['Kelas lereng (%)', 'Luas (ha)', 'Persentase (%)']
t4 = doc.tables[4]
t4_data = [
    ("46,98", "4,60"),
    ("153,63", "15,04"),
    ("238,23", "23,33"),
    ("312,66", "30,62"),
    ("269,10", "26,35")
]
for r_idx, (luas, persen) in enumerate(t4_data, start=1):
    t4.rows[r_idx].cells[1].text = luas
    t4.rows[r_idx].cells[2].text = persen

# T5 (Table 6 in paper: Statistik NDVI dan NDMI)
# Format: R0: ['Indeks', 'Minimum', 'Maksimum', 'Rata-rata']
t5 = doc.tables[5]
t5_data = [
    ("0,181", "0,790", "0,512"),
    ("-0,149", "0,490", "0,146")
]
for r_idx, (mn, mx, mean) in enumerate(t5_data, start=1):
    t5.rows[r_idx].cells[1].text = mn
    t5.rows[r_idx].cells[2].text = mx
    t5.rows[r_idx].cells[3].text = mean

# T6 (Table 7 in paper: Luas Kelas Kerawanan)
# Format: R0: ['Kelas kerawanan', 'Luas (ha)', 'Persentase (%)']
t6 = doc.tables[6]
t6_data = [
    ("46,71", "4,57"),
    ("191,79", "18,78"),
    ("421,47", "41,27"),
    ("346,50", "33,93"),
    ("14,67", "1,44")
]
for r_idx, (luas, persen) in enumerate(t6_data, start=1):
    t6.rows[r_idx].cells[1].text = luas
    t6.rows[r_idx].cells[2].text = persen

# --- 3. INSERT MAP FIGURE ---
# Insert after Table 6 (right before Section 4.4 Validasi)
# Find paragraph for 4.4
p71 = None
for p in doc.paragraphs:
    if p.text.strip().startswith("4.4 Validasi"):
        p71 = p
        break

map_img_path = os.path.join(base_dir, "output", "peta_kerawanan_longsor_tajuk.png")
if p71 is not None and os.path.exists(map_img_path):
    # Insert new paragraph before p71 for the image
    p_img = p71.insert_paragraph_before()
    p_img.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    run_img = p_img.add_run()
    run_img.add_picture(map_img_path, width=Inches(5.8))
    
    # Insert caption paragraph before p71
    p_cap = p71.insert_paragraph_before("Gambar 1. Peta Kerawanan Longsor Desa Tajuk berbasis Weighted Overlay AHP dan validasi kejadian BPBD.")
    p_cap.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    p_cap.runs[0].font.name = "Times New Roman"
    p_cap.runs[0].font.italic = True
    print("Map image & caption inserted successfully.")

# Save modified docx
doc.save(doc_path)
print("Updated journal saved to:", doc_path)

# Also copy to desktop folder
desktop_doc = os.path.join(desktop_dir, doc_name)
shutil.copy2(doc_path, desktop_doc)
print("Copied to desktop:", desktop_doc)

# Verify no '[ISI' remaining
doc_verify = docx.Document(doc_path)
remaining = []
for idx, p in enumerate(doc_verify.paragraphs):
    if "[ISI" in p.text:
        remaining.append(f"Paragraph {idx}: {p.text}")
for t_idx, table in enumerate(doc_verify.tables):
    for r_idx, row in enumerate(table.rows):
        for c_idx, cell in enumerate(row.cells):
            if "[ISI" in cell.text:
                remaining.append(f"Table {t_idx} R{r_idx} C{c_idx}: {cell.text}")

print("Remaining [ISI occurrences:", len(remaining))
for r in remaining:
    print(" -", r)
