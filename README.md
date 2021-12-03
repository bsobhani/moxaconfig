# moxaconfig

Python interface to Moxa NPort5150A

Example:

from nport5150a import NPort5150A

moxa = NPort5150A("192.168.127.254")
moxa.set_baud_rate("9600")
