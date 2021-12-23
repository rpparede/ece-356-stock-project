CREATE TABLE company (
    ticker varchar(5) NOT NULL,
    name varchar(255) NOT NULL,
    market_cap bigint NOT NULL,
    sector varchar(255),
    industry varchar(255),
    city varchar(255) NOT NULL,
    state varchar(255),
    PRIMARY KEY (ticker)
);

CREATE TABLE stock_info (
    ticker varchar(5) NOT NULL,
    date DATETIME NOT NULL,
    volume bigint NOT NULL,
    open float,
    high float,
    low float,
    close float,
    adj_close float,
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);

CREATE TABLE user (
    user_id int NOT NULL,
    name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    user_name varchar(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE comment (
    comment_id int NOT NULL,
    date DATETIME NOT NULL,
    ticker varchar(5) NOT NULL,
    content varchar(255),
    commenter_id int,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (commenter_id) REFERENCES user(user_id)
);

CREATE TABLE publisher (
    publisher_id int NOT NULL,
    name text NOT NULL,
    url text NOT NULL,
    PRIMARY KEY (publisher_id)
);

CREATE TABLE news (
    news_id int NOT NULL,
    ticker varchar(5) NOT NULL,
    date DATETIME NOT NULL,
    title varchar(255),
    url text, 
    publisher_id int NOT NULL,
    PRIMARY KEY (news_id),
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
);

CREATE TABLE management (
    ticker varchar(5) NOT NULL,
    ceo_name varchar(255) NOT NULL,
    ceo_age int NOT NULL,
    ceo_gender varchar(255) NOT NULL,
    president_name varchar(255) NOT NULL,
    president_age int NOT NULL,
    president_gender varchar(255) NOT NULL,
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);

CREATE TABLE ipo_data (
    ticker varchar(5) NOT NULL,
    ipo_date DATE NOT NULL,
    first_day_high float,
    first_day_low float,
    first_day_open float,
    first_day_close float,
    first_day_volume float,
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);

CREATE TABLE financial_info (
    ticker varchar(5) NOT NULL,
    liabilities bigint NOT NULL,
    assets bigint,
    property_investment bigint,
    capital_expenditure bigint,
    debt bigint,
    debt_repayment bigint,
    revenue bigint,
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);

CREATE TABLE trend_info (
    ticker varchar(5) NOT NULL,
    month_trend int, 
    three_month_trend int, 
    six_month_trend int, 
    year_trend int, 
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);

CREATE TABLE watchlist (
    trade_id int, 
    user text, 
    ticker varchar(5), 
    date date, 
    price float, 
    amount int, 
    total_price float,
    PRIMARY KEY (trade_id),
    FOREIGN KEY (ticker) REFERENCES company(ticker)
); 