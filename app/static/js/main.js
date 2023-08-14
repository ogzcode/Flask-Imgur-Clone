const toast = document.querySelector('.toast__box');

window.addEventListener('load', () => {
    if (toast) {
        setTimeout(() => {
            toast.style.display = "none";
        }, 3000);
    }
});