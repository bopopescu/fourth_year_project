import requests
from datetime import datetime, timedelta



def main():
    eur_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=compact&apikey=IDXOCTF8K0T83A2A')
    eur_usd = eur_usd.json()
    eur_usd_prices = []

    gbp_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=USD&outputsize=compact&apikey=IDXOCTF8K0T83A2A')
    gbp_usd = gbp_usd.json()
    gbp_usd_prices = []

    gbp_eur = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=EUR&outputsize=compact&apikey=IDXOCTF8K0T83A2A')
    gbp_eur = gbp_eur.json()
    gbp_eur_prices = []

    eur_gbp = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=GBP&outputsize=compact&apikey=IDXOCTF8K0T83A2A')
    eur_gbp = eur_gbp.json()
    eur_gbp_prices = []

    days = []
    i = 0
    for element in eur_usd['Time Series FX (Daily)']:
        today = datetime.today() - timedelta(days=i)
        today = today.strftime('%Y-%m-%d')
        try:
            if today in str(eur_usd['Time Series FX (Daily)']):
                days.append(today)
                obj = eur_usd['Time Series FX (Daily)'][today]['1. open']
                obj = float(obj)
                eur_usd_prices.append(obj)

                obj1 = gbp_usd['Time Series FX (Daily)'][today]['1. open']
                obj1 = float(obj1)
                gbp_usd_prices.append(obj1)

                obj2 = gbp_eur['Time Series FX (Daily)'][today]['1. open']
                obj2 = float(obj2)
                gbp_eur_prices.append(obj2)

                obj3 = eur_gbp['Time Series FX (Daily)'][today]['1. open']
                obj3 = float(obj3)
                eur_gbp_prices.append(obj3)
                i += 1
            else:
                i += 1
        except KeyError:
            i += 1
            pass
    prices = []
    prices.append(eur_usd_prices)
    prices.append(gbp_usd_prices)
    prices.append(eur_gbp_prices)
    with open('fx.txt', 'w') as file:
        file.write(prices)
    return prices

if __name__ == '__main__':
    main()