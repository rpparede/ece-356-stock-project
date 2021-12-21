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
    commentId int NOT NULL,
    date DATETIME NOT NULL,
    ticker int NOT NULL,
    comment varchar(255),
    commenterId int,
    PRIMARY KEY (commentId),
    FOREIGN KEY (ticker) REFERENCES company(ticker),
    FOREIGN KEY (commenterId) REFERENCES user(userId)
);
CREATE TABLE user (
    userId int NOT NULL,
    name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    user_name varchar(255) NOT NULL,
    PRIMARY KEY (userId),
);