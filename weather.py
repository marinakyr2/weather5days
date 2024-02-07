from weather_api import get_weather,get_weather_detals,Weather

def main():
    user_city: str= input('Enter a city: ')

    current_weather: dict = get_weather(user_city, mock=False)
    weather_details: list[Weather]= get_weather_detals(current_weather)

    #get days
    dfmt: str= '%d/%m/%y'
    days: list[str]= sorted(list({f'{date.date:{dfmt}}' for date in weather_details}))
    print(days)

    for day in days:
        print('---')
        print(day)

        grouped: list[Weather]= [current for current in weather_details if f'{current.date:{dfmt}}'== day]
        for element in grouped:
            print(element)

if __name__== '__main__':
    main()