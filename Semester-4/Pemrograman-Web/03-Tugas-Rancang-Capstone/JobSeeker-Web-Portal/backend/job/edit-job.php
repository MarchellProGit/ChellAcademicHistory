<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_js";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the posted data
    $job_plus_id = $_POST['job_plus_id'];
    $job_id = $_POST['job_id'];
    $location = $_POST['location'];
    $salary = $_POST['salary'];
    $requirements = $_POST['requirements'];

    // Prepare SQL update query
    $sql = "UPDATE job_plus 
            SET job_id = ?, location = ?, salary = ?, requirements = ? 
            WHERE job_plus_id = ?";

    // Prepare statement
    if ($stmt = $conn->prepare($sql)) {
        // Bind parameters
        $stmt->bind_param("isssi", $job_id, $location, $salary, $requirements, $job_plus_id);

        // Execute query
        if ($stmt->execute()) {
            echo "Job plus details updated successfully!";
        } else {
            echo "Error updating record: " . $stmt->error;
        }

        // Close statement
        $stmt->close();
    } else {
        echo "Error preparing statement: " . $conn->error;
    }

    // Close connection
    $conn->close();
} else {
    echo "Invalid request.";
}

// Include file untuk menghubungkan ke kelas Job
include('Job.php');

// Membuat objek Job
$job = new Job();

// Mendapatkan data dari form
$user_id = $_POST['user_id'];
$job_id = $_POST['job_id'];
$status = $_POST['status'];

// Mengubah status pendaftaran
if ($job->ubahStatusPendaftaran($user_id, $job_id, $status)) {
    echo "Status pendaftaran berhasil diubah.";
    header("Location: manage_registration.php?job_id=" . $job_id);
} else {
    echo "Gagal mengubah status pendaftaran.";
}
?>
