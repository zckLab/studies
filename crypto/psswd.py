# Função para criptografar a senha usando PyOpenSSL
def encrypt_with_openssl(password):
    # Aqui você usaria as funções do PyOpenSSL para criptografar a senha
    # Este é apenas um exemplo básico e não deve ser utilizado em produção
    encrypted_password = OpenSSL.crypto.encrypt(b'my_secret_key', password.encode('utf-8'))
    return encrypted_password

# Função para criptografar a senha usando cryptography.fernet
def encrypt_with_fernet(password):
    # Gere uma chave para o Fernet
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password, key

# Exemplo de uso das funções
user_password = input("Digite a senha que deseja criptografar: ")

# Criptografia usando PyOpenSSL
encrypted_password_openssl = encrypt_with_openssl(user_password)
print("Senha criptografada com PyOpenSSL:", encrypted_password_openssl)

# Criptografia usando cryptography.fernet
encrypted_password_fernet, encryption_key = encrypt_with_fernet(user_password)
print("Senha criptografada com cryptography.fernet:", encrypted_password_fernet)
print("Chave de criptografia:", encryption_key)