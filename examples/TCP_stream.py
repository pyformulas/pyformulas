import pyformulas as pf

class download_google(pf.net.Stream):
    def on_connect(self):
        self.send(bytes('DeepBlue\n\n', 'utf-8'))

    def on_receive(self, buffer):
        text = buffer.decode('utf-8', 'ignore')
        print(text)

download_google(port=23, address='freechess.org')