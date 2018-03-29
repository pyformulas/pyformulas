from threading import Thread

class thread(Thread):  # TODO: Have to include thread here due to a starnge bug
    def __init__(self, function, callback=None):  # , callback=None):
        from threading import Thread
        Thread.__init__(self)

        self.function = function
        self.callback = callback
        self.result = None

        self.start()

    def run(self):
        self.result = self.function()

        if not isinstance(self.result, tuple):
            self.result = (self.result,)

        if self.callback is not None:
            self.callback(*self.result)

class Stream:
    ##def __new__(self, port, *args, address=None, block=False, **kwargs):
    #def __new__(self, port, address=None):
    #    #kwargs['address'] = address
    #    #kwargs['block'] = block
    #    #self._params = ((port,) + args), kwargs

    #    self.port = port
    #    self.address = address

    #    import socket
    #    self._socket = socket
    #    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #    if address is None:
    #        self._make_server(self)
    #    else:
    #        self._make_client(self)

    #    return self

    def __init__(self, port, address=None):
        #kwargs['address'] = address
        #kwargs['block'] = block
        #self._params = ((port,) + args), kwargs

        self.port = port
        self.address = address

        import socket
        self._socket = socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connections = []

        if address is None:
            self._isserver = True
            self._make_server(self)
        else:
            self._isserver = False
            self._make_client()


    ######## Dummy functions ########


    def on_receive(self, conn, buffer):
        pass

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    ##################################


    class _make_server:
        def __init__(self, parent):
            self.parent = parent

            self.parent.socket.bind(('', self.parent.port))
            max_connections = 5
            self.parent.socket.listen(max_connections)

            for i in range(max_connections):
                thread(self.parent._accept, self.parent._accept_callback)

    def _accept(self):
        try:
            return self.socket.accept()
        except OSError:
            return None, None

    def _accept_callback(self, socket, address):
        if socket is None:
            return

        connection = self.Connection(self, socket)
        self.connections.append(connection)

    def _make_client(self):
        self.socket.connect((self.address, self.port))
        connection = self.Connection(self, self.socket)
        self.connections.append(connection)

    def shutdown(self):# TODO: may break _recv_loop
        for conn in self.connections:
            if conn.socket.fileno() != -1:
                conn.socket.close()

        if self.socket.fileno() != -1:
            self.socket.close()

    class Connection:
        def __init__(self, stream, socket):
            from select import select
            from time import sleep
            self._select = select
            self._sleep = sleep

            self.stream = stream
            self.socket = socket

            thread(self._recv_loop)

            #self.stream.__init__(self, *(self.stream._params[0]), **(self.stream._params[1]))
            self.stream.on_connect(self)

        def disconnect(self):
            self.socket.close()
            self.stream.on_disconnect(self)

            if self.stream._isserver:
                if self.stream.socket.fileno() != -1:# Listen for another connection
                    thread(self.stream._accept, self.stream._accept_callback)

                self.stream.connections.remove(self)

        def send(self, bytes):
            self.socket.send(bytes)

        def _recv_loop(self):
            while self.socket.fileno() != -1 and len(self._select([self.socket], [], [], 0)[0]) == 0:# Wait for the socket to become readable
                #print('waiting')
                self._sleep(1e-9)

            while True:
                if self.socket.fileno() == -1:# or len(self._select([self.socket], [], [], 0)[0]) == 0:
                    #print("socket not readable", self.socket.fileno())
                    break

                try:
                    buffer = self.socket.recv(4096)
                except ConnectionAbortedError:# Peer disconnected?
                    #print("connection aborted")
                    self.disconnect()
                    break

                if len(buffer) > 0:
                    #print("bufsize > 0")
                    self.stream.on_receive(self, buffer)

                elif len(self._select([self.socket], [], [], 0)[0]) == 1: # Socket still readable: peer disconnnected
                    #print("peer disconnected (bufsize 0)")
                    self.disconnect()
                    break