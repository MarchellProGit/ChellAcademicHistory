#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <unistd.h>

void delay(int milliseconds) {
    Sleep(milliseconds);
}

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
            printf("\033[31m%c\033[0m", bentuk); //warna merah
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
            printf("\033[34m%c\033[0m", bentuk); //warna biru
        }

        for (int j = 0; j < 3 * size; j++) {
            printf("\033[32m%c\033[0m", bentuk); // warna hijau
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
                printf("\033[35m%c\033[0m", bentuk); //warna ungu
            } else {
                printf("\033[33m%c\033[0m", bentuk); //warna kuning
            }
        }
        for (int j = 0; j < panjang2; j++) {
            if (warna2 == 1) {
                printf("\033[35m%c\033[0m", bentuk); //warna ungu
            } else {
                printf("\033[33m%c\033[0m", bentuk); //warna kuning
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
    // Menggunakan ANSI escape codes untuk pewarnaan teks
    printf("\033[1;33m+==================================================+\n");
    printf("|   Selamat Datang di Toko Komputer FTI UKSW!!!    |\n");
    printf("+==================================================+\n");
    printf("|No.  |Nama Barang         |Harga Barang(Rp.)      |\n");
    printf("|-----+--------------------+-----------------------|\n");

    for (int i = 0; i < 10; ++i) {
        printf("\033[0;36m|%-5d\033[0m|%-20s\033[0;32m|Rp. %19.2f|\n", barang[i].nomor, barang[i].nama, barang[i].harga);
    }

    printf("\033[1;33m+-----+--------------------+-----------------------+\n");
    printf("\033[0m0. Keluar\n");
}

float prosesPembelian(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang) {
    float totalHarga = 0;

    for (int i = 0; i < *jumlahBarang; ++i) {
        printf("Masukkan nomor barang ke-%d: ", i + 1);
        scanf("%d", &pembelian[i].nomorBarang);

        if (pembelian[i].nomorBarang >= 1 && pembelian[i].nomorBarang <= 10) {
            printf("Masukkan jumlah barang yang ingin dibeli: ");
            scanf("%d", &pembelian[i].jumlah);

            if (pembelian[i].jumlah > 0) {
                totalHarga += pembelian[i].jumlah * barang[pembelian[i].nomorBarang - 1].harga;
            } else {
                printf("Jumlah barang harus lebih dari 0. Silakan masukkan kembali.\n");
                --i;
            }
        } else {
            printf("Nomor barang tidak valid. Silakan masukkan nomor barang yang benar.\n");
            --i;
        }
    }

    return totalHarga;
}

void tampilkanRincianBelanja(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang, float totalHarga) {
    clear_screen();
    printf("\n\033[1;34mDaftar Belanja Anda:\n");
    printf("+====================================================================================+\n");
    printf("|No   |Nama Barang         |Harga Barang(Rp.)   |Jumlah Barang  |      Subtotal      |\n");
    printf("|-----+--------------------+--------------------+---------------+--------------------|\n");

    struct RincianBelanja rincianBelanja[*jumlahBarang];

    for (int i = 0; i < *jumlahBarang; ++i) {
        int nomorBarang = pembelian[i].nomorBarang - 1;

        rincianBelanja[i].nomorBarang = barang[nomorBarang].nomor;
        strcpy(rincianBelanja[i].nama, barang[nomorBarang].nama);
        rincianBelanja[i].harga = barang[nomorBarang].harga;
        rincianBelanja[i].jumlah = pembelian[i].jumlah;
        rincianBelanja[i].subtotal = rincianBelanja[i].harga * rincianBelanja[i].jumlah;

        printf("\033[0;36m|%-5d\033[0m|%-20s|Rp. %16.2f|%-15d|\033[0;32mRp. %16.2f\033[0m|\n",
               rincianBelanja[i].nomorBarang, rincianBelanja[i].nama, rincianBelanja[i].harga,
               rincianBelanja[i].jumlah, rincianBelanja[i].subtotal);
    }

    printf("+-----+--------------------+--------------------+---------------+--------------------+\n");

    float totalBelanja = 0;
    for (int i = 0; i < *jumlahBarang; ++i) {
        totalBelanja += rincianBelanja[i].subtotal;
    }

    printf(" \033[1;31m0. Tidak Jadi Beli\n");
    printf("-1. Batal Beli Barang\n\n");
    printf("\033[1;33mTotal Belanja Anda : Rp. %.2f\n\033[0m", totalBelanja);
}

void batalBeliAtauBayar(struct Barang barang[], struct Pembelian pembelian[], int *jumlahBarang, float *totalHarga) {
    float uangPelanggan;
    float kembalian;
    int nomorBarangPembelian;

    printf("Masukkan Uang Anda : Rp. ");
    scanf("%f", &uangPelanggan);

    if (uangPelanggan == -1) {
        int kodeBatal;
        printf("Masukkan nomor barang yang tidak jadi dibeli: ");
        scanf("%d", &kodeBatal);

        // Cari barang berdasarkan nomorBarang
        int found = 0; // untuk menandai apakah nomor barang ditemukan
        for (int i = 0; i < *jumlahBarang; ++i) {
            if (pembelian[i].nomorBarang == kodeBatal) {
                found = 1; // Nomor barang ditemukan
                nomorBarangPembelian = kodeBatal;

                // Mengurangkan subtotal dari totalHarga
                *totalHarga -= pembelian[i].jumlah * barang[nomorBarangPembelian - 1].harga;

                // Menghapus barang dari pembelian
                for (int j = i; j < *jumlahBarang - 1; ++j) {
                    pembelian[j] = pembelian[j + 1];
                }

                (*jumlahBarang)--;

                // Menampilkan rincian belanja yang diperbarui
                tampilkanRincianBelanja(barang, pembelian, jumlahBarang, *totalHarga);

                // Membersihkan buffer input
                while ((getchar()) != '\n');

                // Meminta konfirmasi pembayaran
                printf("\nApakah Anda ingin melanjutkan pembayaran? (Y/T): ");
                char lanjutTidak;
                scanf(" %c", &lanjutTidak);

                if (toupper(lanjutTidak) == 'Y') {
                    // Melanjutkan proses pembayaran
                    printf("Masukkan uang Anda : Rp. ");
                    scanf("%f", &uangPelanggan);

                    kembalian = uangPelanggan - *totalHarga;

                    if (uangPelanggan == *totalHarga) {
                        printf("Uang Anda pas\n");
                    } else if (kembalian > 0) {
                        printf("\nPembayaran berhasil! Kembalian Anda: Rp. %.2f\n", kembalian);
                    } else {
                        // Meminta input lagi jika uang kurang
                        while (uangPelanggan < *totalHarga) {
                            printf("Uang Anda Kurang !!\n");
                            printf("Silakan Masukkan Lagi Uang Anda : Rp. ");
                            scanf("%f", &uangPelanggan);
                        }
                        // Pembayaran berhasil setelah input uang yang cukup
                        printf("Pembayaran berhasil!\n");
                        printf("Kembalian Anda: Rp. %.2f\n", uangPelanggan - *totalHarga);
                    }

                    // Menanyakan apakah pengguna ingin berbelanja lagi atau tidak
                    printf("\n      Terimakasih Telah Berbelanja\n");
                    printf("Apakah Anda Ingin Berbelanja Lagi (Y/T): ");
                    char respon;
                    scanf(" %c", &respon);

                    if (toupper(respon) == 'Y') {
                        clear_screen();
                        prosesMenuKasir(barang);
                    }
                }
            }
        }

        // Jika nomor barang tidak ditemukan
        if (!found) {
            printf("Nomor barang tidak ditemukan.\n");
        }
} else if (uangPelanggan == 0) {
        // Pembelian dibatalkan, kembali ke display barang
        prosesMenuKasir(barang);
    } else {
        // Menampilkan rincian belanja yang diperbarui
        tampilkanRincianBelanja(barang, pembelian, jumlahBarang, *totalHarga);

        kembalian = uangPelanggan - *totalHarga;

        if (uangPelanggan == *totalHarga) {
            printf("Uang Anda pas\n");
        } else if (kembalian > 0) {
            printf("Pembayaran berhasil!\n");
            printf("Kembalian Anda: Rp. %.2f\n", kembalian);
        } else {
            // Meminta input lagi jika uang kurang
            while (uangPelanggan < *totalHarga) {
                printf("Uang Anda Kurang !!\n");
                printf("Silakan Masukkan Lagi Uang Anda : Rp. ");
                scanf("%f", &uangPelanggan);
            }
            // Pembayaran berhasil setelah input uang yang cukup
            printf("\nPembayaran berhasil!\n");
            printf("Kembalian Anda: Rp. %.2f\n", uangPelanggan - *totalHarga);
        }

        // Menanyakan apakah pengguna ingin berbelanja lagi atau tidak
        printf("\n      Terimakasih Telah Berbelanja\n");
        printf("Apakah Anda Ingin Berbelanja Lagi (Y/T): ");

        char respon;
        scanf(" %c", &respon);

        if (toupper(respon) == 'Y') {
            clear_screen();
            prosesMenuKasir(barang);
        }
    }
}

void prosesMenuKasir(struct Barang barang[]) {
    int jumlahBarang = 0;

    clear_screen();
    displayBarang(barang);
    printf("\nBerapa Jenis Barang yang ingin di Beli: ");
    scanf("%d", &jumlahBarang);

    if (jumlahBarang > 0) {
        struct Pembelian pembelian[jumlahBarang];
        float totalHarga = prosesPembelian(barang, pembelian, &jumlahBarang);

        if (totalHarga > 0) {
            tampilkanRincianBelanja(barang, pembelian, &jumlahBarang, totalHarga);

            // Panggil fungsi batalBeliAtauBayar di sini setelah menampilkan rincian belanja
            batalBeliAtauBayar(barang, pembelian, &jumlahBarang, &totalHarga);
        }
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

    while (1) {
        clear_screen();

        printf("\033[1;33m=============================================\n");
        printf("    Selamat Datang di Program TR Marchell     \n");
        printf("=============================================\033[0m\n");
        printf("Menu:\n");
        printf("1. \033[1;32mBangun Rumah kek di meinkrep\033[0m\n"); // Green color for option 1
        printf("2. \033[1;34mKasir kek di alp*mart\033[0m\n");    // Blue color for option 2
        printf("3. \033[1;31mKeluar udah bosen\033[0m\n");       // Red color for option 3
        printf("4. \033[1;35mSurat Terbuka untuk Asdos DDP B\033[0m\n"); // Magenta color for option 4

        printf("Pilih menu (1-4): ");
        scanf("%d", &menu);

        printf("Anda memilih menu %d. Sedang memproses...\n", menu);
        usleep(1000000);

        switch (menu) {
    case 1: {
        clear_screen();

        printf("****************************************\n");
        printf("*   Selamat Datang di Program Dekorasi *\n");
        printf("*     \033[1;32mBangun Rumah kek di meinkrep\033[0m     *\n");
        printf("****************************************\n");

        int size;
        char bentuk;

        printf("           Masukkan ukuran: ");
        scanf("%d", &size);
        while ((getchar()) != '\n');

        printf("           Masukkan bentuk: ");
        scanf(" %c", &bentuk);

        printf("****************************************\n");

        cerobong(size, bentuk);
        atap(size, bentuk);
        cetakDinding(size, bentuk, 1, 2);

        printf("****************************************\n");

        system("pause");
        break;
    }

            case 2:
                prosesMenuKasir(daftarBarang);
                break;

            case 3:
            clear_screen();

            // Escape sequences ANSI untuk warna teks
            printf("\033[1;32m"); // Warna hijau terang untuk garis atas dan bawah
            printf("+==================================================+\n");
            printf("\033[1;33m"); // Warna kuning terang untuk teks nama dan NIM
            printf("|        Programmed by Marchell Adi Pratama        |\n");
            printf("|                  NIM 672023081                   |\n");
            printf("\033[1;32m"); // Warna hijau terang untuk garis atas dan bawah
            printf("+==================================================+\n");
            printf("\033[0m");    // Mengembalikan warna ke default

            return 0;

    case 4:
        clear_screen();
        const char *red = "\033[1;31m";
        printf("%sKata-kata:\n", red);
        delay(500);

        const char *kataKata = "Tak terasa satu semester berlalu.\nTerima kasih kakak Asdos DDP B.\n\n\nAgar silaturahmi terus berjalan mulus, \nnilai dulu dong seratus. :D xixixi\n\n";

        for (int i = 0; kataKata[i] != '\0'; i++) {
            putchar(kataKata[i]);
            delay(50);
        }

            system("pause");
            break;
            default:
                printf("\nTidak Tersedia, Ulangi !!\n");
                system("pause");
        }
    }

    return 0;
}
