
const nav = document.getElementById('main-nav');
const navLogo = document.getElementById('nav-logo');
const navLinks = document.getElementById('nav-links');
const skillsSection = document.getElementById('skills');

window.addEventListener('scroll', () => {
    const skillsTop = skillsSection.getBoundingClientRect().top;

    // When scrolling into the Dark Skills Section
    if (skillsTop <= 70) { 
        // Switch to Dark Glass
        nav.classList.replace('bg-white/10', 'bg-slate-900/40');
        nav.classList.replace('border-white/20', 'border-slate-700/50');
        
        navLogo.classList.replace('text-blue-800', 'text-white');
        navLinks.classList.replace('text-gray-800', 'text-gray-200');

        document.querySelectorAll('#nav-sub-links a').forEach(link => {
            link.classList.replace('text-gray-500', 'text-gray-400');
        });
    } 
    // When back at the White About Section
    else {
        // Switch back to Light Glass
        nav.classList.replace('bg-slate-900/40', 'bg-white/10');
        nav.classList.replace('border-slate-700/50', 'border-white/20');
        
        navLogo.classList.replace('text-white', 'text-blue-800');
        navLinks.classList.replace('text-gray-200', 'text-gray-800');

        document.querySelectorAll('#nav-sub-links a').forEach(link => {
            link.classList.replace('text-gray-400', 'text-gray-500');
        });
    }
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if(target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('opacity-100', 'translate-y-0');
            entry.target.classList.remove('opacity-0', 'translate-y-10');
        }
    });
}, observerOptions);

document.querySelectorAll('#education .group').forEach(card => {
    card.classList.add('opacity-0', 'translate-y-10', 'transition-all', 'duration-700');
    observer.observe(card);
});

document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Logic for Education Cards
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal-card').forEach(card => {
        revealObserver.observe(card);
    });

    // Your existing Navbar logic stays here...
});

// Cat Wisdom Logic
const catQuotes = [
    "I'm not a regular cat, I'm a cool teacher cat.",
    "Your grammar is paws-itively amazing today.",
    "Did you cite your sources? Fur real?",
    "Books: The only thing better than catnip.",
    "Stay paws-itive, graduation is coming!",
    "Meow-ch better! Your essay improved 100%.",
    "I read your draft. It's purr-fect.",
    "Stop feline sad and start studying!",
    "Linguistics is the cat's pajamas."
];

function generateMeme() {
    const quoteElement = document.getElementById('meme-quote');
    const randomQuote = catQuotes[Math.floor(Math.random() * catQuotes.length)];
    
    // Add a little fade effect when changing text
    quoteElement.style.opacity = 0;
    setTimeout(() => {
        quoteElement.innerText = `"${randomQuote}"`;
        quoteElement.style.opacity = 1;
    }, 200);
}

// Run once when page loads so it's not empty
document.addEventListener('DOMContentLoaded', () => {
    generateMeme();
});