import requests #HTTP
import base64 #BASE64

auth_header = "Basic c2l0aXVtOnN1Y2Nlc3M="

encoded_auth_data = auth_header.split(' ')[1]
decoded_auth_data = base64.b64decode(encoded_auth_data).decode('utf-8')

username, password = decoded_auth_data.split(':')

with open('dictionary.txt') as f:  #otwieramy przykładowy słownik potrzebny do cracka hasła
    for line in f:
        if line.strip() == password:
            print(f'Użytkownik {username} został zautoryzowany z hasłem {password}')