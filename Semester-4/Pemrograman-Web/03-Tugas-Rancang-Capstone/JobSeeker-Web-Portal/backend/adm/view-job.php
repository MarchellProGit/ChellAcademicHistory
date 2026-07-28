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

// Fetch job data
$sql = "SELECT job_plus_id, job_id, location, salary, requirements FROM job_plus";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Job Plus</title>
</head>
<body>
    <h1>Job Plus Details</h1>
    <table border="1">
        <tr>
            <th>Job Plus ID</th>
            <th>Job ID</th>
            <th>Location</th>
            <th>Salary</th>
            <th>Requirements</th>
            <th>Actions</th>
        </tr>
        <?php
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<tr>
                        <td>" . $row["job_plus_id"] . "</td>
                        <td>" . $row["job_id"] . "</td>
                        <td>" . $row["location"] . "</td>
                        <td>" . $row["salary"] . "</td>
                        <td>" . $row["requirements"] . "</td>
                        <td>
                            <a href='edit-job.php?id=" . $row["job_plus_id"] . "'>Edit</a> |
                            <a href='delete-job.php?id=" . $row["job_plus_id"] . "'>Delete</a>
                        </td>
                    </tr>";
            }
        } else {
            echo "<tr><td colspan='6'>No records found</td></tr>";
        }

        $conn->close();
        ?>
    </table>
</body>
</html>
