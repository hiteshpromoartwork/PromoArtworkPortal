function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        document.getElementById("uploaded_image").style.display = "block";
        reader.onload = function (e) {
            $('#uploaded_image')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}