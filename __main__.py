from .config import Config
from .account import Account     
def main():
    config=Config()
    account=Account(config)
    account.get_USDT()
main()