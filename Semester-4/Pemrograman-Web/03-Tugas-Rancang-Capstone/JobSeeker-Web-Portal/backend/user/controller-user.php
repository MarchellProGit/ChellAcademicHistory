<?php
require_once "user.php";

class ControllerUser {
    private $userModel;

    public function __construct() {
        $this->userModel = new User();
    }

    // Mengambil data pekerjaan
    public function getJobs() {
        return $this->userModel->tampilkanSemuaJobs();
    }

    // Mengambil data job_plus
    public function getJobPlus() {
        return $this->userModel->tampilkanSemuaJobPlus();
    }

    // Mengambil data user berdasarkan ID
    public function getUserDataById($user_id) {
        return $this->userModel->tampilkanDataById($user_id);
    }
}
?>
