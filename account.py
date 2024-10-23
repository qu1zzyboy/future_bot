from binance.um_futures import UMFutures
from .config import Config
config=Config()
class Account:
    def __init__(self,config:Config):
        self.client=UMFutures(key=config.HP_API_KEY,private_key=config.HP_SECRET_KEY)
    def open_order(self,config:Config):
        params = {
            'symbol': 'WLDUSDT',
            'side': 'SELL',
            'type': 'MARKET',
            
            'quantity': config.WLD_AMOUNT,
        }
        self.client.new_order(**params)
        print("Successfully open order with amount of", config.WLD_AMOUNT)
    def get_live_order(self,config:Config):
        live_order=self.client.get_open_orders(config.TRADING_PAIR)
        print(live_order)
    def get_all_orders(self,config:Config):  
        all_orders=self.client.get_all_orders(config.TRADING_PAIR)
        print(all_orders)
    def cancel_all_orders(self,config:Config):
        cancel_all_orders=self.client.cancel_open_orders(config.TRADING_PAIR)
        print(cancel_all_orders)
    def get_USDT(self):
        account_balance=self.client.balance()
        print(account_balance)

