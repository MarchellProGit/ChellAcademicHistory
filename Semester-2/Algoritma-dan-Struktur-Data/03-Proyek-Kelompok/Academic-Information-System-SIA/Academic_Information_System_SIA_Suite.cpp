#include <iostream> // cout, cin
#include <string> // getline
#include <vector> // vector
#include <fstream> // ofstream
#include <algorithm> // find, find_if, sort
#include <conio.h> // getch
#include <thread> // std::this_thread::sleep_for
#include <chrono> // std::chrono::milliseconds
#include <windows.h> // _getch
#include <iomanip> // std::setw
#include <limits> // std::numeric_limits

using namespace std; // Menghindari penulisan std:: sebelum fungsi atau kelas standar C++

#define BLUE "\033[1;36m" // Warna biru untuk teks
#define RESET "\033[0m" // Reset warna teks
#define RED "\033[1;31m" // Warna merah untuk teks
#define GREEN "\033[32m" // Warna hijau untuk teks

// Fungsi untuk membersihkan layar (tidak ditampilkan di kode yang Anda berikan)
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Struktur data untuk mata kuliah
struct MataKuliah {
    string kode;
    string nama;
    int sks;
    string dosen;
    int ruangan;
    string hari;
    string jam;
};

// Fungsi untuk membandingkan jadwal mata kuliah
bool bandingkanJadwal(const MataKuliah& a, const MataKuliah& b) {

    // Konversi hari ke indeks
    vector<string> urutanHari = {"Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"}; // Urutan hari
    auto itA = find(urutanHari.begin(), urutanHari.end(), a.hari); // Cari hari a
    auto itB = find(urutanHari.begin(), urutanHari.end(), b.hari); // Cari hari b

    // Bandingkan berdasarkan urutan hari
    if (itA != urutanHari.end() && itB != urutanHari.end()) { // Jika hari ditemukan
        if (distance(urutanHari.begin(), itA) != distance(urutanHari.begin(), itB)) { // Jika hari berbeda
            return distance(urutanHari.begin(), itA) < distance(urutanHari.begin(), itB); // Bandingkan berdasarkan indeks
        } else {
            // Jika hari sama, bandingkan berdasarkan jam
            return a.jam < b.jam; // Bandingkan jam
        }
    }
    // Fallback jika ada kesalahan
    return false; // Tidak ada perubahan
}

// Data mata kuliah
vector<MataKuliah> daftarMataKuliah = {
    {"TC504F", "Sistem Basis Data", 2, "Felix David", 465, "Senin", "13 - 15"},
    {"TC534G", "Algoritma dan Struktur Data", 2, "Felix David", 308, "Selasa", "13 - 15"},
    {"TC503C", "Dasar-Dasar Pemrograman", 2, "Ramos Somya", 306, "Selasa", "09 - 11"},
    {"TC533B", "Jaringan Komputer", 2, "Dian Widyanto", 300, "Rabu", "10 - 12"},
    {"TC512H", "Pengantar Teknologi Informasi", 2, "Fajar Ningsih", 312, "Kamis", "09 - 11"},
    {"TC532K", "Statistika dan Propabilitas", 2, "Natalia Bayu", 456, "Kamis", "15 - 17"},
    {"TC535F", "Interaksi Manusia dan Komputer", 2, "Suryahadi", 467, "Kamis", "07 - 09"}
};

// Struktur untuk user
struct User {
    string nim;
    string namaLengkap;
    string fakultas;
    string programStudi;
    double totalTagihanAwal;
    string waliStudi;
    string password;
    bool isRegistered;
    int statusRegistrasi; // 1: Kuliah, 2: Cuti
    int sks;
    vector<MataKuliah> mataKuliahDiambil;
    double terbayar;

};

// Data mahasiswa
vector<User> users; // Vektor untuk menyimpan data mahasiswa

// Fungsi untuk menyembunyikan password saat mengetik
string inputPassword() {
    string password;
    char ch;
    ch = _getch();
    while (ch != 13) { // 13 adalah kode ASCII untuk Enter
        if (ch == 8) { // 8 adalah kode ASCII untuk Backspace
            if (!password.empty()) { // Jika password tidak kosong
                password.pop_back(); // Menghapus karakter terakhir dari password
                cout << "\b \b"; // Menghapus karakter sebelumnya dari tampilan konsol
            }
        } else {
            password.push_back(ch); // Menambahkan karakter ke password
            cout << ' '; // Menampilkan karakter '' sebagai ganti karakter asli
        }
        ch = _getch(); // Membaca karakter berikutnya
    }
    cout << endl; // Pindah baris
    return password; // Mengembalikan password yang sudah dimasukkan
}

