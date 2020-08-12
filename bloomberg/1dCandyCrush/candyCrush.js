// Write a function to crush candy in one dimensional board.
// In candy crushing games, groups of like items are removed from the board.
// In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. This process should be repeated as many time as possible.
// You should greedily remove characters from left to right.

// Example 1:

// Input: "aaabbbc"
// Output: "c"
// Explanation:
// 1. Remove 3 'a': "aaabbbc" => "bbbc"
// 2. Remove 3 'b': "bbbc" => "c"

// Example 2:

// Input: "aabbbacd"
// Output: "cd"
// Explanation:
// 1. Remove 3 'b': "aabbbacd" => "aaacd"
// 2. Remove 3 'a': "aaacd" => "cd"
// start: []
// 0: [{a: 1}]
// 1: [{a: 2}]
// 2: [{a: 2}, { b: 1 }] 
// 3: [{a: 2}, { b: 2 }]
// 4: []
// 4a: [{a: 2}, { b: 3 }]
// 5a: [{a: 3}] 
// 5: [{c: 1}]
// 6: [{c: 1}, {d: 1}];

// Input: "sssshbbcccbfff"
// output: "f"
// expla:
// 1. remove 4 's': "ssssbbcccbf" => "bbcccbf"
// 2. remove 3 'c': "bbcccbf" => "bbbf"
// 3. remove 3 'b': "bbbf" => 'f'

const candyCrush = (board) => {
  const stack = [];
  board.split('').forEach((char) => {
  // is the currentCharacter at the top of the stack?
    const top = stack[stack.length - 1];
    if (top && top.char === char) {
      const newTop = {...top, count: top.count + 1 }
      stack[stack.length - 1] = newTop;
    } else {
      if (top && top.count > 2) {
        stack.pop();
        const peek = stack[stack.length - 1];

        if (peek && peek.char === char) {
          const newTop = {...peek, count: peek.count + 1 }
          stack[stack.length - 1 ] = newTop;
        } else {
          stack.push({ char, count: 1 })  
        }
      } else {
        stack.push({ char, count: 1 });
      }
    }
  });

  if (stack[stack.length - 1].count > 2) stack.pop();
  return stack.reduce((acc, { count, char }) => {
    let newString = '';
    let i = 0
    while (i < count) {
      newString = newString + char;
      i++
    }
    return acc + char;
  }, '');
};

console.log(candyCrush('aaabbbc'));

console.log(candyCrush('aabbbacd'));

console.log(candyCrush('sssshbbcccbfff'));
