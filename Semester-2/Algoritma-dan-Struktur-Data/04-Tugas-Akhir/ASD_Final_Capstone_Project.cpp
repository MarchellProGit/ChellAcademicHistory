//CATATAN: Program ini dibuat dengan menggunakan bahasa pemrograman C++ dan dapat dijalankan pada terminal Linux atau Command Prompt Windows.

#include <iostream>
#include <limits>
#include <cstdlib>
#include <cstring>

using namespace std;

struct Peminjaman {
    string pinjamID;
    string kodePeminjam;
    string namaPeminjam;
    string jenisPeminjam;
    string tanggalPinjam;
    string tanggalKembali;
    string namaBuku;
    int jumlah;
    Peminjaman* next;
};

struct Book {
    string kodeBuku;
    string judulBuku;
    int jumlahStok;
};

Peminjaman* head = nullptr;

Book rak1[] = {
    {"101", "Panduan Ilmu Pengetahuan Alam", 5},
    {"102", "Eksplorasi Luar Angkasa", 3},
    {"103", "Fisika untuk Pemula", 4},
    {"104", "Kimia Dasar", 6},
    {"105", "Biologi Modern", 2},
    {"106", "Matematika Terapan", 7},
    {"107", "Geologi dan Mineral", 3},
    {"108", "Astronomi untuk Anak-Anak", 5},
    {"109", "Ekologi dan Lingkungan", 4},
    {"110", "Robotika dan Kecerdasan Buatan", 6}
};

Book rak2[] = {
    {"201", "Sejarah Dunia Kuno", 4},
    {"202", "Revolusi Industri", 3},
    {"203", "Perang Dunia I", 5},
    {"204", "Perang Dunia II", 6},
    {"205", "Sejarah Asia", 4},
    {"206", "Dinasti-dinasti di Tiongkok", 2},
    {"207", "Peradaban Mesir Kuno", 3},
    {"208", "Sejarah Modern", 7},
    {"209", "Kerajaan Majapahit", 5},
    {"210", "Peradaban Romawi", 3}
};

Book rak3[] = {
    {"301", "Kumpulan Puisi", 6},
    {"302", "Novel Klasik Dunia", 5},
    {"303", "Drama dan Teater", 4},
    {"304", "Sastra Modern", 3},
    {"305", "Sastra Indonesia", 2},
    {"306", "Karya William Shakespeare", 7},
    {"307", "Antologi Cerpen", 3},
    {"308", "Fiksi Ilmiah", 5},
    {"309", "Fabel dan Legenda", 4},
    {"310", "Sastra Kontemporer", 6}
};

Book rak4[] = {
    {"401", "Pengantar Teknologi Informasi", 5},
    {"402", "Revolusi Digital", 3},
    {"403", "Teknologi Komputer", 6},
    {"404", "Dasar-Dasar Pemrograman", 4},
    {"405", "Jaringan Komputer", 5},
    {"406", "Teknologi Internet of Things", 2},
    {"407", "Sistem Operasi", 3},
    {"408", "Keamanan Siber", 7},
    {"409", "Teknologi Blockchain", 3},
    {"410", "Aplikasi Mobile", 4}
};

Book rak5[] = {
    {"501", "Panduan Hidup Sehat", 6},
    {"502", "Nutrisi dan Diet", 5},
    {"503", "Kesehatan Mental", 3},
    {"504", "Ilmu Kedokteran Dasar", 4},
    {"505", "Penyakit dan Pencegahannya", 2},
    {"506", "Olahraga dan Kebugaran", 5},
    {"507", "Meditasi dan Relaksasi", 3},
    {"508", "Kesehatan Anak", 7},
    {"509", "Gaya Hidup Sehat", 3},
    {"510", "Perawatan Kulit dan Kecantikan", 6}
};

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void pause() {
    cout << "Tekan Enter untuk melanjutkan...";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cin.get();
}

