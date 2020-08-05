// There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

// Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

// Example 1:

// Input: [[10,20],[30,200],[400,50],[30,20]]
// Output: 110
// Explanation: 
// The first person goes to city A for a cost of 10.
// The second person goes to city A for a cost of 30.
// The third person goes to city B for a cost of 50.
// The fourth person goes to city B for a cost of 20.

// The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

// Note:

// 1 <= costs.length <= 100
// It is guaranteed that costs.length is even.
// 1 <= costs[i][0], costs[i][1] <= 1000

// Leetcode #1029

// TODO HEAP IT UP

// EXACTLY N candidates to city A
// Exactly N candidates to city B

// sorting by either value doesnt work
// sort by how much you save from going to either city A or City B

// ex1 by city A savings: 10, 270, -350, -10
// sorted: 270, 10, -10, -350

// thereby the first N/2 elements will be the maximum profit for city A.
// we MUST assign N/2 people to city A

// Time Complexity is nLogn, as you simply sort;

const findCosts = (costs) => {
  let cityATotal = 0;
  let cityBTotal = 0;
  // sort by profit margin
  const sortByMargin = costs.sort((
    [cityA1, cityB1],
    [cityA2, cityB2]
    ) => ((cityB2 - cityA2) - (cityB1 - cityA1)));

    for (let i = 0; i < costs.length; i++) {
      if (i < costs.length / 2) {
        // city A has better profit
        cityATotal += sortByMargin[i][0];
      } else {
        // city B has better profit
        cityBTotal += sortByMargin[i][1];
      }
    }
    return cityATotal + cityBTotal;
}

console.log(findCosts([
  [10, 20],
  [30, 200],
  [400, 50],
  [30, 20],
])); // should return 110

console.log(findCosts([
  [20, 60],
  [10, 50],
  [30, 300],
  [40, 200],
])); // should return 180

// Sort
