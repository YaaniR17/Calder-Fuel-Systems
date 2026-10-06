import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.fuel_price.B7P'])

fuel.columns = ['B7P_Price']
fuel = fuel.dropna(subset=['B7P_Price'])

price_counts = fuel['B7P_Price'].value_counts().sort_index()
national_avg = fuel['B7P_Price'].mean()
print(f"The average B7P price is: {national_avg:.2f}")

price_counts.plot(kind='bar')
plt.title("Number of Forecourts per B7P Price Point")
plt.xlabel("Price (B7P)")
plt.ylabel("Number of Forecourts")
plt.show()
