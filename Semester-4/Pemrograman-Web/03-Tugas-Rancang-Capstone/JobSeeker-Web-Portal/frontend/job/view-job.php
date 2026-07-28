<!-- view-jobs.php -->
<html>
<head>
    <title>View Jobs</title>
</head>
<body>
    <h2>Job Listings</h2>
    <table border="1">
        <tr>
            <th>Job ID</th>
            <th>Location</th>
            <th>Salary</th>
            <th>Requirements</th>
            <th>Action</th>
        </tr>
        
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
                      </tr>";
            }
        } else {
            echo "<tr><td colspan='5'>No records found</td></tr>";
        }
        $conn->close();
        ?>
    </table>
</body>
</html>