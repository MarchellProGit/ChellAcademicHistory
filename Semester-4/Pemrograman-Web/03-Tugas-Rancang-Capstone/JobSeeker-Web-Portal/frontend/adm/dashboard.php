<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="../../assets/dash-adm.css">
</head>
<body>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">FTI JOBSEEKER</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mr-auto">
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="logout.php">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>

        <!-- Dashboard Home Section -->
        <div id="home" class="mt-4">
            <h2>Welcome to Admin Dashboard</h2>
            <p>Manage job listings and vacancies.</p>
        </div>

        <!-- Job Listings -->
        <div id="jobListings" class="mt-4">
                    <h2>Job Listings</h2>
                    <?php
                    // Include database connection
                    include '../../config/database.php';
                    include '../../backend/adm/dashboard-adm.php';
                    // Create a new instance of the class that handles job data
                    $jobData = new Admin();
                    $jobs = $jobData->tampilkanSemuaData();
                    ?>
                    <?php if (!empty($jobs)): ?>
                        <ul class="list-group">
                            <?php foreach ($jobs as $job): ?>
                                <li class="list-group-item">
                                    <p><strong>Company:</strong> <?php echo htmlspecialchars($job['company_name']); ?></p>
                                    <p><strong>Title:</strong> <?php echo htmlspecialchars($job['title']); ?></p>
                                    <p><strong>Description:</strong> <?php echo htmlspecialchars($job['description']); ?></p>
                                    <p><strong>Location:</strong> <?php echo htmlspecialchars($job['location']); ?></p>
                                    <p><strong>Salary:</strong> <?php echo htmlspecialchars($job['salary']); ?></p>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                    <?php else: ?>
                        <p>No job listings found.</p>
                    <?php endif; ?>
                </div>
            </div>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>
</html>
<!-- Add Job Listing Form -->
<div id="addJobListing" class="mt-4">
    <h2>Add Job Listing</h2>
    <form action="add_job.php" method="POST">
        <div class="form-group">
            <label for="title">Job Title</label>
            <input type="text" class="form-control" id="title" name="title" required>
        </div>
        <div class="form-group">
            <label for="description">Job Description</label>
            <textarea class="form-control" id="description" name="description" rows="3" required></textarea>
        </div>
        <div class="form-group">
            <label for="type">Job Type</label>
            <input type="text" class="form-control" id="type" name="type" required>
        </div>
        <div class="form-group">
            <label for="company_name">Company Name</label>
            <input type="text" class="form-control" id="company_name" name="company_name" required>
        </div>
        <div class="form-group">
            <label for="posted_by">Posted By</label>
            <input type="text" class="form-control" id="posted_by" name="posted_by" required>
        </div>
        <div class="form-group">
            <label for="kuota">Quota</label>
            <input type="number" class="form-control" id="kuota" name="kuota" required>
        </div>
        <div class="form-group">
            <label for="location">Location</label>
            <input type="text" class="form-control" id="location" name="location" required>
        </div>
        <div class="form-group">
            <label for="salary">Salary</label>
            <input type="number" class="form-control" id="salary" name="salary" required>
        </div>
        <div class="form-group">
            <label for="requirements">Requirements</label>
            <textarea class="form-control" id="requirements" name="requirements" rows="3" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Add Job</button>
    </form>
</div>
<!-- Edit Job Listing Form -->
<div id="editJobListing" class="mt-4">
    <h2>Edit Job Listing</h2>
    <form action="edit_job.php" method="POST">
        <div class="form-group">
            <label for="edit_title">Job Title</label>
            <input type="text" class="form-control" id="edit_title" name="title" required>
        </div>
        <div class="form-group">
            <label for="edit_description">Job Description</label>
            <textarea class="form-control" id="edit_description" name="description" rows="3" required></textarea>
        </div>
        <div class="form-group">
            <label for="edit_type">Job Type</label>
            <input type="text" class="form-control" id="edit_type" name="type" required>
        </div>
        <div class="form-group">
            <label for="edit_company_name">Company Name</label>
            <input type="text" class="form-control" id="edit_company_name" name="company_name" required>
        </div>
        <div class="form-group">
            <label for="edit_posted_by">Posted By</label>
            <input type="text" class="form-control" id="edit_posted_by" name="posted_by" required>
        </div>
        <div class="form-group">
            <label for="edit_kuota">Quota</label>
            <input type="number" class="form-control" id="edit_kuota" name="kuota" required>
        </div>
        <div class="form-group">
            <label for="edit_location">Location</label>
            <input type="text" class="form-control" id="edit_location" name="location" required>
        </div>
        <div class="form-group">
            <label for="edit_salary">Salary</label>
            <input type="number" class="form-control" id="edit_salary" name="salary" required>
        </div>
        <div class="form-group">
            <label for="edit_requirements">Requirements</label>
            <textarea class="form-control" id="edit_requirements" name="requirements" rows="3" required></textarea>
        </div>
        <input type="hidden" id="edit_job_id" name="job_id">
        <button type="submit" class="btn btn-primary">Edit Job</button>
    </form>
</div>

<!-- Delete Job Listing Form -->
<div id="deleteJobListing" class="mt-4">
    <h2>Delete Job Listing</h2>
    <form action="delete_job.php" method="POST">
        <div class="form-group">
            <label for="delete_job_id">Job ID</label>
            <input type="number" class="form-control" id="delete_job_id" name="job_id" required>
        </div>
        <button type="submit" class="btn btn-danger">Delete Job</button>
    </form>
</div>