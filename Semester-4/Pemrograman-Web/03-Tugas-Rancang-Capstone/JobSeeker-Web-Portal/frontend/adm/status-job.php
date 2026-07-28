<?php
// Include database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "db_js";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $application_id = $_POST['application_id'];
    $status = $_POST['status'];

    // Update the status in the database
    $sql = "UPDATE applications SET status = ? WHERE application_id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param('si', $status, $application_id);

    if ($stmt->execute()) {
        echo "Status updated successfully.";
    } else {
        echo "Error updating status: " . $conn->error;
    }

    $stmt->close();
}

// Fetch applications
$sql = "SELECT application_id, user_id, job_id, status FROM applications";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Application Status</title>
</head>
<body>
    <h1>Update Application Status</h1>
    <form method="post" action="">
        <label for="application_id">Application ID:</label>
        <select name="application_id" id="application_id" required>
            <?php while ($row = $result->fetch_assoc()): ?>
                <option value="<?php echo $row['application_id']; ?>">
                    <?php echo "Application ID: " . $row['application_id'] . " - Status: " . $row['status']; ?>
                </option>
            <?php endwhile; ?>
        </select>
        <br>
        <label for="status">Status:</label>
        <select name="status" id="status" required>
            <option value="pending">Pending</option>
            <option value="lolos">Lolos</option>
            <option value="tidak_lolos">Tidak Lolos</option>
        </select>
        <br>
        <button type="submit">Update Status</button>
    </form>
</body>
</html>

<?php
$conn->close();
?>