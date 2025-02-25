import time
from app.dev_utility.ultutilitarians import clear
from app.services.binance_service import ServicesBot
from app.config.settings import settings

client = ServicesBot()


def account_info():
    response = client.get_account_info()
    print(f'Account info: {response}')

def acount_asset_balace():
    response = client.get_asset_balance(settings.btc_asset)
    print(f'Account asset: {response}')

def get_price_bet():
    buy = float("{:.8f}".format(settings.buy_value)) # Defina o valor de alerta compra
    sell = float("{:.8f}".format(settings.sell_value)) # Defina o Valoe de alerta de venda
    client.get_info_btc()
    time.sleep(10)
    while True:
        btc_price = client.get_btc_price(settings.btc_asset)
        print(f"Preço do BTC: {btc_price} {settings.btc_asset}")
        clear()
        client.check_price_alert(btc_price, buy, sell)
        time.sleep(5)


if __name__ == '__main__':
    get_price_bet()