void signUp() {
    clearScreen(); // Membersihkan layar konsol
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan judul "Sign Up" dengan warna biru
    cout << BLUE << "                Sign Up                 " << RESET << endl; // Menampilkan judul "Sign Up" dengan warna biru
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan judul "Sign Up" dengan warna biru
    User newUser; // Membuat objek User baru
    cout << "Nama Lengkap   : "; // Menampilkan teks "Nama Lengkap   : "
    getline(cin, newUser.namaLengkap); // Membaca inputan nama lengkap dari pengguna
    cout << "Fakultas       : "; // Menampilkan teks "Fakultas       : "
    getline(cin, newUser.fakultas); // Membaca inputan fakultas dari pengguna
    cout << "Program Studi  : "; // Menampilkan teks "Program Studi  : "
    getline(cin, newUser.programStudi); // Membaca inputan program studi dari pengguna
    cout << "Wali Studi     : "; // Menampilkan teks "Wali Studi     : "
    getline(cin, newUser.waliStudi); // Membaca inputan wali studi dari pengguna
    cout << "NIM            : "; // Menampilkan teks "NIM            : "
    getline(cin, newUser.nim); // Membaca inputan NIM dari pengguna
    cout << "Password       : "; // Menampilkan teks "Password       : "
    newUser.password = inputPassword(); // Memanggil fungsi inputPassword() untuk membaca dan menyimpan password dari pengguna
    newUser.isRegistered = false; // Mengeset isRegistered menjadi false
    newUser.statusRegistrasi = 0; // Mengeset statusRegistrasi menjadi 0
    newUser.sks = 0; // Mengeset sks menjadi 0
    newUser.terbayar = 0.0; // Mengeset terbayar menjadi 0.0
    users.push_back(newUser); // Menambahkan newUser ke dalam vektor users

    ofstream outFile("users.txt", ios::app); // Membuka file users.txt dengan mode append
    if (outFile.is_open()) { // Jika file berhasil dibuka
        outFile << newUser.namaLengkap << "," << newUser.fakultas << "," << newUser.programStudi << "," // Menulis data newUser ke dalam file
                << newUser.waliStudi << "," << newUser.nim << "," << newUser.password << endl; // Menulis data newUser ke dalam file
        outFile.close(); // Menutup file
    }
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << GREEN << "Sign Up berhasil!" << RESET; // Menampilkan pesan "Sign Up berhasil!" dengan warna hijau
}

// Fungsi untuk menampilkan animasi loading
void showLoadingAnimation() {
    const int loadingDuration = 5; // Durasi dalam detik
    const int loadingWidth = 50; // Lebar loading bar
    const int interval = loadingDuration * 1000 / loadingWidth; // Interval dalam milidetik

    cout << "["; // Menampilkan karakter '[' sebagai awal loading bar
    for (int i = 0; i < loadingWidth; ++i) { // Melakukan iterasi sebanyak lebar loading bar
        cout << "#"; // Menampilkan karakter '#' sebagai bagian dari loading bar
        cout.flush(); // Memastikan output ditampilkan segera
        this_thread::sleep_for(chrono::milliseconds(interval)); // Menunda eksekusi selama interval yang ditentukan
    }
    cout << "]" << endl; // Menampilkan karakter ']' sebagai akhir loading bar dan pindah baris
}

User* login() {
    clearScreen(); // Membersihkan layar konsol
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan judul "Login" dengan warna biru
    cout << BLUE << "                 Login                  " << RESET << endl; // Menampilkan judul "Login" dengan warna biru
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan judul "Login" dengan warna biru
    string nim, password;
    cout << "NIM        : "; // Menampilkan teks "NIM        : "
    getline(cin, nim); // Membaca inputan NIM dari pengguna
    cout << "Password   : "; // Menampilkan teks "Password   : "
    password = inputPassword(); // Memanggil fungsi inputPassword() untuk membaca dan menyimpan password dari pengguna

   // showLoadingAnimation();

    for (auto& user : users) { // Melakukan iterasi pada vektor users
        if (user.nim == nim && user.password == password) { // Jika NIM dan password cocok dengan data user
            cout << GREEN << "Login berhasil!" << RESET << endl; // Menampilkan pesan "Login berhasil!" dengan warna hijau
            return &user; // Mengembalikan pointer ke user yang berhasil login
        }
    }
    cout << BLUE << "========================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << RED << "NIM atau Password salah!" << RESET << endl; // Menampilkan pesan "NIM atau Password salah!" dengan warna merah
    return nullptr; // Mengembalikan nullptr jika login gagal
}