void tambahData() {
    char lanjut;
    do {
        clearScreen();
        cout << "\033[1;36m=======================================================\033[0m\n";
        cout << "\033[1;36m=                   Program Tambah Data               =\033[0m\n";
        cout << "\033[1;36m=======================================================\033[0m\n\n";
        Peminjaman* baru = new Peminjaman();

        do {
            cout << "Masukkan PinjamID (teks-3): ";
            cin >> baru->pinjamID;
            if (baru->pinjamID.length() != 3) {
                cout << "PinjamID harus berupa teks 3 karakter.\n";
            }
        } while (baru->pinjamID.length() != 3);

        do {
            cout << "Masukkan KodePeminjam (teks-3): ";
            cin >> baru->kodePeminjam;
            if (baru->kodePeminjam.length() != 3) {
                cout << "KodePeminjam harus berupa teks 3 karakter.\n";
            }
        } while (baru->kodePeminjam.length() != 3);

        do {
            cout << "Masukkan NamaPeminjam (teks-255): ";
            cin.ignore();
            getline(cin, baru->namaPeminjam);
            if (baru->namaPeminjam.length() > 255) {
                cout << "NamaPeminjam tidak boleh lebih dari 255 karakter.\n";
            }
        } while (baru->namaPeminjam.length() > 255);

        do {
            cout << "Masukkan JenisPeminjam (Mahasiswa/Dosen/Umum): ";
            getline(cin, baru->jenisPeminjam);
            if (baru->jenisPeminjam != "Mahasiswa" && baru->jenisPeminjam != "Dosen" && baru->jenisPeminjam != "Umum") {
                cout << "JenisPeminjam harus berupa Mahasiswa, Dosen, atau Umum.\n";
            }
        } while (baru->jenisPeminjam != "Mahasiswa" && baru->jenisPeminjam != "Dosen" && baru->jenisPeminjam != "Umum");

        do {
            cout << "Masukkan TanggalPinjam (teks-10, format YYYY-MM-DD): ";
            cin >> baru->tanggalPinjam;
            if (baru->tanggalPinjam.length() != 10) {
                cout << "TanggalPinjam harus berupa teks 10 karakter dengan format YYYY-MM-DD.\n";
            }
        } while (baru->tanggalPinjam.length() != 10);

        do {
            cout << "Masukkan TanggalKembali (teks-10, format YYYY-MM-DD): ";
            cin >> baru->tanggalKembali;
            if (baru->tanggalKembali.length() != 10) {
                cout << "TanggalKembali harus berupa teks 10 karakter dengan format YYYY-MM-DD.\n";
            }
        } while (baru->tanggalKembali.length() != 10);

        do {
            cout << "Masukkan NamaBuku (teks-255): ";
            cin.ignore();
            getline(cin, baru->namaBuku);
            if (baru->namaBuku.length() > 255) {
                cout << "NamaBuku tidak boleh lebih dari 255 karakter.\n";
            }
        } while (baru->namaBuku.length() > 255);

        do {
            cout << "Masukkan Jumlah (integer): ";
            cin >> baru->jumlah;
            if (cin.fail() || baru->jumlah <= 0) {
                cout << "Jumlah harus berupa bilangan bulat positif.\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
            }
        } while (baru->jumlah <= 0);

        if (head == nullptr) {
            head = baru;
            head->next = head;
        } else {
            Peminjaman* temp = head;
            while (temp->next != head) {
                temp = temp->next;
            }
            temp->next = baru;
            baru->next = head;
        }

        cout << "Data berhasil ditambahkan.\n";
        cout << "Apakah Anda ingin menambah data lagi? (y/n): ";
        cin >> lanjut;
    } while (lanjut == 'y' || lanjut == 'Y');
}

