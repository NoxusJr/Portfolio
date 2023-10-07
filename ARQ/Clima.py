#ULTIMA ATUALIZAÇÃO: 06/10/2023

import requests
import os

API_KEY = "3e4dd683cf98705c0a3a70604f82c5dc"

def sistema():
    while True:

        # INTERFACE
        os.system("cls")

        print("-"*50)
        print("[1] - Consultar Clima")
        print("[2] - Sair")
        print("-"*50)

        escolha = int(input())
        print("-"*50)
        if escolha == 1:

            cidade = input("Informe A Cidade: ")
            print("-"*50)

        # CONEXÃO COM A API PASSANDO OS PARAMETROS DESEJADOS
            link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

        # OBETENDO E FORMATANDO OS DADOS
            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()

        # SELECIONANDO OS DADOS DESEJADOS
            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15
            umidade = requisicao_dic['main']['humidity']

            os.system("cls")
            
            print("+"*50)
            print(f"A Condição De {cidade} É De '{descricao}'")
            print("-"*50)
            print(f"A Temperatura Atual É De {temperatura:.2f}°C")
            print("-"*50)
            print(f"A Umidade Do Ar É De {umidade}")
            print("+"*50)
            i = input("Pressione Enter Para Continuar")
            print("-"*50)
            sistema()   
        else:
            exit()

sistema()