// Fungsi untuk memberikan kritik dan saran kepada asisten dosen
void kritikSaranAsdos() {
    clearScreen(); // Membersihkan layar konsol
    cout << BLUE << "Kritik dan Saran Asdos" << RESET << endl; // Menampilkan judul "Kritik dan Saran Asdos" dengan warna biru
    const char* kritik = "Kritik: \nSaat kelas, penjelasan dari asdos singkat, padat, dan kurang jelas (sepertinya mereka saja yang menganggap begitu), \nkita mah ga usah dijelasin udah paham soalnya bapak kita Elon Musk (bapaknya Dito), Steve Jobs (bapaknya Aji), Mark Zuckerberg (bapaknya Klemens), Yesus (bapaknya Marchell)."; // Menyimpan kritik dalam bentuk string
    const char* saran = "\n\nSaran: \nBerikan penjelasan yang mendalam terkait materi yang disampaikan, \nmungkin dapat disertai dengan contoh yang relevan dengan materi untuk memastikan semua mahasiswa mengerti dengan materi yang disampaikan. Menurut mereka, itu akan membantu. \nKalau saran dari kita mah, mending kasih kita A. Udah sih gitu aja. \nSekian, Tuhan Yesus memberkati."; // Menyimpan saran dalam bentuk string

    putchar('\n'); // Menampilkan karakter newline
    putchar('\n'); // Menampilkan karakter newline
    for (int i = 0; kritik[i] != '\0'; i++) { // Melakukan perulangan sebanyak karakter dalam kritik
        cout << kritik[i] << flush; // Menampilkan karakter kritik satu per satu dengan menghapus buffer
         this_thread::sleep_for(chrono::milliseconds(50)); // Menunda eksekusi selama 50 milidetik
    }
    putchar('\n'); // Menampilkan karakter newline
    for (int i = 0; saran[i] != '\0'; i++) { // Melakukan perulangan sebanyak karakter dalam saran
        cout << saran[i] << flush; // Menampilkan karakter saran satu per satu dengan menghapus buffer
        this_thread::sleep_for(chrono::milliseconds(50)); // Menunda eksekusi selama 50 milidetik
    }
}

void displayBiodata(User* user) {
    clearScreen(); // Membersihkan layar
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << BLUE << "                       Biodata                       " << RESET << endl; // Menampilkan judul "Biodata" dengan warna biru
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << "NIM                : " << user->nim << endl; // Menampilkan NIM dari user
    cout << "Nama Lengkap       : " << user->namaLengkap << endl; // Menampilkan nama lengkap dari user
    cout << "Universitas        : Universitas Kristen Satya Wacana" << endl; // Menampilkan nama universitas
    cout << "Fakultas           : " << user->fakultas << endl; // Menampilkan fakultas dari user
    cout << "Program Studi      : " << user->programStudi << endl; // Menampilkan program studi dari user
    cout << "Status Registrasi  : " << (user->statusRegistrasi == 1 ? "Kuliah" : (user->statusRegistrasi == 0 ? "-" : "Cuti")) << endl; // Menampilkan status registrasi berdasarkan kondisi
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
}

void displayKTM(User* user) {
    clearScreen(); // Membersihkan layar
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << BLUE << "                 Kartu Tanda Mahasiswa               " << RESET << endl; // Menampilkan judul "Kartu Tanda Mahasiswa" dengan warna biru
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
    cout << "NIM            : " << user->nim << endl; // Menampilkan NIM dari user
    cout << "Nama Lengkap   : " << user->namaLengkap << endl; // Menampilkan nama lengkap dari user
    cout << "Universitas    : Universitas Kristen Satya Wacana" << endl; // Menampilkan nama universitas
    cout << "Fakultas       : " << user->fakultas << endl; // Menampilkan fakultas dari user
    cout << "Program Studi  : " << user->programStudi << endl; // Menampilkan program studi dari user
    cout << BLUE << "=====================================================" << RESET << endl; // Menampilkan garis pembatas dengan warna biru
}

