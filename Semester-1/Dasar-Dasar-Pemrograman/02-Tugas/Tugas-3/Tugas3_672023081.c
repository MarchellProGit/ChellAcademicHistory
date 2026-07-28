#include <stdio.h>

int main() {
    printf("NAMA : Marchell Adi Pratama ||\n");
    printf("NIM  : 672023081            ||\n");
    printf("=============================\n\n");

    int n;

    printf("Masukkan jumlah angka: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Nilai min dan maks dari barisan tersebut berturut-turut adalah %d dan %d\n", n);
        return 0;
    }

    int data[n];

    for (int i = 0; i < n; ++i) {
        printf("Masukkan angka index ke-%d: ", i);
        scanf("%d", &data[i]);
    }

    int max = data[0];
    int min = data[0];

    for (int i = 1; i < n; ++i) {
        if (data[i] > max) {
            max = data[i];
        }
        if (data[i] < min) {
            min = data[i];
        }
    }
    printf("Nilai min dan maks dari barisan tersebut bertururut adalah %d dan %d\n", min, max);

    return 0;
}
