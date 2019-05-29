import requests
from django.shortcuts import (render, redirect)
from django.http import (Http404, HttpResponse, HttpResponseRedirect)
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, authenticate, get_user_model)
from django.template import loader
from .forms import EditProfileForm
from .models import UserDetails
from datetime import datetime, timedelta
from textblob import TextBlob
import tweepy
from predict import rsiFunc, computeMACD
#import oandapyV20
#import oandapyV20.endpoints.orders as orders
#from coinbase.wallet.client import Client
#from coinbase.wallet.client import OAuthClient


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

def index(request):
    latest_user_list = User.objects.order_by('-date_added')[:5]
    template = loader.get_template('smartpredict/index.html')
    now = datetime.now()
    time = "It is now %s." % now

    return render(request, 'smartpredict/index.html', {'content': [time, latest_user_list]})
    #CURL REQUESTS https://curl.trillworks.com/

def sentiment(request):
    consumer_key = 'x'
    consumer_secret = 'x'
    access_token = 'x-x'
    access_secret = 'x'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    tweets = []
    for tweet in tweepy.Cursor(api.search, q='bitcoin', lang='en', tweet_mode='extended').items(100):
        # Defining Tweets Creators Name
        tweettext = str(tweet.full_text.lower().encode('ascii', errors='ignore'))  # encoding to get rid of characters that may not be able to be displayed
        tweets.append(tweettext)

    sent = 0
    good = []
    bad = []
    neutral = []
    for tweet in tweets:
        analysis = TextBlob(tweet)
        score = analysis.sentiment.polarity
        sent += score
        if score > 0.1:
            good.append(score)
        elif score < -0.1:
            bad.append(score)
        else:
            neutral.append(score)

    sents = []
    sents.append(len(good))
    sents.append(len(bad))
    sents.append(len(neutral))

    return render(request, 'smartpredict/sentiment.html', {'sents': sents, 'sent':sent})

@login_required()
def dashboard(request):
    now = datetime.now()
    time = "It is now %s." % now
    return render(request, 'smartpredict/dashboard.html', {'time': time})


