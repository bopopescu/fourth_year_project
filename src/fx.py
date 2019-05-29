import requests
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_absolute_error
from datetime import datetime, timedelta



def AddDates():
    eur_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey=x')
    eur_usd = eur_usd.json()
    eur_usd_prices = []

    gbp_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=USD&outputsize=full&apikey=x')
    gbp_usd = gbp_usd.json()
    gbp_usd_prices = []

    gbp_eur = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=EUR&outputsize=full&apikey=x')
    gbp_eur = gbp_eur.json()
    gbp_eur_prices = []

    eur_gbp = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=GBP&outputsize=full&apikey=x')
    eur_gbp = eur_gbp.json()
    eur_gbp_prices = []

# FX = Predictions
# FX1 = EUR/USD     FX2 = GBP/USD    FX3 = GBP/EUR    FX4 = EUR/GBP


    l = []
    today = datetime.today()
    str_today = today.strftime('%Y-%m-%d')
    stri = datetime.strptime(str_today, '%Y-%m-%d')
    with open('fx1.txt', 'r') as file:
        f = file.readlines()
        day = f[-1]
        day = day[:10]
        day = day.strip("\n")
        day = datetime.strptime(day, '%Y-%m-%d')
        file.close()
    i = 0
    while stri > day:
        #print(stri)
        today2 = datetime.today() - timedelta(days=i)
        str_today2 = today2.strftime('%Y-%m-%d')
        if str_today2 in str(eur_usd['Time Series FX (Daily)']):
            obj = eur_usd['Time Series FX (Daily)'][str_today2]['4. close']
            obj = float(obj)
            eur_usd_prices.append(obj)
        li = str_today2 + " , " + str(obj)
        l.append(li)
        i += 1
        stri = datetime.strptime(str_today, '%Y-%m-%d') - timedelta(days=i)
    for item in l[::-1]:
        with open('fx1.txt', 'a') as file2:
             file2.write(item)
             file2.write("\n")

    l = []
    today = datetime.today()
    str_today = today.strftime('%Y-%m-%d')
    stri = datetime.strptime(str_today, '%Y-%m-%d')
    with open('fx2.txt', 'r') as file:
        f = file.readlines()
        day = f[-1]
        day = day[:10]
        day = day.strip("\n")
        day = datetime.strptime(day, '%Y-%m-%d')
        file.close()
    i = 0
    while stri > day:
        #print(stri)
        today2 = datetime.today() - timedelta(days=i)
        str_today2 = today2.strftime('%Y-%m-%d')
        if str_today2 in str(gbp_usd['Time Series FX (Daily)']):
            obj = gbp_usd['Time Series FX (Daily)'][str_today2]['4. close']
            obj = float(obj)
            gbp_usd_prices.append(obj)
        li = str_today2 + " , " + str(obj)
        l.append(li)
        i += 1
        stri = datetime.strptime(str_today, '%Y-%m-%d') - timedelta(days=i)
    for item in l[::-1]:
        with open('fx2.txt', 'a') as file2:
            file2.write(item)
            file2.write("\n")

    l = []
    today = datetime.today()
    str_today = today.strftime('%Y-%m-%d')
    stri = datetime.strptime(str_today, '%Y-%m-%d')
    with open('fx3.txt', 'r') as file:
        f = file.readlines()
        day = f[-1]
        day = day[:10]
        day = day.strip("\n")
        day = datetime.strptime(day, '%Y-%m-%d')
        file.close()
    i = 0
    while stri > day:
        #print(stri)
        today2 = datetime.today() - timedelta(days=i)
        str_today2 = today2.strftime('%Y-%m-%d')
        if str_today2 in str(gbp_eur['Time Series FX (Daily)']):
            obj = gbp_eur['Time Series FX (Daily)'][str_today2]['4. close']
            obj = float(obj)
            gbp_eur_prices.append(obj)
        li = str_today2 + " , " + str(obj)
        l.append(li)
        i += 1
        stri = datetime.strptime(str_today, '%Y-%m-%d') - timedelta(days=i)
    for item in l[::-1]:
        with open('fx3.txt', 'a') as file2:
            file2.write(item)
            file2.write("\n")

    l = []
    today = datetime.today()
    str_today = today.strftime('%Y-%m-%d')
    stri = datetime.strptime(str_today, '%Y-%m-%d')
    with open('fx4.txt', 'r') as file:
        f = file.readlines()
        day = f[-1]
        day = day[:10]
        day = day.strip("\n")
        day = datetime.strptime(day, '%Y-%m-%d')
        file.close()
    i = 0
    while stri > day:
        #print(stri)
        today2 = datetime.today() - timedelta(days=i)
        str_today2 = today2.strftime('%Y-%m-%d')
        if str_today2 in str(eur_gbp['Time Series FX (Daily)']):
            obj = eur_gbp['Time Series FX (Daily)'][str_today2]['4. close']
            obj = float(obj)
            eur_gbp_prices.append(obj)
        li = str_today2 + " , " + str(obj)
        l.append(li)
        i += 1
        stri = datetime.strptime(str_today, '%Y-%m-%d') - timedelta(days=i)
    for item in l[::-1]:
        with open('fx4.txt', 'a') as file2:
            file2.write(item)
            file2.write("\n")

    return

