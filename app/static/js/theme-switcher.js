document.getElementById('theme-toggle').addEventListener('click', function() {
    const body = document.body;
    body.classList.toggle('light-theme');
    body.classList.toggle('dark-theme');

    // Save preference in local storage
    const theme = body.classList.contains('dark-theme') ? 'dark-theme' : 'light-theme';
    localStorage.setItem('theme', theme);
});

// Load saved theme preference
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.classList.add(savedTheme);
    }
});
