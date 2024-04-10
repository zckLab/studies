import os
from cryptography.fernet import Fernet

sex = Fernet.generate_key()

print(sex)