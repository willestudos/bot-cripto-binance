from binance.client import Client
from app.config.settings import settings

api_key = settings.bnc_api_key
api_secret = settings.bnc_api_secret
class ClientBinance:

    def connect_client(self):
        """
        Inicializa o cliente da Binance com as chaves de API fornecidas.

        :param api_key: Sua API Key da Binance.
        :param api_secret: Sua Secret Key da Binance.
        """
        client = Client(api_key, api_secret)
        return client