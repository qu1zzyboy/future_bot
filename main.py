from binance.um_futures import UMFutures;
api_key="MTXEJs8Qr2vGGS80cFPcQv3wGMp1lS34icsvAv6ViPVrh9uB8A33n8v1Oc59McKL"
with open ("/home/litterpigger/.keypair/Private_key") as f:
    private_key=f.read()

client=UMFutures(key=api_key,private_key=private_key)
params={
    'symbol':'WLDUSDT',
    'side':'SELL',
    'type':'MARKET',
     'quantity':4,
}
account_balance=client.new_order(**params);
print(account_balance)