void registrasiMatakuliah(User* user) {
    clearScreen(); // Membersihkan layar

    cout << BLUE << "===================================================" << RESET << endl;
    cout << BLUE << "               Registrasi Matakuliah               " << RESET << endl;
    cout << BLUE << "===================================================" << RESET << endl;

    cout << " 1. Kuliah: dan menghabiskan uang ortu" << endl; // Opsi 1 untuk registrasi kuliah
    cout << " 2. Cuti: sama aja tapi lebih dikit" << endl; // Opsi 2 untuk registrasi cuti

    cout << BLUE << "---------------------------------------------------" << RESET << endl;

    cout << "\nPilih Status Registrasi        : "; // Meminta input status registrasi
    int statusRegistrasi;
    cin >> statusRegistrasi;

    // Validasi input status registrasi
    while (cin.fail() || statusRegistrasi < 1 || statusRegistrasi > 2) {
        cin.clear(); // Menghapus error state pada cin
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Mengabaikan sisa input
        cout << RED << "Pilihan tidak valid! pilih opsi 1 atau 2" << RESET << endl;
        cout << "\nPilih Status Registrasi        : ";
        cin >> statusRegistrasi;
    }

    user->statusRegistrasi = statusRegistrasi; // Mengatur status registrasi pada user

    if (statusRegistrasi == 1) { // Jika status registrasi adalah 1 (kuliah)
        cout << "Jumlah SKS yang akan diambil   : ";
        cin >> user->sks; // Meminta input jumlah SKS yang akan diambil

        // Validasi input jumlah SKS
        while (user->sks < 2 || user->sks > 14) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');

            if (user->sks < 2) {
                cout << RED << "\nMinimal ambil 2 SKS.\n" << RESET;
            } else {
                cout << RED << "\nMaksimal ambil 14 SKS.\n" << RESET;
            }

            cout << "Silakan masukkan jumlah SKS: ";
            cin >> user->sks; // Meminta input jumlah SKS yang akan diambil
        }
    }

    cout << BLUE << "===================================================" << RESET << endl;
    cout << GREEN << "\nSelamat! Anda telah berhasil melakukan registrasi.\n" << RESET << endl;
}

// Fungsi untuk menampilkan menu utama
void pilihMatakuliah(User* user) {
    clearScreen();

    if (user->statusRegistrasi != 1) {
        cout << RED << "\nAnda belum melakukan registrasi matakuliah." << RESET << endl; // Menampilkan pesan jika user belum melakukan registrasi matakuliah
        return;
    }

    int totalSKSDiambil = 0; // Menghitung total SKS yang sudah diambil oleh user
    for (const auto& mk : user->mataKuliahDiambil) { // Menghitung total SKS yang sudah diambil oleh user
        totalSKSDiambil += mk.sks; // Menghitung total SKS yang sudah diambil oleh user
    }

    while (true) {
        cout << BLUE << "===================================================================" << RESET << endl; // Menampilkan header
        cout << BLUE << "                         Pilih Matakuliah                          " << RESET << endl; // Menampilkan judul
        cout << BLUE << "===================================================================" << RESET << endl; // Menampilkan garis pemisah
        cout << "|    Total SKS yang diregistrasikan: " << user->sks << endl; // Menampilkan total SKS yang diregistrasikan
        cout << "|    Total SKS yang sudah diambil: " << totalSKSDiambil << endl; // Menampilkan total SKS yang sudah diambil
        cout << "|    SKS yang tersisa: " << (user->sks - totalSKSDiambil) << endl; // Menampilkan SKS yang tersisa
        cout << BLUE << "===================================================================" << RESET << endl; // Menampilkan garis pemisah

        if (totalSKSDiambil >= user->sks) {
            cout << RED << "Anda sudah mencapai batas maksimal SKS yang bisa diambil." << RESET << endl; // Menampilkan pesan jika sudah mencapai batas maksimal SKS
            cin.ignore();
            break;
        }

        cout << "\nDaftar Matakuliah yang tersedia:" << endl; // Menampilkan daftar matakuliah yang tersedia
        for (size_t i = 0; i < daftarMataKuliah.size(); ++i) { // Menampilkan daftar matakuliah yang tersedia
            bool sudahDipilih = false; // Menandai matakuliah yang sudah dipilih
            for (const auto& mk : user->mataKuliahDiambil) { // Cek apakah matakuliah sudah dipilih sebelumnya
                if (mk.kode == daftarMataKuliah[i].kode) { // Cek apakah matakuliah sudah dipilih sebelumnya
                    sudahDipilih = true; // Menandai matakuliah yang sudah dipilih
                    break;
                }
            }
            if (!sudahDipilih) {
                cout << daftarMataKuliah[i].kode << " - " << daftarMataKuliah[i].nama << " (" << daftarMataKuliah[i].sks << " SKS)" << endl; // Menampilkan kode, nama, dan SKS matakuliah yang tersedia
            }
        }

        cout << BLUE << "====================================================================" << RESET <<  endl; // Menampilkan garis pemisah
        cout << "\nApakah anda ingin mengambil mata kuliah? (Y/N): ";
        char choice;
        cin >> choice;
        if (choice == 'Y' || choice == 'y') {
            cout << "Masukan kode Mata Kuliah yang diambil: ";
            string kode;
            cin >> kode;

            // Cek apakah matakuliah sudah dipilih sebelumnya
            bool sudahDipilih = false;
            for (const auto& mk : user->mataKuliahDiambil) {
                if (mk.kode == kode) {
                    sudahDipilih = true;
                    break;
                }
            }

            if (!sudahDipilih) {
                auto it = find_if(daftarMataKuliah.begin(), daftarMataKuliah.end(), [&kode](const MataKuliah& mk) {
                    return mk.kode == kode;
                });
                if (it != daftarMataKuliah.end()) {
                    if (totalSKSDiambil + it->sks <= user->sks) {
                        user->mataKuliahDiambil.push_back(*it);
                        totalSKSDiambil += it->sks;
                        cout << RED << "Mata Kuliah telah diambil" << RESET << endl; // Menampilkan pesan jika mata kuliah berhasil diambil
                        clearScreen();
                    } else {
                        cout << RED << "Tidak dapat mengambil mata kuliah ini karena melebihi batas SKS yang telah diregistrasikan." << RESET << endl; // Menampilkan pesan jika melebihi batas SKS yang diregistrasikan
                        clearScreen();
                    }
                } else {
                    cout << RED << "Kode Mata Kuliah tidak ditemukan" << RESET << endl; // Menampilkan pesan jika kode mata kuliah tidak ditemukan
                    cin.ignore();
                    cin.get();
                    clearScreen();
                    continue;

                }
            } else {
                cout << RED << "Anda sudah memilih mata kuliah ini sebelumnya." << RESET << endl; // Menampilkan pesan jika mata kuliah sudah dipilih sebelumnya
                clearScreen();
            }
        } else {
            break;
        }
    }
}

