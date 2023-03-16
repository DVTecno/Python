from time import sleep
import requests
from datetime import datetime
import psycopg2
import psycopg
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
          'user':"postgres",
          'password':"5710",
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
def show_min_max(current_coins):
  query = """SELECT  simbolo,min(price),max(price)
          FROM    coin_price
          INNER JOIN coins ON coins.id=coin_price.coin_id
          WHERE   timestamp >= NOW() - INTERVAL '24 HOURS'
          GROUP BY coin_id simbolo"""
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print('-'*60)
  print('|{:>6}|{:>16}|{:>16}|{:>16} |'.format('Moneda', 'Actual', 'Minimo 24h', 'Maximo 24h'))
  print('-'*60)
  for reg in myresult:
    if reg[0] in current_coins:
        current_price = current_coins[reg[0]]['precio']
    print(f'|{reg[0]:>6}|{current_price:>16.4f}|{float(reg[1]):>16.4f}|{float(reg[2]):>16.4f} |')
  print('-'*60)

conf = Config()

mydb = psycopg2.connect(
    host=conf.database_conn['host'],
    user=conf.database_conn['user'],
    password=conf.database_conn['password'],
    database=conf.database_conn['database'],
    port='5050'
    )

mycursor = mydb.cursor()
while True:
  coins = get_currency(conf.url, conf.headers, conf.parameters)
  for key, coin in coins.items():
    mycursor.execute(f"SELECT * FROM coins WHERE simbolo='{key}'")
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
      for x in myresult:
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
show_min_max(coins)
  
  
print_table()
for i in range(0, 61):
    print(f'Esperando para actualizar... {60-i:03d} seg', end='\r')
    sleep(1)
print('\n') 
 