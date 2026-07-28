<!DOCTYPE html>
<html>
<head>
    <title>SignUp</title>
    <link rel="stylesheet" href="../../assets/signup.css">
</head>
<body>
<!-- Navbar -->
<nav>
    <h1>FTI JOB SEEKER</h1>
</nav>

    <div class="container">
        <h2>Form SignUp</h2>
        <form method="POST" action="../../backend/login/proses-signup.php"> 
            <label>Email:</label>
            <input type="email" name="email" required><br>
            <label>Password:</label>
            <input type="password" name="password" required><br>
            <label>Confirm Password:</label>
            <input type="password" name="confirm_password" required><br>
            <input type="submit" value="Signup">

            <p>Sudah punya akun? <a href="login.php">Login di sini</a></p>
        </form>
    </div>

        <!-- Footer -->
        <footer class="bg-dark text-white text-center py-4">
        <p class="mb-0">© 2024 FTI JOB SEEKER - 100++ juta</p>
    </footer>
</body>
</html>