void displayKST(User* user) {
    clearScreen(); // Membersihkan layar sebelum menampilkan KST

    // Menampilkan header KST
    cout << BLUE << "========================================================================================" << RESET <<  endl;
    cout << BLUE << "                                   Kartu Studi Tetap                                    " << RESET << endl;
    cout << BLUE << "========================================================================================" << RESET << endl;

    // Menampilkan informasi user
    cout <<         "|  Nama Universitas   : Universitas Kristen Satya Wacana" << endl;
    cout <<         "|  Fakultas           : " << user->fakultas << endl;
    cout <<         "|  Program Studi      : " << user->programStudi << endl;
    cout <<         "|  Wali Studi         : " << user->waliStudi << endl;
    cout <<         "|  NIM                : " << user->nim << endl;
    cout <<         "|  Nama Lengkap       : " << user->namaLengkap << endl;

    // Menampilkan baris pemisah
    cout << BLUE << "========================================================================================" << RESET << endl << endl;

    // Menampilkan daftar mata kuliah yang diambil oleh user
    for (const auto& mk : user->mataKuliahDiambil) {
        cout <<     "----------------------------------------------------------------------------------------" << endl;
        cout << setw(0) << "| " << left << mk.kode; // Menampilkan kode mata kuliah
        cout << setw(2) << " | " << left << mk.nama; // Menampilkan nama mata kuliah
        cout << setw(2) << " | " << left << mk.sks; // Menampilkan jumlah SKS
        cout << setw(2) << " | " << left << mk.dosen; // Menampilkan nama dosen
        cout << setw(2) << " | " << left << mk.ruangan; // Menampilkan nomor ruangan
        cout << setw(2) << " | " << left << mk.hari; // Menampilkan hari kuliah
        cout << setw(2) << " | " << left << mk.jam << " |"<< endl; // Menampilkan jam kuliah
        cout <<     "----------------------------------------------------------------------------------------" << endl;
    }
}

