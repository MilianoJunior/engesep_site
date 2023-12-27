let currentSlide = 0;

function moveSlide(step) {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    currentSlide = (currentSlide + step + totalSlides) % totalSlides;
    slides.style.transform = 'translateX(' + (-currentSlide * 100) + '%)';
}
