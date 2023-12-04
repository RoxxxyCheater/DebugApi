# import scrapy
import requests
from log import API_KEY
# from scrapy.crawler import CrawlerProcess
from utils import write_request, generate_random_coordinates, gen_code
try_count = 0
try_uid_count = 0
bad_try_count = 0
good_try_count = 0
obj_count = 0
uid = ''


def get_weather_info(lat='48.9764357', lon='14.4079751'):
    global good_try_count
    global try_uid_count
    global obj_count
    global uid
    try:
        if try_uid_count > 9 or obj_count < good_try_count:
            print(try_uid_count)
            try_uid_count = 0
            print(try_uid_count)
            uid = gen_code()
            get_weather_info(lat=lat, lon=lon)
        elif try_uid_count <= 9 and obj_count > good_try_count:   
            response = requests.get(url = 'https://api.weatherbit.io/v2.0/normals?lat=48.9764357&lon=14.4079751&start_day=01-01&end_day=12-31&tp=daily&series_year=%201989-2020&key={API_KEY}').json()
            try_uid_count += 1
            data = {
                '[app_temp]': response['data'][0]['app_temp'],
                '[aqi]': response['data'][0]['aqi'],
                '[city_name]': response['data'][0]['city_name'],
                '[clouds]': response['data'][0]['clouds'],
                '[Region]': response['data'][0]['country_code'],
                '[datetime]': response['data'][0]['datetime'],
                '[dewpt]': response['data'][0]['dewpt'],
                '[Lat]': response['data'][0]['lat'],
                '[Lon]': response['data'][0]['lon'],
                '[dhi]': response['data'][0]['dhi'],
                '[dni]': response['data'][0]['dni'],
                '[elev_angle]': response['data'][0]['elev_angle'],
                '[ghi]': response['data'][0]['ghi'],
                '[gust]': response['data'][0]['gust'],
                '[h_angle]': response['data'][0]['h_angle'],
                '[sunrise]': response['data'][0]['sunrise'],
                '[sunset]': response['data'][0]['sunset'],
                '[temp]': response['data'][0]['temp'],
                '[timezone]': response['data'][0]['timezone'],            
            }
            if 'data' in response and response['data']:
                write_request(data)
                good_try_count += 1
                return data 
            elif 'API key not valid' in response['error'] : 
                print('[!] API key not valid or Empty or missing data in the response.')
                global bad_try_count
                bad_try_count += 1
                raise KeyError
    except requests.exceptions.ConnectionError:
        print('[!] Please check youre connection!')
    except KeyError:
        print('[!] Key error. The "data" field is missing in the response.')
        main()
        return None



def main():
    global uid
    global try_count
    global obj_count
    uid = gen_code()     
    generated_coordinates = generate_random_coordinates() # кординаты в случае погоды
    print(f"Generated coordinates: Latitude={generated_coordinates[0]}, Longitude={generated_coordinates[1]}")
    res = input('Послать запрос по новым координатам? (y/n): ')
    obj_count  = int(input('Какое колличество обьектов/страниц необходимо?(Введите числовое значение): '))
    if res == 'y':
        try_count += 1
        get_weather_info(generated_coordinates[0], generated_coordinates[1])
    else:
        print('Генерирую новые кординаты')
        main()
if __name__ == "__main__":

    main()