// Fungsi untuk menghapus mata kuliah dari daftar mata kuliah yang diambil oleh user
void hapusMatakuliah(User* user) {
    // Menghitung total tagihan yang harus dibayar
    int totalSKS = 0;
    for (const auto& mk : user->mataKuliahDiambil) {
        totalSKS += mk.sks;
    }

    int uangKuliah = totalSKS * 250000; // Menghitung biaya dengan integer
    int sppBpp = 1500000;
    int uangKemahasiswaan = 500000;
    int totalTagihan = uangKuliah + sppBpp + uangKemahasiswaan;
    if (user->statusRegistrasi == 2) { // Cuti
        totalTagihan = 1500000;
    }

    int yangHarusDibayar = totalTagihan - static_cast<int>(user->terbayar);

    // Memeriksa apakah tagihan sudah lunas
    if (yangHarusDibayar <= 0) {
        cout << RED << "Anda tidak bisa mengakses menu ini dikarenakan tagihan anda sudah lunas." << RESET << endl;
        return;
    }

    while (true) {
        displayKST(user); // Menampilkan Kartu Studi Tetap (KST) user
        if (user->mataKuliahDiambil.empty()) { // Jika user belum mengambil mata kuliah
            cout << RED << "Anda belum mengambil matakuliah." << RESET << endl; // Menampilkan pesan bahwa user belum mengambil mata kuliah
            break;
        }
        cout << "\nMasukan Kode MataKuliah yang akan dihapus: "; // Meminta input kode mata kuliah yang akan dihapus
        string kode; // Variabel untuk menyimpan kode mata kuliah yang akan dihapus
        cin >> kode; // Meminta input kode mata kuliah yang akan dihapus
        auto it = find_if(user->mataKuliahDiambil.begin(), user->mataKuliahDiambil.end(), [&kode](const MataKuliah& mk) { // Mencari mata kuliah berdasarkan kode
            return mk.kode == kode; // Mencari mata kuliah berdasarkan kode
        });
        if (it != user->mataKuliahDiambil.end()) { // Jika mata kuliah dengan kode yang dimasukkan ditemukan
            user->mataKuliahDiambil.erase(it); // Menghapus mata kuliah dari daftar mata kuliah yang diambil oleh user
            cout << "Mata Kuliah telah dihapus" << endl;
        } else {
            cout << RED << "Kode Mata Kuliah tidak ditemukan" << RESET << endl; // Menampilkan pesan bahwa kode mata kuliah tidak ditemukan
        }
        if (!user->mataKuliahDiambil.empty()) { // Jika masih ada mata kuliah yang diambil oleh user
            cout << "Menghapus Mata Kuliah lagi? (Y/N): ";
            char choice;
            cin >> choice;
            if (choice == 'N' || choice == 'n') { // Jika user tidak ingin menghapus mata kuliah lagi
                break;
            }
        } else {
            break;
        }
    }
}

// Fungsi untuk menampilkan jadwal kuliah berdasarkan mata kuliah yang diambil
void jadwalKuliah(const vector<MataKuliah>& mataKuliahDiambil) {
    clearScreen(); // Membersihkan layar sebelum menampilkan jadwal kuliah

    // Mengurutkan jadwal mata kuliah berdasarkan hari dan jam
    vector<MataKuliah> sortedJadwal = mataKuliahDiambil;
    sort(sortedJadwal.begin(), sortedJadwal.end(), bandingkanJadwal);

    // Menampilkan judul jadwal kuliah
    cout << BLUE << "============================================================================================" << RESET << endl;
    cout << BLUE << "                                      Jadwal Kuliah                                         " << RESET << endl;
    cout << BLUE << "============================================================================================" << RESET << endl;

    // Menampilkan jadwal kuliah yang sudah diurutkan
    for (const auto& mk : sortedJadwal) {
        cout << mk.kode << " | " << mk.nama << " | " << mk.sks << " SKS | " << mk.dosen << " | " << mk.hari << " | " << mk.jam << " | Ruang " << mk.ruangan << endl;
    }

    // Menampilkan garis pemisah
    cout << BLUE << "============================================================================================" << RESET << endl;
}

void displayTagihan(User* user) {
    clearScreen();
    if (user->statusRegistrasi == 0) {
        cout << RED << "ANDA BELUM REGISTRASI MATAKULIAH." << RESET << endl;
    } else {
        int totalSKS = 0;
        for (const auto& mk : user->mataKuliahDiambil) {
            totalSKS += mk.sks;
        }

        int uangKuliah = totalSKS * 250000; // Menghitung biaya dengan integer
        int sppBpp = 1500000;
        int uangKemahasiswaan = 500000;
        int totalTagihan = uangKuliah + sppBpp + uangKemahasiswaan;
        if (user->statusRegistrasi == 2) { // Cuti
            totalTagihan = 1500000;
        }

        // Update totalTagihanAwal only if no payment has been made
        if (user->terbayar == 0) {
            user->totalTagihanAwal = totalTagihan;
        }

        int yangHarusDibayar = user->totalTagihanAwal - static_cast<int>(user->terbayar);

        cout << BLUE << "===============================================" << RESET << endl;
        cout << BLUE << "                    TAGIHAN                    " << RESET << endl;
        cout << BLUE << "===============================================" << RESET << endl;
        cout << "Uang Kuliah         : "  << uangKuliah << endl;
        cout << "SPP/BPP             : "  << sppBpp << endl;
        cout << "Uang Kemahasiswaan  : "  << uangKemahasiswaan << endl;
        cout << "Total Tagihan       : "  << totalTagihan << endl;
        cout << "Terbayar            : "  << static_cast<int>(user->terbayar) << endl;
        cout << "Yang harus dibayar  : "  << yangHarusDibayar << endl;
        cout << BLUE << "===============================================" << RESET << endl;
    }
}

