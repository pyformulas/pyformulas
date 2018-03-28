import pyformulas as pf

class play_chess(pf.net.Stream):
    def on_connect(self):
        self.send(bytes('DeepBlue\n\n', 'utf-8'))

    def on_receive(self, buffer):
        text = buffer.decode('utf-8', 'ignore')
        print(text)

        if 'Message Of The Day' in text:
            self.disconnect()

play_chess(port=23, address='freechess.org')