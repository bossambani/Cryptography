// Handle Signup Form
const signupForm = document.getElementById('signup-form');
if (signupForm) {
  signupForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirm-password').value.trim();
    const messageDiv = document.getElementById('signup-message');
    messageDiv.innerHTML = '';

    // Password Match Check
    if (password !== confirmPassword) {
      messageDiv.innerHTML = `<div class="alert alert-danger">❌ Passwords do not match!</div>`;
      document.getElementById('password').value = '';
      document.getElementById('confirm-password').value = '';
      return;
    }

    try {
      const res = await fetch('http://localhost:9000/api/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password })
      });

      const data = await res.json();

      if (res.status === 201) {
        messageDiv.innerHTML = `<div class="alert alert-success">✅ ${data.message}</div>`;
        setTimeout(() => window.location.href = "/login", 2000);
      } else {
        messageDiv.innerHTML = `<div class="alert alert-danger">❌ ${data.error}</div>`;
      }

    } catch (err) {
      console.error(err);
      messageDiv.innerHTML = `<div class="alert alert-danger">❌ Something went wrong. Please try again.</div>`;
    }
  });
}

// Handle Login Form
const loginForm = document.getElementById('login-form');
if (loginForm) {
  loginForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const messageDiv = document.getElementById('login-message');
    messageDiv.innerHTML = '';

    try {
      const res = await fetch('http://localhost:9000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      const data = await res.json();

      if (res.status === 200) {
        messageDiv.innerHTML = `<div class="alert alert-success">✅ ${data.message}</div>`;
        setTimeout(() => window.location.href = "/ciphers", 2000);
      } else {
        messageDiv.innerHTML = `<div class="alert alert-danger">❌ ${data.error}</div>`;
      }

    } catch (err) {
      console.error(err);
      messageDiv.innerHTML = `<div class="alert alert-danger">❌ Something went wrong. Try again.</div>`;
    }
  });
}
