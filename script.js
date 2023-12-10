function updateImages() {
    var text = document.getElementById('textInput').value;
    var imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = ''; // Clear previous images

    for (var i = 0; i < text.length; i++) {
        if (text[i] === ' ') {
            var br = document.createElement('br');
            imageContainer.appendChild(br);
        } else {
            var img = document.createElement('img');
            img.src = 'images/' + text[i].toLowerCase() + '.png';
            imageContainer.appendChild(img);
        }
    }
}
