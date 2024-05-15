import yfinance as yf

data = yf.Ticker("EURUSD=X")
print(data.get_fast_info()["previousClose"])


print(86.33/79.56)

print(56.51/52.24)
print(86.33/1.09)
print("--------")


data = yf.Ticker("US9L.DU")
print(data.get_fast_info()["twoHundredDayAverage"])