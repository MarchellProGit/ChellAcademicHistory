# Semester 4 — Pemrograman Berorientasi Objek (PBO)

**Course**: Pemrograman Berorientasi Objek (Object-Oriented Programming in Java) 
**Primary Tech Stack**: Java (`JDK 11+`), Swing GUI, MySQL (`JDBC`), MVC Pattern (Model-View-Controller) 
**Author**: Marchell Adi Pratama (`672023081`) 

---

## Coursework & Project Index

### `01-Java-OOP-Fundamentals/`
* `Java_Template_Basics.java`: Fundamental Java OOP class structure, methods, and syntax baseline.

### `02-Quiz-and-Exercises/`
* `Quiz2_PBO_Submission.java`: Object-oriented inheritance and encapsulation quiz implementation.
* `Warung_Management_OOP/`: Interface and multi-class restaurant order management system (`Barang.java`, `Warunginterface.java`, `Warungmakan.java`, `Warungroti.java`).

### `03-Tugas-Rancang-Capstone/`
* `Inventory-Management-System-MVC/`:
 * Desktop Java Swing application built using strict **Model-View-Controller (MVC)** software architecture.
 * Features inventory management, stock transaction auditing, admin role authentication, low-stock notifications, and report generation with MySQL database connection (`JDBC`).
 * `schema.sql`: Relational database creation script.

---

## How to Compile & Run

### Running Inventory Management System (Swing MVC):
```bash
cd 03-Tugas-Rancang-Capstone/Inventory-Management-System-MVC/
javac -d bin src/config/*.java src/model/*.java src/controller/*.java src/view/*.java src/main/*.java
java -cp bin main.Main
```
