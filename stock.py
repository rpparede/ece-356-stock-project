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

@click.group()
def main():
    """
    CLI for stock information
    """
    pass

@main.command()
@click.option('-v', '--version', is_flag=True, help="Will show version number of CLI")
def stock(version):
    click.echo(version)

@click.argument('TICKER')
@click.option('-p', '--price', help="Gives the latest price from the update")
def stock(TICKER):


if __name__== "__main__":
    main()
