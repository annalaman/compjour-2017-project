# compjour-2017-project
Final Project

Title: Free Money? Correlations in Financial Markets

Elevator Pitch: 
In this project, I use a news application to understand information surrounding financial markets. Financial markets are vital to people from around the world. Thus, an understanding of how various financial assets interact is crucial to all types of people, from retirees to hedge fund managers. The purpose of this web application was to better understand these interactions in financial markets from around the world.

In this application, I analyze a variety of financial assets. The choice of assets includes stocks (e.g. U.S. Dow Jones Index, Europe STOXX Index, France CAC40, Argentina Merval Index, Japan Nikkei225 Index, etc.), bonds (e.g. 2YR US Treasury yield, 10YR US Treasury yield), commodities (e.g. WTI crude oil spot price), and exchange rates (e.g. USDJPY, EURUSD). In this project, daily data going back to 2003 is used, and, for each day, I collected spot prices for all of the financial assets seen in the attached CSV. However, because I collected data for such a large amount of assets, not all assets were included in the web application. However, the assets seen on the web application can easily be replaced in the HTML program. 

People should use this application because it is vital to understand how financial assets interact. Almost all people invest capital in financial markets, so they need to understand where their money is going. Also, if people learn to invest properly, then they can invest their own money without paying a fee to invest managers. This app enables people to look at historical data of a variety of financial assets, which is invaluable to all investors, no matter how much capital they have. 

Articles
1.	https://www.wsj.com/articles/falling-correlations-spell-opportunity-for-investors-1487241004 “Falling Correlations Spell Opportunity for Investors”
a.	This article discusses the importance of correlations in financial markets. Often times, when the correlation between various asset prices changes, there is an opportunity for investors to make money. This articles outlines this strategy.

2.	https://www.wsj.com/articles/sectors-go-wild-s-p-500-correlations-crumble-1479908402
a.	On average, certain assets have fairly intuitive correlations. For example, since Chile is a large exporter of copper, when copper prices are high, we often expect the Chilean stock market to be booming because numerous Chilean companies export copper. This article analyzes a time when sector correlations altered in the S&P500 and the opportunity for investors.

3.	https://www.ft.com/content/5a40b6a8-d176-11df-96d1-00144feabdc0 
a.	This article discusses how correlations alter within markets. For example, stock and bond prices often have a negative correlation. In other words, when stocks (the more ‘risky’ asset) are performing well, bonds often take a hit (an vice-versa). However, this trend often times reverses. 

4.	https://www.ft.com/content/5ffde876-2ada-3b6f-9ed5-7dd108f5fde6
a.	Similar to the previous articles, this source describes stock picking. If individuals are interested in picking stocks, then this application is valuable to them.


Data sources:
All of the data was collected from public sources. Both quandl (https://www.quandl.com/) and the Federal Reserve Economic Database (FRED) were used to access all asset prices. FRED was used for the majority of assets, and the data from FRED is extremely reliable and up to date since it is run by the Federal Reserve (https://fred.stlouisfed.org/). For each asset, the data was downloaded individually, and then I combined all of these spot prices into one large CSV with all of the daily data. This CSV is attached.

Inspirations and prior work
1.	https://www.robinhood.com/ “Robinhood”
a.	Robinhood is an app that allows people to invest in particular stocks and other financial assets (such as ETFs).
2.	https://finmason.com/  “Finmason”
a.	Finmason is an independently run financial analytics platform for both retail and institutional investors. The purpose of this application is to help investors better understand financial assets. 
3.	“iQuantfi”
a.	This application was one of the first virtual financial advistors for the retail audience. The purpose of this application was to help individuals make the best possible investment chouices.

Compare/contrast your app with others
1.	Contrast: My application shows daily data and dives deeper into more assets for each day.
2.	Contrast: This application does not provide direct analysis into whether an asset should be purchased or not. Other assets such as iQuantfi do provide this advice.
3.	Compare: All of these applications provide insight into which assets are worth purchasing in depending on the individual goals of the investor.
