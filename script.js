document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card");

    function showCardsOnScroll() {
        const triggerBottom = window.innerHeight * 0.85;

        cards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top;
            if (cardTop < triggerBottom) {
                card.classList.add("show");
            }
        });
    }

    window.addEventListener("scroll", showCardsOnScroll);
    showCardsOnScroll(); // Run on page load in case cards are already in view
});
