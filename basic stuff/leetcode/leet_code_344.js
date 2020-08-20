var reverseString = function(s) {
  let end = s.length - 1;
  for (let start = 0; start < end; start++) {
      const temp = s[start];
      s[start] = s[end];
      s[end] = temp;
      end -= 1;
  }
};