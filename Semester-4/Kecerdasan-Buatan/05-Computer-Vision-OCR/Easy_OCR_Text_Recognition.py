import easyocr
import cv2

# Membaca gambar dan mendeteksi teks
def detect_text_from_image(image):
    reader = easyocr.Reader(['en', 'id'])  # Mendukung bahasa Inggris dan Indonesia
    print("Mendeteksi teks pada gambar...")
    result = reader.readtext(image)  # Membaca teks dari gambar

    detected_texts = []
    print("Hasil mentah EasyOCR:", result)  # Debugging output

    # Jika ada teks terdeteksi, proses setiap hasil
    for (bbox, text, _) in result:
        detected_texts.append(text)
        # Menggambar kotak pembatas dan teks pada gambar
        top_left = tuple(map(int, bbox[0]))  # Koordinat kiri atas kotak pembatas
        bottom_right = tuple(map(int, bbox[2]))  # Koordinat kanan bawah kotak pembatas
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)  # Menggambar kotak pembatas
        cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)  # Menambahkan teks di atas kotak pembatas

    return image, detected_texts  # Mengembalikan gambar dengan kotak pembatas dan teks yang terdeteksi

# Menggunakan kamera untuk deteksi teks
def detect_from_camera():
    cap = cv2.VideoCapture(0)  # Menggunakan kamera pertama
    if not cap.isOpened():
        print("Kamera tidak dapat diakses.")
        return

    print("Tekan 'q' untuk keluar.")
    while True:
        ret, frame = cap.read()  # Membaca frame dari kamera
        if not ret:
            print("Gagal membaca frame dari kamera.")
            break

        # Deteksi teks pada frame kamera
        frame, detected_texts = detect_text_from_image(frame)

        if detected_texts:
            print("Teks terdeteksi pada frame:")
            for text in detected_texts:
                print(f"- {text}")
        else:
            print("Tidak ada teks yang terdeteksi pada frame ini.")

        # Perbesar frame
        frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

        # Menampilkan frame dengan teks terdeteksi
        cv2.imshow('Camera Frame', frame)

        # Keluar jika menekan 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Menu utama
def main():
    print("Pilih menu:")
    print("1. Deteksi teks dari gambar")
    print("2. Deteksi teks dari kamera")
    choice = input("Masukkan pilihan (1/2): ")

    if choice == '1':
        image_path = input("Masukkan path gambar: ")
        image = cv2.imread(image_path)  # Membaca gambar dari path

        if image is None:
            print("Gambar tidak ditemukan! Periksa kembali path gambar.")
            return

        result_image, detected_texts = detect_text_from_image(image)
        if detected_texts:
            print("\nTeks yang terdeteksi:")
            for text in detected_texts:
                print(f"- {text}")
        else:
            print("\nTidak ada teks yang terdeteksi pada gambar.")

        # Tampilkan hasil deteksi di jendela
        cv2.imshow('Hasil Deteksi Gambar', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '2':
        detect_from_camera()
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()