from sqlite3 import Cursor
from time import sleep
import mysql.connector
import requests
from datetime import datetime


class Config:
      def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'fea42815-ebda-4b39-9a22-3e057beda67d',
    }
        self.parameters = {
      'limit': '50',
      'convert': 'USD',
      'sort': 'market_cap'
    }
        self.database_conn = {
      'host':"localhost",
      'port':"3306",
      'user':"root",
      'password':"DVTecno",
      'database':"criptocoins"
    }

def get_currency(url, headers, parameters):
  result = requests.get(url, headers=headers, params=parameters)
  cripto_lastest = result.json()['data']
  coins = {}
  if (cripto_lastest):
    for cripto in cripto_lastest:
      coin = {}
      coin['nombre'] = cripto['name']
      coin['simbolo'] = cripto['symbol']
      coin['precio'] = cripto['quote']['USD']['price']
      coin['volumen_24h'] = cripto['quote']['USD']['volume_24h']
      coins[coin['simbolo']] = coin
  return coins 

def update_average(current_coins):
  tiempo = 30
  query = f"""SELECT  simbolo,AVG(price)
          FROM    coin_price
          INNER JOIN coins ON coins.id=coin_price.coin_id
          WHERE   timestamp >= NOW() - INTERVAL {tiempo} MINUTE
          GROUP BY coin_id"""
  mycursor.execute(query)
  
  myresult = mycursor.fetchall()
  for reg in myresult:# type: ignore
    coins_table[reg[0]] = [current_coins[reg[0]]['precio'], reg[1]]
  for tiempo in range(5, 15, 5):
    query = f"""SELECT  simbolo,AVG(price)
          FROM    coin_price
          INNER JOIN coins ON coins.id=coin_price.coin_id
          WHERE   timestamp >= NOW() - INTERVAL {tiempo} MINUTE
          GROUP BY coin_id"""
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for reg in myresult:# type: ignore
      coins_table[reg[0]].append(reg[1])

def print_table():
  print('-'*78)
  print('|{:>6}|{:>16}|{:>16}|{:>16} |{:>16} |'.format(
      'Moneda', '5 Minutos', '10 Minutos', '15 Minutos', '30 Minutos'))
  print('-'*78)
  for key, coin in coins_table.items():
    print(
        f'|{key:>6}|{coin[0]:>16.4f}|{float(coin[1]):>16.4f}|{float(coin[2]):>16.4f} |{float(coin[3]):>16.4f} |')
  print('-'*78)
  
conf = Config()
coins_table = dict()

mydb = mysql.connector.connect(
    host=conf.database_conn['host'],
    user=conf.database_conn['user'],
    password=conf.database_conn['password'],
    database=conf.database_conn['database']
    )

mycursor = mydb.cursor()
while True:
  coins = get_currency(conf.url, conf.headers, conf.parameters)
  for key, coin in coins.items():
    mycursor.execute(f"SELECT * FROM coins WHERE simbolo='{key}'")
    myresult = mycursor.fetchall()
    if len(myresult) > 0:# type: ignore 
      for x in myresult:# type: ignore
        sql = "INSERT INTO coin_price (timestamp, coin_id, price) VALUES (%s,%s,%s)"
        val = (datetime.now(), x[0], coin['precio'])
        mycursor.execute(sql, val)
        mydb.commit()
    else:
      sql = "INSERT INTO coins (simbolo, nombre) VALUES (%s, %s)"
      val = (key, coin['nombre'])
      mycursor.execute(sql, val)
      result = mydb.commit()
  print('Se han registrados los precios de las monedas')
  #show_min_max(coins)
  
  update_average(coins)
  print_table()
  for i in range(0, 61):
    print(f'Esperando para actualizar... {60-i:03d} seg', end='\r')
    sleep(1)
  print('\n') 
 