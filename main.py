from binance.um_futures import UMFutures;
from config import Config
co=Config()
api_key=co.PC_API_KEY
print(api_key)
with open ("/home/litterpigger/.keypair/Private_key") as f:
    private_key=f.read()

client=UMFutures(key=api_key,private_key=private_key)
params={
    'symbol':'WLDUSDT',
    'side':'SELL',
    'type':'MARKET',
     'quantity':4,
}
print(client.get_open_orders(symbol="WLDUSDT"))

