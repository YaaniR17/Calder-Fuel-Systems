import pandas as pd
import io

fueldata = pd.read_csv("UpdatedFuelPrice-1773396000051.csv")

buffer = io.StringIO()
fueldata.info(buf=buffer)
with open("columns.txt", "w") as file:
    file.write(buffer.getvalue())

brandnames = fueldata['forecourts.brand_name'].unique()
with open("brands.txt", "w") as file:
    for name in brandnames:
        file.write(f"{name}\n")

tescofuel = fueldata[fueldata["forecourts.brand_name"] == "TESCO"]
tescofuel.head()

bradford = fueldata[fueldata['forecourts.location.postcode'].str.contains(r"^BD\d{1,2}\s", regex=True, na=False)]
bradford.to_csv('bradford2.csv', index=False)

print(f"{len(bradford)} locations in Bradford.")
