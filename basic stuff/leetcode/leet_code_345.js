const vowCheck = (ch) => ('aeiou'.includes(ch.toLowerCase()));

var reverseVowels = function(str) {
    const split = str.split('');
    const vowPlacement = [];
    split.forEach(ch => {
        if (vowCheck(ch)) {
            vowPlacement.unshift(ch);
        }
    });
    return split.map(ch => {
        if (vowCheck(ch)) {
            return vowPlacement.shift();
        } else {
            return ch;
        }
    }).join('')
};