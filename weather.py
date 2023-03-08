import requests

def Weather(city):
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=bcb59ece5810e1272e46ade32b2ef8ed'
    # city = input('Enter the  city: ')
    # url = api_address + city 
    json_data = requests.get(api_address).json() 
    # format_add = json_data['main'] 
    print(json_data) 
    return json_data