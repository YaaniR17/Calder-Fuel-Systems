import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.location.city', 'forecourts.fuel_price.E10', 'forecourts.fuel_price.E5'])

fuel['forecourts.location.city'] = fuel['forecourts.location.city'].str.strip().str.title()
halifax_fuel = fuel[fuel['forecourts.location.city'] == 'Halifax'].copy()

halifax_fuel.columns = ['City', 'E10_Price', 'E5_Price']

e10_counts = halifax_fuel['E10_Price'].value_counts().sort_index()
e5_counts = halifax_fuel['E5_Price'].value_counts().sort_index()

print(f"The average E10 price in Halifax is: {halifax_fuel['E10_Price'].mean():.2f}")
print(f"The average E5 price in Halifax is: {halifax_fuel['E5_Price'].mean():.2f}")

plt.figure(figsize=(10, 6))

e10_counts.plot(kind='line', marker='o', label='E10 Petrol')
e5_counts.plot(kind='line', marker='s', label='E5 Petrol (Premium)')

plt.title("Number of Forecourts per Price Point (Halifax)")
plt.xlabel("Price (pence)")
plt.ylabel("Number of Forecourts")
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
