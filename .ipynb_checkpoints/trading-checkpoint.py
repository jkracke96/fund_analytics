import pandas as pd
import numpy as np

df = pd.read_csv("data/^990100-USD-STRD (1).csv")


df["daily_movement"] = df["Close"] / df["Open"] - 1
df["daily_movement_2x"] = df["daily_movement"] * 2
df["daily_movement_3x"] = df["daily_movement"] * 3
df = df.dropna(axis=0)

df = df.sort_values("daily_movement_3x", ascending=False)

print(df.tail())
