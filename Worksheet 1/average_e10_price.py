import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.fuel_price.E10'])

fuel.columns = ['E10_Price']
fuel = fuel.dropna(subset=['E10_Price'])

price_counts = fuel['E10_Price'].value_counts().sort_index()
national_avg = fuel['E10_Price'].mean()
print(f"The average E10 price is: {national_avg:.2f}")

price_counts.plot(kind='bar')
plt.title("Number of Forecourts per E10 Price Point")
plt.xlabel("Price (E10)")
plt.ylabel("Number of Forecourts")
plt.show()
