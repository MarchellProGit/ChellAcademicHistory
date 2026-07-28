<?php
require '../config/database.php'; // Pastikan path ini sesuai dengan struktur folder Anda

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Mendapatkan data dari form
    $job_id = (int)$_POST['job_id'];
    $location = $_POST['location'];
    $salary = $_POST['salary'];
    $requirements = $_POST['requirements'];
    $type = $_POST['type'];

    try {
        // Memulai transaksi
        $pdo->beginTransaction();

        // Memasukkan data ke tabel jobs (jika belum ada job_id yang terdaftar)
        $sql_insert_job = "INSERT INTO jobs (job_id, type) 
                           VALUES (:job_id, :type)";
        $stmt = $pdo->prepare($sql_insert_job);
        $stmt->execute([
            ':job_id' => $job_id,
            ':type' => $type,
        ]);

        // Memasukkan data ke tabel job_plus
        $sql_insert_job_plus = "INSERT INTO job_plus (job_id, location, salary, requirements) 
                               VALUES (:job_id, :location, :salary, :requirements)";
        $stmt = $pdo->prepare($sql_insert_job_plus);
        $stmt->execute([
            ':job_id' => $job_id,
            ':location' => $location,
            ':salary' => $salary,
            ':requirements' => $requirements,
        ]);

        // Commit transaksi jika berhasil
        $pdo->commit();
        echo "Job successfully added!";
    } catch (Exception $e) {
        // Rollback jika terjadi kesalahan
        $pdo->rollBack();
        echo "Failed to add job: " . $e->getMessage();
    }
} else {
    echo "Invalid request.";
}
?>
