# CA400 Blog
## Blog 1.
### 5th October 2018.

Yesterday I met with Martin Crane to assess my initial idea for the project. Martin provided some food for thought and I came out of the meeting quite happy and encouraged. 

My plan is to make a WebApp which would help traders make decisions on whether to buy or sell stocks. This would include Crypto Currencies such as Bitcoin and regular Forex stock.
The functionality behind the predictor will include a trained algorithm based on past data. I'm currently looking into further components of the App. Martin mentioned including a
graphical comparison of the price of Bitcoin stock alongside Gold and other commodities which I feel would be nice to include. 

I am yet to decide on which language to write it in. Python has good inbuilt libraries for these calculations, Java would be most intuitive to me and I've heard that C++ would be
more efficient if there are complex calculations to be made. I'm quite familiar with JavaScript and XML due to my third year project. My internship with SAP improved my knowledge
with MVC (Model View Controller) architecture. Both of which will stand to me during this project I feel. 

My main focus at the minute is to broaden my knowledge on the finance industry in general, I have an interest in this field which should make it easier. I'm also concerned about 
getting approval from the submissions board, I need to develop a clearer strategy on how I'll accomplish this project and the logistics involved.

I'm looking forward to getting my hands dirty.

More updates soon,
Ben.

## Blog 2.
### 12th October 2018.

I made the final changes to my Project Proposal yesterday. I've decided to name the project **Smart Predict (Trading Platform)**. As part of the documentation I had to make some decisions about the technologies I planned on using but there are still 
some decisions I have to make regarding which specific platform/languages I'll be implementing. Next on my agenda will be  creating a logo for the project and creating accounts on
various platforms to see how their API keys work. I also need to do some research into which dataset I'll be using for the past and current data for each stock. This could end up being a 
headache if I have to manually scrape websites for data or if I don't choose the right one so it's an important task.

Ben.

## Blog 3.
### 19th October 2018.

Yesterday I finished my work on creating a logo for the project. I gave this somewhat of a priority early on in the project lifecycle. I believe it's important to establish an identity within the hundred or so projects that the examiners will be grading this year. It also helps me create a theme that will be consistent throughout all the documentation I'll provide. Here's what it looks like.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/logo.png "logo")

The majority of the research I've done about using machine learning to predict financial data has suggested using Python because of it's powerful libraries like NumPy etc. To develop a WebApp written in Python will be something completely new to me. Again, a lot of articles online suggest that you use Django in order to achieve this. I’ve also never used Django before.

A lot of my time today was spent getting all of the systems that I will be using for the project up to date. This included downloading a newer version of Python(3.7) so that Django will run without a hitch while I'm working at home. I also had to update my laptop to the newest Mac OS so it supports this new version of Python. Lastly, of course, installing Django itself, I am still open to trying other platforms so Django will be used on a trial basis for now.

I am reluctant to start writing substantial amounts of code before getting approval from the submissions board. If they don't approve my project I will have completely wasted my time, this is why I've been spending my time doing research and design rather than the nitty-gritty parts of the project.

Prior to this week, I had all of my blogs written on a blog site, but in the spec for the blogs, it’s says they must be written in MarkDown. This is something I’ve adapted from now which is why the commits and dates on the first 2 blogs will be off.

I've also set up fortnighly meetings with Martin to ensure I'm staying on track. These meetings really helped me last year and gave me good insights into what path to take etc. so I'm hopeful they'll be just as helpful this year.

More news soon,
Ben.

## Blog 4.
### 22nd October 2018.

Over the weekend I've been preparing for my Project Approval meeting on Tuesday. I had to ensure that I was clear on what the project would involve, what the business impact would be, who the users would be etc.
I made a small questionnaire so I can brief myself before stepping into the room on Tuesday.
* What platform will you use?
    * Django because of it’s python functionalities
    
* How will you collect your data? Datasets?
    * Datasets online, good datasets on Kaggle and EODdata
* What will you train your algorithm based on?
    * 2 separate algorithms, because one is likely to be more volatile than the other, other factors affect each financial area different
    * Based on chart analysis
* My Supervisor is: 
    * Martin Crane
* My Project Title is: 
    * Smart Predict (Trading Platform)
* The Purpose of my project is to: 
    * Provide users with an all-in-one solution to their trading needs, help them make intelligent decisions on buying and selling of stocks through Machine Learning.
* For my solution, I propose the following major components:
    * WebApp 
    * AWS for login to app (server side)
* The major challenges in my project are in the following areas:
    * Using AI for the first time. Done in practice, never written a single line of code
    * Making a WebApp for the first time
    * Getting familiar with cryptocurrency & Forex stock (What affects stock prices)
    * Using new environments and technologies eg. Django 


    
## Blog 5.
### 26th October 2018.

After meeting with the project Approval panel this week I’m pleased to say my project has been approved. Thomas and Charlie gave me some advice on the challenges I might face. One of which is likely to be the lack of accuracy my AI predictor will have. To combat this I’ll have to implement some sort of sentiment analysis. I’m unsure whether I’ll have to create this myself or use some sort of plug-in. As with everything in the project it’s extremely time dependent. I’ll insert the notes they gave me on my Dashboard below.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/approval.png "approval")

