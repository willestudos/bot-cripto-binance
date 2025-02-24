from typing import Any

from binance import BinanceAPIException

from app.interface.bnc_cliente_interface import ClientBinance

client_bnc = ClientBinance()

class ServicesBot:

    def get_account_info(self):
        """Retorna informações da conta."""
        try:
            data = client_bnc.connect_client().get_account()
            return data
        except BinanceAPIException as e:
            print(f"Erro ao acessar a API da Binance: {e}")
            return None

    def get_asset_balance(self, asset):
        """Retorna o saldo de um ativo específico."""
        account_info = self.get_account_info()
        if account_info:
            for balance in account_info['balances']:
                if balance['asset'] == asset:
                    return float(balance['free'])
        return 0.0

    def get_btc_price(self, symbol):
        ticker = client_bnc.connect_client().get_symbol_ticker(symbol=symbol)
        return float(ticker['price'])

    def check_price_alert(self, price, buy, sell ):
        if price < buy:
            print(f"Alerta: O preço do BTC caiu abaixo de {buy} USDT!")
            self.buy_btc("BTCUSDT",1)

        if price > sell:
            print(f"Alerta: O preço do BTC esta acima de {sell} USDT!")

    def buy_btc(self, symbol, quantity):
        """
        Cria uma ordem de mercado para comprar uma quantidade específica de um ativo.

        :param symbol: O par de trading (ex: 'BTCUSDT').
        :param quantity: Quantidade do ativo a ser comprada.
        :return: Resposta da API da Binance.
        """
        try:
            order = client_bnc.connect_client().order_market_buy(
                symbol=symbol,
                quantity=quantity
            )
            return order
        except BinanceAPIException as e:
            print(f"Erro ao criar ordem de compra: {e}")
            return None