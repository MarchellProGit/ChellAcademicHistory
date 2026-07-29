# Semester 2 — Algoritma dan Struktur Data (ASD)

**Course**: Algoritma dan Struktur Data (Algorithms & Data Structures) 
**Primary Tech Stack**: C++ (`C++11` / `C++17` / `GCC` / `MSVC`) 
**Key Concepts**: Standard Template Library (`std::vector`, `std::map`), Binary File I/O Serialization, Custom Structs, Dynamic Sorting, Searching Algorithms, CLI Architecture 
**Author**: Marchell Adi Pratama (`672023081`) 

---

## Professional Coursework & Project Index

### `01-Latihan-dan-Quiz/`
Introductory C++ exercises, structs, and quiz evaluations:
* `Array_Iteration_Exercise.cpp`: C++ array initialization & iteration logic.
* `SKS_Calculator_Exercise.cpp`: Credit hour (SKS) computation algorithm.
* `Struct_Mahasiswa_Exercise.cpp`: Custom `struct` modeling for student records.
* `Student_Grade_Evaluator.cpp`: Grade threshold evaluation & condition logic.

### `02-Tugas/` (Data Structure Deep-Dives)
* `01-Vector-Data-Structure/Vector_Student_Grades_Manager.cpp`: OOP Class wrapper around `std::vector` for dynamic array management and grade computation.
* `02-Map-Data-Structure/Map_Associative_Lookup.cpp`: Associative key-value data storage and lookup using `std::map`.

### `03-Proyek-Kelompok/` (Group Systems & Real-World Applications)
* `Supermarket-Warehouse-System/`:
 * `Supermarket_Warehouse_Management_System.cpp`: Full supermarket warehouse inventory CLI system with binary data serialization (`.dat` file streams), `std::map`, and multi-role authentication.
 * Data files: `gudang_supermarket.dat`, `gudang.txt`, `users.dat`, `users.txt`.
* `Academic-Information-System-SIA/`:
 * `Academic_Information_System_SIA_Suite.cpp`: Comprehensive Academic Information System (SIA) featuring user authentication, course enrollment, sorting algorithms, and text-stream data persistence.

### `04-Tugas-Akhir/` (Capstone Project)
* `ASD_Final_Capstone_Project.cpp`: Integrated Data Structure Final Capstone Project for ASD course combining multi-layered data structures, sorting routines, and interactive CLI menus.

---

## How to Compile & Run

All projects can be compiled using any modern C++ compiler (`g++` or `clang++`):

```bash
# Example: Compiling the Supermarket Warehouse System
g++ -O2 -std=c++11 03-Proyek-Kelompok/Supermarket-Warehouse-System/Supermarket_Warehouse_Management_System.cpp -o warehouse_app
./warehouse_app
```
