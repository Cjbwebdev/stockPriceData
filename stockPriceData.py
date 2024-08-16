import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Define the tickers and date range
tickers = ['SPY', 'GLD', 'TSLA']
end_date = datetime.today()
start_date = end_date - timedelta(days=2*365)

# Create a DataFrame to store the closing prices
close_df = pd.DataFrame()

# Fetch the data and store it in the DataFrame
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_df[ticker] = data['Close']

# Save the DataFrame to a CSV file
close_df.to_csv('stock_prices.csv')

# Plot the closing prices
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(close_df.index, close_df[ticker], label=ticker)

# Customize the chart
plt.title('Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

# Optional: Save the plot as an image file
plt.savefig('stock_prices_chart.png')
