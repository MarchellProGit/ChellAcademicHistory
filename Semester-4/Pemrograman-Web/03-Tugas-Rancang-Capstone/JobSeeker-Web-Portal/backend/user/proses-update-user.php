<?php
// Memasukkan koneksi database
include '../../config/database.php';

// Define database connection variables
$dsn = 'mysql:host=localhost;dbname=your_database_name';
$username = 'db_js';
$password = '';

// Inisialisasi koneksi database
$pdo = new PDO($dsn, $username, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Cek apakah form telah dikirim
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Ambil data dari form
    $email = htmlspecialchars($_POST['email']);
    $name = htmlspecialchars($_POST['name']);
    $description = htmlspecialchars($_POST['description']);
    
    // Validasi input
    if (empty($email) || empty($name) || empty($description)) {
        echo "Email, Name, and Description cannot be empty!";
        exit;
    }

    // Cek apakah email ada di database
    try {
        // Query untuk mencari pengguna berdasarkan email
        $query = "SELECT id FROM users WHERE email = :email";
        
        // Siapkan statement
        $stmt = $pdo->prepare($query);
        
        // Bind parameter email
        $stmt->bindParam(':email', $email);
        
        // Eksekusi query
        $stmt->execute();

        // Cek apakah pengguna ditemukan
        if ($stmt->rowCount() > 0) {
            // Ambil ID pengguna yang ditemukan
            $user = $stmt->fetch(PDO::FETCH_ASSOC);
            $user_id = $user['id'];

            // Query untuk memperbarui data pengguna berdasarkan id
            $updateQuery = "UPDATE users SET name = :name, description = :description WHERE id = :id";
            
            // Siapkan statement untuk update
            $updateStmt = $pdo->prepare($updateQuery);
            
            // Bind parameter
            $updateStmt->bindParam(':name', $name);
            $updateStmt->bindParam(':description', $description);
            $updateStmt->bindParam(':id', $user_id);

            // Eksekusi query pembaruan
            if ($updateStmt->execute()) {
                echo "User data updated successfully.";
                // Redirect ke halaman lain setelah berhasil
                header('Location: user_dashboard.php');
                exit;
            } else {
                echo "Failed to update user data.";
            }
        } else {
            echo "User not found with the provided email.";
        }
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>