For the meantime I’ll focus on creating a simple front-end and connecting the WebApp to the database. I also need to do more reading on chart analysis and Long Short Term Memory as recommended by Martin.

## Blog 6.
### 14th November 2018.

The last two weeks have predominantly been spent creating and implementing a simple Django front-end, writing the functional spec for the project as well as also completing assignments for my other modules. The lack of blogs and updates over the past 2 weeks is simply a consequence of this sheer amount of work. I'll insert a few screenshots of my progress over the few weeks.

Here's what the initial installation screen looks like. This is just on localhost.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/StartScreen.png "frontend")

## Blog 7.
### 22nd December 2018.

After connecting and setting up an Amazon Web Services Database instance to the app I ran into issues with Amazon charging me for using their RDS system. They charged me $10 for exceeding their free usage limit, I figured that $10 every month with little usage of the database would be unsustainable for the duration of the project, particularly when it came to the more database intensive periods.
I now face the problem of creating a new Database instance and re-connecting it to the app. This will have to be achieved after my exams which, unfortunately, will have to take top priority until they conclude in late January.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/Capture.PNG "free tier limit")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/aws_bill.png "billing")

## Blog 8.
### 5th Febuary 2019.

Due to the increasing time demands of assignments from semester 1 and the ensuing exams following Christmas the project had to take a back seat. I have today solved the issue with the search for a database system. I have concluded that simply running an SQLite DB system locally will be sufficient for the remainder of the project. Which is disappointing as I had hoped to gain insights such as the demographics of the app via the use of a cloud-based system such as AWS.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/sp_index.png "SP Index")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/time.png "Time")

An observation I've made is that progress on the app is far from linear, which I naively assumed it would be. But rather bouts of "sprints" let's say. I am hoping this semester will provide more opportunities to work on the project, as last year was a logistical nightmare for trying to be productive.

## Blog 9.
### 25th Febuary 2019.

Login, sign up and reset password functionality have been added to the app. Now the challenge will be making the app look nice through Bootstrap,
providing a trading connection through API keys and creating the AI.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/login.png "login")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/reset_pass.png "Reset Password")


## Blog 10.
### 1st March 2019.

I have successfully connected SmartPredict to the CoinBase API through an OAuth connection, this is more secure than the API key connection I had 
previously planned.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/crypt_api.png "crypto api connecton")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/crypt_email.png "crypto api email")

## Blog 11.
### 5th March 2019.

The past few days have been spent filling out the ethical approval form for the project. I required a level 2 notification approval for my user and usability testing
this was quickly approved so I can now proceed with other parts of the project, namely the AI implementation and Bootstrap front-end.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/ethical_approval.png "ethics")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/dashboard.png "dashboard")

## Blog 12.
### 14th March 2019.

The site is now live [here](http://kellyb45.pythonanywhere.com/smartpredict/). I am hosting it through PythonAnywhere.

The site wasn't up long before getting this email! working on getting it back online now.
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/phising.png "phishing")

## Blog 13.
### 15th March 2019.

While I'm waiting for PythonAnywhere to get back to me about the hosting I've been working locally to make the front-end look nicer. I implemented Bootstrap
to achieve a more professional looking app. Here is how the index looks now. 

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/local_index.png "index")

## Blog 14.
### 23rd March 2019.

The site is back live again [here](http://kellyb45.pythonanywhere.com/smartpredict/) after some battling with pythonAnywhere.

A few aesthetic changes have been made through Bootstrap and this can be best seen with the newly created 'About' page.
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/live.png "live")

## Blog 15.
### 29th March 2019.

I have finally gotten the Oanda API cooperating so that I can return current price data, past data for each user, make trades etc. on the Forex market.
This data is returned in JSON format, the next challenge will be making it readable for users.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/forex.png "JSON data")

Just a side note, I prefer to work offline (localhost) while implementing new solutions and then push the final product rather than work online constantly
as this has led to errors in the past (see blog 12).

## Blog 16.
### 2nd April 2019.

I have finished work on parsing the JSON object so the user can read it and gain valuable information such as real-time stock prices.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/prices.png "FOREX currency pairs")

This is the start of the FOREX Dashboard, it looks basic for now but the core functionality is complete. These prices are grabbed from the OANDA API and are updated on the site every minute.
I will now work on making trade calls from our side so that users can trade without leaving SmartPredict. I have the trading element working for my account
but the tricky part will be to get it working for any user so that they can dynamically input their info and make trades etc.

## Blog 17.
### 7th April 2019.
I have developed the Crypto Dashboard further so that it can now graph data on the spot. It currently displays the last 100 days in euro, I intend to make this interchangeable so that users can choose the currency and the number of days to be displayed. The graphs are nice because upon hovering over the price point it shows you information about it, I've been having trouble with changing
the datestamp (on the X-axis) to a readable date. The problem is when I pass the python list to the javascript implementation of Chart.js is gives out when the list is anything but integers. I'm currently working on a 
workaround for this. Next will be getting the RSI (Relative Strength Index) of each currency.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/btcchart.png "Bitcoin Graph")
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/ethchart.png "Etherueum Graph")


