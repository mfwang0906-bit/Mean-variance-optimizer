# Mean-variance-optimizer
finding the best way to allocate your investment portfolio funds, using the most statistically backed up way 

This optimizer aims to pull historical data and estimate a value of your return as well as the volatility. It does not take into account any special events happening (financial crisis, signing new deals, etc). It calculates a sharpe value, Sharpe = (Your Return - Risk Free Return) / Volatility. Where using past years data, we can estimate a mean return, and also calculating the volatility using a covariance matrix. Take note that I am hard coding the risk free rate to be 4% (the US treasury yield).

then my model tries to follow this flow to plot out the set of sharpe values with the following flow:

Randomly split money across 5 stocks

Calculate what return that split would have given historically

Calculate how volatile that split would have been

Compute Sharpe = return / volatility

Record that as one dot on the graph

Repeat 10,000 times

Find the dot with the highest Sharpe

--------------------------------------------------------------

some limitations i noticed but haven't improved:

Backward-looking model: assumes future behaviour mirrors historical data

Monte Carlo gives slightly different weights each run due to randomness

---------------------------------------------------------------

ps. this is just a pet/passion project, feel free to let me know any other areas of improvements doing this because i am an active trader in my own time, as well as an undergraduate studying EEE, looking to specialise in software!
