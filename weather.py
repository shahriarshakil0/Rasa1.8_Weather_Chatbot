import requests
def Weather(city):
    API_key = "6d7df9a897613928d3c4c102d99cbea2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    Final_url = base_url + "appid=" + API_key + "&q=" + city 
    weather_data = requests.get(Final_url).json()
    
    kword={
        'main':weather_data['main'],
        'weather':weather_data['weather'],
        'wind':weather_data['wind'],
    }

    return kword