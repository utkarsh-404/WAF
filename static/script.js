function scrollToSection() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const sections = document.querySelectorAll('.content-section');
    
    sections.forEach(section => {
        const heading = section.querySelector('h2').textContent.toLowerCase();
        if (heading.includes(searchTerm)) {
            section.scrollIntoView({ behavior: 'smooth' });
            section.style.animation = 'highlight 1s';
        }
    });
}

// Add event listener for real-time search
document.getElementById('searchInput').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const sections = document.querySelectorAll('.content-section');
    
    sections.forEach(section => {
        const heading = section.querySelector('h2').textContent.toLowerCase();
        section.style.display = heading.includes(searchTerm) ? 'block' : 'none';
    });
});
