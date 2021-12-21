CREATE TABLE company (
    ticker varchar(5) NOT NULL,
    name varchar(255) NOT NULL,
    market_cap int NOT NULL,
    sector varchar(255),
    industry varchar(255),
    city varchar(255),
    state varchar(255),
    PRIMARY KEY (ticker)
);
CREATE TABLE stock_info (
    ticker varchar(5) NOT NULL,
    date DATETIME NOT NULL,
    volume int NOT NULL,
    open int,
    high int,
    low int,
    close int,
    adj_close int,
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);
);
CREATE TABLE comment (
    comment_id int NOT NULL,
    date DATETIME NOT NULL,
    ticker varchar(5) NOT NULL,
    content varchar(255),
    commenter_id int,
    PRIMARY KEY (commentId),
    FOREIGN KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (commenter_id) REFERENCES user(user_id)
);
CREATE TABLE user (
    user_id int NOT NULL,
    name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    user_name varchar(255) NOT NULL,
    PRIMARY KEY (user_id),
);
CREATE TABLE news (
    news_id int NOT NULL,
    ticker varchar(5) NOT NULL,
    date DATETIME NOT NULL,
    title varchar(255),
    publisher_id int NOT NULL,
    PRIMARY KEY (news_id),
    FOREIGN KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)

);
CREATE TABLE publisher (
    publisher_id int NOT NULL,
    name varchar(255) NOT NULL,
    url varchar(255) NOT NULL,
    PRIMARY KEY (publisher_d),
);
CREATE TABLE managment (
    ticker varchar(5) NOT NULL,
    ceo_name varchar(255) NOT NULL,
    ceo_gender varchar(255) NOT NULL,
    president_name varchar(255) NOT NULL,
    president_gender varchar(255) NOT NULL,
    city varchar(255) NOT NULL,
    state varchar(255) NOT NULL,
    PRIMARY KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (ticker) REFERENCES company(ticker),
);
CREATE TABLE ipo_data (
    ticker varchar(5) NOT NULL,
    ipo_date DATE NOT NULL,
    first_day_high int,
    first_day_low int,
    first_day_open int,
    first_day_close int,
    first_day_volume int,
    PRIMARY KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (ticker) REFERENCES company(ticker)
);
CREATE TABLE finantial_info (
    ticker varchar(5) NOT NULL,
    liabilities DATE NOT NULL,
    assets int,
    property_investment int,
    capital_expenditure int,
    debt int,
    debt_repayment int,
    revenue int,
    PRIMARY KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (ticker) REFERENCES company(ticker),
);
CREATE TABLE trend_info (
    ticker varchar(5) NOT NULL,
    date DATE,
);