import io
import pandas as pd

fueldata = pd.read_csv("UpdatedFuelPrice-1773396000051.csv")
buffer = io.StringIO()
fueldata.info(buf=buffer)
with open("columns.txt","w") as file:
    file.write(buffer.getvalue())
file.close()
