from socketio import Client


class ClientIOS:
    def __init__(self, network_nodes=None):
        if network_nodes is None:
            network_nodes = []
        self.ios: list[Client] = []
        for node in network_nodes:
            clientio = Client()
            try:
                clientio.connect(node)
                self.ios.append(clientio)
            except Exception as e:
                print("impossible connect to " + node + "\n" + str(e))

    def register_nodes(self, network_nodes=None):
        if network_nodes is None:
            network_nodes = []
        self.ios: list[Client] = []
        for node in network_nodes:
            clientio = Client()
            try:
                clientio.connect(node)
                self.ios.append(clientio)
            except Exception as e:
                print("impossible connect to " + node + '\n' + str(e))

    def emit(self, call, message):
        if message is None:
            return
        for c in self.ios:
            try:
                c.emit(call, message)
            except Exception as e:
                print(f'\x1b[30;41m {str(e)} \x1b[0m')
                #log(str(e))


    def to_dict(self) -> dict:
        d: dict = {}
        for c in self.ios:
            d[c.connection_url] = c.sid
        return d
