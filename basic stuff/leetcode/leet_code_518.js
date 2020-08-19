// Work through this problem on https://leetcode.com/problems/coin-change-2/ and use the specs given there.
// Feel free to use this file for scratch work.

const numChange = (coins, amount, memo = {}) => {
  let key = amount + '-' + coins
  if (memo[key]) return memo[key]
  if (amount === 0) return 1;
  const currentCoin = coins[coins.length - 1];
  let total = 0
  for(let qty = 0; qty * currentCoin <= amount ; qty++) {
    const check = amount - qty * currentCoin;
    const change = numChange(coins.slice(0,-1), check, memo);
    total += change;
  }
  memo[key] = total;
  return total
}
console.log(numChange([1,2,5], 5));