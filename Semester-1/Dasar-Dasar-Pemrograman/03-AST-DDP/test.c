
#include <stdio.h>

int main() {
    int NIP, Jam_Lembur, Pendapatan, Gaji_Kotor, Potongan, Gaji_Bersih, GA = 2000000, GB = 1500000, GC = 1000000, BA = 300000, BB = 200000, BC = 100000, BAA =150000, BBB = 100000, BCC = 50000;
    char Nama, Golongan;


    printf("Program Perhitungan Gaji Pegawai\n\n");

    printf("NIP: ");
    scanf("%d", &NIP);
    printf("Nama: ");
    scanf(" %[^\n]", &Nama);
    printf("Golongan: ");
    scanf(" %[^\n]", &Golongan);
    printf("Jam Lebur: ");
    scanf("%d", &Jam_Lembur);

if("A"){

        printf("a. Pendapatan: \n");
        printf(" Gaji Pokok : Rp. %d \n",GA);

            if(Jam_Lembur >= 10){
                printf("Bonus: Rp. %d \n", BA);
            }else if(Jam_Lembur <= 9){
                printf(" Bonus: Rp. %d \n", BAA);
            }
            printf(" Gaji Kotor  = Rp %d\n", GA+BA);

        printf("b. Potongan = Rp 24500");

}

if("B"){
        printf("a. Pendapatan: \n");
        printf(" Gaji Pokok : Rp. %d \n",GB);

            if(Jam_Lembur= 10){
                printf("Bonus: Rp. %d \n",BB);
            }else if(Jam_Lembur <= 9){
                printf(" Bonus: Rp. %d \n",BBB);
            }
            printf(" Gaji Kotor = Rp %d\n", GB+BB);
        printf("b. Potongan = Rp 15000");

}

if("C"){

        printf("a. Pendapatan: \n");
        printf(" Gaji Pokok : Rp. %d \n",GC);

            if(Jam_Lembur >= 10){
                printf("Bonus: Rp. %d \n",BC);
            }else if(Jam_Lembur <= 9){
                printf(" Bonus: Rp. %d \n", BCC);
            }
            printf(" Gaji Kotor = Rp %d \n",BCC+BC);

        printf("b. Potongan = Rp 11000");
}
    return 0;
}


