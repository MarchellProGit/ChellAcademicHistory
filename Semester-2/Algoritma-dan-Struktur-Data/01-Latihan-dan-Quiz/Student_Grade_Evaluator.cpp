#include <iostream>
#include <string>
using namespace std;

int main() {
    string nama;
    float nilai1, nilai2, nilai3;

    cout << "======================" << endl;
    cout << "|Marchell Adi Pratama|" << endl;
    cout << "|     672023081      |" << endl;
    cout << "======================" << endl;

    cout << endl << "Nama Anda: ";
    getline(cin, nama);

    cout << "Masukkan nilai 1: ";
    cin >> nilai1;

    cout << "Masukkan nilai 2: ";
    cin >> nilai2;

    cout << "Masukkan nilai 3: ";
    cin >> nilai3;

    float ratarata = (nilai1 + nilai2 + nilai3) / 3;

    if (ratarata >= 90) {
        cout << nama << ", Anda lulus dengan nilai " << ratarata << " Predikat A";
    } else if (ratarata >= 80) {
        cout << nama << ", Anda lulus dengan nilai " << ratarata << " Predikat B";
    } else if (ratarata >= 70) {
        cout << nama << ", Anda lulus dengan nilai " << ratarata << " Predikat C";
    } else if (ratarata >= 60) {
        cout << nama << ", Anda lulus dengan nilai " << ratarata << " Predikat D";
    } else {
        cout << nama << ", Anda tidak lulus dengan nilai " << ratarata;
    }

    return 0;
}
