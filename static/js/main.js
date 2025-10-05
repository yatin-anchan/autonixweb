// Modern Autonix Website JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(37, 99, 235, 0.98)';
        } else {
            navbar.style.background = 'rgba(37, 99, 235, 0.95)';
        }
    });
    
    // Fade in animation on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.feature-card, .tech-item').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
    
    // Download button click tracking
    const downloadBtns = document.querySelectorAll('a[href*="download"]');
    downloadBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Add loading state
            const originalText = this.innerHTML;
            this.innerHTML = '<span class="loading"></span> Preparing Download...';
            this.disabled = true;
            
            setTimeout(() => {
                this.innerHTML = originalText;
                this.disabled = false;
            }, 2000);
        });
    });
    
    // Stats counter animation
    const stats = document.querySelectorAll('.stat-item h4');
    stats.forEach(stat => {
        const target = parseInt(stat.textContent.replace(/\D/g, '')) || 0;
        if (target > 0) {
            animateCounter(stat, 0, target, 2000);
        }
    });
    
    function animateCounter(element, start, end, duration) {
        let startTime = null;
        
        function step(timestamp) {
            if (!startTime) startTime = timestamp;
            const progress = Math.min((timestamp - startTime) / duration, 1);
            const current = Math.floor(progress * (end - start) + start);
            
            element.textContent = current + '+';
            
            if (progress < 1) {
                requestAnimationFrame(step);
            }
        }
        
        requestAnimationFrame(step);
    }
    
    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<span class="loading"></span> Sending...';
                submitBtn.disabled = true;
            }
        });
    });
    
    // Mobile menu enhancement
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarNav = document.querySelector('#navbarNav');
    
    if (navbarToggler && navbarNav) {
        navbarToggler.addEventListener('click', function() {
            this.classList.toggle('active');
        });
        
        // Close mobile menu when clicking on links
        const navLinks = navbarNav.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navbarNav.classList.remove('show');
                navbarToggler.classList.remove('active');
            });
        });
    }
});

// Parallax effect for hero section
window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const rate = scrolled * -0.5;
    const heroElements = document.querySelectorAll('.hero-section::before');
    
    heroElements.forEach(element => {
        element.style.transform = `translateY(${rate}px)`;
    });
});

// Touch and swipe support for mobile
let startX, startY, distX, distY;
const threshold = 100;

document.addEventListener('touchstart', function(e) {
    const touch = e.touches[0];
    startX = touch.clientX;
    startY = touch.clientY;
});

document.addEventListener('touchend', function(e) {
    const touch = e.changedTouches[0];
    distX = touch.clientX - startX;
    distY = touch.clientY - startY;
    
    if (Math.abs(distX) > threshold && Math.abs(distY) < 100) {
        // Handle swipe gestures if needed
    }
});
