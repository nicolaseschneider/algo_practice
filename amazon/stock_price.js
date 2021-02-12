stonk_prices = [10, 7, 5, 8, 11, 9, 1];

const getDatPaper = (stonks) => {
    let maxProfit = -Infinity;
    let buyPoint = Infinity;
    for (stonk in stonks) {
        buyPoint = Math.min(buyPoint, stonk);
        maxProfit = Math.max(maxProfit, stonk - buyPoint);
    }
    return maxProfit;
}

function maxProfit(stonks) {
    return stonk_prices.reduce((prev, cur, idx) => {
        console.log(prev, cur, idx);
        return Math.max(stonk_prices.slice(idx, stonk_prices.length)
            .reduce((p2, c2) => c2 > p2 ? c2 : p2) - cur, prev)
        }, 0)
}


console.log(maxProfit(stonk_prices)); // 6
