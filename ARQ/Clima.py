import requests
import os

API_KEY = "3e4dd683cf98705c0a3a70604f82c5dc"

def sistema():
    while True:
        os.system("cls")

        print("-"*80)
        print("[1] - Consultar Clima")
        print("[2] - Sair")
        print("-"*80)

        escolha = int(input())
        print("-"*80)
        if escolha == 1:

            cidade = input("Informe A Cidade: ")
            print("-"*80)
            link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

            requisicao = requests.get(link)
            requisicao_dic = requisicao.json()

            descricao = requisicao_dic['weather'][0]['description']
            temperatura = requisicao_dic['main']['temp'] - 273.15

            print(f"A Condição De {cidade} É De '{descricao}'. A Temperatura Atual É De {temperatura:.2f}°C")
            print("-"*80)
            i = input("Pressione Enter Para Continuar")
            print("-"*80)
            sistema()   
        elif escolha ==2:
            exit()

sistema()