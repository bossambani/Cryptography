
  const themeToggle = document.getElementById('themeToggle');
  const themeIcon = document.getElementById('themeIcon');
  const body = document.body;

  function applyTheme(theme) {
    if (theme === 'dark') {
      body.classList.add('dark-mode');
      localStorage.setItem('darkMode', 'enabled');
    } else {
      body.classList.remove('dark-mode');
      localStorage.setItem('darkMode', 'disabled');
    }
  }

  // Load saved preference
  window.onload = () => {
    const savedTheme = localStorage.getItem('darkMode');
    if (savedTheme === 'enabled') {
      body.classList.add('dark-mode');
    }
  };

  // Toggle on click
  themeToggle.addEventListener('click', () => {
    if (body.classList.contains('dark-mode')) {
      applyTheme('light');
    } else {
      applyTheme('dark');
    }
  });

