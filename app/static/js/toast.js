const toast = document.querySelector('.toast');

if (toast) {
    setTimeout(() => {
        toast.classList.remove('show');
    }
    , 3000);
}