## Blog 18.
### 12th April 2019.

I have improved the graph date format as discussed previously and implemented new graphs for other currencies and markets, namely forex. It makes sense to put forex on the same graph as they are closely related and don't blow the proportionality of the graph out as BTC and ETH would. 

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/forexchart.png "Forex Graph")

 The two Dashboards are now only lacking Sentiment Analysis and Algorithmic input which I've been working on for the last few days.
 
## Blog 19.
### 17th April 2019.

I have gotten a large amount of work done on the Dashboard over the past week. The crypto AI is producing a semi-accurate prediction, this was developed using Tensorflow's LSTM (Long Short Term Memory) algorithm along with Numpy, Pandas and Keras for some useful functions. The prediction algorithm itself
is not fully complete with other influences still to be added to it and therefore weightings changed. But as it stands I'm pretty happy with it. I've also returned RSI (Relative Strength Index) AND MACD (Moving Average Convergence/Divergence) data to the Dashboard, this will help users make accurate trading decisions when the time comes.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/predict.png "Prediction Output")

The RSI indicator will be:
* Green when the value is greater than 60
* Yellow when between 50 and 60
* Red when below 50

The Output price will be shown in:
* Green if the currency's price is expected to increase
* Red if it is expected to decrease

This will give the user a simple traffic-light system to follow for easier understanding. The MACD can be seen on the graph with the fast value being calculated over 12 day period and slow being calculated over 26 days of EMA (Exponential Moving Average).
The crossover of these lines on the graph is of particular interest to the user, 'when the MACD falls below the signal line, it is a bearish signal which indicates that it may be time to sell. Conversely, when the MACD rises above the signal line, the indicator gives a bullish signal, which suggests that the price of the asset is likely to experience upward momentum.'

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/MACD.png "MACD")

## Blog 20.
### 19th April 2019.

I have implemented Sentiment Analysis as suggested by Thomas Ward in my project approval meeting. The function uses Tweepy and TextBlob to analyse live tweets and return their overall sentiment. This will give the application a deeper understanding of the market.
The text will be displayed in the traffic light system which the user will already be familiar with as well as the graph of the 100 most recent tweets pertaining to the currency, in this case, Bitcoin.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/sent.png "Sentiment Analysis for Bitcoin")

The Dashboard and app look slightly different than before with all elements being centred and a footer is added to the project. This I feel gives the app a more 'professional' look and feel.

## Blog 21.
### 26th April 2019.

Over the past week, I've been finishing the Dashboard, mainly the Forex AI. The model uses ARMIA (AutoRegressive Integrated Moving Average) instead of LSTM as this seems to be more accurate for Forex prices in the documentation I've read. I have to give credit to
[TowardsDataScience](https://towardsdatascience.com) and [Investopedia](https://www.investopedia.com/) for their documentation about investing and finance in general. The model takes daily price points from 2005 to the present day and uses a 90:10 split for training: testing (the same split as the Crypto AI).
In general, the algorithm has good accuracy with the Crypto model having a Mean Absolute Error of ~ 0.02 and the Forex algorithm ranges ~ (0.002-0.004) depending on the currency. The difference in accuracy is expected because of the highly volatile nature of cryptocurrencies. This relatively high error in Bitcoin is perhaps less risky than a smaller percentage of inaccuracy for forex and the margins for profit are much smaller.


I am supporting 3 currency pairs with both sides of EUR/GBP for particular interest due to Brexit. The full list is:
* EUR/USD
* EUR/GBP
* GBP/USD
* GBP/EUR

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/accuracy.png "Accuracy for EUR/GBP")

Here is a graph of EUR/USD with the blue line being the actual data and red being the algorithm's prediction of the final 25 day period.
![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/pred_graph.png "Predition for EUR/USD")

**It is important to note that while developing and implementing both algorithms I made a conscious effort to keep 'tinkering' to a minimum, This would cause overfitting of the small dataset I had of 2000 data entries for Bitcoin and ~ 4000 data entries for each Forex currency pair.**

## Blog 22.
### 5th May 2019.

I have been testing the app for the past few weeks, as expected this has uprooted some underlying errors which have since been eradicated. I plan on doing some final refactoring after the exams are finished. 
The testing so far has been mainly:
* Unit & Coverage Testing
* Environment & Server Testing
* Integration Testing
* Lint Testing
* User Testing

I am nearly finished the user testing, with most of the other forms being completed already.

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/unit1.png "Unit Tests")

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/coverage.png "Percentage Coverage")

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/score1.png "Lint Test")

![](https://https://github.com/kellyb45/fourth_year_project/blob/master/docs/blog/images/score3.png "Lint Test")

Full Testing Documentation can be found In the Docs Section.



