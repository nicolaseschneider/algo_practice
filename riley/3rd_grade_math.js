

const lcm = (num1, num2) => {
// least common multiple
    // const max = Math.max(num1, num2);
    // const min = Math.min(num1, num2);

    // let result = max;

    // while (result % min !== 0) {
    //     result += max;
    // }
    return (num1 * num2) / gcd(num1, num2);
    // return result
}



function gcd(x, y) {
    x = Math.abs(x);
    y = Math.abs(y);
    while(y) {
        // console.log({ x, y });
      var temp = y;
      y = x % y;
      x = temp;
    //   console.log({ x, y });
    }
    return x;
  }

console.log(lcm(12, 5)) //60

// console.log(gcd_two_numbers(8,12))

// lcm(a, b) * gcd(a, b) = a*b

// lcm(a,b) = a*b / gcd(a,b)