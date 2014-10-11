# Python-practice

Practice with Python

This repo is my sandbox for Python programming. Code is organized by folder, which is listed here.

## Benford's Law

I was introduced to this concept during the "Introduction to Data Science" class on Coursera. It is a very interesting proposition, so I decide to test it out using real world data.

Data on stock price and market value (in csv format) come from [here](http://www.nasdaq.com/screening/company-list.aspx). Analyzing the data, it seems for NYSE and NASDAQ stocks:

- The first digit of LastSale (price) and MarketCap (total market value) closely follow Benford's Law.

- The only exception is the first digit of LastSale for NYSE stocks. Digit 2 seems to have much higher proportion (about double) than predicted by Benford's Law.

- The second and third digits of LastSale and MarketCap roughly follow a uniform distribution, very different from Benford's Law.
