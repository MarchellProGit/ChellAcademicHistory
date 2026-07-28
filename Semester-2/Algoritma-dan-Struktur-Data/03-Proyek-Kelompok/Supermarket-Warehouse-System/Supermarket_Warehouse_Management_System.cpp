#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <iomanip>
#include <map>
#include <chrono>
#include <thread>

using namespace std;

#ifdef _WIN32
#include <windows.h>
#define CLEAR "cls"
#else
#define CLEAR "clear"
#endif

struct Barang {
    int ID;
    char bulan[20];
    char distributor[50];
    char namaBarang[50];
    float jumlah;
};

vector<Barang> gudang;

void clearScreen() {
    system(CLEAR);
}

void simpanData() {
    ofstream file("Kelompok 1_GudangSuperMarket_672023027_672023081_672023098_672023102.dat", ios::binary);
    if (!file) {
        cout << "\nGagal membuka file untuk menulis." << endl;
        return;
    }
    int jumlahBarang = gudang.size();
    file.write(reinterpret_cast<char*>(&jumlahBarang), sizeof(int));
    file.write(reinterpret_cast<char*>(gudang.data()), jumlahBarang * sizeof(Barang));
    file.close();
}

void muatData() {
    ifstream file("Kelompok 1_GudangSuperMarket_672023027_672023081_672023098_672023102.dat", ios::binary);
    if (!file) {
        cout << "\nTidak ada data yang ditemukan." << endl;
        return;
    }
    int jumlahBarang;
    file.read(reinterpret_cast<char*>(&jumlahBarang), sizeof(int));
    gudang.resize(jumlahBarang);
    file.read(reinterpret_cast<char*>(gudang.data()), jumlahBarang * sizeof(Barang));
    file.close();
}

void tambahData() {
    while (true) {
        if (gudang.size() >= 100) {
            cout << "\nGudang penuh!" << endl;
            return;
        }
        Barang barangBaru;
        barangBaru.ID = (gudang.empty()) ? 1 : gudang.back().ID + 1;

        cout << "\nMasukkan bulan: ";
        cin >> barangBaru.bulan;
        cin.ignore();
        cout << "Masukkan nama distributor: ";
        cin.getline(barangBaru.distributor, 50);
        cout << "Masukkan nama barang: ";
        cin.getline(barangBaru.namaBarang, 50);
        cout << "Masukkan jumlah (kg): ";
        cin >> barangBaru.jumlah;
        gudang.push_back(barangBaru);
        simpanData();

        char pilihan;
        cout << "Apakah Anda ingin menginput data lagi? (y/n): ";
        cin >> pilihan;
        if (pilihan != 'y' && pilihan != 'Y') {
            break;
        }
    }
}

void ubahData() {
    while (true) {
        int id;
        cout << "\nMasukkan ID barang yang akan diubah: ";
        cin >> id;

        bool ditemukan = false;
        for (auto &barang : gudang) {
            if (barang.ID == id) {
                cout << "Masukkan bulan baru: ";
                cin >> barang.bulan;
                cin.ignore();
                cout << "Masukkan nama distributor baru: ";
                cin.getline(barang.distributor, 50);
                cout << "Masukkan nama barang baru: ";
                cin.getline(barang.namaBarang, 50);
                cout << "Masukkan jumlah baru (kg): ";
                cin >> barang.jumlah;
                simpanData();
                ditemukan = true;
                break;
            }
        }
        if (!ditemukan) {
            cout << "\nBarang tidak ditemukan!" << endl;
        }

        char pilihan;
        cout << "Apakah Anda ingin mengubah data lagi? (y/n): ";
        cin >> pilihan;
        if (pilihan != 'y' && pilihan != 'Y') {
            break;
        }
    }
}

void tampilkanData() {
    if (gudang.empty()) {
        cout << "\nTidak ada data untuk ditampilkan." << endl;
        return;
    }

    cout << "======================================================================================" << endl;

    cout << "| " << setw(8) << "ID" << " | "
         << setw(13) << "Bulan" << " | "
         << setw(18) << "Distributor" << " | "
         << setw(18) << "Nama Barang" << " | "
         << setw(13) << "Jumlah (kg)" << " |" << endl;
    cout << "======================================================================================" << endl;

    for (const auto &barang : gudang) {
        cout << "| " << setw(8) << barang.ID
             << " | " << setw(13) << barang.bulan
             << " | " << setw(18) << barang.distributor
             << " | " << setw(18) << barang.namaBarang
             << " | " << setw(13) << barang.jumlah
             << " |" << endl;
    }

    cout << "======================================================================================" << endl;

    char pilihan;
    cout << "\nApakah Anda ingin kembali ke menu utama? (y/n): ";
    cin >> pilihan;
    if (pilihan != 'y' && pilihan != 'Y') {
        exit(0);
    }
}

