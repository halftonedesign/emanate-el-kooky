"""
You are given a list of stock prices.

Assume (unrealistically) there's only one stock price for each entire day.

What's the max profit you can make? 
"""
def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit