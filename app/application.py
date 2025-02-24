import time

from app.services.binance_service import ServicesBot
client = ServicesBot()


def account_info():
    response = client.get_account_info()
    print(f'Account info: {response}')

def acount_asset_balace():
    response = client.get_asset_balance("FLOKIUSDT")
    print(f'Account asset: {response}')

def get_price_bet():
    buy = 0.00004049 # Defina o valor de alerta compra
    sell = 0.00012049 # Defina o Valoe de alerta de venda
    while True:
        btc_price = client.get_btc_price("FLOKIUSDT")
        print(f"Preço do BTC: {btc_price} FLOKIUSDT")
        client.check_price_alert(btc_price, buy, sell)
        time.sleep(1)


if __name__ == '__main__':
    get_price_bet()