void hitungRataRata() {
    if (gudang.empty()) {
        cout << "\nTidak ada data untuk dihitung rata-rata." << endl;
        return;
    }

    float totalJumlah = 0;
    for (const auto &barang : gudang) {
        totalJumlah += barang.jumlah;
    }
    float rataRataUniversal = totalJumlah / gudang.size();
    cout << "\nRata-rata jumlah barang (universal): " << rataRataUniversal << " kg" << endl;

    map<string, pair<float, int>> jumlahPerBulan;

    for (const auto &barang : gudang) {
        jumlahPerBulan[barang.bulan].first += barang.jumlah;
        jumlahPerBulan[barang.bulan].second += 1;
    }

    cout << "\nRata-rata jumlah barang per bulan:" << endl;
    for (const auto &entry : jumlahPerBulan) {
        float rataRataBulan = entry.second.first / entry.second.second;
        cout << "Bulan " << entry.first << ": " << rataRataBulan << " kg" << endl;
    }

    char pilihan;
    cout << "\nApakah Anda ingin kembali ke menu utama? (y/n): ";
    cin >> pilihan;
    if (pilihan != 'y' && pilihan != 'Y') {
        exit(0);
    }
}

void hapusSemuaData() {
    char konfirmasi;
    cout << "Apakah Anda yakin akan menghapus semua data? (y/n): ";
    cin >> konfirmasi;
    if (konfirmasi == 'y' || konfirmasi == 'Y') {
        gudang.clear();
        simpanData();
        cout << "Semua data telah dihapus." << endl;
    } else {
        cout << "Penghapusan data dibatalkan." << endl;
    }

    char pilihan;
    cout << "\nApakah Anda ingin kembali ke menu utama? (y/n): ";
    cin >> pilihan;
    if (pilihan != 'y' && pilihan != 'Y') {
        exit(0);
    }
}

int main() {
    muatData();
    int pilihan;

    do {
        clearScreen();
        cout << "\n\033[1;33m===========================================================\033[0m\n";
        cout << "\033[1;32m         Selamat Datang di Program TTS Kelompok 1        \033[0m\n";
        cout << "\033[1;34m       1. Klemens Imanuel Sancaka (672023027)            \033[0m\n";
        cout << "\033[1;35m       2. Marchell Adi Pratama (672023081)               \033[0m\n";
        cout << "\033[1;36m       3. Wahyu Aji Prasetyo (672023098)                 \033[0m\n";
        cout << "\033[1;31m       4. Rafael Paulus Ardhito Sihaloho (672023102)     \033[0m\n";
        cout << "\033[1;33m===========================================================\033[0m\n\n";

        cout << "\033[1;33m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m\n";
        cout << "\033[1;32mMenu Gudang Supermarket:\033[0m\n";
        cout << "1. Tambah Data\n";
        cout << "2. Ubah Data\n";
        cout << "3. Tampilkan Data\n";
        cout << "4. Hitung Rata-rata\n";
        cout << "5. Hapus Semua Data\n";
        cout << "6. Keluar\n";
        cout << "\033[1;33mPilihan: \033[0m";
        cin >> pilihan;
        cout << "\033[1;33m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m\n";

        switch (pilihan) {
            case 1:
                clearScreen();
                tambahData();
                break;
            case 2:
                clearScreen();
                ubahData();
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
            case 3:
                clearScreen();
                tampilkanData();
                std::this_thread::sleep_for(std::chrono::seconds(1));
                clearScreen();
                break;
            case 4:
                clearScreen();
                hitungRataRata();
                std::this_thread::sleep_for(std::chrono::seconds(1));
                clearScreen();
                break;
            case 5:
                clearScreen();
                hapusSemuaData();
                break;
            case 6:
                cout << "Keluar dari program." << endl;
                return 0;
            default:
                cout << "Pilihan tidak valid!" << endl;
                std::this_thread::sleep_for(std::chrono::seconds(1));
                break;
        }
    } while (true);

    return 0;
}
