
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void clear_screen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void cerobong(int size, char bentuk) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < (size * 2) / 2; j++) {
            printf(" ");
        }

        for (int j = 0; j < size; j++) {
            printf("\033[31m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna merah
        }

        printf("\n");
    }
}

void atap(int size, char bentuk) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            printf(" ");
        }

        for (int j = 0; j < 2 * i + 1; j++) {
            printf("\033[34m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna biru
        }

        for (int j = 0; j < 3 * size; j++) {
            printf("\033[32m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna hijau
        }

        printf("\n");
    }
}

void cetakDinding(int size, char bentuk, int warna1, int warna2) {
    int panjang1 = 2 * size - 1;
    int panjang2 = 3 * size;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < panjang1; j++) {
            if (warna1 == 1) {
                printf("\033[35m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna ungu
            } else {
                printf("\033[33m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna kuning
            }
        }
        for (int j = 0; j < panjang2; j++) {
            if (warna2 == 1) {
                printf("\033[35m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna ungu
            } else {
                printf("\033[33m%c\033[0m", bentuk); // Escape sequences ANSI untuk warna kuning
            }
        }
        printf("\n");
    }
}

struct Barang {
    int nomor;
    char nama[50];
    float harga;
};

struct Pembelian {
    int nomorBarang;
    int jumlah;
};

struct RincianBelanja {
    int nomorBarang;
    char nama[50];
    float harga;
    int jumlah;
    float subtotal;
};

void displayBarang(struct Barang barang[]) {
    printf("+==================================================+\n");
    printf("|   Selamat Datang di Toko Komputer FTI UKSW!!!    |\n");
    printf("+==================================================+\n");
    printf("|No.  |Nama Barang         |Harga Barang(Rp.)      |\n");
    printf("|-----+--------------------+-----------------------|\n");

    for (int i = 0; i < 10; ++i) {
        printf("|%-5d|%-20s|Rp. %19.2f|\n", barang[i].nomor, barang[i].nama, barang[i].harga);
    }

    printf("+-----+--------------------+-----------------------+\n");
    printf("0. Keluar\n");
}

float prosesPembelian(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang) {
    float totalHarga = 0;

    for (int i = 0; i < *jumlahBarang; ++i) {
        printf("Masukkan nomor barang ke-%d yang ingin dibeli: ", i + 1);
        scanf("%d", &pembelian[i].nomorBarang);

        if (pembelian[i].nomorBarang == 0) {
            return 0;
        } else if (pembelian[i].nomorBarang >= 1 && pembelian[i].nomorBarang <= 10) {
            printf("Masukkan jumlah barang yang ingin dibeli: ");
            scanf("%d", &pembelian[i].jumlah);

            if (pembelian[i].jumlah > 0) {
                totalHarga += pembelian[i].jumlah * barang[pembelian[i].nomorBarang - 1].harga;
            } else {
                printf("Jumlah barang harus lebih dari 0.\n");
                --i;
            }
        } else {
            printf("Nomor barang tidak valid.\n");
            --i;
        }
    }

    return totalHarga;
}

void tampilkanRincianBelanja(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang) {
    clear_screen();
    printf("\nDaftar Belanja Anda:\n");
    printf("+====================================================================================+\n");
    printf("|Kode |Nama Barang         |Harga Barang(Rp.)   |Jumlah Barang  |      Subtotal      |\n");
    printf("|-----+--------------------+--------------------+---------------+--------------------|\n");

    struct RincianBelanja rincianBelanja[*jumlahBarang];

    for (int i = 0; i < *jumlahBarang; ++i) {
        int nomorBarang = pembelian[i].nomorBarang - 1;

        rincianBelanja[i].nomorBarang = barang[nomorBarang].nomor;
        strcpy(rincianBelanja[i].nama, barang[nomorBarang].nama);
        rincianBelanja[i].harga = barang[nomorBarang].harga;
        rincianBelanja[i].jumlah = pembelian[i

].jumlah;
        rincianBelanja[i].subtotal = rincianBelanja[i].harga * rincianBelanja[i].jumlah;

        printf("|%-5d|%-20s|Rp. %16.2f|%-15d|Rp. %16.2f|\n",
               rincianBelanja[i].nomorBarang, rincianBelanja[i].nama, rincianBelanja[i].harga,
               rincianBelanja[i].jumlah, rincianBelanja[i].subtotal);
    }

    printf("+-----+--------------------+--------------------+---------------+--------------------+\n");

    float totalBelanja = 0;
    for (int i = 0; i < *jumlahBarang; ++i) {
        totalBelanja += rincianBelanja[i].subtotal;
    }

    printf(" 0. Tidak Jadi Beli\n");
    printf("-1. Batal Beli Barang\n\n");
    printf("Total Belanja Anda      : Rp. %.2f\n", totalBelanja);
}

void batalBeliBarang(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang) {
    int kodeBatal;
    printf("Masukkan Kode Barang yang Tidak Jadi Di Beli: ");
    scanf("%d", &kodeBatal);

    if (kodeBatal == 0) {
        printf("Transaksi dibatalkan.\n");
        exit(0);
    } else if (kodeBatal == -1) {
        printf("Batal beli barang.\n");
        *jumlahBarang = 0;
    } else {
        for (int i = 0; i < *jumlahBarang; ++i) {
            if (pembelian[i].nomorBarang == kodeBatal) {
                printf("%s Tidak Jadi Di Beli\n", barang[kodeBatal - 1].nama);

                for (int j = i; j < *jumlahBarang - 1; ++j) {
                    pembelian[j] = pembelian[j + 1];
                }

                (*jumlahBarang)--;

                return;
            }
        }

        printf("Kode Barang %d tidak ditemukan dalam daftar belanja.\n", kodeBatal);
    }
}

int main() {
    struct Barang daftarBarang[10] = {
        {1, "Printer AIO", 550000.00},
        {2, "SSD 1TB", 1500000.00},
        {3, "HDD 1TB", 1250000.00},
        {4, "Keyboard", 80000.00},
        {5, "Mouse", 50000.00},
        {6, "Jack RJ45/PCS", 6000.00},
        {7, "Kabel UTP/M", 3500.00},
        {8, "Kabel Audio", 8000.00},
        {9, "Kabel USB 1m", 9000.00},
        {10, "Kabel USB 5m", 10000.00}
    };

    int menu;
    int jumlahBarang = 0;
    float uangPelanggan;

    while (1) {
        clear_screen();
        printf("Menu\n");
        printf("1. Rumah\n");
        printf("2. Kasir\n");
        printf("3. Keluar\n");

        printf("Pilih menu: ");
        scanf("%d", &menu);

        switch (menu) {
            case 1: {
                int size;
                char bentuk;

                clear_screen();
                printf("Masukkan ukuran: ");
                scanf("%d", &size);
                while ((getchar()) != '\n');

                printf("Masukkan bentuk: ");
                scanf(" %c", &bentuk);

                cerobong(size, bentuk);
                atap(size, bentuk);
                cetakDinding(size, bentuk, 1, 2);
                system("pause");
                break;
            }

            case 2: {
                clear_screen();
                displayBarang(daftarBarang);
                printf("\nBerapa Jenis Barang yang ingin di Beli: ");
                scanf("%d", &jumlahBarang);

                if (jumlahBarang > 0 && jumlahBarang <= 10) {
                    struct Pembelian pembelian[jumlahBarang];
                    float totalHarga = prosesPembelian(daftarBarang, pembelian, &jumlahBarang);

                    if (totalHarga > 0) {
                        tampilkanRincianBelanja(daftarBarang, pembelian, &jumlahBarang);

                        printf("Masukkan Uang Anda       : Rp. ");
                        scanf("%f", &uangPelanggan);

                        while (uangPelanggan < totalHarga) {
                            printf("\nUANG YANG DIMASUKKAN KURANG. SILAHKAN MASUKKAN UANG LAGI.\n");
                            printf("Masukkan Uang Anda Lagi : Rp. ");
                            scanf("%f", &uangPelanggan);
                        }

                        float kembalian = uangPelanggan - totalHarga;

                        if (kembalian > 0) {
                            printf("\nUANG KEMBALIAN          : Rp. %.2f\n", kembalian);
                        } else if (kembalian == 0) {
                            printf("\nTidak Ada Uang Kembalian\n");
                        } else {
                printf("\nUANG PAS\n");
            }
        } else {
            printf("Jumlah barang yang dimasukkan tidak valid.\n");
        }
    } else {
        printf("Jumlah barang yang dimasukkan tidak valid.\n");
    }

    printf("\nTekan tombol apapun untuk kembali ke menu utama...");
    getchar(); // Menunggu masukan dari pengguna
            }
    return 0;
}
    }}}}
