function previewImage(input) {
    var imagePreview = document.getElementById("imagePreview");
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
        };
        reader.readAsDataURL(input.files[0]);
        imagePreview.style.display = "block";
    } else {
        imagePreview.src = "#"; // Reset preview if no image is selected
    }
}

window.addEventListener("load", function () {
    const navbarHeight = document.querySelector('.navbar').offsetHeight;
    const formContainer = document.querySelector('.form__container');
    formContainer.style.height = `calc(100vh - ${navbarHeight}px)`;
});