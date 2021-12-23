-- load company
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/company.csv' INTO TABLE company 
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@dummy, @tick, @name, @market_cap, @sector, @industry, @city, @stateCountry)
    SET ticker=@tick, name=@name, market_cap=@market_cap, sector=@sector, industry=@industry, city=@city, state=@stateCountry;  

-- load stock_info
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/fh_5yrs.csv' INTO TABLE stock_info 
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@date, @vol, @op, @hi, @lo, @cls, @adjcls, @tick)
    SET ticker=@tick, date=@date, volume=@vol, open=@op, high=@hi, low=@lo, close=@cls, adj_close=@adjcls;    

-- load publisher
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/publisher.csv' INTO TABLE publisher
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@publisher_id, @url, @name)
    SET publisher_id=@publisher_id, name=@name, url=@url; 

-- load news
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/news.csv' INTO TABLE news
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@news_id, @headline, @url, @date, @ticker)
    SET news_id=@news_id, ticker=@ticker, date=@date, title=@headline, url=@url, publisher_id=@news_id; 

-- load management
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/management.csv' INTO TABLE management
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@dummy, @symbol, @ceo_age, @ceo_name, @ceo_gender, @pres_age, @pres_name, @pres_gender)
    SET ticker=@symbol, ceo_name=@ceo_name, ceo_name=@ceo_name, ceo_gender=@ceo_gender, president_name=@pres_name, president_age=@pres_age, president_gender=@pres_gender; 

-- load ipo_data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ipo_data.csv' INTO TABLE ipo_data
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@dummy, @symbol, @close, @hi, @open, @lo, @volume, @date)
    SET ticker=@symbol, ipo_date=@date, first_day_high=@hi, first_day_low=@lo, first_day_open=@open, first_day_close=@close, first_day_volume=@volume;

-- load financial_info
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/financial_health.csv' INTO TABLE financial_info
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@dummy, @symbol, @assets, @liab, @prop_inv, @cap_exp, @debt, @debt_rep, @revenue)
    SET ticker=@symbol, liabilities=@liab, assets=@assets, property_investment=@prop_inv, capital_expenditure=@cap_exp, debt=@debt, debt_repayment=@debt_rep, revenue=@revenue;

-- load trend_info
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/trend_info.csv' INTO TABLE trend_info
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"' 
    ESCAPED BY '\\'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES 
    (@dummy, @symbol, @month, @3month, @6month, @year)
    SET ticker=@symbol, monthTrend=@month, threeMonthTrend=@3month, sixMonthTrend=@6month, yearTrend=@year;
