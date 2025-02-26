from binance import BinanceAPIException
from app.interface.bnc_cliente_interface import ClientBinance
from app.config.settings import settings
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

    def get_info_btc(self):
        try:
            data = client_bnc.connect_client().get_symbol_info(settings.btc_asset)
            print(f'BTC info: {data}')
        except BinanceAPIException as e:
            print(f"Erro ao acessar info BTC: {e}")
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
        symbol_ticker = client_bnc.connect_client().get_symbol_ticker(symbol=symbol)
        ticker = client_bnc.connect_client().get_ticker(symbol=symbol)
        price_change = float(ticker['priceChange'])
        price_change_percent = float(ticker['priceChangePercent'])
        print(f'Variação preço: {price_change}\n Porcentagem de variação: {price_change_percent}%')
        price = float(symbol_ticker['price'])
        return float("{:.8f}".format(price))  # Formata para 8 casas decimais e converte de volta para float

    def check_price_alert(self, price, buy, sell ):
        if price < buy:
            print(f"Alerta: O preço do BTC caiu abaixo de {buy} USDT!")
            self.buy_btc(settings.btc_asset,1)

        if price > sell:
            print(f"Alerta: O preço do BTC estaUIi acima de {sell} USDT!")
            self.sell_btc(settings.btc_asset, settings.buy_quantity)

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

    def sell_btc(self, symbol, quantity):
        """
        Cria uma ordem de mercado para vender uma quantidade específica de um ativo.

        :param symbol: O par de trading (ex: 'BTCUSDT').
        :param quantity: Quantidade do ativo a ser vendida.
        :return: Resposta da API da Binance.
        """
        try:
            order = client_bnc.connect_client().order_market_sell(
                symbol=symbol,
                quantity=quantity
            )
            return order
        except BinanceAPIException as e:
            print(f"Erro ao criar ordem de venda: {e}")
            return None