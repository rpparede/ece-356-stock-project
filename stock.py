import click
from datetime import datetime
import mysql.connector

versionid = "v0.10"

userid = "k48shah"
server = "localhost"
database = "ece356"
password = "Katman098$"

def connect(): #connect to a mysql database
    connection = mysql.connector.connect(
        host=server, #stated above
        database=database, #stated above
        user=userid, #stated above
        password=password #stated above
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

def disconnect(connection, cursor): #disconnect from a mysql database (typically after commands end)
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("connection not found to disconnect")

@click.group()
def main():
    """
    CLI grouping for stock information
    """
    pass

@main.command(name='version', help="\tShow version number of CLI")
def version():
    click.echo(versionid)

# @main.command(name='update', help="\tUpdate all price history tables with new data")
# def update():
#     connection, cursor = connect()
#     try:
        
#     except:
#         click.echo("Could not insert data into ")

#stock.py price TSLA
@main.command(name='price', help="\tShow the most recent price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def price(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='" + ticker + "' AND date='" + date + "';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

@main.command(name='low', help="\tShow the lowest day price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def low(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, low FROM stock_info WHERE ticker='" + ticker + "' AND date='" + date + "';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, low FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

@main.command(name='high', help="\tShow the highest day price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def price(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, high FROM stock_info WHERE ticker='" + ticker + "'AND date=''" + date + "'';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, high FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

@main.command(name='close', help="\tShow the day closing price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def price(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='" + ticker + "' AND date=''" + date + "'';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='open', help="\tShow the day openning price of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def price(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, open FROM stock_info WHERE ticker='" + ticker + "' AND date=''" + date + "'';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, open FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='volume', help="\tShow the volume during the day of a company using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format yyyy-mm-dd to get data for a specific day")
def price(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, volume FROM stock_info WHERE ticker='" + ticker + "' AND date='" + date + "';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, volume FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker:{ticker}")
    finally:
        disconnect(connection, cursor)

@main.command(name='summary', help="\tShow a brief summary of the company's trading day!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format dd/mm/yyyy to get data for a specific day")
def summary(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, open, low, high, close, volume FROM stock_info WHERE ticker='" + ticker + "' AND date='" + newDate + "';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, open, low, high, close, volume FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

@main.command(name='afterhours', help="\tShow the after hours trading price using its ticker!")
@click.argument('ticker', default='AAPL', type=click.STRING)
@click.option('-d', '--date', help="Input the date in this format dd/mm/yyyy to get data for a specific day")
def afterhours(ticker, date):
    connection, cursor = connect()
    try:
        if (date):
            cursor.execute("SELECT ticker, date, adj_close FROM stock_info WHERE ticker='" + ticker + "' AND date=''" + newDate + "'';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
        else:
            cursor.execute("SELECT ticker, date, adj_close FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchone():
                click.echo(str(num_fields[count]) + "\t" + str(row))
                count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

#stock.py news -p FOXNEWS TSLA
@main.command(name='news', help="\tShow the latest news!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def news(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT * FROM news WHERE ticker='" + ticker + "' LIMIT 10;")
        for row in cursor.fetchall():
                click.echo(str(row[2]))
                click.echo("Title:\t" + row[3])
                click.echo("URL:\t" + row[4])
                click.echo("\n")
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

#TODO: Stock analysis ticker

@main.command(name='desc', help="\tA description of the company and what they do!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def desc(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, name, market_cap, industry, sector, state, city  FROM company WHERE ticker='" + ticker + "';")
        num_fields = cursor.column_names
        
        count = 0
        for row in cursor.fetchone():
            click.echo(str(num_fields[count]) + "\t" + str(row))
            count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)


#TODO: trendinfo command
@main.command(name='ipobrief', help="\tSome brief data to get an initial understanding of the company")
@click.argument('ticker', default='AAPL', type=click.STRING)
def brief(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, name, sector, ipo_date, first_day_high, first_day_low, first_day_open, first_day_close, first_day_volume FROM stock_info INNER JOIN company USING(ticker) INNER JOIN ipo_data USING(ticker) WHERE ticker='" + ticker + "'")
        num_fields = cursor.column_names
        
        count = 0
        for row in cursor.fetchone():
            click.echo(str(num_fields[count]) + "\t" + str(row))
            count += 1
    except:
        click.echo("There is no ticker: " + ticker)
    finally:
        disconnect(connection, cursor)

@main.command(name='user', help='Create your user to leave your stock thoughts!')
@click.argument('username', type=click.STRING)
@click.option('-n', '--name', nargs=2, required=True, help='Put your name in quotes so we can identify you! {first_name last_name} [Required]')
def user(username, name):
    connection, cursor = connect()
    first, last = name
    newUser = 1
    try:
        cursor.execute("SELECT COUNT(*) FROM user WHERE user_name='" + username + "'")
        userCount = cursor.fetchone()
        cursor.execute("SELECT MAX(user_id) FROM user")
        maxUser = cursor.fetchone()
        if (maxUser[0] != 0):
            newUser = maxUser[0] + 1
        if (int(userCount[0]) <= 0):
            cursor.execute("INSERT INTO user(user_id, name, last_name, user_name) VALUES (" + str(newUser) + ", '" + first +"', '" + last + "', '" + username + "');")
            connection.commit()
            click.echo("User has been made!")
        else:
            click.echo("This user already exists")
    except:
        click.echo("User could not be added, please try again")
    finally:
        disconnect(connection, cursor)

@main.command(name='talk', help='\tShow latest comments on a given stock!')
@click.argument('ticker', default='N/A', type=click.STRING)
def talk(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, user_name, content FROM comment INNER JOIN user ON comment.commenter_id=user.user_id LIMIT 10")
        num_fields = cursor.column_names
        
        count = 0
        for row in cursor.fetchall():
            click.echo(row[0] + ":\t" + str(row[1]) + "\t" + row[2])
            click.echo("comment: " + row[3])
    except:
        click.echo("No comments found for the stock, try a different one or come back other time")
    finally:
        disconnect(connection, cursor)
        


@main.command(name='comment', help='\tConversate with others on this stock!')
@click.argument('ticker', default='N/A', type=click.STRING)
@click.option('-u', '--user', help="Input your username!")
@click.option('-m', '--message', required=True, help="Type your message after the tag in quotes")
def comment(ticker, user, message):
    connection, cursor = connect()
    newID = 0
    try:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("SELECT MAX(comment_id) FROM comment;")
        currentID = cursor.fetchone()
        if (currentID[0] != None):
            newID = currentID[0] + 1
        if (user):
            try:
                cursor.execute("SELECT user_id, user_name FROM user WHERE user_name='" + user + "';")
                user_id, newUser = cursor.fetchone()
            except:
                click.echo("No known user: " + user + ". Please create user with 'python stock.py user")
        else:
            user_id = 0
            newUser = "ANON"
        
        cursor.execute("INSERT INTO comment (comment_id, date, ticker, content, commenter_id) VALUES (" + str(newID) + ", '" + formatted_date + "', '" + ticker + "', '" + message + "', " + str(user_id) + ");")
        click.echo("Thanks for leaving your comment on " + ticker + ", check back later to see if anyone else has left a comment for you")
        connection.commit()
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
            cursor.execute("SELECT * FROM watchlist WHERE user='" + username + "';")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchall():
                click.echo(row[1] + "\t" + row[2] + "\t" + str(row[3]))
                click.echo("price:\t$" + str(row[4]))
                click.echo("amount:\t" + str(row[5]))
                click.echo("total:\t$" + str(row[6]))
                click.echo("\n")
        else:
            cursor.execute("SELECT * FROM watchlist WHERE user='" + username + "' LIMIT 10;")
            num_fields = cursor.column_names
            
            count = 0
            for row in cursor.fetchall():
                click.echo(row[1] + "\t" + row[2] + "\t" + str(row[3]))
                click.echo("price:\t$" + str(row[4]))
                click.echo("amount:\t" + str(row[5]))
                click.echo("total:\t$" + str(row[6]))
                click.echo("\n")
    except:
        click.echo("No watches found for that user, try a different user or come back another time")
    finally:
        disconnect(connection, cursor)
  
@main.command(name='trade', help='\tAdd trades to your watchlist!')
@click.argument('username', type=click.STRING)
@click.option('-t', '--ticker', required=True, help="Use this tag to make a trade on a specific company")
@click.option('-a', '--amount', type=click.INT, help="Keep track of how many you purchased")
def trade(username, ticker, amount):
    connection, cursor = connect()
    
    try:
        cursor.execute("SELECT close FROM stock_info WHERE ticker='" + ticker + "' LIMIT 1;")
        price = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) FROM watchlist WHERE ticker='" + ticker + "' and user='" + username + "';")
        tickerIn = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*) FROM user WHERE user_name='" + username + "';")
        currUser = cursor.fetchone()

        if (currUser[0] <= 0):
            click.echo("Username does not exist")
        else:
            if (not amount and tickerIn[0] > 0):
                click.echo("You have already added the ticker to your watchlist previously")
            elif(amount and tickerIn[0] > 0):
                cursor.execute("SELECT amount FROM watchlist WHERE ticker='" + ticker + "' and user='" + username + "'")
                currAmount = cursor.fetchone()
                newAmount = currAmount[0] + int(amount)
                cursor.execute("UPDATE watchlist SET amount=" + str(newAmount) + ", total_price=" + str(newAmount*price[0]) + ", price=" + str(price[0]) + " WHERE ticker='" + ticker + "' AND user='" + username + "';")
                connection.commit()
                click.echo("Updated existing watchlist!")
            else:
                newAmount = 0
                newID = 0
                if (amount):
                    newAmount = amount
                cursor.execute("SELECT MAX(trade_id) FROM watchlist;")
                currentID = cursor.fetchone()
                if (currentID[0] != None):
                    newID = currentID[0] + 1


                if (currUser[0] > 0):
                    now = datetime.now()
                    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("INSERT INTO watchlist(trade_id, user, ticker, date, price, amount, total_price) VALUES(" + str(newID) + ", '" + username + "', '" + ticker + "', '" + formatted_date + "', " + str(price[0]) + ", " + str(newAmount) + ", " + str(newAmount*price[0]) + ");")
                    click.echo("Added " + ticker + " to your watchlist!")
                    connection.commit()
    except:
        click.echo("Could not add " + ticker + " to your watchlist")
    finally:
        disconnect(connection, cursor)


        
 
if __name__== "__main__":
    main()
