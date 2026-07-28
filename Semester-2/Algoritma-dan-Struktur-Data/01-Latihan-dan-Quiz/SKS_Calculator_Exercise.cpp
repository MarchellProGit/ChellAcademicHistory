#include <iostream>

using std::cout;
using std::string;
using std::endl;

int main (){
    int jumlahSKS;
    std::string nama = "cuy";

    std::cout << "Masukkan SKS: ";
    std::cin >> jumlahSKS; //ini untuk input
    std::cout << "jumlahSKS anda: " << jumlahSKS << std::endl; //ini untuk output
    std::cout << nama;

    return 0;
}
