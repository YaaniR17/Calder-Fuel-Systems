import io
import pandas as pd
fueldata = pd.read_csv("UpdatedFuelPrice-1773396000051.csv")
buffer = io.StringIO()
fueldata.info(buf=buffer)

brandnames = fueldata['forecourts.brand_name']

with open("brands.txt","w") as file:
    for name in brandnames:
        file.write(f"{brandnames}\n")
file.close()
