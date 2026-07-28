<?php
include 'Job.php';

$job = new Job();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user_id = $_POST['user_id'];
    $job_id = $_POST['job_id'];
    $status = $_POST['status'];

    if ($job->ubahStatusPendaftaran($user_id, $job_id, $status)) {
        echo json_encode(['status' => 'success', 'message' => 'Status updated successfully']);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Failed to update status']);
    }
}
