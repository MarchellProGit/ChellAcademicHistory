<?php
include "user-auth.php";

// Membuat objek UserAuth
$userAuth = new UserAuth();

// Memproses login
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Melakukan login
    $user = $userAuth->login($email, $password);

    if ($user) {
        $userId = $user['user_id'];
        header("Location: ../../frontend/user/dashboard.php?email=$email&user_id=$userId"); // Arahkan ke halaman profil setelah login
        exit();
    } else {
        echo "Login gagal! Email atau password salah.";
    }
}
?>
