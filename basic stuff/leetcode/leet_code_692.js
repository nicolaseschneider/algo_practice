

const hashWords = (words, hash) => {
  words.forEach(word => {
    if (hash[word]) {
      hash[word] += 1;
    } else {
      hash[word] = 1;
    }
  });
}
var topKFrequent = function(words, k) {
  const hash = {};
  hashWords(words, hash);
  // {
  //   word: 'word',
  //   count: 1,
  // }
  const wordObjs = Object.keys(hash).map(word => {
    return {
      word,
      count: hash[word]
    }
  }); 

  const sorted = wordObjs.sort((word1, word2) => {
    if (word1.count > word2.count) {
      return -1;
    } else if (word1.count < word2.count) {
      return 1;
    } else if (word1.count === word2.count) {
      if (word1.word > word2.word) {
        return 1;
      }
      return -1;
    }
  }).slice(0, k);
  
  return sorted.map(wordObj => {
    return wordObj.word
  })

};