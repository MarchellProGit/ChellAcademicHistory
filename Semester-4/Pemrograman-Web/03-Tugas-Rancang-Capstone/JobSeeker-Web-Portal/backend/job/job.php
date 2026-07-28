<?php

class Job {
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

    // Fungsi untuk menampilkan semua data jobs
    public function tampilkanSemuaJobs() {
        $query = $this->db->prepare("SELECT * FROM jobs");
        $query->execute();
        return $query->fetchAll(PDO::FETCH_ASSOC);
    }

    // Fungsi untuk menambahkan data pekerjaan baru
    public function tambahJob($title, $description, $type, $company_name, $location, $salary) {
        $query = $this->db->prepare("INSERT INTO jobs (title, description, type, company_name, location, salary) 
            VALUES (:title, :description, :type, :company_name, :location, :salary)");
        $query->bindParam(":title", $title);
        $query->bindParam(":description", $description);
        $query->bindParam(":type", $type);
        $query->bindParam(":company_name", $company_name);
        $query->bindParam(":location", $location);
        $query->bindParam(":salary", $salary);
        return $query->execute();
    }

    // Fungsi untuk memperbarui data pekerjaan
    public function updateJob($job_id, $title, $description, $type, $company_name, $location, $salary) {
        $query = $this->db->prepare("UPDATE jobs 
            SET title = :title, description = :description, type = :type, company_name = :company_name, 
            location = :location, salary = :salary WHERE job_id = :job_id");
        $query->bindParam(":job_id", $job_id);
        $query->bindParam(":title", $title);
        $query->bindParam(":description", $description);
        $query->bindParam(":type", $type);
        $query->bindParam(":company_name", $company_name);
        $query->bindParam(":location", $location);
        $query->bindParam(":salary", $salary);
        return $query->execute();
    }

    // Fungsi untuk menghapus data pekerjaan
    public function hapusJob($job_id) {
        $query = $this->db->prepare("DELETE FROM jobs WHERE job_id = :job_id");
        $query->bindParam(":job_id", $job_id);
        return $query->execute();
    }

    // Fungsi untuk mengecek pendaftaran
public function cekPendaftaran($user_id, $job_id) {
    $query = $this->db->prepare("SELECT * FROM applications WHERE user_id = :user_id AND job_id = :job_id");
    $query->bindParam(":user_id", $user_id);
    $query->bindParam(":job_id", $job_id);
    $query->execute();
    
    // Jika ada hasil, berarti user sudah mendaftar
    if ($query->rowCount() > 0) {
        return true;  // Sudah mendaftar
    } else {
        return false; // Belum mendaftar
    }
}

// Fungsi untuk mengubah status pendaftaran
public function ubahStatusPendaftaran($user_id, $job_id, $status) {
    // Pastikan status yang diterima valid
    if (in_array($status, ['pending', 'accepted', 'rejected'])) {
        $query = $this->db->prepare("UPDATE applications SET status = :status WHERE user_id = :user_id AND job_id = :job_id");
        $query->bindParam(":status", $status);
        $query->bindParam(":user_id", $user_id);
        $query->bindParam(":job_id", $job_id);
        return $query->execute();
    } else {
        return false; // Status tidak valid
    }
}

}
?>


