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

function closeModal(event) {
    const modal = document.querySelector(".form__modal");
    const input = document.querySelector(".form__input");
    const imagePreview = document.getElementById("imagePreview");
    if (event.target == modal) {
        modal.style.top = "-100%";
        input.value = "";
        imagePreview.src = "#";
        imagePreview.style.display = "none";
    }
}

function openModal() {
    document.querySelector(".form__modal").style.top = "0";
}