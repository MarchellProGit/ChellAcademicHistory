#include <iostream>
#include <string>
#include <map>
#include <cstdlib>
#include <conio.h>

using namespace std;

map<string, string> users;

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void signIn() {
    clearScreen();
    string username, password;
    cout << "Sign In:\n";
    cout << "Masukkan username baru: ";
    cin.ignore();
    getline(cin, username);
    if (users.find(username) != users.end()) {
        cout << "Username sudah ada. Coba lagi.\n";
        return;
    }
    cout << "Masukkan password: ";
    
    password = "";
    char ch;
    while ((ch = getch()) != '\r') {
        if (ch == '\b') {
            if (!password.empty()) {
                password.pop_back();
                cout << "\b \b";
            }
        } else {
            password.push_back(ch);
            cout << "*";
        }
    }
    
    users[username] = password;
    cout << "\nRegistrasi berhasil!\n";
}

void login() {
    clearScreen();

    if (users.empty()) {
        cout << "Anda harus Sign In terlebih dahulu!\n";
        return;
    }

    string username, password;
    cout << "Login:\n";
    cout << "Masukkan username: ";
    cin.ignore();
    getline(cin, username);

    cout << "Masukkan password: ";

    password = "";
    char ch;
    while ((ch = getch()) != '\r') {
        if (ch == '\b') {
            if (!password.empty()) {
                password.pop_back();
                cout << "\b \b";
            }
        } else {
            password.push_back(ch);
            cout << "*";
        }
    }

    if (users.find(username) != users.end() && users[username] == password) {
        cout << "\nLogin berhasil!\n";
    } else {
        cout << "\nUsername atau password salah.\n";
    }
}

int main() {
    int pilihan;
    while (true) {
        cout << "+-----------------------------------+\n";
        cout << "| Selamat datang di program Tugas 2 |\n";
        cout << "|  Marchell Adi Pratama (672023081) |\n";
        cout << "+-----------------------------------+\n\n";

        cout << "Menu:\n";
        cout << "1. Sign In\n";
        cout << "2. Login\n";
        cout << "3. Exit\n";
        cout << "Pilihan: ";
        cin >> pilihan;
        cin.ignore();

        switch (pilihan) {
            case 1:
                signIn();
                break;
            case 2:
                login();
                break;
            case 3:
                cout << "Keluar dari program.\n";
                return 0;
            default:
                cout << "Pilihan tidak valid. Coba lagi.\n";
                break;
        }

        cout << "\nTekan Enter untuk melanjutkan...";
        cin.get();
        clearScreen();
    }
}