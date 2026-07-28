#include <stdio.h>
#include <stdlib.h>

int merah, hijau, merah_hijau;
char pilihan;

int main() {

    printf("NAMA : Marchell Adi Pratama ||\n");
    printf("NIM  : 672023081            ||\n");
    printf("=============================\n\n");

        printf("Program Menghitung Apel\n\n");
        printf("merah: 1, hijau: 2, merah hijau: 3\n");

        do {
        printf(" Masukkan warna apel: ");

        int input;
        scanf("%d", &input);

        switch (input) {
            case 1:
                merah++;
                break;
            case 2:
                hijau++;
                break;
            case 3:
                merah_hijau++;
                break;
            default:
                printf("Pilihan anda salah\n");
        }

        printf("Masukkan apel lagi? (y/n): ");
        scanf(" %c", &pilihan);

    } while (pilihan == 'y');

    printf("\nDETAIL JUMLAH APEL\n");
    printf("Apel Merah       : %d buah\n", merah);
    printf("Apel Hijau       : %d buah\n", hijau);
    printf("Apel Merah Hijau : %d buah\n", merah_hijau);

    return 0;
}
