#include <stdio.h>

    int angka1, angka2, penjumlahan, perkalian, pembagian;

int main() {

    printf("Masukkan Angka Pertama : ");
    scanf("%d", &angka1);

    printf("Masukkan Angka Kedua : ");
    scanf("%d", &angka2);

    printf("\nHasil Penjumlahan = %d\n", angka1 + angka2);
    printf("Hasil Pengurangan = %d\n", angka1 - angka2);
    printf("Hasil Perkalian = %d\n", angka1 * angka2);
    printf("Hasil Pembagian = %d\n", angka1 / angka2);

    return 0;
}
