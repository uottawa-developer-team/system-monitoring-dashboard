document.addEventListener("DOMContentLoaded", function() {
    const menuBar = document.getElementById("menu-bar");
    const scrollLinks = document.querySelectorAll(".scroll-link");

    // Hide menu bar on scroll
    window.addEventListener("scroll", function() {
        if (window.scrollY > 100) {
            menuBar.classList.add("hidden");
        } else {
            menuBar.classList.remove("hidden");
        }
    });

    // Show menu bar on scroll up
    window.addEventListener("scroll", function() {
        if (window.scrollY < 100) {
            menuBar.classList.remove("hidden");
        }
    });

    // Add event listener to scroll links
    scrollLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const href = link.getAttribute("href");
            const target = document.querySelector(href);
            const offsetTop = target.offsetTop;
            window.scrollTo({
                top: offsetTop,
                behavior: "smooth"
            });
        });
    });
});