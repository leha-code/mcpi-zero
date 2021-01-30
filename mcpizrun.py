from sys import version
from mcpizero.util import platform, start_normal
from mcpizero.shared_functions import *
if platform == 'RaspberryPi':
    from mcpizero.mcpi_functions import *
elif platform == 'RaspberryJuice':
    from mcpizero.raspberryjuice_functions import *


if start_normal:
    try: start()
    except ConnectionRefusedError:
        print('Sorry. restart shell and run minecraft pi at the same time. You didn\'t run minecraft')
if __name__ == '__main__':
    chat('Hello Minecraft World!')
