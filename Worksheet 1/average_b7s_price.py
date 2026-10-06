import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.fuel_price.B7S'])

fuel.columns = ['B7S_Price']
fuel = fuel.dropna(subset=['B7S_Price'])

price_counts = fuel['B7S_Price'].value_counts().sort_index()
national_avg = fuel['B7S_Price'].mean()
print(f"The average B7S price is: {national_avg:.2f}")

price_counts.plot(kind='bar')
plt.title("Number of Forecourts per B7S Price Point")
plt.xlabel("Price (B7S)")
plt.ylabel("Number of Forecourts")
plt.show()
