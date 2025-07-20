
import time

import requests
import pandas as pd

for i in range(10):
    market_activity = requests.get("https://whitebit.com/api/v4/public/ticker")
    data = market_activity.json()
    time_now = time.strftime("%H:%M:%S", time.localtime())
    df = pd.DataFrame(data).T

    row_names = list(df.index)
    df = df[df.index.str.endswith("_PLN")]
    max_row = df[df["change"] == df["change"].max()]
    selected_columns = max_row[["last_price", "base_volume", "change"]]

    print(selected_columns)
    print(time_now)
    time.sleep(1)