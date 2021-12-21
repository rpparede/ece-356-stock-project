import click
import os
import sys
import mysql.connector

version = "v0.10"

userid = "db356test1"
server = "marmoset03.shoshin.uwaterloo.ca"
database = "db_${userid}"
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

@main.command(name='-v', help="\tShow version number of CLI")
def version(version):
    click.echo(version)

#TODO: command update

@main.command(name='price', help="\tShow the most recent price of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='low', help="\tShow the lowest day price of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def low(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, low FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='high', help="\tShow the highest day price of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, high FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='close', help="\tShow the day closing price of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, close FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='open', help="\tShow the day openning price of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, open FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='volume', help="\tShow the volume during the day of a company!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, volume FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='summary', help="\tShow a brief summary of the company's trading day!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT ticker, date, open, low, high, close, volume FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

@main.command(name='afterhours', help="\tShow a brief summary of the company's trading day!")
@click.argument('ticker', default='AAPL', type=click.STRING)
def price(ticker):
    connection, cursor = connect()
    try:
        cursor.execute("SELECT  FROM stock_info WHERE ticker='${TICKER}'")
    except:
        click.echo("There is no ticker:${TICKER}")
    finally:
        disconnect(connection, cursor)

if __name__== "__main__":
    main()
