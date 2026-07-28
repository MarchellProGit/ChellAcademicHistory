<?php 

class UserAuth {
    // Atribut untuk konfigurasi database
    public $host = "127.0.0.1";
    public $name = "db_js";
    public $user = "root";
    public $pass = "";
    public $db;

    // Konstruktor
    public function __construct() {
        $this->db = new PDO(
            "mysql:host={$this->host};dbname={$this->name}",
            $this->user,
            $this->pass
        );
    }

    // Fungsi untuk login
    public function login($email, $password) {
        $query = $this->db->prepare("SELECT * FROM users WHERE email = :email");
        $query->bindParam(":email", $email);
        $query->execute();

        if ($query->rowCount() > 0) {
            $user = $query->fetch(PDO::FETCH_ASSOC);
            if (password_verify($password, $user['password'])) {
                return $user; // Login berhasil, kembalikan data user
            } else {
                return false; // Password salah
            }
        }
        return false; // Email tidak ditemukan
    }

    // Fungsi untuk signup
    public function signup($email, $password) {
        // Periksa apakah email sudah terdaftar
        $query = $this->db->prepare("SELECT * FROM users WHERE email = :email");
        $query->bindParam(":email", $email);
        $query->execute();

        if ($query->rowCount() > 0) {
            return false; // Email sudah terdaftar
        }

        // Jika belum terdaftar, tambahkan data
        $hashed_password = password_hash($password, PASSWORD_BCRYPT);
        $query = $this->db->prepare("INSERT INTO users (email, password) VALUES (:email, :password)");
        $query->bindParam(":email", $email);
        $query->bindParam(":password", $hashed_password);

        return $query->execute(); // True jika berhasil
    }
}
?>
