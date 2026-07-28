<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <link rel="stylesheet" href="../../assets/dash-user.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <!-- Navbar -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">FTI JOBSEEKER</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mr-auto"></ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="../../backend/login/logout.php">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>

        <!-- Tab Navigation -->
        <nav>
            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                <a class="nav-item nav-link active" id="nav-home-tab" data-toggle="tab" href="#nav-home" role="tab" aria-controls="nav-home" aria-selected="true">Home</a>
                <a class="nav-item nav-link" id="nav-profile-tab" data-toggle="tab" href="#nav-profile" role="tab" aria-controls="nav-profile" aria-selected="false">Profile</a>
                <a class="nav-item nav-link" id="nav-status-tab" data-toggle="tab" href="#nav-status" role="tab" aria-controls="nav-status" aria-selected="false">Status</a>
            </div>
        </nav>

        <!-- Tab Content -->
        <div class="tab-content" id="nav-tabContent">
            <!-- Home Tab -->
            <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
                <div id="home" class="mt-4">
                    <h2>Welcome to User Dashboard</h2>
                    <p>View job listings and apply for jobs.</p>
                </div>

                <!-- Job Listings -->
                <div id="jobListings" class="mt-4">
                    <h2>Job Listings</h2>
                    <?php
                    // Include database connection
                    include '../../config/database.php';
                    include '../../backend/user/user.php';

                    // Create a new instance of the class that handles job data
                    $jobData = new User();
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
                                    <form action="../../backend/job/apply.php" method="post">
                                        <input type="hidden" name="job_id" value="<?php echo htmlspecialchars($job['job_id']); ?>">
                                        <button type="submit" class="btn btn-primary">Apply</button>
                                    </form>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                    <?php else: ?>
                        <p>No job listings found.</p>
                    <?php endif; ?>
                </div>
            </div>

            <!-- Profile Tab -->
            <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
                <div id="userDescription" class="mt-4">
                    <h2>User Description</h2>
                    <form action="../../backend/user/proses-update-user.php" method="post">
                        <div class="form-group">
                            <label for="email">Email:</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="name">Name:</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="description">Description:</label>
                            <textarea class="form-control" id="description" name="description" rows="3" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">Update</button>
                    </form>
                </div>
            </div>

            <!-- Status Tab -->
            <div class="tab-pane fade" id="nav-status" role="tabpanel" aria-labelledby="nav-status-tab">
                <div id="applicationStatus" class="mt-4">
                    <h2>Application Status</h2>
                    <?php
                    // Query to fetch application status
                    $applications = $jobData->getApplicationStatus($user_id); 
                    ?>
                    <?php if (!empty($applications)): ?>
                        <ul class="list-group">
                            <?php foreach ($applications as $app): ?>
                                <li class="list-group-item">
                                    <p><strong>Job Title:</strong> <?php echo htmlspecialchars($app['title']); ?></p>
                                    <p><strong>Status:</strong> <?php echo htmlspecialchars($app['status']); ?></p>
                                    <p><strong>Applied At:</strong> <?php echo htmlspecialchars($app['applied_at']); ?></p>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                    <?php else: ?>
                        <p>No applications found.</p>
                    <?php endif; ?>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-4">
        <p class="mb-0">© 2024 FTI JOB SEEKER - 100++ juta</p>
    </footer>

    <!-- Scripts -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>
</html>
