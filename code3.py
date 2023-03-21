import pandas as pd
df = pd.read_json("phone_details.json")
df["price"] = df["price"].apply(lambda x:int(x.replace(",","")))
df["id"] = df.index
df.to_json("data.json",orient="records",indent=4,index=True)
