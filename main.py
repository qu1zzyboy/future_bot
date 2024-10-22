from binance.um_futures import UMFutures;
from config import Config
import json
co=Config()
api_key=co.HP_API_KEY
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
account_rec_data=client.account()
assets_array=account_rec_data.get("assets")
for asset in assets_array:
    if(float(asset.get("walletBalance"))!=0):
        print(asset.get("asset"))


