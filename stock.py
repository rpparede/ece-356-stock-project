import click
from datetime import datetime
import mysql.connector

version = "v0.10"

userid = "lamehta"
server = "localhost"
database = "db_{userid}"
password = "password"

def connect():
    connection = mysql.connector.connect(
        host=server,
        database=database,
        user=userid,
        password=password
    )
    if connection.is_connected():
        dbInfo = connection.get_server_info()
        print("Connected to MySQL Server version", dbInfo)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    else:
        print("Connection is not established")
    return [connection, cursor]

def disconnect(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("connection not found to disconnect")

@click.group()
def main():
    """
    CLI for stock information
    """
    pass

@main.command(name='version', help="\tShow version number of CLI")
def version(version):
    click.echo(version)

#TODO: command update

#stock.py price TSLA
@main.command(name='price', help="\tShow the most recent price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='low', help="\tShow the lowest day price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def low(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, low FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='high', help="\tShow the highest day price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, high FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='close', help="\tShow the day closing price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='open', help="\tShow the day openning price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, open FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='volume', help="\tShow the volume during the day of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, volume FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='summary', help="\tShow a brief summary of the company's trading day using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def summary(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, open, low, high, close, volume FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='afterhours', help="\tShow the after hours trading price! using its ticker")
@click.argument('ticker', default='AAPL', type=click.STRING)
def afterhours(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT adjclose FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

#stock.py news -p FOXNEWS TSLA
@main.command(name='news', help="\tShow the latest news!")
@click.option('-p', '--publisher', help="Show only news from a specific publisher")
@click.argument('ticker', default='AAPL', type=click.STRING)
def news(ticker, publisher):
    connection, cursor = connect()
    try:
        if (publisher):
            cursor.execute("SELECT date, title, url FROM StockNews INNER JOIN Publisher ON StockNews.publisherId=Publisher.publisherID WHERE ticker='{ticker}' AND name='{publisher}' LIMIT 10;")
            for row in cursor:
                click.echo(row)
        else:
            cursor.execute("SELECT date, title, url FROM StockNews WHERE ticker='{ticker}' LIMIT 10;")
            for row in cursor:
                click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

#TODO: Stock analysis ticker

@main.command(name='desc', help="\tA description of the company and what they do!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def desc(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, companyName, description FROM StockInfo INNER JOIN Company ON StockInfo.ticker=Company.ticker WHERE ticker='{ticker}'")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='brief', help="\tSome brief data to get an initial understanding of the company")
@click.argument('ticker', default='AAPL', type=click.STRING)
def brief(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, companyName, ipoDate, ipoPrice, description, url FROM StockInfo INNER JOIN Company ON StockInfo.ticker=Company.ticker INNER JOIN IPOData ON Company.ticker=IPOData.ticker WHERE ticker='{ticker}'")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='user', help='Create your user to leave your stock thoughts!')
@click.argument('username', type=click.STRING)
@click.option('-e', '--email', required=True, help='Lets associate your username to an email! [Required]')
def user(username, email):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT COUNT(user) FROM userInfo WHERE user='{username}'")
        userCount = cursor.fetchone()
        if (userCount <= 0):
            cursor.execute("SELECT COUNT(email) FROM userInfo WHERE email='{email}'")
            emailCount = cursor.fetchone()
            if (emailCount <= 0):
                cursor.execute("INSERT INTO userInfo (user, email) VALUES ('{username}', '{email}')")
                click.echo("User has been made!")
            else:
                click.echo("This email has already been used for another user")
        else:
            click.echo("This user already exists")
    except:
        click.echo("User could not be added, please try again")
    finally:
        disconnect(connection, cursor)

@main.command(name='talk', help='\tShow latest comments on a given stock!')
@click.argument('ticker', default='N/A', type=click.string)
def talk(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, user, message FROM comment LIMIT 10")
        for row in cursor:
            click.echo(row)
    except:
        click.echo("No comments found for the stock, try a different one or come back other time")
    finally:
        disconnect(connection, cursor)
        


@main.command(name='comment', help='\tConversate with others on this stock!')
@click.argument('ticker', default='N/A', type=click.string)
@click.option('-u', '--user', help="Input your username!")
@click.option('-m', '--message', required=True, help="Type your message after the tag in quotes")
def comment(ticker, user):
    connection, cursor = connect()
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("SELECT MAX(commentID) FROM Comment")
        currentID = cursor.fetchOne() + 1
        cursor.execute("INSERT INTO comment (commentID, ticker, date, user, message) VALUES ({currentID}, {ticker}, {formatted_date}, {user}, {message});")
    except:
        click.echo("Unfortunately no messages here :(")
    finally:
        disconnect(connection, cursor)


@main.command(name='watch', help='\tShow 10 recent stock watches made by given user')
@click.argument('username', type=click.STRING)
@click.option('-v', '--viewall')
def watch(username, viewall):
    connection, cursor = connect()
    try:
        if (viewall):
            cursor.execute("SELECT user, ticker, date, price, amount, totalPrice FROM Trades WHERE EXISTS(SELECT user FROM UserInfo WHERE user={username});")
            for row in cursor:
                click.echo(row)
        else:
            cursor.execute("SELECT user, ticker, date, price, amount, totalPrice FROM Trades WHERE WHERE EXISTS(SELECT user FROM UserInfo WHERE user={username});")
            for row in cursor:
                click.echo(row)
    except:
        click.echo("No watches found for that user, try a different user or come back other time")
    finally:
        disconnect(connection, cursor)
  
@main.command(name='trade', help='\tAdd trades to your watchlist!')
@click.argument('username', type=click.STRING)
@click.option('-t', '--ticker', required=True, help="Use this tag to make a trade on a specific company")
@click.option('-a', '--amount', type=click.INT, help="Keep track of how many you purchased")
def trade(username, ticker, amount):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT close FROM stock_info WHERE ticker='{ticker}' LIMIT 1;")
        price = cursor.fetchone()

        cursor.execute("SELECT ticker FROM Trades WHERE ticker='{ticker}' and user='{username}';")
        tickerIn = cursor.fetchone()
        if (not amount and tickerIn > 0):
            click.echo("You have already added the ticker to your watchlist")
        elif(amount and tickerIn > 0):
            cursor.execute("SELECT amount FROM Trades WHERE ticker='{ticker}' and user='{username}'")
            currAmount = cursor.fetchone()
            newAmount = currAmount + amount
            cursor.execute("UPDATE Trades SET amount={newAmount} WHERE ticker='{ticker}' AND user='{username}'")
            #TODO: implement price change algebra
        else:
            newAmount = 0
            if (amount):
                newAmount = amount
            cursor.execute("SELECT MAX(tradeID) FROM Trades")
            currentID = cursor.fetchOne() + 1
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            cursor.executes("INSERT INTO Trades(tradeID, user, ticker, date, price, amount) VALUES({currentID}, {username}, {ticker}, {formatted_date}, {price}, {newAmount}}")
    except:
        click.echo("Could not add {ticker} to your listing")
    finally:
        disconnect(connection, cursor)


        
 
if __name__== "__main__":
    main()
