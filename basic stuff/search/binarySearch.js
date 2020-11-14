// the goal with binary search is to find an element within a sorted array in log n time.
// we accomplish this by dividing the sorted array in half and calling binarySearch recursively on the half that contains the target element;

const binarySearch = (sorted, target) => {

  if (sorted.length === 0) {
    return false
    // the target was not found
  }
  let midpoint;
  if (sorted.length % 2 === 0) {
    midpoint = sorted.length / 2;
  } else {
    midpoint = (sorted.length - 1) / 2;
  }
  if (sorted[midpoint] === target) {

    return true;
  } else if (sorted[midpoint] < target) {
    const searchWindow = sorted.slice(midpoint + 1, sorted.length);
    return binarySearch(searchWindow, target);
  } else {
    const searchWindow = sorted.slice(0, midpoint);

    return binarySearch(searchWindow, target);
  }
}

const test = [];

for (let i = 0; i < 101; i++) {
  test.push(i);
}

console.log(binarySearch(test, 50)); // true
console.log(binarySearch(test, 32)); // true
console.log(binarySearch(test, -2)); // false
console.log(binarySearch(test, 1001)); // false
console.log(binarySearch(test, 88)); // true