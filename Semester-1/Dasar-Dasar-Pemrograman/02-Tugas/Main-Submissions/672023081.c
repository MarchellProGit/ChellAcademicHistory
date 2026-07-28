#include <stdio.h>
#include <math.h>

// Fungsi untuk menghitung luas persegi
float luasPersegi(float sisi) {
    return sisi * sisi;
}

// Fungsi untuk menghitung luas persegi panjang
float luasPersegiPanjang(float panjang, float lebar) {
    return panjang * lebar;
}

// Fungsi untuk menghitung luas segitiga
float luasSegitiga(float alas, float tinggi) {
    return 0.5 * alas * tinggi;
}

// Fungsi untuk menghitung luas lingkaran
float luasLingkaran(float jariJari) {
    return M_PI * jariJari * jariJari;
}

int main() {

        printf("NAMA : Marchell Adi Pratama ||\n");
        printf("NIM  : 672023081            ||\n");
        printf("=============================\n\n");

    int pilihan;
    float sisiPersegi, panjangPersegiPanjang, lebarPersegiPanjang, alasSegitiga, tinggiSegitiga, jariJariLingkaran;

    do {

        printf("\nProgram Fungsi Menghitung Luas Bangun Datar\n");

        // Menampilkan menu
        printf("\nMenu:\n");
        printf("1. Luas Persegi\n");
        printf("2. Luas Persegi Panjang\n");
        printf("3. Luas Segitiga\n");
        printf("4. Luas Lingkaran\n");
        printf("0. Keluar\n\n");

        // Input pilihan menu
        printf("Pilih menu (0-4): ");
        scanf("%d", &pilihan);

        switch (pilihan) {
            case 1:
                // Input sisi persegi
                printf("Masukkan panjang sisi persegi: ");
                scanf("%f", &sisiPersegi);
                printf("Luas Persegi: %.2f\n", luasPersegi(sisiPersegi));
                break;

            case 2:
                // Input panjang dan lebar persegi panjang
                printf("\nMasukkan panjang persegi panjang: ");
                scanf("%f", &panjangPersegiPanjang);
                printf("Masukkan lebar persegi panjang: ");
                scanf("%f", &lebarPersegiPanjang);
                printf("Luas Persegi Panjang: %.2f\n\n", luasPersegiPanjang(panjangPersegiPanjang, lebarPersegiPanjang));
                break;

            case 3:
                // Input alas dan tinggi segitiga
                printf("Masukkan alas segitiga: ");
                scanf("%f", &alasSegitiga);
                printf("Masukkan tinggi segitiga: ");
                scanf("%f", &tinggiSegitiga);
                printf("Luas Segitiga: %.2f\n\n", luasSegitiga(alasSegitiga, tinggiSegitiga));
                break;

            case 4:
                // Input jari-jari lingkaran
                printf("Masukkan jari-jari lingkaran: ");
                scanf("%f", &jariJariLingkaran);
                printf("Luas Lingkaran: %.2f\n\n", luasLingkaran(jariJariLingkaran));
                break;

            case 0:
                printf("Program berakhir.\n");
                break;

            default:
                printf("Pilihan tidak valid. Silakan pilih lagi.\n");
        }

    } while (pilihan != 0);

    return 0;
}
