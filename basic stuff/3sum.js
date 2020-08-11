// 3 sum, given an array of numbers, return all triplets that sum to 0;
// Given array nums = [-1, 0, 1, 2, -1, -4],
// [
//   [-1, 0, 1],
//   [-1, -1, 2]
// ]
const threeSum = (nums, target=0) => {
  const result = [];

  if (nums.length < 3) return result;

  let sorted = nums.sort((el1, el2) => {
    if (el1 > el2) return 1;
    if (el2 > el1) return -1;
    return 0
  });

  for (let i = 0; i < sorted.length - 2; i++) {
    if (i === 0 || sorted[i] > sorted[i - 1]) {
      let start = i + 1;
      let end = sorted.length - 1;
      while (start < end) {
        if (sorted[start] + sorted[end] + sorted[i] === target) {
          result.push([sorted[i], sorted[start], sorted[end]]);
        }
  
        if (sorted[start] + sorted[end] + sorted[i] < target) {
          let curr_start = start;
          while (sorted[start] === sorted[curr_start]  && start < end) {
            start += 1;
          }
  
        } else {
          let curr_end = end;
          while (sorted[end] === sorted[curr_end] && start < end) {
            end -= 1;
          }
  
        }
      }
    }
  }
  return result;
}

console.log(threeSum([-1,0,1,2,-1,-4]));
