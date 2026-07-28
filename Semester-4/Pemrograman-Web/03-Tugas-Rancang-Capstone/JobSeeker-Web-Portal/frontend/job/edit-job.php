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

// Fetch job_plus data
$sql = "SELECT job_plus_id, job_id, location, salary, requirements FROM job_plus";
$result = $conn->query($sql);
?>

<html>
<head>
    <title>Edit Job Plus</title>
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
            <th>Action</th>
        </tr>
        <?php
        if ($result->num_rows > 0) {
            // Output data of each row
            while($row = $result->fetch_assoc()) {
                echo "<tr>
                        <td>" . $row["job_plus_id"]. "</td>
                        <td>" . $row["job_id"]. "</td>
                        <td>" . $row["location"]. "</td>
                        <td>" . $row["salary"]. "</td>
                        <td>" . $row["requirements"]. "</td>
                        <td>
                            <a href='edit-job.php?id=". $row["job_plus_id"]. "'>Edit</a>
                            <a href='delete-job.php?id=". $row["job_plus_id"]. "'>Delete</a>
                        </td>
                      </tr>";
            }
        } else {
            echo "<tr><td colspan='6'>No records found</td></tr>";
        }
        $conn->close();
        ?>
    </table>

    <?php
    if (isset($_GET['id'])) {
        $job_plus_id = $_GET['id'];
        $sql = "SELECT job_id, location, salary, requirements FROM job_plus WHERE job_plus_id = $job_plus_id";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            ?>
            <h2>Edit Job Plus</h2>
            <form action="update_job.php" method="post">
                <input type="hidden" name="job_plus_id" value="<?php echo $job_plus_id; ?>">
                <label for="job_id">Job ID:</label>
                <input type="text" name="job_id" value="<?php echo $row['job_id']; ?>"><br>
                <label for="location">Location:</label>
                <input type="text" name="location" value="<?php echo $row['location']; ?>"><br>
                <label for="salary">Salary:</label>
                <input type="text" name="salary" value="<?php echo $row['salary']; ?>"><br>
                <label for="requirements">Requirements:</label>
                <input type="text" name="requirements" value="<?php echo $row['requirements']; ?>"><br>
                <input type="submit" value="Update">
            </form>
            <?php
        }
    }
    ?>
</body>
</html>