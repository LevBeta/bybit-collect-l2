from pybit.unified_trading import WebSocket

class BybitLinear:
    def __init__(self, queue, symbols):
        self.symbols = symbols
        self.queue = queue
        self.ws = WebSocket(
            testnet=False,
            channel_type="linear"
        )

    def start(self):
        for symbol in self.symbols:
            self.ws.orderbook_stream(50, symbol, self._handle_ob)

    def _handle_ob(self, message):
        self.queue.put(message)