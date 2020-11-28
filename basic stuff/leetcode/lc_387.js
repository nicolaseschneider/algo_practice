var firstUniqChar = function(s) {
  const hash = {};
  const split = s.split('')
  split.forEach((char) => {
    if (hash[char]) {
      hash[char] += 1
    } else {
      hash[char] = 1
    }
  });
  let firstUnique = -1;
  split.forEach((ch, idx) => {
    if (hash[ch] === 1 && firstUnique < 0) {
      firstUnique = idx
    }
  })
  
  
  return firstUnique;
};