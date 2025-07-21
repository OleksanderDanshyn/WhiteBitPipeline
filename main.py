
import time

import requests
import pandas as pd


def get_market_mood(change, volume):
    change = float(change)
    volume = float(volume)

    if change > 5 and volume > 1000:
        return "Euphoria (Strong Bullish)"
    elif change > 1 and volume > 100:
        return "Bullish"
    elif change > 1:
        return "Weak Bullish"
    elif -1 <= change <= 1:
        return "Neutral"
    elif change < -5 and volume > 1000:
        return "Panic Selling (Strong Bearish)"
    elif change < -1 and volume > 100:
        return "Bearish"
    elif change < -1:
        return "Weak Bearish"
    else:
        return "Uncertain"


for i in range(10):
    market_activity = requests.get("https://whitebit.com/api/v4/public/ticker")
    data = market_activity.json()
    time_now = time.strftime("%H:%M:%S", time.localtime())
    df = pd.DataFrame(data).T

    row_names = list(df.index)
    df = df[df.index.str.endswith("_UAH")]
    max_row = df[df["change"] == df["change"].max()]
    selected_columns = max_row[["last_price", "base_volume", "change"]]

    change = max_row["change"].iloc[0]
    volume = max_row["base_volume"].iloc[0]
    mood = get_market_mood(change, volume)

    print(time_now)
    print(selected_columns)
    print(mood)
    time.sleep(1)