void bayarTagihan(User* user) {
    clearScreen();
    while (true) {
        if (user->statusRegistrasi == 0) {
            cout << RED << "Anda belum registrasi matakuliah." << RESET << endl;
            break;
        }
        displayTagihan(user);

        int yangHarusDibayar = user->totalTagihanAwal - static_cast<int>(user->terbayar);

        if (yangHarusDibayar == 0) {
            cout << GREEN << "Anda sudah lunas. Tidak ada tagihan yang harus dibayar." << RESET << endl;
            break;
        }

        cout << "Apakah mau membayar tagihan? (Y/N): ";
        char choice;
        cin >> choice;
        if (choice == 'Y' || choice == 'y') {
            int pembayaran;
            do {
                // Meminta pengguna untuk memasukkan jumlah pembayaran
                cout << "Masukkan Uang anda (bilangan bulat): "; // Meminta input jumlah pembayaran
                cin >> pembayaran; // Meminta input jumlah pembayaran

                // Validasi input: memastikan bahwa yang dimasukkan adalah angka
                if (cin.fail()) { // Validasi input: memastikan bahwa yang dimasukkan adalah angka
                    cin.clear();  // Membersihkan status error pada cin
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Mengabaikan input yang salah
                    cout << RED << "Masukan tidak valid. Silakan masukkan angka." << RESET << endl; // Menampilkan pesan bahwa input tidak valid
                } else if (pembayaran <= 0) { // Validasi input: memastikan bahwa pembayaran adalah angka positif
                    cout << RED << "Pembayaran tidak valid. Silakan masukkan angka positif." << RESET << endl; // Menampilkan pesan bahwa pembayaran tidak valid
                } else if (pembayaran != yangHarusDibayar) { // Validasi input: memastikan bahwa pembayaran sesuai dengan tagihan yang harus dibayar
                    cout << RED << "Pembayaran harus sesuai dengan tagihan yang harus dibayar: " << yangHarusDibayar << RESET << endl; // Menampilkan pesan bahwa pembayaran harus sesuai dengan tagihan yang harus dibayar
                }
            } while (cin.fail() || pembayaran <= 0 || pembayaran != yangHarusDibayar); // Mengulang permintaan input jika input tidak valid

            // Menambahkan jumlah yang dibayar ke total yang sudah dibayar oleh user
            user->terbayar += pembayaran; // Menambahkan jumlah pembayaran ke total yang sudah dibayar oleh user
            cout << GREEN << "Pembayaran Berhasil" << RESET << endl; // Menampilkan pesan bahwa pembayaran berhasil

            // Menunggu pengguna menekan Enter untuk melanjutkan
            cout << "Tekan Enter untuk melanjutkan...";
            cin.ignore();
            cin.get();

        } else {
            break;  // Keluar dari loop jika pengguna tidak ingin membayar
        }
    }
}

// Fungsi untuk membersihkan input yang tidak valid
void clearInput() {
    cin.clear(); // Menghapus status error pada cin
    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Mengabaikan input yang tidak valid
}

