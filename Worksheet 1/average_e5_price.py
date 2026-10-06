import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.fuel_price.E5'])

fuel.columns = ['E5_Price']
fuel = fuel.dropna(subset=['E5_Price'])

price_counts = fuel['E5_Price'].value_counts().sort_index()
national_avg = fuel['E5_Price'].mean()
print(f"The average E5 price is: {national_avg:.2f}")

price_counts.plot(kind='bar')
plt.title("Number of Forecourts per E5 Price Point")
plt.xlabel("Price (E5)")
plt.ylabel("Number of Forecourts")
plt.show()
