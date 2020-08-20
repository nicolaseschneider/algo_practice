def numChange(coins, amount):
  table = [0] * (amount + 1);
  table[0] = 1
  for coin in coins:
    i = coin;
    while i < len(table):
      table[i] += table[i - coin]
      i += 1
  return table[amount]


print(numChange([1,2,5], 5))

# any given idex in the array is going to store the number of ways to make change from that index