@login_required
def cryptodashboard(request):

    headers = {'authorization': 'Apikey {x}'}

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

    eth_current = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,JPY,EUR'
    eth_current = requests.get(eth_current, headers=headers)
    eth_current = eth_current.json()
    eth_current = eth_current['EUR']
    eth_current = float(eth_current)
    eth_message = 'Current Ethereum price: €%.2f' % eth_current

    btc_current = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    btc_current = requests.get(btc_current, headers=headers)
    btc_current = btc_current.json()
    btc_current = btc_current['EUR']
    btc_current = str(round(btc_current, 2))


    while i <= 100:
        btc_price = float(btc_string['Data'][i]['close'])
        time = btc_string['Data'][i]['time']
        btc_prices.append(btc_price)

        eth_price = float(eth_string['Data'][i]['close'])
        eth_prices.append(eth_price)
        i += 1
        time = datetime.fromtimestamp(time).isoformat()
        time = time[:10]
        time = str(time)
        times.append(time)
    btc_rsi = float(rsiFunc(btc_prices, 14))
    btc_rsi = round(btc_rsi, 2)
    eth_rsi = float(rsiFunc(eth_prices, 14))
    eth_rsi = round(eth_rsi, 2)
    btc_macd = computeMACD(btc_prices)
    btc_macd_dif = btc_macd['btc_macd_dif']
    btc_macd_signal = btc_macd['btc_macd_cotrol']
    with open('pred.txt', 'r') as file:
        lines = file.readlines()
    prediction = lines[-1]

    consumer_key = 'HF9ENJeHDmsvE2vdOd2hgdcue'
    consumer_secret = '1i7w1EUNlQmGwvFUCMQ9KHq5fCOikilWIBBIyNgxzmVwo7e5vA'
    access_token = '2768999237-ae9azJ4K2arDP8qDNyzcmSu6Dkwhw7zFlOOe61T'
    access_secret = 'WuLkjuFQKMvUsIgKFSEUarsfnwRq83kBAE6qUOpttnQ1b'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    btc_tweets = []
    for btc_tweet in tweepy.Cursor(api.search, q='bitcoin', lang='en', tweet_mode='extended').items(100):
        # Defining Tweets Creators Name
        tweettext = str(btc_tweet.full_text.lower().encode('ascii', errors='ignore'))  # encoding to get rid of characters that may not be able to be displayed
        btc_tweets.append(tweettext)

    btc_sent = 0
    btc_good = []
    btc_bad = []
    btc_neutral = []
    for tweet in btc_tweets:
        analysis = TextBlob(tweet)
        btc_score = analysis.sentiment.polarity
        btc_sent += btc_score
        if btc_score > 0.05:
            btc_good.append(btc_score)
        elif btc_score < -0.05:
            btc_bad.append(btc_score)
        else:
            btc_neutral.append(btc_score)
    btc_sent = round(btc_sent, 2)
    btc_sents = []
    btc_sents.append(len(btc_good))
    btc_sents.append(len(btc_bad))
    btc_sents.append(len(btc_neutral))

    api2 = tweepy.API(auth)
    eth_tweets = []
    for eth_tweet in tweepy.Cursor(api2.search, q='ethereum', lang='en', tweet_mode='extended').items(100):
        # Defining Tweets Creators Name
        tweettext = str(eth_tweet.full_text.lower().encode('ascii', errors='ignore'))  # encoding to get rid of characters that may not be able to be displayed
        eth_tweets.append(tweettext)

    eth_sent = 0
    eth_good = []
    eth_bad = []
    eth_neutral = []
    for tweet in eth_tweets:
        analysis = TextBlob(tweet)
        eth_score = analysis.sentiment.polarity
        eth_sent += eth_score
        if eth_score > 0.05:
            eth_good.append(eth_score)
        elif eth_score < -0.05:
            eth_bad.append(eth_score)
        else:
            eth_neutral.append(eth_score)
    eth_sent = round(eth_sent, 2)
    eth_sents = []
    eth_sents.append(len(eth_good))
    eth_sents.append(len(eth_bad))
    eth_sents.append(len(eth_neutral))
    print(eth_sent,eth_sents)

    return render(request, 'smartpredict/cryptodashboard.html', {'eth_sent':eth_sent, 'eth_sents':eth_sents, 'eth_current':eth_current, 'btc_sents':btc_sents, 'btc_sent':btc_sent, 'btc_macd_dif': btc_macd_dif, 'btc_macd_signal':btc_macd_signal, 'prediction':prediction, 'eth_rsi':eth_rsi, 'btc_rsi':btc_rsi, 'times': times, 'btc_prices': btc_prices, 'eth_prices': eth_prices, 'btc_current': btc_current, 'eth_message': eth_message})


