import os
from cryptography.fernet import Fernet
from OpenSSL import crypto , SSL

files = []
#T
with open("chave.key", "rb") as key:
    secretkey = key.read()#T

# Verifica se já existe a chave e a carrega, ou a gera e salva.T 
if os.path.exists("chave.key"):
    with open("chave.key", "rb") as chave:
        key = chave.read()
else:
    key = Fernet.generate_key()
    with open("chave.key", "wb") as chave:
        chave.write(key)
#T
cipher = Fernet(key) #T
#T
for file in os.listdir():
    if file == "main.py" or file == "chave.key" or file == "mlwr.py":
        continue
    if os.path.isfile(file):
        files.append(file)
#T
for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
        conteudo_decrypted = cipher.decrypt(conteudo)
        with open(file, "wb") as arquivo:
            arquivo.write(conteudo_decrypted)
