#include <stdio.h>
#include <stdlib.h>

#define MAX_ROWS 10
#define MAX_COLS 10

#include <stdio.h>
#include <stdlib.h>

void clear_screen() {
    #ifdef _WIN32
        system("cls"); // Untuk Windows
    #else
        system("clear"); // Untuk sistem Unix (Linux, macOS)
    #endif
}


void tampilkan_menu(char *nama) {  // Perbaikan #1: Tambahkan parameter untuk menerima nama
    printf("Masukkan nama Anda: ");
    scanf("%s", nama);  // Perbaikan #2: Baca nama pengguna
    printf("====================PROGRAM MATRIKS====================\n");
    printf("Selamat datang, %s!\n", nama);  // Perbaikan #3: Tampilkan nama pengguna
    printf("Petunjuk : Pilih menu yang tersedia dengan menginputkan\n");
    printf("           nomor menu\n\n");

    printf("Menu : \n");
    printf("       1. Transpose Matriks\n");
    printf("       2. Mengubah Nilai Matriks\n");
    printf("       3. Keluar\n");
    printf("-------------------------------------------------------\n");
    printf("Masukkan pilihan Anda : ");
}

void transpose_matriks() {
    int matriks[MAX_ROWS][MAX_COLS];
    int transpos[MAX_COLS][MAX_ROWS];
    int baris, kolom;

    printf("Masukkan jumlah baris matriks: ");
    scanf("%d", &baris);

    printf("Masukkan jumlah kolom matriks: ");
    scanf("%d", &kolom);

    // Meminta pengguna memasukkan elemen matriks
    printf("Masukkan elemen matriks:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("Masukkan elemen matriks[%d][%d]: ", i, j);
            scanf("%d", &matriks[i][j]);
        }
    }
    // Menampilkan matriks sebelum transpose
    printf("Matriks sebelum di-transpose:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("%d\t", matriks[i][j]);
        }
        printf("\n");
    }

    // Melakukan operasi transpose
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            transpos[j][i] = matriks[i][j];
        }
    }

    // Menampilkan matriks hasil transpose
    printf("Matriks setelah di-transpose:\n");
    for (int i = 0; i < kolom; ++i) {
        for (int j = 0; j < baris; ++j) {
            printf("%d\t", transpos[i][j]);
        }
        printf("\n");
    }
}  // Perbaikan #2: Tambahkan tanda kurung kurawal penutup

void ubah_nilai_matriks() {
    int matriks[MAX_ROWS][MAX_COLS];
    int baris, kolom;

    printf("Masukkan jumlah baris matriks: ");
    scanf("%d", &baris);

    printf("Masukkan jumlah kolom matriks: ");
    scanf("%d", &kolom);

    // Meminta pengguna memasukkan elemen matriks
    printf("Masukkan elemen matriks:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("Masukkan elemen matriks[%d][%d]: ", i, j);
            scanf("%d", &matriks[i][j]);
        }
    }

    // Menampilkan matriks sebelum perubahan nilai
    printf("Matriks sebelum perubahan nilai:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("%d\t", matriks[i][j]);
        }
        printf("\n");
    }

    // Meminta pengguna untuk memasukkan kelipatan nilai yang ingin diubah
    int kelipatan, nilaiBaru;
    printf("Masukkan kelipatan nilai yang ingin diubah: ");
    scanf("%d", &kelipatan);

    // Meminta pengguna untuk memasukkan nilai baru
    printf("Masukkan nilai baru: ");
    scanf("%d", &nilaiBaru);

    // Melakukan perubahan nilai
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            if (matriks[i][j] % kelipatan == 0) {
                matriks[i][j] = nilaiBaru;
                printf("Nilai pada indeks [%d][%d] berhasil diubah menjadi %d\n", i, j, nilaiBaru);
            }
        }
    }

    // Menampilkan matriks setelah perubahan nilai
    printf("Matriks setelah perubahan nilai:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("%d\t", matriks[i][j]);
        }
        printf("\n");
    }
}  // Perbaikan #3: Tambahkan tanda kurung kurawal penutup

int main() {
    char pilihan, lanjut;
    char nama[50];  // Perbaikan #4: Tambahkan array untuk menyimpan nama pengguna

    while (1) {
        tampilkan_menu(nama);  // Perbaikan #5: Kirim nama sebagai argumen
        scanf(" %c", &pilihan);

        switch (pilihan) {
            case '1':
                do {
                clear_screen();
                printf("------------------1. TRANSPOSE MATRIKS------------------\n");
                transpose_matriks();
                printf("Apakah Anda ingin melanjutkan ke operasi transpose lagi? (Y/N) : ");
                scanf(" %c", &lanjut);
                } while (lanjut == 'y' || lanjut == 'Y');
                break;
            case '2':
                do{
                clear_screen();
                printf("---------------2. MENGUBAH NILAI MATRIKS---------------\n");
                ubah_nilai_matriks();
                printf("Apakah Anda ingin melanjutkan ke operasi transpose lagi? (Y/N) : ");
                scanf(" %c", &lanjut);
                } while (lanjut == 'y' || lanjut == 'Y');
                break;
            case '3':
             clear_screen();
                printf("-------------------------KELUAR-------------------------\n\n");
                printf("Terima kasih telah menggunakan program ini!!!\n\n");
                printf("Programmed by Marchell Adi Pratama\n");
                printf("NIM 672023081\n");
                printf("========================================================\n");
                exit(0);
            default:
                printf("Pilihan tidak valid. Silakan coba lagi.\n");
        }
    }

    return 0;
}
