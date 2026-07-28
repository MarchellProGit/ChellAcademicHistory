#include <stdio.h>
#include <string.h>

int main() {
    char input[20], pilihan;
    int merah = 0, hijau = 0, merah_hijau = 0;

    printf("NAMA : Marchell Adi Pratama\n");
    printf("NIM : 672023081\n\n");
    printf("Program Menghitung Apel\n\n");

    do {
        printf("Masukkan warna apel (merah, hijau, merah hijau): ");
        fgets(input, sizeof(input), stdin);

        if (strcmp(input, "merah\n") == 0) {
            merah++;
        } else if (strcmp(input, "hijau\n") == 0) {
            hijau++;
        } else if (strcmp(input, "merah hijau\n") == 0) {
            merah_hijau++;
        } else {
            printf("Pilihan anda salah\n");
        }

        printf("Masukkan apel lagi? (y/n): ");
        scanf(" %c", &pilihan);
        getchar();

    } while (pilihan == 'y' || pilihan == 'Y');

    printf("\n");

    printf("DETAIL JUMLAH APEL\n");
    printf("Apel Merah: %d buah\n", merah);
    printf("Apel Hijau: %d buah\n", hijau);
    printf("Apel Merah Hijau: %d buah\n", merah_hijau);

    return 0;
}
