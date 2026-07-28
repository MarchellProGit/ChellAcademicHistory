#include <iostream>
#include <vector>

using namespace std;

class Kelas {
private:
    vector<int> nilai;
    double passingGrade;
public:
    void tambahNilai(int n) {
        nilai.push_back(n);
    }

    double hitungRataRata() {
        if (nilai.empty()) {
            return 0.0;
        }
        double total = 0.0;
        for (int n : nilai) {
            total += n;
        }
        return total / nilai.size();
    }

    double hitungPresentaseKelulusan() {
        if (nilai.empty()) {
            return 0.0;
        }
        int lulus = 0;
        for (int n : nilai) {
            if (n >= passingGrade) {
                lulus++;
            }
        }
        return static_cast<double>(lulus) / nilai.size() * 100;
    }

    void tampilkanNilai(int kelasKe) {
        cout << "*********************************************************************************" << endl;
        cout << "Nilai kelas ke-" << kelasKe << endl;
        for (int i = 0; i < nilai.size(); ++i) {
            cout << "   Nilai mahasiswa ke-" << i + 1 << " di kelas " << kelasKe << " adalah: " << nilai[i] << endl;
        }
        cout << "Rata-rata nilai di kelas ke-" << kelasKe << " adalah " << hitungRataRata() << endl;
        cout << "Presentase kelulusan di kelas ke-" << kelasKe << " adalah " << hitungPresentaseKelulusan() << "%" << endl;
        cout << "*********************************************************************************" << endl;
    }

    void setPassingGrade(double nilai) {
        passingGrade = nilai;
    }
};

int main() {


        cout << "\033[1;33m=============================================" << endl;
        cout << "    Selamat Datang di Program Marchell     " << endl;
        cout << "                672023081                  " << endl;
        cout << "=============================================\033[0m" << endl << endl;


    int banyakKelas, banyakMahasiswa;
    cout << "Masukkan banyak kelas: ";
    cin >> banyakKelas;

    vector<Kelas> kelas(banyakKelas);

    for (int i = 0; i < banyakKelas; ++i) {
        cout << "Masukkan banyak mahasiswa dalam kelas ke-" << i + 1 << ": ";
        cin >> banyakMahasiswa;

        Kelas kelasKeI;
        double nilaiTotal = 0.0;
        for (int j = 0; j < banyakMahasiswa; ++j) {
            int nilai;
            cout << "   Masukkan nilai mahasiswa ke-" << j + 1 << ": ";
            cin >> nilai;
            kelasKeI.tambahNilai(nilai);
            nilaiTotal += nilai;
        }
        kelasKeI.setPassingGrade(nilaiTotal / banyakMahasiswa);
        kelas[i] = kelasKeI;
    }

    cout << endl << "=================================================================================" << endl;
    for (int i = 0; i < banyakKelas; ++i) {
        kelas[i].tampilkanNilai(i + 1);
    }
    cout << "=================================================================================" << endl;

    return 0;
}
