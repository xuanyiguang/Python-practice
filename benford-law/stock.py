import pandas as pd
import matplotlib.pyplot as plt
import re
import math

# # Data (csv file) downloaded from 
# # http://www.nasdaq.com/screening/company-list.aspx

if __name__ == "__main__":
    # # read csv file
    df = pd.read_csv('companylist_nyse.csv')
    # df = pd.read_csv('companylist_nasdaq.csv')

    # # choose the field to analyze
    field = 'LastSale' # price
    # field = 'MarketCap' # market size

    # # the digit to look at (1st digit => 0)
    digit = 0

    # # find the first (or second ...) non-zero digit
    pattern = r'[^1-9]'
    df['digit'] = map(
        lambda x: re.sub(pattern,'',str(x))[digit]
        if len(re.sub(pattern,'',str(x))) > digit else None,
        df[field])

    ptable = df.pivot_table(field,rows='digit',aggfunc=len)
    # # normalize count
    prop_table = pd.DataFrame(ptable / ptable.sum())

    # # probability according to Benford's Law
    prop_table['Benford Law'] = [math.log10(1+1.0/i) for i in range(1,10)]
    
    title_text = '{}{} Digit of {}'.format(
        digit+1,
        'st' if digit==0 else 'nd' if digit==1 else 'rd' if digit==2 else 'th',
        field)
    prop_table.plot(kind='bar',title=title_text)
    plt.show()

"""Findings

For NYSE and NASDAQ stocks:

- The first digit of LastSale (price) and MarketCap (total market value) closely follow Benford's Law.

- The only exception is the first digit of LastSale for NYSE stocks. Digit 2 seems to have much higher proportion (about double) than predicted by Benford's Law.

- The second and third digits of LastSale and MarketCap roughly follow a uniform distribution, very different from Benford's Law.
"""
