<?php
// Database connection
$servername = "localhost";
$dbname = "db_js";
$username = "root";
$password = "";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if ID is provided for deletion
if (isset($_GET['id'])) {
    $job_plus_id = $_GET['id'];

    // Delete job from the database
    $sql = "DELETE FROM job_plus WHERE job_plus_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('i', $job_plus_id);

    if ($stmt->execute()) {
        echo "Job deleted successfully!";
    } else {
        echo "Error: " . $conn->error;
    }

    $stmt->close();
}

$conn->close();
?>
