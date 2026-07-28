<?php
require '../config/database.php';

try {
    $sql = "SELECT jobs.*, job_plus.location, job_plus.salary, job_plus.requirements 
            FROM jobs 
            LEFT JOIN job_plus ON jobs.job_id = job_plus.job_id";
    $stmt = $pdo->query($sql);

    $jobs = $stmt->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($jobs);
} catch (Exception $e) {
    echo "Error fetching jobs: " . $e->getMessage();
}
?>
