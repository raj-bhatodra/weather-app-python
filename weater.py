import requests

API_KEY = 'fd3c8caaa887ba999bdd97145cdb6289'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter City Name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print('Weather: ', weather)
    print('Temperature: ', temperature,'°C')
else:
    print('An error occurred')