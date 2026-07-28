<?php

class User {
    // Konfigurasi database
    private $host = "127.0.0.1";
    private $name = "db_js";
    private $user = "root";
    private $pass = "";
    private $db;

    // Konstruktor
    public function __construct() {
        $this->db = new PDO(
            "mysql:host={$this->host};dbname={$this->name}",
            $this->user,
            $this->pass
        );
    }

    // SELECT (Tampilkan Semua Data dari table job dan job_plus)
    public function tampilkanSemuaData() {
        $query = $this->db->prepare("
            SELECT 
                j.job_id, 
                j.title, 
                j.description, 
                j.type, 
                j.company_name, 
                j.posted_by, 
                j.kuota, 
                jp.location, 
                jp.salary, 
                jp.requirements
            FROM jobs j 
            JOIN job_plus jp 
            ON j.job_id = jp.job_id
        ");
        $query->execute();
        return $query->fetchAll(PDO::FETCH_ASSOC);
    }

    //inser deskripsi user
    public function insertDeskripsi($user, $deskripsi) {
        $query = $this->db->prepare(
            "INSERT INTO user (user, description) 
            VALUES (:user, :description)"
        );
        $query->bindParam(":user", $user);
        $query->bindParam(":description", $deskripsi);
        return $query->execute();
    }

    // update data user (nama, deskripsi)
    public function updateData($user, $name, $deskripsi) {
        $query = $this->db->prepare(
            "UPDATE user 
            SET name = :name, description = :description 
            WHERE user = :user"
        );
        $query->bindParam(":user", $user);
        $query->bindParam(":name", $name);
        $query->bindParam(":description", $deskripsi);
        return $query->execute();
    }

    // SELECT (Tampilkan Status Berdasarkan user_id dan job_id)
    public function tampilkanStatus($user_id, $job_id) {
        $query = $this->db->prepare(
            "SELECT status 
            FROM applications 
            WHERE user_id = :user_id AND job_id = :job_id"
        );
        $query->bindParam(":user_id", $user_id);
        $query->bindParam(":job_id", $job_id);
        $query->execute();
        return $query->fetch(PDO::FETCH_ASSOC);
    }

    public function applyJob($job_id, $user_id) {
        $query = $this->db->prepare("INSERT INTO applications (job_id, user_id, status, applied_at) VALUES (?, ?, 'Pending', NOW())");
        $query->execute([$job_id, $user_id]);
    }

    public function getApplicationStatus($user_id) {
        $query = $this->db->prepare("SELECT applications.*, jobs.title FROM applications JOIN jobs ON applications.job_id = jobs.job_id WHERE applications.user_id = ?");
        $query->execute([$user_id]);
        return $query->fetchAll(PDO::FETCH_ASSOC);
    }
    

    /*------------------------------*/
    
    // INSERT (Tambah Data Baru)
    public function tambahData($name, $email, $password, $role) {
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);
        $query = $this->db->prepare(
            "INSERT INTO users (name, email, password, role) 
            VALUES (:name, :email, :password, :role)"
        );
        $query->bindParam(":name", $name);
        $query->bindParam(":email", $email);
        $query->bindParam(":password", $hashed_password);
        $query->bindParam(":role", $role);
        return $query->execute();
    }

    // SELECT (Tampilkan Data Berdasarkan ID)
    public function tampilkanDataById($user_id) {
        $query = $this->db->prepare("SELECT * FROM users WHERE user_id = :user_id");
        $query->bindParam(":user_id", $user_id);
        $query->execute();
        return $query->fetch(PDO::FETCH_ASSOC);
    }

    // SELECT (Tampilkan Data Berdasarkan Email)
    public function tampilkanDataByEmail($email) {
        $query = $this->db->prepare("SELECT * FROM users WHERE email = :email");
        $query->bindParam(":email", $email);
        $query->execute();
        return $query->fetch(PDO::FETCH_ASSOC);
    }

    // UPDATE (Ubah Data Berdasarkan ID)
    public function ubahDataById($user_id, $name, $email, $password, $role) {
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);
        $query = $this->db->prepare(
            "UPDATE users 
            SET name = :name, email = :email, password = :password, role = :role 
            WHERE user_id = :user_id"
        );
        $query->bindParam(":user_id", $user_id);
        $query->bindParam(":name", $name);
        $query->bindParam(":email", $email);
        $query->bindParam(":password", $hashed_password);
        $query->bindParam(":role", $role);
        return $query->execute();
    }

    // DELETE (Hapus Data Berdasarkan ID)
    public function hapusData($user_id) {
        $query = $this->db->prepare("DELETE FROM users WHERE user_id = :user_id");
        $query->bindParam(":user_id", $user_id);
        return $query->execute();
    }

    // Verifikasi Login
    public function verifikasiLogin($email, $password) {
        $query = $this->db->prepare("SELECT * FROM users WHERE email = :email");
        $query->bindParam(":email", $email);
        $query->execute();
        $user = $query->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            return $user; // Mengembalikan data pengguna jika login berhasil
        }
        return false; // Jika gagal login
    }
    
        // Fungsi untuk menampilkan semua data jobs
        public function tampilkanSemuaJobs() {
            $query = $this->db->prepare("SELECT * FROM jobs");
            $query->execute();
            return $query->fetchAll(PDO::FETCH_ASSOC);
        }
    
        // Fungsi untuk menampilkan semua data job_plus
        public function tampilkanSemuaJobPlus() {
            $query = $this->db->prepare("SELECT * FROM job_plus");
            $query->execute();
            return $query->fetchAll(PDO::FETCH_ASSOC);
        }
}
?>
