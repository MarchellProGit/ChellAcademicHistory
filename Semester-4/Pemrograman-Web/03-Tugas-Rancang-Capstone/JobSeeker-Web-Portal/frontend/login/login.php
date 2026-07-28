<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="../../assets/login.css">
</head>
<body>
<!-- Navbar -->
<nav>
    <h1>FTI JOB SEEKER</h1>
</nav>
    <h2>Form Login</h2>
    <form method="POST" action="../../backend/login/proses-login.php">
        <label>Email:</label>
        <input type="email" name="email" required><br>
        <label>Password:</label>
        <input type="password" name="password" required><br>
        <input type="submit" value="Login">

        <p>Belum punya akun? <a href="signup.php">Daftar di sini</a></p>
    </form>

        <!-- Footer -->
        <footer class="bg-dark text-white text-center py-4">
        <p class="mb-0">© 2024 FTI JOB SEEKER - 100++ juta</p>
    </footer>
</body>
</html>