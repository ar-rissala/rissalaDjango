document.addEventListener('DOMContentLoaded', () => {
    // Determine if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
        // If reduced motion is preferred, immediately reveal everything
        // (Handled mostly via CSS, but good measure to add 'is-revealed' instantly)
        document.querySelectorAll('.reveal, .reveal-up, .reveal-left, .reveal-right, .reveal-scale, .image-reveal, .stagger-item').forEach(el => {
            el.classList.add('is-revealed');
        });
        return;
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: window.innerWidth < 768 ? 0.05 : 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;

                // Handle stagger containers specially
                if (target.classList.contains('stagger-container')) {
                    const items = target.querySelectorAll('.stagger-item');
                    items.forEach((item, index) => {
                        // Apply a staggered delay, e.g., 100ms per item
                        item.style.transitionDelay = `${index * 100}ms`;
                        
                        // We use requestAnimationFrame to ensure the delay is set before the class is added
                        requestAnimationFrame(() => {
                            item.classList.add('is-revealed');
                        });
                    });
                } else {
                    // Regular reveal items
                    target.classList.add('is-revealed');
                }

                // Stop observing once revealed
                observer.unobserve(target);
            }
        });
    }, observerOptions);

    // Observe individual reveal elements
    const revealElements = document.querySelectorAll(
        '.reveal:not(.stagger-item), ' +
        '.reveal-up:not(.stagger-item), ' +
        '.reveal-left:not(.stagger-item), ' +
        '.reveal-right:not(.stagger-item), ' +
        '.reveal-scale:not(.stagger-item), ' +
        '.image-reveal:not(.stagger-item)'
    );
    
    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Observe stagger containers
    const staggerContainers = document.querySelectorAll('.stagger-container');
    staggerContainers.forEach(container => {
        revealObserver.observe(container);
    });
});
