<!-- berisi membuat perusahaan berdasarkan database table job_plus -->
<html>
<head>
    <title>Document</title>
</head>
<body>
    <form action="../../backend/add-job.php" method="post">
        <div>
            <label for="job_id">Job ID:</label>
            <input type="number" id="job_id" name="job_id" required>
        </div>
        <div>
            <label for="location">Location:</label>
            <input type="text" id="location" name="location" required>
        </div>
        <div>
            <label for="salary">Salary:</label>
            <input type="text" id="salary" name="salary" required>
        </div>
        <div>
            <label for="requirements">Requirements:</label>
            <textarea id="requirements" name="requirements" required></textarea>
        </div>
        <div>
            <label for="job_type">Job Type:</label>
            <select id="job_type" name="job_type" required>
                <option value="intern">Intern</option>
                <option value="fulltime">Full Time</option>
            </select>
        </div>
        <div>
            <button type="submit">Add Job</button>
    </div>
</form>
</body>
</html>