@login_required
def forexdashboard(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer x-x',
    }

    head = {'authorization': 'Apikey {x}'}

    response = requests.get('https://api-fxtrade.oanda.com/v3/accounts/001-004-x-x/pricing?instruments=EUR_USD%2CGBP_USD', headers=headers)
    string = response.json()
    string1 = string['prices'][0]['bids'][0]['price']
    current_eur_usd = round(float(string1), 2)

    string2 = string['prices'][1]['bids'][0]['price']
    current_gbp_usd = round(float(string2), 2)


    eur_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=x')
    eur_usd = eur_usd.json()
    eur_usd_prices = []

    gbp_usd = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=USD&apikey=x')
    gbp_usd = gbp_usd.json()
    gbp_usd_prices = []

    gbp_eur = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=EUR&apikey=x')
    gbp_eur = gbp_eur.json()
    gbp_eur_prices = []

    eur_gbp = requests.get('https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=GBP&apikey=x')
    eur_gbp = eur_gbp.json()
    eur_gbp_prices = []

    price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=EUR&tsyms=GBP', headers=head)
    price = price.json()
    eur_gbp_current = round(float(price['GBP']), 2)

    price2 = requests.get('https://min-api.cryptocompare.com/data/price?fsym=GBP&tsyms=EUR', headers=head)
    price2 = price2.json()
    gbp_eur_current = round(float(price2['EUR']), 2)

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
    try:
        eur_usd_rsi = round(float(rsiFunc(eur_usd_prices, 14)), 2)
    except IndexError:
        eur_usd_rsi = 45
    try:
        gbp_usd_rsi = round(float(rsiFunc(gbp_usd_prices, 14)), 2)
    except IndexError:
        gbp_usd_rsi = 45
    try:
        gbp_eur_rsi = round(float(rsiFunc(gbp_eur_prices, 14)), 2)
    except IndexError:
        gbp_eur_rsi = 45
    try:
        eur_gbp_rsi = round(float(rsiFunc(eur_gbp_prices, 14)), 2)
    except IndexError:
        eur_gbp_rsi = 45
    with open('fx.txt', 'r') as file:
        f = file.readlines()
        eur_usd_price = f[-4]
        eur_usd_price = eur_usd_price.strip("\n")
        eur_usd_price = eur_usd_price.strip()
        pred_eur_usd_price = round(float(eur_usd_price), 2)
        gbp_usd_price = f[-3]
        gbp_usd_price = gbp_usd_price.strip("\n")
        gbp_usd_price = gbp_usd_price.strip()
        pred_gbp_usd_price = round(float(gbp_usd_price), 2)
        gbp_eur_price = f[-2]
        gbp_eur_price = gbp_eur_price.strip("\n")
        gbp_eur_price = gbp_eur_price.strip()
        gbp_eur_price = round(float(gbp_eur_price), 2)
        pred_gbp_eur_price = round(float(gbp_eur_price), 2)
        eur_gbp_price = f[-1]
        eur_gbp_price = eur_gbp_price.strip("\n")
        eur_gbp_price = eur_gbp_price.strip()
        pred_eur_gbp_price = round(float(eur_gbp_price), 2)

    consumer_key = 'x'
    consumer_secret = 'x'
    access_token = 'x-x'
    access_secret = 'x'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    tweets = []
    for tweet in tweepy.Cursor(api.search, q='forex', lang='en', tweet_mode='extended').items(100):
        # Defining Tweets Creators Name
        tweettext = str(tweet.full_text.lower().encode('ascii', errors='ignore'))  # encoding to get rid of characters that may not be able to be displayed
        tweets.append(tweettext)
    s = []
    sent = 0
    good = 0
    bad = 0
    neutral = 0
    for tweet in tweets:
        analysis = TextBlob(tweet)
        score = analysis.sentiment.polarity
        sent += score
        s.append(score)
        if score > 0:
            good += 1
        elif score < 0:
            bad += 1
        else:
            neutral += 1
    sents = []
    sents.append(good)
    sents.append(bad)
    sents.append(neutral)

    return render(request, 'smartpredict/forexdashboard.html', {'gbp_eur_current':gbp_eur_current, 'eur_gbp_current':eur_gbp_current, 'sent':sent, 'sents':sents, 'pred_eur_gbp_price':pred_eur_gbp_price, 'pred_gbp_eur_price':pred_gbp_eur_price, 'eur_usd_rsi':eur_usd_rsi, 'gbp_usd_rsi':gbp_usd_rsi, 'gbp_eur_rsi':gbp_eur_rsi, 'eur_gbp_rsi':eur_gbp_rsi, 'pred_eur_usd_price':pred_eur_usd_price, 'pred_gbp_usd_price':pred_gbp_usd_price, 'current_eur_usd': current_eur_usd, 'current_gbp_usd': current_gbp_usd, 'days': days, 'eur_usd_prices': eur_usd_prices, 'gbp_usd_prices': gbp_usd_prices, 'gbp_eur_prices': gbp_eur_prices, 'eur_gbp_prices': eur_gbp_prices})

def apiconnect(request):

    now = datetime.now()
    time = "It is now %s." % now

    return render(request, 'smartpredict/apiconnect.html', {'content':[time]})

def forex(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer xx-xxx',
    }

    data = {
        "order": {
            "units": "1",
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
        }
    }

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            api_key = form.cleaned_data['forex_api']
            form.save()
            return redirect('/smartpredict/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'smartpredict/forex.html', args)


def crypto(request):
    url = 'https://www.coinbase.com/oauth/authorize?client_id=x&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fsmartpredict%2Foauth%2Fcoinbaseredirect%2F&response_type=code&scope=wallet%3Auser%3Aread'
    response = requests.get(url)

    return HttpResponse(response)

def about(request):
    print(UserDetails.objects.all())
    latest_user_list = UserDetails.objects.order_by('-date_added')[:5]
    print(latest_user_list)
    return render(request, 'smartpredict/about.html', {'latest_user_list': latest_user_list})

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def maketradeforex(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer x-x',
    }

    data = {
        "order": {
            "units": "1",
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }

    response = requests.post('https://api-fxtrade.oanda.com/v3/accounts/001-004-x-x/orders', headers=headers, data=data)
    return HttpResponse(response)

