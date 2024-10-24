from .config import Config
from .account import Account     
def main():
    config=Config()
    account=Account(config)
    account.close_position(keypair=config.TRADING_PAIR[0])
main()