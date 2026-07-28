# 🌐 Semester 4 — Pemrograman Web (PW)

**Course**: Pemrograman Web (Web Development & Architecture)  
**Primary Tech Stack**: PHP (`PHP 8`), MySQL (`PDO` / `MySQLi`), HTML5, CSS3, JavaScript  
**Author**: Marchell Adi Pratama (`672023081`)  

---

## 📁 Coursework & Web Project Index

### 🔹 `01-HTML-CSS-Fundamentals/`
* `index.html` & `style.css`: Custom HTML5 canvas layout, CSS3 grid design, and UI component styling.

### 🔹 `02-PHP-Form-and-Array-Processing/`
* `PHP_Form_Handling.php` & `PHP_Output_Render.php`: Dynamic HTTP GET/POST form validation and rendering.
* `PHP_Array_Catalog_Processor.php`: Multi-dimensional array iteration, data manipulation, and catalog display.
* `PHP_Inventory_Session_Manager.php`: Session-based inventory tracking and user state management.

### 🔹 `03-Tugas-Rancang-Capstone/`
* `JobSeeker-Web-Portal/`:
  * Full-stack PHP & MySQL Web Application for Job Search, Application Tracking, and Admin Job Management.
  * Modular Architecture:
    * `config/database.php`: MySQL database connection configuration.
    * `backend/`: Admin (`adm/`), Job Controller (`job/`), Authentication (`login/`), User State (`user/`).
    * `frontend/`: Interactive views and dashboards for Admins, Job Seekers, and Applicants.
    * `db/`: Database schemas (`jobseeker.sql`, `127_0_0_1.sql`).
    * `assets/`: Custom stylesheets (`dash-adm.css`, `dash-user.css`, `login.css`, `signup.css`).

---

## ⚡ How to Run

Serve locally using PHP Built-in Web Server:

```bash
cd 03-Tugas-Rancang-Capstone/JobSeeker-Web-Portal/
php -S localhost:8000
```
Then navigate to `http://localhost:8000`.
