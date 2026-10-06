import pandas as pd
import matplotlib.pyplot as plt

fuel = pd.read_csv("UpdatedFuelPrice-1773396000051.csv", usecols=['forecourts.location.city', 'forecourts.fuel_price.B7S', 'forecourts.fuel_price.B7P'])

fuel['forecourts.location.city'] = fuel['forecourts.location.city'].str.strip().str.title()
halifax_fuel = fuel[fuel['forecourts.location.city'] == 'Halifax'].copy()

halifax_fuel.columns = ['City', 'B7S_Price', 'B7P_Price']

b7s_counts = halifax_fuel['B7S_Price'].value_counts().sort_index()
b7p_counts = halifax_fuel['B7P_Price'].value_counts().sort_index()

print(f"The average B7S price in Halifax is: {halifax_fuel['B7S_Price'].mean():.2f}")
print(f"The average B7P price in Halifax is: {halifax_fuel['B7P_Price'].mean():.2f}")

b7s_counts.plot(kind='line', marker='o', label='B7S Diesel')
b7p_counts.plot(kind='line', marker='s', label='B7P Diesel (Premium)')

plt.title("Number of Forecourts per Price Point (Halifax)")
plt.xlabel("Price (pence)")
plt.ylabel("Number of Forecourts")
plt.show()
