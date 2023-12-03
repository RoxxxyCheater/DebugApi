import scrapy
import requests
from log import API_KEY
from scrapy.crawler import CrawlerProcess

class RealitySpiderSpider(scrapy.Spider):
    name = "reality_spider"
    allowed_domains = ["api.weatherbit.io"]
    start_urls = ["http://api.weatherbit.io/v2.0/current?lat=48.9764357&lon=14.4079751&key={API_KEY}"]
    pages_count = 25

    def start_requests(self):
        for page in range(1, 1 + self.pages_count):
            url = f'http://api.weatherbit.io/v2.0/current?lat=48.9764357&lon=14.4079751&key={API_KEY}&page={page}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        api_response = requests.get(response.url)
        if api_response.status_code == 200: 
            data = api_response.json()
        
            with open("output.txt", "w") as file:
                for key, value in data.items():
                    file.write(f"{key}: {value}\n")

# Создаем объект CrawlerProcess
process = CrawlerProcess()

# Запускаем паука
process.crawl(RealitySpiderSpider)
process.start()

# def write_to(data):
#     with open("output.txt", "w") as file:
#         for key, value in data.items():
#             file.write(f"{key}: {value}\n")


#     # with open("output.py", "w") as file:
#     #     file.write("my_data = " + repr(data))

#     # with open("output.json", "w") as file:
#     #     json.dump(data, file)

# def get_weather_info(ip='127.0.0.1'):
#     try:
#         response = requests.get(url=f'http://api.weatherbit.io/v2.0/current?lat=48.9764357&lon=14.4079751&key={API_KEY}& {ip}').json()
#         data = {
#             '[app_temp]': response['data'][0]['app_temp'],
#             '[aqi]': response['data'][0]['aqi'],
#             '[city_name]': response['data'][0]['city_name'],
#             '[clouds]': response['data'][0]['clouds'],
#             '[Region]': response['data'][0]['country_code'],
#             '[datetime]': response['data'][0]['datetime'],
#             '[dewpt]': response['data'][0]['dewpt'],
#             '[Lat]': response['data'][0]['lat'],
#             '[Lon]': response['data'][0]['lon'],
#             '[dhi]': response['data'][0]['dhi'],
#             '[dni]': response['data'][0]['dni'],
#             '[elev_angle]': response['data'][0]['elev_angle'],
#             '[ghi]': response['data'][0]['ghi'],
#             '[gust]': response['data'][0]['gust'],
#             '[h_angle]': response['data'][0]['h_angle'],
#             '[sunrise]': response['data'][0]['sunrise'],
#             '[sunset]': response['data'][0]['sunset'],
#             '[temp]': response['data'][0]['temp'],
#             '[timezone]': response['data'][0]['timezone'],            
#         }

#         write_to(data)
#         return data
#     except requests.exceptions.ConnectionError:
#         print('[!] Please check youre connection!')



# get_weather_info()