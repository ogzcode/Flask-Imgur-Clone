window.addEventListener("load", function () {
    const navbarHeight = document.querySelector('.navbar').offsetHeight;
    const formContainer = document.querySelector('.container');
    formContainer.style.height = `calc(100vh - ${navbarHeight}px)`;
});