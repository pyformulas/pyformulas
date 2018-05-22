"""
Connects to a chess server over telnet, by creating a pf.net.Stream
"""

import pyformulas as pf

class play_chess(pf.net.Stream):
    def on_connect(self, conn):
        conn.send(bytes('DeepBlue\n\n', 'utf-8'))

    def on_receive(self, conn, buffer):
        text = buffer.decode('utf-8', 'ignore')
        print(text)

        if 'Message Of The Day' in text:
            conn.disconnect()

play_chess(port=23, address='freechess.org')