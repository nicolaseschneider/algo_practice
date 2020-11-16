// https://www.hackerrank.com/challenges/ctci-ransom-note/problem

const hashMag = (mag, hash) => {
  mag.forEach((word) => {
    if (hash[word]) {
      hash[word] += 1;
    } else {
      hash[word] = 1;
    }
  })
}

function checkMagazine(magazine, note) {
  const magazineHash = {}

  hashMag(magazine, magazineHash);

  note.forEach((word) => {
    if (magazineHash[word]) {
      magazineHash[word] -= 1;
    } else {
      return 'no'
    }
  })
  return 'yes'
}