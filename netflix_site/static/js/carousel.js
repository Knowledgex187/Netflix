// carousel.js
document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll('.banner-slide');
    let currentSlide = 0;
    const totalSlides = slides.length;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.transform = `translateX(${(i - index) * 100}%)`;
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    // Show the first slide initially
    showSlide(currentSlide);

    // Set interval to automatically change slides
    setInterval(nextSlide, 5000); // Change every 5 seconds
});
