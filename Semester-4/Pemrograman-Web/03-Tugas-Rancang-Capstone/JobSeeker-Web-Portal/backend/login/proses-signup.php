<?php
include "user-auth.php";

// Membuat objek UserAuth
$userAuth = new UserAuth();

// Memproses signup
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $password = $_POST['password'];

    if (filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($password)) {
        // Menjalankan signup
        $status = $userAuth->signup($email, $password);
        if ($status) {
            header("Location: ../../frontend/login/login.php");
            exit();
        } else {
            echo "Email sudah terdaftar!";
        }
    } else {
        echo "Email atau password tidak valid!";
    }
}
?>
