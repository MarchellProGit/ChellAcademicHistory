// Function to toggle the visibility of the password
function togglePasswordVisibility() {
    const passwordField = document.getElementById('password');
    const togglePasswordIcon = document.getElementById('toggle-password');

    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        togglePasswordIcon.src = 'VECTOR/vector_62_x2.svg'; // Icon for visible password
    } else {
        passwordField.type = 'password';
        togglePasswordIcon.src = 'VECTOR/vector_20_x2.svg'; // Icon for hidden password
    }
}

// Add event listener to the password visibility toggle
document.getElementById('toggle-password')?.addEventListener('click', togglePasswordVisibility);

// Function to handle the Sign Up form submission
document.getElementById('signup-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const phone = document.getElementById('signup-phone').value;
    const password = document.getElementById('signup-password').value;

    // Perform validation and/or API request here
    console.log('Sign Up Data:', { phone, password });

    // Simulate successful signup
    alert('Sign Up Successful!');
});

// Function to handle the Sign In form submission
document.getElementById('login-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;

    // Perform validation and/or API request here
    console.log('Sign In Data:', { phone, password });

    // Simulate successful login
    alert('Sign In Successful!');
});

// Function to handle Forgot Password form submission
document.getElementById('forgot-password-form')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('reset-email').value;

    // Perform validation and/or API request here
    console.log('Reset Password Email:', email);

    // Show notification
    document.getElementById('reset-notification').style.display = 'block';

    // Simulate sending reset link
    setTimeout(() => {
        document.getElementById('reset-notification').style.display = 'none';
        document.getElementById('overlay').style.display = 'none'; // Hide overlay
    }, 3000); // Hide notification after 3 seconds
});

// Function to show the Forgot Password overlay
document.getElementById('forgot-password')?.addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'flex';
});

// Function to close the Forgot Password overlay
document.getElementById('close-overlay')?.addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
});
