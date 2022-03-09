# O trecho abaixo foi desenvolvido utilizando técnica de Web Scraping no site weather.com

#   -----------------------------------Início do código---------------------------------------

# from bs4 import BeautifulSoup
# from datetime import datetime
# import requests

# def get_info():

#     # Horário
#     last_upd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

#     # Definindo o site
#     # Nesse caso utilizei o link para os dados de Porto Alegre, mas poderia utilizar
#     # outro método, por exemplo passando a longitude e a latitude do local desejado:
#     # https://weather.com/weather/today/l/-30.02,-51.22 - Bairro Marcílio Dias, Porto Alegre, RS

#     html_page = requests.get("https://weather.com/weather/today/l/02497c1d67234f59ca3948f6a3361bfe5ebd55a13098b72e30391e48ce83be28").text
#     soup = BeautifulSoup(html_page,"lxml")


#     # Localização
#     current_location = soup.find("div", class_ = "CurrentConditions--header--27uOE")
#     location = current_location.find("h1", class_ = "CurrentConditions--location--kyTeL").text

#     # Temperatura
#     current_temperature = soup.find("div", class_ = "CurrentConditions--primary--2SVPh")
#     temperature_c = round((int(current_temperature.find("span", class_ = "CurrentConditions--tempValue--3a50n").text[:-1]) - 32) * (5 / 9),2)

#     # Sensação Térmica
#     current_feelslike = soup.find("div", class_ = "TodayDetailsCard--feelsLikeTemp--3fwAJ")
#     feelslike = round((int(current_feelslike.find("span", class_ = "TodayDetailsCard--feelsLikeTempValue--Cf9Sl").text[:-1]) - 32) * (5 / 9),2)

#     # Detalhes
#     current_details = soup.find("div", class_ = "TodayDetailsCard--detailsContainer--16Hg0")

#     # Umidade
#     humidity = current_details.find("span",{"data-testid":"PercentageValue"}).text

#     return last_upd, location, temperature_c, feelslike, humidity

#   -----------------------------------Fim do código---------------------------------------

# A partir da linha 47 foi utilizada a API da OpenWeather

from datetime import datetime
import requests

# Essa é a função utilizada para chamar a API e receber os dados

def getData(location):

    # Horário
    last_upd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    city = location
    api_key = ""            # Nesse campo é necessário utilizar a sua chave, é possível obter uma gratuitamente se registrando no site da OpenWeather
    unity_type = "metric"
    language = "pt_br"

    # Maiores detalhes sobre a API utilizada podem ser encontradas
    # na página de documentação https://openweathermap.org/current

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units={unity_type}&lang={language}")

    # Armazenando os dados obtidos em json pela API
    file_json = response.json()

    # Percorrendo os dados dentro do dicionário principal e armazenando dentro de outros dicionários os dados relevantes
    for key in file_json:
        if(key == "coord"):
            coord = file_json[key]
        if(key == "weather"):
            aux_weather = file_json[key]
            dict_aux = aux_weather[0]
            weather = dict_aux
        if(key == "base"):
            base = file_json[key]
        if(key == "main"):
            main = file_json[key]
        if(key == "visibility"):
            visibility = file_json[key]
        if(key == "wind"):
            wind = file_json[key]
        if(key == "clouds"):
            clouds = file_json[key]
        if(key == "dt"):
            dt = file_json[key]
        if(key == "sys"):
            sys = file_json[key]
        if(key == "timezone"):
            timezone = file_json[key]
        if(key == "id"):
            id = file_json[key]
        if(key == "name"):
            name = file_json[key]
        if(key == "cod"):
            cod = file_json[key]

    # Armazenando dados específicos de acordo com a chave requisitada
    temp = main.get("temp")
    feels_like = main.get("feels_like")
    humidity = main.get("humidity")
    description = weather.get("description")

    # Retornando alguns dos dados obtidos
    return last_upd, location, temp, feels_like, humidity, description.capitalize()