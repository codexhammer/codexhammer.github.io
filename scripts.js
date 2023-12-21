document.addEventListener("DOMContentLoaded", function () {
    var currentPage = window.location.pathname;

    // Get all the navigation links
    var navLinks = document.querySelectorAll("nav a");

    // Loop through the links
    navLinks.forEach(function (link) {
        var linkPath = link.getAttribute("href");

        // Check if the link is for the current page
        if (linkPath === currentPage) {
            link.classList.add("active");
            link.style.color = "green"; // Change the text color to green
        }
    });
});