void menuUtama(User* user) {
    while (true) {
        int choice;

        clearScreen();
        cout <<BLUE<< "================================" <<RESET << endl; // Menampilkan judul menu utama
        cout <<BLUE<< "=         Menu utama           =" <<RESET << endl; // Menampilkan judul menu utama
        cout <<BLUE<< "================================" <<RESET << endl; // Menampilkan judul menu utama
        cout << "+------------------------------+" << endl; // Menampilkan garis pemisah
        cout << "| 1. Biodata                   |" << endl; // Pilihan untuk menampilkan biodata
        cout << "| 2. Kartu Tanda Mahasiswa     |" << endl; // Pilihan untuk menampilkan kartu tanda mahasiswa
        cout << "| 3. Registrasi Matakuliah     |" << endl; // Pilihan untuk melakukan registrasi matakuliah
        cout << "| 4. Pilih Matakuliah          |" << endl; // Pilihan untuk memilih matakuliah
        cout << "| 5. Kartu Studi Tetap         |" << endl; // Pilihan untuk menampilkan kartu studi tetap
        cout << "| 6. Hapus Matakuliah          |" << endl; // Pilihan untuk menghapus matakuliah
        cout << "| 7. Jadwal Kuliah             |" << endl; // Pilihan untuk menampilkan jadwal kuliah
        cout << "| 8. Tagihan                   |" << endl; // Pilihan untuk menampilkan tagihan
        cout << "| 9. Bayar Tagihan             |" << endl; // Pilihan untuk membayar tagihan
        cout << "| 0. Log Out                   |" << endl; // Pilihan untuk keluar dari akun
        cout << "+------------------------------+" << endl; // Menampilkan garis pemisah
        cout << " Pilih menu: ";

        cin >> choice; // Meminta input pilihan menu dari pengguna

        if (cin.fail()) {
            clearInput();
            cout << endl;
            cout << RED << "Input tidak valid! Silakan masukkan angka." << RESET;
            getch();
            continue; // Kembali ke awal loop untuk meminta input lagi
        }

        switch (choice) {
            case 1:
                displayBiodata(user); // Memanggil fungsi untuk menampilkan biodata
                break;
            case 2:
                displayKTM(user); // Memanggil fungsi untuk menampilkan kartu tanda mahasiswa
                break;
            case 3:
                registrasiMatakuliah(user); // Memanggil fungsi untuk melakukan registrasi matakuliah
                break;
            case 4:
                pilihMatakuliah(user); // Memanggil fungsi untuk memilih matakuliah
                break;
            case 5:
                displayKST(user); // Memanggil fungsi untuk menampilkan kartu studi tetap
                break;
            case 6:
                hapusMatakuliah(user); // Memanggil fungsi untuk menghapus matakuliah
                break;
            case 7:
                jadwalKuliah(user->mataKuliahDiambil); // Memanggil fungsi untuk menampilkan jadwal kuliah
                break;
            case 8:
                displayTagihan(user); // Memanggil fungsi untuk menampilkan tagihan
                break;
            case 9:
                bayarTagihan(user); // Memanggil fungsi untuk membayar tagihan
                break;
            case 0:
                return; // Keluar dari fungsi menuUtama, sehingga program bisa keluar atau ke menu sebelumnya
            default:
                std::cout << "Pilihan tidak valid!" << std::endl; // Menampilkan pesan jika pilihan tidak valid
                break;
        }

        std::cout << "\n\nTekan Enter untuk melanjutkan...";
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.get(); // Menunggu pengguna menekan Enter
    }
}


int main() {
    while (true) {
        int choice;

        clearScreen();
        cout << BLUE << "================================" << RESET << endl;
        cout << BLUE << "=   Sistem Informasi Akademik  = " << RESET << endl;
        cout << BLUE << "================================" << RESET << endl;
        cout << "+------------------------------+" << endl;
        cout << "+ 1. Sign Up                   +" << endl; // Pilihan untuk mendaftar
        cout << "+ 2. Login                     +" << endl; // Pilihan untuk masuk
        cout << "+ 3. Kritik dan Saran Asdos    +" << endl; // Pilihan untuk memberikan kritik dan saran
        cout << "+ 4. Keluar                    +" << endl; // Pilihan untuk keluar
        cout << "+------------------------------+" << endl;
        cout << "Pilih menu: ";

        cin >> choice;

        if (cin.fail()) { // Jika input tidak valid
            clearInput(); // Membersihkan input yang tidak valid
            cout << endl; // Pindah baris
            cout << RED << "Input tidak valid! Silakan masukkan angka." << RESET << endl; // Menampilkan pesan jika input tidak valid
            cout << "\nTekan ENTER untuk kembali"; // Menampilkan pesan untuk menekan tombol ENTER
            getch(); 
            continue; // Kembali ke awal loop untuk meminta input lagi
        }

        cin.ignore();

        switch (choice) {
            case 1:
                signUp(); // Memanggil fungsi signUp() untuk mendaftar
                break;
            case 2: {
                User* user = login(); // Memanggil fungsi login() untuk masuk
                if (user) {
                    menuUtama(user); // Memanggil fungsi menuUtama() untuk menampilkan menu utama
                }
                break;
            }
            case 3:
                kritikSaranAsdos(); // Memanggil fungsi kritikSaranAsdos() untuk memberikan kritik dan saran
                break;
            case 4:
                clearScreen();
                cout << "===================================================" << endl;
                cout << "=               Anggota Kelompok                  =" << endl;
                cout << "===================================================" << endl;
                cout << "=  1. Klemens Imanuel Sancaka (672023027)         =" << endl;
                cout << "=  2. Marchell Adi Pratama (672023081)            =" << endl;
                cout << "=  3. Wahyu Aji Prasetyo (672023098)              =" << endl;
                cout << "=  4. Rafael Paulus Ardhito Sihaloho (672023102)  =" << endl;
                cout << "===================================================" << endl;
                return 0; // Keluar dari program
            default:
                cout << "Pilihan tidak valid!" << endl;
                break;
        }

        cout << "\n\nTekan Enter untuk melanjutkan...";
        // Mengabaikan karakter yang tersisa di input stream sampai karakter newline ('\n')
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    return 0;
}
