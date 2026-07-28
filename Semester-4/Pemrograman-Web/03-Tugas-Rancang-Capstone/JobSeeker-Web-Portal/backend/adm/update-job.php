<?php
// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_js";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Fetch the job ID from the URL
if (isset($_GET['id'])) {
    $job_plus_id = $_GET['id'];

    // Fetch job data from the database
    $sql = "SELECT * FROM job_plus WHERE job_plus_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('i', $job_plus_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $job = $result->fetch_assoc();

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $job_id = $_POST['job_id'];
        $location = $_POST['location'];
        $salary = $_POST['salary'];
        $requirements = $_POST['requirements'];
        $job_type = $_POST['job_type'];

        $update_sql = "UPDATE job_plus SET job_id = ?, location = ?, salary = ?, requirements = ?, job_type = ? WHERE job_plus_id = ?";
        $update_stmt = $conn->prepare($update_sql);
        $update_stmt->bind_param('sssssi', $job_id, $location, $salary, $requirements, $job_type, $job_plus_id);

        if ($update_stmt->execute()) {
            echo "Job updated successfully!";
        } else {
            echo "Error: " . $conn->error;
        }
    }
}

$conn->close();
?>
