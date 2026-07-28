<?php
// Database connection
$servername = "localhost";
$dbname = "db_js";
$username = "root";
$password = "";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $job_id = $_POST['job_id'];
    $location = $_POST['location'];
    $salary = $_POST['salary'];
    $requirements = $_POST['requirements'];
    $job_type = $_POST['job_type'];

    // Insert job data into the database
    $sql = "INSERT INTO job_plus (job_id, location, salary, requirements, job_type) VALUES (?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('sssss', $job_id, $location, $salary, $requirements, $job_type);

    if ($stmt->execute()) {
        echo "Job added successfully!";
    } else {
        echo "Error: " . $conn->error;
    }

    $stmt->close();
}

$conn->close();
?>
