let shiftKey = Math.floor(Math.random() * 25) + 1;

function encryptText() {
    const input = document.getElementById('nameInput').value;
    let encrypted = '';

    for (let char of input) {
        if (char.match(/[a-z]/i)) {
            const isUpper = char === char.toUpperCase();
            let charCode = char.toLowerCase().charCodeAt(0);
            let newCharCode = ((charCode - 97 + shiftKey) % 26) + 97;
            let shiftedChar = String.fromCharCode(newCharCode);
            encrypted += isUpper ? shiftedChar.toUpperCase() : shiftedChar;
        } else {
            encrypted += char;
        }
    }

    document.getElementById('encryptedText').innerText = `Encrypted: ${encrypted}`;
}

function checkGuess() {
    const guess = parseInt(document.getElementById('guessInput').value);
    const result = guess === shiftKey ? 'Correct! 🎉' : 'Wrong key. Try again!';
    document.getElementById('guessResult').innerText = result;
}
