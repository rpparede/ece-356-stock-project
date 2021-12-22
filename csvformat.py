import pandas as pd

# create ipo_data csv
col_ipo = ["Symbol", "ipoDate", "highDay0", "lowDay0", "openDay0", "closeDay0", "volumeDay0"]
df1 = pd.read_csv('IPODataFull.csv', usecols=col_ipo)
df1.to_csv('ipo_data.csv')

# create trend_info csv
col_trend = ["Symbol", "MarketMonthTrend", "Market3MonthTrend", "Market6MonthTrend", "MarketYearTrend"]
df2 = pd.read_csv('IPODataFull.csv', usecols=col_trend)
df2.to_csv('trend_info.csv')

# create company csv
col_company = ["Name", "Symbol", "MarketCap", "Sector", "Industry", "City", "stateCountry"]
df3 = pd.read_csv('IPODataFull.csv', usecols=col_company, encoding="latin1")
df3.to_csv('company.csv')

# create financial_health csv
col_health = ["Symbol", "Total_liabilitiesYearBeforeIPO", "Total_assetsYearBeforeIPO", "Investments_in_property,_plant,_and_equipmentYearBeforeIPO",
               "Capital_expenditureYearBeforeIPO", "Long-term_debtYearBeforeIPO", "Debt_repaymentYearBeforeIPO", "Total_net_revenueYearBeforeIPO"]
df4 = pd.read_csv('IPODataFull.csv', usecols=col_health)
df4.to_csv('financial_health.csv')

# create management csv
col_mgmt = ["Symbol", "CEOAge", "CEOName", "CEOGender", "PresidentAge", "PresidentName", "PresidentGender"]
df5 = pd.read_csv('IPODataFull.csv', usecols=col_mgmt, encoding="latin1")
df5.to_csv('management.csv')

# create news csv
col_news = ["stock", "date", "headline", "url"]
df6 = pd.read_csv('raw_partner_headlines.csv', usecols=col_news)
df6.to_csv('news.csv')

# create publisher csv
col_publisher = ["publisher", "url"]
df7 = pd.read_csv('raw_partner_headlines.csv', usecols=col_publisher)
df7.to_csv('publisher.csv')