void cariData() {
    int pilihan;
    cout << "Pilih opsi pencarian:\n";
    cout << "1. Cari Buku\n";
    cout << "2. Cari Data Peminjam\n";
    cout << "Masukkan pilihan (1/2): ";
    cin >> pilihan;

    if (pilihan == 1) {
        string kodeBuku;
        clearScreen();
        cout << "=======================================================\n";
        cout << "=                   Program Cari Buku                 =\n";
        cout << "=======================================================\n\n";
        cout << "Masukkan Kode Buku yang akan dicari: ";
        cin >> kodeBuku;

        bool found = false;

        for (const auto& buku : rak1) {
            if (buku.kodeBuku == kodeBuku) {
                cout << "Buku ditemukan di rak 1:\n";
                cout << "Kode Buku: " << buku.kodeBuku << "\n";
                cout << "Judul Buku: " << buku.judulBuku << "\n";
                cout << "Jumlah Stok: " << buku.jumlahStok << "\n";
                found = true;
                break;
            }
        }

        if (!found) {
            for (const auto& buku : rak2) {
                if (buku.kodeBuku == kodeBuku) {
                    cout << "Buku ditemukan di rak 2:\n";
                    cout << "Kode Buku: " << buku.kodeBuku << "\n";
                    cout << "Judul Buku: " << buku.judulBuku << "\n";
                    cout << "Jumlah Stok: " << buku.jumlahStok << "\n";
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            for (const auto& buku : rak3) {
                if (buku.kodeBuku == kodeBuku) {
                    cout << "Buku ditemukan di rak 3:\n";
                    cout << "Kode Buku: " << buku.kodeBuku << "\n";
                    cout << "Judul Buku: " << buku.judulBuku << "\n";
                    cout << "Jumlah Stok: " << buku.jumlahStok << "\n";
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            for (const auto& buku : rak4) {
                if (buku.kodeBuku == kodeBuku) {
                    cout << "Buku ditemukan di rak 4:\n";
                    cout << "Kode Buku: " << buku.kodeBuku << "\n";
                    cout << "Judul Buku: " << buku.judulBuku << "\n";
                    cout << "Jumlah Stok: " << buku.jumlahStok << "\n";
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            for (const auto& buku : rak5) {
                if (buku.kodeBuku == kodeBuku) {
                    cout << "Buku ditemukan di rak 5:\n";
                    cout << "Kode Buku: " << buku.kodeBuku << "\n";
                    cout << "Judul Buku: " << buku.judulBuku << "\n";
                    cout << "Jumlah Stok: " << buku.jumlahStok << "\n";
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            cout << "Buku dengan Kode tersebut tidak ditemukan.\n";
        }

    } else if (pilihan == 2) {
        clearScreen();
        cout << "=======================================================\n";
        cout << "=                 Program Cari Peminjam               =\n";
        cout << "=======================================================\n\n";

        if (head == nullptr) {
            cout << "Belum ada data.\n";
            pause();
            return;
        }

        string peminjamID;
        cout << "Masukkan ID Peminjam yang akan dicari: ";
        cin >> peminjamID;

        Peminjaman* temp = head;
        bool found = false;
        do {
            if (temp->kodePeminjam == peminjamID) {
                cout << "Data peminjam ditemukan:\n";
                cout << "PinjamID: " << temp->pinjamID << "\n";
                cout << "KodePeminjam: " << temp->kodePeminjam << "\n";
                cout << "NamaPeminjam: " << temp->namaPeminjam << "\n";
                cout << "JenisPeminjam: " << temp->jenisPeminjam << "\n";
                cout << "TanggalPinjam: " << temp->tanggalPinjam << "\n";
                cout << "TanggalKembali: " << temp->tanggalKembali << "\n";
                cout << "NamaBuku: " << temp->namaBuku << "\n";
                cout << "Jumlah: " << temp->jumlah << "\n";
                found = true;
                break;
            }
            temp = temp->next;
        } while (temp != head);

        if (!found) {
            cout << "Data peminjam dengan ID tersebut tidak ditemukan.\n";
        }

    } else {
        cout << "Pilihan tidak valid.\n";
    }

    pause();
}

void ubahData() {
    char lanjut;
    do {
        if (head == nullptr) {
            cout << "Belum ada data.\n";
            pause();
            return;
        }

        string id;
        cout << "Masukkan PinjamID yang akan diubah: ";
        cin >> id;

        Peminjaman* temp = head;
        do {
            if (temp->pinjamID == id) {
                cout << "Data ditemukan, masukkan data baru:\n";

                do {
                    cout << "Masukkan KodePeminjam (teks-3): ";
                    cin >> temp->kodePeminjam;
                    if (temp->kodePeminjam.length() != 3) {
                        cout << "KodePeminjam harus berupa teks 3 karakter.\n";
                    }
                } while (temp->kodePeminjam.length() != 3);

                do {
                    cout << "Masukkan NamaPeminjam (teks-255): ";
                    cin.ignore();
                    getline(cin, temp->namaPeminjam);
                    if (temp->namaPeminjam.length() > 255) {
                        cout << "NamaPeminjam tidak boleh lebih dari 255 karakter.\n";
                    }
                } while (temp->namaPeminjam.length() > 255);

                do {
                    cout << "Masukkan JenisPeminjam (Mahasiswa/Dosen/Umum): ";
                    getline(cin, temp->jenisPeminjam);
                    if (temp->jenisPeminjam != "Mahasiswa" && temp->jenisPeminjam != "Dosen" && temp->jenisPeminjam != "Umum") {
                        cout << "JenisPeminjam harus berupa Mahasiswa, Dosen, atau Umum.\n";
                    }
                } while (temp->jenisPeminjam != "Mahasiswa" && temp->jenisPeminjam != "Dosen" && temp->jenisPeminjam != "Umum");

                do {
                    cout << "Masukkan TanggalPinjam (teks-10, format YYYY-MM-DD): ";
                    cin >> temp->tanggalPinjam;
                    if (temp->tanggalPinjam.length() != 10) {
                        cout << "TanggalPinjam harus berupa teks 10 karakter dengan format YYYY-MM-DD.\n";
                    }
                } while (temp->tanggalPinjam.length() != 10);

                do {
                    cout << "Masukkan TanggalKembali (teks-10, format YYYY-MM-DD): ";
                    cin >> temp->tanggalKembali;
                    if (temp->tanggalKembali.length() != 10) {
                        cout << "TanggalKembali harus berupa teks 10 karakter dengan format YYYY-MM-DD.\n";
                    }
                } while (temp->tanggalKembali.length() != 10);

                do {
                    cout << "Masukkan NamaBuku (teks-255): ";
                    cin.ignore();
                    getline(cin, temp->namaBuku);
                    if (temp->namaBuku.length() == 0 || temp->namaBuku.length() > 255) {
                        cout << "NamaBuku tidak boleh kosong atau lebih dari 255 karakter.\n";
                    }
                } while (temp->namaBuku.length() == 0 || temp->namaBuku.length() > 255);

                do {
                    cout << "Masukkan Jumlah (integer positif): ";
                    cin >> temp->jumlah;
                    if (cin.fail() || temp->jumlah <= 0) {
                        cout << "Jumlah harus berupa bilangan bulat positif.\n";
                        cin.clear();
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    }
                } while (temp->jumlah <= 0);

                cout << "Data berhasil diubah.\n";
                pause();
                return;
            }
            temp = temp->next;
        } while (temp != head);

        if (temp == head && temp->pinjamID != id) {
            cout << "Data dengan PinjamID tersebut tidak ditemukan.\n";
            cout << "Apakah Anda ingin mencoba lagi? (y/n): ";
            cin >> lanjut;
        }
    } while (lanjut == 'y' || lanjut == 'Y');
}

void hapusData() {
    char lanjut;
    do {
        if (head == nullptr) {
            cout << "Belum ada data.\n";
            pause();
            return;
        }

        string id;
        cout << "Masukkan PinjamID yang akan dihapus: ";
        cin >> id;

        Peminjaman* temp = head;
        Peminjaman* prev = nullptr;
        bool found = false;

        do {
            if (temp->pinjamID == id) {
                found = true;
                break;
            }
            prev = temp;
            temp = temp->next;
        } while (temp != head);

        if (found) {
            if (temp == head && temp->next == head) {
                head = nullptr;
            } else if (temp == head) {
                Peminjaman* tail = head;
                while (tail->next != head) {
                    tail = tail->next;
                }
                head = head->next;
                tail->next = head;
            } else {
                prev->next = temp->next;
            }
            delete temp;
            cout << "Data berhasil dihapus.\n";
        } else {
            cout << "Data dengan PinjamID tersebut tidak ditemukan.\n";
        }

        cout << "\nApakah Anda ingin menghapus data lain? (y/n): ";
        cin >> lanjut;
    } while (lanjut == 'y' || lanjut == 'Y');
}

void cetakSemuaData() {
    if (head == nullptr) {
        cout << "Belum ada data untuk dicetak.\n";
        pause();
        return;
    }

    Peminjaman* temp = head;
    do {
        cout << "=======================================================\n";
        cout << "PinjamID: " << temp->pinjamID << "\n";
        cout << "KodePeminjam: " << temp->kodePeminjam << "\n";
        cout << "NamaPeminjam: " << temp->namaPeminjam << "\n";
        cout << "JenisPeminjam: " << temp->jenisPeminjam << "\n";
        cout << "TanggalPinjam: " << temp->tanggalPinjam << "\n";
        cout << "TanggalKembali: " << temp->tanggalKembali << "\n";
        cout << "NamaBuku: " << temp->namaBuku << "\n";
        cout << "Jumlah: " << temp->jumlah << "\n";
        cout << "=======================================================\n\n";
        temp = temp->next;
    } while (temp != head);

    pause();
}

void tampilkanRakBuku(Book rak[], int size) {
    clearScreen();
    cout << "Daftar Buku pada Rak:\n";
    cout << "=======================================================\n";
    for (int i = 0; i < size; ++i) {
        cout << "Kode Buku: " << rak[i].kodeBuku << "\n";
        cout << "Judul Buku: " << rak[i].judulBuku << "\n";
        cout << "Jumlah Stok: " << rak[i].jumlahStok << "\n";
        cout << "-------------------------------------------------------\n";
    }
    cout << "=======================================================\n";
    pause();
}

int main() {
    int pilihan;
    do {
        clearScreen();
        cout << "\033[1;36m+================================================+\033[0m\n";
        cout << "\033[1;36m+            SISTEM MANAJEMEN PEMINJAMAN         +\033[0m\n";
        cout << "\033[1;36m+================================================+\033[0m\n";
        cout << "\033[1;36m+                                                +\033[0m\n";
        cout << "\033[1;36m+  1. Tambah Data Peminjaman                     +\033[0m\n";
        cout << "\033[1;36m+  2. Cari Data                                  +\033[0m\n";
        cout << "\033[1;36m+  3. Ubah Data Peminjaman                       +\033[0m\n";
        cout << "\033[1;36m+  4. Hapus Data Peminjaman                      +\033[0m\n";
        cout << "\033[1;36m+  5. Cetak Semua Data Peminjaman                +\033[0m\n";
        cout << "\033[1;36m+  6. Rak Buku                                   +\033[0m\n";
        cout << "\033[1;36m+  7. Keluar                                     +\033[0m\n";
        cout << "\033[1;36m+                                                +\033[0m\n";
        cout << "\033[1;36m+================================================+\033[0m\n";
        cout << "\033[1;36m+  Pilihan (1-7):                                +\033[0m\n";
        cout << "\033[1;36m+================================================+\033[0m\n";
        cout << "Pilihan Anda: ";
        cin >> pilihan;

        switch (pilihan) {
            case 1:
                clearScreen();
                tambahData();
                break;
            case 2:
                clearScreen();
                cout << "\033[1;36m=======================================================\033[0m\n";
                cout << "\033[1;36m=                   Program Cari Data                 =\033[0m\n";
                cout << "\033[1;36m=======================================================\033[0m\n\n";
                cariData();
                break;
            case 3:
                clearScreen();
                cout << "\033[1;36m=======================================================\033[0m\n";
                cout << "\033[1;36m=                   Program Ubah Data                 =\033[0m\n";
                cout << "\033[1;36m=======================================================\033[0m\n\n";
                ubahData();
                break;
            case 4:
                clearScreen();
                cout << "\033[1;36m=======================================================\033[0m\n";
                cout << "\033[1;36m=                   Program Hapus Data                =\033[0m\n";
                cout << "\033[1;36m=======================================================\033[0m\n\n";
                hapusData();
                break;
            case 5:
                clearScreen();
                cout << "\033[1;36m=======================================================\033[0m\n";
                cout << "\033[1;36m=                   Program Cetak Data                =\033[0m\n";
                cout << "\033[1;36m=======================================================\033[0m\n\n";
                cetakSemuaData();
                break;
            case 6:
                int rakPilihan;
                clearScreen();
                cout << "=======================================================\n";
                cout << "=                       Rak Buku                      =\n";
                cout << "=======================================================\n";
                cout << "=  Pilih Rak Buku yang ingin dilihat:                 =\n";
                cout << "=  1. Rak 1: Buku Pengetahuan                         =\n";
                cout << "=  2. Rak 2: Buku Sejarah                             =\n";
                cout << "=  3. Rak 3: Buku Sastra                              =\n";
                cout << "=  4. Rak 4: Buku Teknologi                           =\n";
                cout << "=  5. Rak 5: Buku Kesehatan                           =\n";
                cout << "=======================================================\n";
                cout << "=  Pilihan Rak (1-5)                                  =\n";
                cout << "=======================================================\n";
                cout << " Rak yang anda pilih: ";
                cin >> rakPilihan;

                switch (rakPilihan) {
                    case 1:
                        tampilkanRakBuku(rak1, sizeof(rak1) / sizeof(rak1[0]));
                        break;
                    case 2:
                        tampilkanRakBuku(rak2, sizeof(rak2) / sizeof(rak2[0]));
                        break;
                    case 3:
                        tampilkanRakBuku(rak3, sizeof(rak3) / sizeof(rak3[0]));
                        break;
                    case 4:
                        tampilkanRakBuku(rak4, sizeof(rak4) / sizeof(rak4[0]));
                        break;
                    case 5:
                        tampilkanRakBuku(rak5, sizeof(rak5) / sizeof(rak5[0]));
                        break;
                    default:
                        cout << "Pilihan tidak valid.\n";
                        pause();
                }
                break;
            case 7:
                clearScreen();
                cout << "\033[1;36m+------------------------------------------------+\033[0m\n";
                cout << "\033[1;36m+           Programmed by Kelompok 7:            +\033[0m\n";
                cout << "\033[1;36m+  1. Klemens Imanuel Sancaka (672023027)        +\033[0m\n";
                cout << "\033[1;36m+  2. Marchell Adi Pratama (672023081)           +\033[0m\n";
                cout << "\033[1;36m+  3. Wahyu Aji Prasetyo (672023098)             +\033[0m\n";
                cout << "\033[1;36m+  4. Rafael Paulus Ardhito Sihaloho (672023102) +\033[0m\n";
                cout << "\033[1;36m+------------------------------------------------+\033[0m\n";
                break;
            default:
                cout << "Pilihan tidak valid. Silakan pilih antara 1-7.\n";
                pause();
        }
    } while (pilihan != 7);

    return 0;
}
