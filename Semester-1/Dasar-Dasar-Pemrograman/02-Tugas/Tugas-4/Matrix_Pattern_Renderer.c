#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_ROWS 10
#define MAX_COLS 10

void clear_screen() {
    #ifdef _WIN32
        system("cls"); // Untuk Windows
    #else
        system("clear"); // Untuk sistem Unix (Linux, macOS)
    #endif
}

void tampilkan_awalan_nama(char *nama) {
    printf("Selamat datang di Program Matriks!\n");
    printf("\nSilakan masukkan nama Anda untuk memulai: ");
    scanf("%s", nama);
}

void tampilkan_menu(char *nama) {
    clear_screen();
    printf("====================PROGRAM MATRIKS====================\n");
    printf("Selamat datang, %s!\n", nama);
    printf("\nPetunjuk : Pilih menu yang tersedia dengan menginputkan\n");
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
    printf("\nMasukkan elemen matriks:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("Masukkan elemen matriks[%d][%d]: ", i, j);
            scanf("%d", &matriks[i][j]);
        }
    }
    // Menampilkan matriks sebelum transpose
    clear_screen();
    printf("------------------1. TRANSPOSE MATRIKS------------------\n");
    printf("\nMatriks sebelum di-transpose:\n\n");
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
    printf("\nMatriks setelah di-transpose:\n\n");
    for (int i = 0; i < kolom; ++i) {
        for (int j = 0; j < baris; ++j) {
            printf("%d\t", transpos[i][j]);
        }
        printf("\n");
    }
}

void ubah_nilai_matriks() {
    int matriks[MAX_ROWS][MAX_COLS];
    int baris, kolom;

    printf("Masukkan jumlah baris matriks: ");
    scanf("%d", &baris);

    printf("Masukkan jumlah kolom matriks: ");
    scanf("%d", &kolom);

    // Meminta pengguna memasukkan elemen matriks
    printf("\nMasukkan elemen matriks:\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("Masukkan elemen matriks[%d][%d]: ", i, j);
            scanf("%d", &matriks[i][j]);
        }
    }

    // Menampilkan matriks sebelum perubahan nilai
    clear_screen();
    printf("---------------2. MENGUBAH NILAI MATRIKS---------------\n");
    printf("Matriks sebelum perubahan nilai:\n\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("%d\t", matriks[i][j]);
        }
        printf("\n");
    }

    // Meminta pengguna untuk memasukkan kelipatan nilai yang ingin diubah
    int kelipatan, nilaiBaru;
    printf("\nMasukkan kelipatan nilai yang ingin diubah: ");
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
    printf("\nMatriks setelah perubahan nilai:\n\n");
    for (int i = 0; i < baris; ++i) {
        for (int j = 0; j < kolom; ++j) {
            printf("%d\t", matriks[i][j]);
        }
        printf("\n");
    }
}

int main() {
    char pilihan, lanjut;
    char nama[50];

    tampilkan_awalan_nama(nama);

    while (1) {
        tampilkan_menu(nama);
        scanf(" %c", &pilihan);

        switch (pilihan) {
            case '1':
                do {
                    clear_screen();
                    printf("------------------1. TRANSPOSE MATRIKS------------------\n");
                    transpose_matriks();
                    printf("\n-------------------------------------------------------\n");
                    printf("Apakah Anda ingin melanjutkan ke operasi transpose lagi? (Y/N) : ");
                    scanf(" %c", &lanjut);
                } while (toupper(lanjut) == 'Y');
                break;
            case '2':
                do {
                    clear_screen();
                    printf("---------------2. MENGUBAH NILAI MATRIKS---------------\n");
                    ubah_nilai_matriks();
                    printf("\n-------------------------------------------------------\n");
                    printf("Apakah Anda ingin melanjutkan ke operasi perubahan nilai lagi? (Y/N) : ");
                    scanf(" %c", &lanjut);
                } while (toupper(lanjut) == 'Y');
                break;
            case '3':
                clear_screen();
                printf("-------------------------KELUAR-------------------------\n\n");
                printf("Terima kasih telah menggunakan program ini!!!\n\n");
                printf("Programmed by Marchell Adi Pratama\n");
                printf("NIM 672023081\n");
                printf("\n========================================================\n");
                system("pause");
                exit(0);
                getchar();
                break;
            default:
                printf("Pilihan tidak valid. Silakan coba lagi.\n");
                clear_screen();
                tampilkan_menu(nama);
        }
    }

    return 0;
}
