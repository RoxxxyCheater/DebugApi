API_KEY = '3580f26990a64cbbb6db495bb0fad4a3'




# class RealitySpiderSpider(scrapy.Spider):
#     name = "reality_spider"
#     allowed_domains = ["api.weatherbit.io"]
#     start_urls = ["http://api.weatherbit.io/v2.0/current?lat=48.9764357&lon=14.4079751&key={API_KEY}"]
#     pages_count = 25

#     def start_requests(self):
#         for page in range(1, 1 + self.pages_count):
#             url = f'http://api.weatherbit.io/v2.0/current?lat=48.9764357&lon=14.4079751&key={API_KEY}&page={page}'
#            # response = requests.get(url=f'http://api.weatherbit.io/v2.0/current?{lat}&{lon}&key={API_KEY}').json()
#             yield scrapy.Request(url, callback=self.parse)

#     def parse(self, response):
#         api_response = requests.get(response.url)
#         if api_response.status_code == 200: 
#             data = api_response.json()
        
#             with open("output.txt", "w") as file:
#                 for key, value in data.items():
#                     file.write(f"{key}: {value}\n")

# # Создаем объект CrawlerProcess
# process = CrawlerProcess()

# # Запускаем паука
# process.crawl(RealitySpiderSpider)
# process.start()
