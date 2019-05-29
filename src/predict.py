import urllib.request, urllib.error, urllib.parse
import time
import requests
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc
import matplotlib
import pylab

matplotlib.rcParams.update({'font.size': 9})


def rsiFunc(stocks, n=14):
    deltas = np.diff(stocks)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(stocks)
    rsi[:n] = 100. - 100. / (1. + rs)

    for i in range(n, len(stocks)):
        delta = deltas[i - 1]  # cause the diff is 1 shorter

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n

        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)
    #print(rsi[-1])
    return rsi[-1]


def movingaverage(values, window):
    weigths = np.repeat(1.0, window) / window
    smas = np.convolve(values, weigths, 'valid')
    return smas  # as a numpy array


def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a = np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    a = a.tolist()
    #print(a)
    return a


def computeMACD(x, slow=26, fast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    emaslow = ExpMovingAverage(x, slow)
    emafast = ExpMovingAverage(x, fast)
    #emadif = emafast - emaslow
    #print(emaslow,emafast)
    btc_macd_dif = []
    j = 0
    while j < len(emafast):
        dif = emafast[j] - emaslow[j]
        btc_macd_dif.append(dif)
        j += 1
    btc_macd_cotrol = ExpMovingAverage(btc_macd_dif, 9)
    context = {'btc_macd_dif': btc_macd_dif, 'btc_macd_cotrol': btc_macd_cotrol}
    return context



def getData():
    headers = {'authorization': 'Apikey {5fd159fba0ac5f6c57a7408f616c83e708847738a64f5a0d80ce1d21d173aafc}'}
    btc_endpoint = 'https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=EUR&limit=100'
    btc_response = requests.get(btc_endpoint, headers=headers)
    btc_string = btc_response.json()
    i = 0
    btc_prices = []
    times = []
    eth_prices = []

    eth_endpoint = 'https://min-api.cryptocompare.com/data/histoday?fsym=ETH&tsym=EUR&limit=100'
    eth_response = requests.get(eth_endpoint, headers=headers)
    eth_string = eth_response.json()

    while i <= 100:
        btc_price = float(btc_string['Data'][i]['open'])
        time = btc_string['Data'][i]['time']
        btc_prices.append(btc_price)

        eth_price = float(eth_string['Data'][i]['open'])
        eth_prices.append(eth_price)
        i += 1
        times.append(time)
    stocks = [btc_prices,eth_prices]
    return(stocks)

def main():
    stocks = getData()
    btc = stocks[0]
    eth = stocks[1]
    #rsiFunc(btc, 14)
    #computeMACD(btc)
    #a = [0.0, 0.3181818181818182, 0.0, 0.0, 0.0, 0.4333333333333333, 0.4333333333333333, 0.0, -0.1, 0.03888888888888886, -0.04666666666666666, 0.7125, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3211111111111111, 0.4, 0.041666666666666664, -0.2333333333333333, 0.16666666666666666, 0.26666666666666666, 0.0, 0.0, 0.0, 0.4333333333333333, 0.0, 0.19119318181818182, 0.0, 0.0, -0.25, -0.25, 0.425, 0.26666666666666666, -0.5, 0.5, 0.0, 0.06666666666666665, 0.012500000000000004, 0.1, 0.17222222222222222, 0.0, 0.0, 0.0, 0.3, 0.0, 0.5, 0.03125, 0.375, 0.0, 0.0, 0.0, 0.270995670995671, 0.3333333333333333, 0.13636363636363635, 0.270995670995671, 0.270995670995671, 0.270995670995671, 0.016666666666666677, 0.0, 0.16666666666666666, 0.0, 0.0, 0.06666666666666665, 0.0, -0.1625, 0.0, 0.4, 0.0, 0.270995670995671, 0.270995670995671, 0.0, 0.270995670995671, 0.270995670995671, 0.4, -0.05, 0.4, 0.0, 0.0, 0.0, 0.3, 0.8, 0.4, 0.0, -0.2333333333333333, 0.0, 0.0, -0.020833333333333332, 0.0, -0.03181818181818183, 0.7, 0.0, -0.005555555555555573, -0.12222222222222216, -0.03181818181818183, 0.0]
    #movingaverage(a,26)



if __name__ == '__main__':
    main()