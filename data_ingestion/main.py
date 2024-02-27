# https://pypi.org/project/websocket_client/
import websocket
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("API_KEY")
SYMBOLS = ["AAPL", "AMZN"]


@dataclass
class WebSocket:
    token: str
    symbols: list[str]
    endpoint: str = "wss://ws.finnhub.io?token="

    def __on_message(self, ws, message):
        print(message)

    def __on_error(self, ws, error):
        print(error)

    def __on_close(self, ws):
        print("### closed ###")

    def __on_open(self, ws):
        for symbol in SYMBOLS:
            ws.send('{{"type":"subscribe","symbol":"{}"}}'.format(symbol))

    def run_forever(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            f"{self.endpoint}{self.token}",
            on_message=self.__on_message,
            on_error=self.__on_error,
            on_close=self.__on_close,
        )
        ws.on_open = self.__on_open
        ws.run_forever()


if __name__ == "__main__":
    websocket_object = WebSocket(TOKEN, SYMBOLS)
    websocket_object.run_forever()
