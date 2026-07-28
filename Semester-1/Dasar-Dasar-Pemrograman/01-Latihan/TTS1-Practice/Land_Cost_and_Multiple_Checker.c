#include <stdio.h>
#include <stdlib.h>

int pan, leb, har, kel, angka;
char pil;


int main() {
    printf("Menu Program\n");
    printf("1. Menghitung biaya harga tanah\n");
    printf("2. Menentukan Kelipatan\n");
    printf("Masukkan pilihan anda: (1-2) " );

    int pilih;
    scanf("%d", &pilih);

    if (pilih == 1){
        printf("\nProgram Menghitung Biaya Harga Tanah\n");
        printf("Masukkan data - data berikut\n");
            printf("Panjang Tanah (meter) : ");
                scanf("%d", &pan);
            printf("Lebar Tanah   (meter) : ");
                scanf("%d", &leb);
            printf("Harga Tanah           : Rp ");
                scanf("%d", &har);


            printf("\nKeliling Tanah : %d meter\n", 2*(pan+leb));
            printf("Luas Tanah     : %d meter persegi\n", pan*leb);
            printf("Harga Tanah    : %d Rp \n", pan*leb*har);
            printf("Apakah anda ingin membelinya? (y/t) ");

                scanf(" %c", &pil);

            if(pil == 'Y' || pil == 'y'){
                    printf("Anda memutuskan membeli tanah seluas %d meter persegi\n", pan*leb);
                    printf("Silakan menyiapkan uang sebesar Rp %d \nTERIMAKASIH", har);
            } else if(pil == 'T' || pil == 't'){
                    printf("Anda TIDAK jadi membeli tanah seluas %d meter persegi dengan harga Rp %d\nTERIMAKASIH", pan*leb, har);
            } else {
                printf("Pilihan tidak valid.\n");
                }
    }

    if (pilih == 2){
        printf("Maaf kak, yang ini aku ga bisa hehe\n");
        }



    return 0;
}
