function buy_and_sell_stock_once(prices){
    var min_final = prices[0];
    var max_final = 0;
    prices.forEach(price => {
        var max_temp = price - min_final < 0 ? price - min_final : price;
        max_final = Math.max(max_final, max_temp);
        min_final = Math.min(min_final,price);
    })
    return max_final;
  }
  