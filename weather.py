import requests

from config import URL
class WeatherApp:
    def __init__(self, api_key):
        self.__url = URL
        self.api_key = api_key
        self.session = requests.Session()


    def _make_request(self, *, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response

    def get_weather(self, city, lang='ru', units='metric'):
        request_url = self.__url.format(city, self.api_key, lang, units)
        response = self._make_request(url = request_url)
        if response.ok:
            city = response.json()['name']
            temp = response.json()['main']['temp']
            return f'{city}: {temp}'
        return 'Something went wrong with request'
