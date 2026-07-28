<?php
require '../config/database.php';

if (!isset($_GET['job_id']) || empty($_GET['job_id'])) {
    echo "Error: job_id tidak ditemukan.";
    exit();
}

$job_id = (int)$_GET['job_id'];

try {
    $pdo->beginTransaction();

    // Hapus data di tabel job_plus terlebih dahulu
    $sql_delete_job_plus = "DELETE FROM job_plus WHERE job_id = :job_id";
    $stmt = $pdo->prepare($sql_delete_job_plus);
    $stmt->execute([':job_id' => $job_id]);

    // Hapus data di tabel jobs
    $sql_delete_job = "DELETE FROM jobs WHERE job_id = :job_id";
    $stmt = $pdo->prepare($sql_delete_job);
    $stmt->execute([':job_id' => $job_id]);

    $pdo->commit();

    echo "Job successfully deleted.";
} catch (Exception $e) {
    $pdo->rollBack();
    echo "Error deleting job: " . $e->getMessage();
}
?>
