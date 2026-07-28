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
}

    // insert/tambah lowongan pekerjaaan
    public function insertLowongan($title, $description, $type, $company_name, $posted_by, $kuota, $location, $salary, $requirements) {
        $query = $this->db->prepare(
            "INSERT INTO jobs (title, description, type, company_name, posted_by, kuota) 
            VALUES (:title, :description, :type, :company_name, :posted_by, :kuota)"
        );
        $query->bindParam(":title", $title);
        $query->bindParam(":description", $description);
        $query->bindParam(":type", $type);
        $query->bindParam(":company_name", $company_name);
        $query->bindParam(":posted_by", $posted_by);
        $query->bindParam(":kuota", $kuota);
        $query->execute();

        $job_id = $this->db->lastInsertId();

        $query = $this->db->prepare(
            "INSERT INTO job_plus (job_id, location, salary, requirements) 
            VALUES (:job_id, :location, :salary, :requirements)"
        );
        $query->bindParam(":job_id", $job_id);
        $query->bindParam(":location", $location);
        $query->bindParam(":salary", $salary);
        $query->bindParam(":requirements", $requirements);
        return $query->execute();
    }

        // delete data lowongan pekerjaan
        public function deleteLowongan($job_id) {
            $query = $this->db->prepare(
                "DELETE FROM jobs 
                WHERE job_id = :job_id"
            );
            $query->bindParam(":job_id", $job_id);
            $query->execute();
    
            $query = $this->db->prepare(
                "DELETE FROM job_plus 
                WHERE job_id = :job_id"
            );
            $query->bindParam(":job_id", $job_id);
            return $query->execute();
        }

            // update data lowongan pekerjaan
    public function updateLowongan($job_id, $title, $description, $type, $company_name, $posted_by, $kuota, $location, $salary, $requirements) {
        $query = $this->db->prepare(
            "UPDATE jobs 
            SET title = :title, description = :description, type = :type, company_name = :company_name, posted_by = :posted_by, kuota = :kuota 
            WHERE job_id = :job_id"
        );
        $query->bindParam(":job_id", $job_id);
        $query->bindParam(":title", $title);
        $query->bindParam(":description", $description);
        $query->bindParam(":type", $type);
        $query->bindParam(":company_name", $company_name);
        $query->bindParam(":posted_by", $posted_by);
        $query->bindParam(":kuota", $kuota);
        $query->execute();

        $query = $this->db->prepare(
            "UPDATE job_plus 
            SET location = :location, salary = :salary, requirements = :requirements 
            WHERE job_id = :job_id"
        );
        $query->bindParam(":job_id", $job_id);
        $query->bindParam(":location", $location);
        $query->bindParam(":salary", $salary);
        $query->bindParam(":requirements", $requirements);
        return $query->execute();
    }

    ?>