# get data
def GetData():
    eur_usd_prices = []
    gbp_usd_prices = []
    gbp_eur_prices = []
    eur_gbp_prices = []
    days = []
    i = 0
    with open('fx1.txt', 'r') as file:
        f = file.readlines()
        while i < len(f):
            day = f[i]
            price = day[12:]
            day = day[:10]
            day = day.strip("\n")
            day = datetime.strptime(day, '%Y-%m-%d')
            days.append(day)
            price = price.strip("\n")
            price = price.strip()
            price = float(price)
            eur_usd_prices.append(price)
            i += 1
    j = 0
    with open('fx2.txt', 'r') as file:
        f = file.readlines()
        while j < len(f):
            day = f[j]
            price = day[12:]
            day = day[:10]
            day = day.strip("\n")
            day = datetime.strptime(day, '%Y-%m-%d')
            days.append(day)
            price = price.strip("\n")
            price = price.strip()
            price = float(price)
            gbp_usd_prices.append(price)
            j += 1
    k = 0
    with open('fx3.txt', 'r') as file:
        f = file.readlines()
        while k < len(f):
            day = f[k]
            price = day[12:]
            day = day[:10]
            day = day.strip("\n")
            day = datetime.strptime(day, '%Y-%m-%d')
            days.append(day)
            price = price.strip("\n")
            price = price.strip()
            price = float(price)
            gbp_eur_prices.append(price)
            k += 1
    l = 0
    with open('fx4.txt', 'r') as file:
        f = file.readlines()
        while l < len(f):
            day = f[l]
            price = day[12:]
            day = day[:10]
            day = day.strip("\n")
            day = datetime.strptime(day, '%Y-%m-%d')
            days.append(day)
            price = price.strip("\n")
            price = price.strip()
            price = float(price)
            eur_gbp_prices.append(price)
            l += 1

    context = {'eur_usd_prices':eur_usd_prices,'gbp_usd_prices':gbp_usd_prices,'gbp_eur_prices':gbp_eur_prices,'eur_gbp_prices':eur_gbp_prices}

    return eur_gbp_prices

# Function that calls ARIMA model to fit and forecast the data
def StartARIMAForecasting(Actual, P, D, Q):
    model = ARIMA(Actual, order=(P, D, Q))
    model_fit = model.fit(disp=0)
    prediction = model_fit.forecast()[0]
    return prediction

def main():
    AddDates()
    # Get exchange rates

    ActualData = GetData()
    # Size of exchange rates
    NumberOfElements = len(ActualData)
    #print(ActualData)

    # Use 90% of data as training, rest 10% to Test model
    TrainingSize = int(NumberOfElements * 0.9)
    TrainingData = ActualData[0:TrainingSize]
    TestData = ActualData[TrainingSize:NumberOfElements]

    # new arrays to store actual and predictions
    Actual = [x for x in TrainingData]
    Predictions = []

    # in a for loop, predict values using ARIMA model
    for timepoint in range(len(TestData)):
        ActualValue = TestData[timepoint]
        # forecast value
        Prediction = StartARIMAForecasting(Actual, 3, 1, 0)
        #print('Actual=%f, Predicted=%f' % (ActualValue, Prediction))
        # add it in the list
        Predictions.append(Prediction)
        Actual.append(ActualValue)

    # Print MAE to see accurate the model is
    pred = Predictions[-1][0]
    Error = mean_absolute_error(TestData, Predictions)
    print('Test Mean Absolute Error: %.3f' % Error)

    #plot
    #pyplot.plot(TestData)
    #pyplot.plot(Predictions, color='red')
    #pyplot.show()
    str_pred = str(pred)
    with open('fx.txt', 'a') as file2:
        file2.write(str_pred + "\n")
    return pred

if __name__ == '__main__':
    main()
