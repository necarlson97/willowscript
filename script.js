function updateImages() {
    var text = document.getElementById('textInput').value;
    var imageContainer = document.getElementById('imageContainer');
    imageContainer.innerHTML = ''; // Clear previous images

    var wordDiv = null;

    for (var i = 0; i < text.length; i++) {
        if (text[i].match(/\s/)) { // Check for whitespace
            wordDiv = null; // End the current word
            var br = document.createElement('br');
            imageContainer.appendChild(br);
        } else {
            if (!wordDiv) {
                wordDiv = document.createElement('div'); // Start a new word
                wordDiv.className = 'word';
                imageContainer.appendChild(wordDiv);
            }
            var img = document.createElement('img');
            img.alt = ''; // Don't show image if it is missing
            img.src = getImageSource(text, i);
            wordDiv.appendChild(img);
        }
    }
}

function getImageSource(text, i) {
    if (text[i] === '"') {
        if (atStartOfWord(text, i)) return 'images/top-quote.png';
        return 'images/bottom-quote.png';
    } else if (text[i] === '?') {
        if (atStartOfWord(text, i)) return 'images/top-question.png';
        return 'images/bottom-question.png';
    } else if (text[i] === '.') {
        return 'images/period.png'
    } else if (text[i] === ',') {
        return 'images/comma.png'
    } else {
        return 'images/' + text[i].toLowerCase() + '.png';
    }
}

function atStartOfWord(text, i) {
    // Returns true if the given index is at the start of a word
    return (i < text.length - 1 && text[i + 1] !== ' ');
}

window.onload = updateImages; // Call updateImages on window load
