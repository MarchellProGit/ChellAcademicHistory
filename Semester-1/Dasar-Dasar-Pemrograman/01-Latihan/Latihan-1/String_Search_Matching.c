#include <stdio.h>

int main() {
    // Target string yang ingin dibentuk
    char target[] = "Marchell";
    int target_length = sizeof(target) - 1;  // Panjang dari kata "Marchell"

    // Indeks untuk melacak posisi huruf dalam target
    int target_index = 0;

    // Perulangan karakter dari 'A' hingga 'Z' secara terus menerus
    for (char c = 'A'; ; c++) {
        // Reset karakter ke 'A' jika melebihi 'Z'
        if (c > 'Z') {
            c = 'A';
        }

        // Cek apakah karakter saat ini cocok dengan karakter target
        if (c == target[target_index]) {
            printf("%c", c);  // Cetak huruf yang sesuai
            target_index++;   // Pindah ke karakter berikutnya dalam target
        }

        // Jika semua karakter dari target telah ditemukan, hentikan loop
        if (target_index == target_length) {
            break;
        }
    }

    printf("\n");  // Baris baru setelah string selesai dicetak

    return 0;
}
