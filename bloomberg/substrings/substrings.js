// Given a string print all subsets (not permutations)
// Eg. String "abc" should output
// empty string
// a
// b
// c
// ab
// bc
// ac
// abc

// CANT DO FOREACH ON A STRING IN JS

const stringSubset = (string) => {
  const result = [];
  helper(string, result, [], 0);
  return result;
}
const helper = (string, resArr, curSubset, currIdx) => {
  console.log([...curSubset].join(''));
  resArr.push([...curSubset].join(''));
  for (let i = currIdx; i < string.length; i++) {
    curSubset.push(string[i]);
    helper(string, resArr, curSubset, i + 1);
    curSubset.pop();
  }
};

console.log((stringSubset('abc')));

console.log((stringSubset('abcdef')));

console.log((stringSubset('abbba')));
// time complexity is 2^n