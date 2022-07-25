import requests
import config  # config.py com api_key = 'xxxxxx'

api_key = config.api_key

def clima(cidade):




cidade_atual = input('Favor inserir o nome de uma cidade: ')
cidade_atual = cidade_atual.lower()
# print(cidade)


while requisicao_atual.status_code != 200:
    print('Cidade inválida, tente novamente.')
    cidade_atual = input('Favor inserir o nome de uma cidade: ')
    cidade_atual = cidade_atual.lower()
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade_atual}&appid={api_key}&lang=pt_br'
    requisicao_atual = requests.get(link)

requisicao_dic_atual = requisicao_atual.json()
# print(requisicao_dic_atual)

temperatura_atual = requisicao_dic_atual['main']['temp'] - 273.15
descricao_atual = requisicao_dic_atual['weather'][0]['description']
sensacao_termica_atual = requisicao_dic_atual['main']['feels_like'] - 273.15

print(f'O tempo em {cidade_atual.capitalize()}:')
print(f'Temperatura: {temperatura_atual:.2f}°C')
print(f'Céu: {descricao_atual.capitalize()}')
print(f'Sensação térmica de: {sensacao_termica_atual:.2f}°C')
