  document.getElementById('signup-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent page reload

    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    const messageDiv = document.getElementById('signup-message');

    // Clear previous messages
    messageDiv.innerHTML = '';

    // Reset any previous styles
    password.classList.remove('is-invalid');
    confirmPassword.classList.remove('is-invalid');

    // Check if passwords match
    if (password.value.trim() !== confirmPassword.value.trim()) {
      // Clear the password fields
      password.value = '';
      confirmPassword.value = '';

      // Add red border to both fields
      password.classList.add('is-invalid');
      confirmPassword.classList.add('is-invalid');

      // Show message
      messageDiv.innerHTML = `<div class="alert alert-danger">❌ Passwords do not match. Please re-enter your passwords.</div>`;

      // Optional: Move cursor back to password field
      password.focus();

      return;
    }

    try {
      const res = await fetch('http://localhost:9000/api/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: username.value.trim(),
          email: email.value.trim(),
          password: password.value.trim()
        })
      });

      const data = await res.json();

      if (res.status === 201) {
        messageDiv.innerHTML = `<div class="alert alert-success">✅ ${data.message}</div>`;
        document.getElementById('signup-form').reset();

        // Redirect after 2 seconds
        setTimeout(() => window.location.href = "/login", 2000);
      } else {
        messageDiv.innerHTML = `<div class="alert alert-danger">❌ ${data.error}</div>`;
      }

    } catch (err) {
      console.error(err);
      messageDiv.innerHTML = `<div class="alert alert-danger">❌ Something went wrong. Please try again.</div>`;
    }
  });

