<?php
require_once "job.php";

class ControllerJob {
    private $jobModel;

    public function __construct() {
        $this->jobModel = new Job();
    }

    // Fungsi untuk menampilkan semua lowongan pekerjaan
    public function getAllJobs() {
        return $this->jobModel->tampilkanSemuaJobs();
    }

    // Fungsi untuk menambahkan lowongan pekerjaan baru
    public function addJob($title, $description, $type, $company_name, $location, $salary) {
        return $this->jobModel->tambahJob($title, $description, $type, $company_name, $location, $salary);
    }

    // Fungsi untuk memperbarui lowongan pekerjaan
    public function updateJob($job_id, $title, $description, $type, $company_name, $location, $salary) {
        return $this->jobModel->updateJob($job_id, $title, $description, $type, $company_name, $location, $salary);
    }

    // Fungsi untuk menghapus lowongan pekerjaan
    public function deleteJob($job_id) {
        return $this->jobModel->hapusJob($job_id);
    }
}
?>
