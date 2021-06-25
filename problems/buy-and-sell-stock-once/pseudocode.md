# Buy and sell stock once

## Problem pattern
"Bookkeeping of min/max"

## Strategy details

The maximum profit is the max delta between today's stock price and a previous day's stock price.

Since, according to the problem spec, we don't care which _particular_ day it was in the past, we can just track a "min price found (so far)" variable.

Similarly, we track a "max profit found (so far)" variable, and update that whenever we find a higher delta between today's price and the min price so far. 

That's it!

## State tables

### Example 1
Day|1|2|3|4|5
---|---|---|---|---|---|
**Price**|3|4|6|2|4
**Lowest price**|3|3|3|2|2
**Today profit**|0|1|3|0|2
**Highest profit**|0|1|3|3|3

---

### Example 2
Day|1|2|3|4|5|6|7|8
---|---|---|---|---|---|---|---|---|
**Price**|15|5|7|9|12|11|3|6
**Lowest price**|15|5|5|5|5|5|3|3
**Today profit**|0|0|2|4|7|6|0|3
**Highest profit**|0|0|2|4|7|7|7|7

