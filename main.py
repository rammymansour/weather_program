import requests
from datetime import date
api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=gothenburg'

url = api_address
json_data = requests.get(url).json()
format_add = json_data['weather'] [0] ["description"]
formatted_add = json_data['main'] ["temp"]
Kelvin = float(formatted_add)

Celsius = Kelvin - 273.15
temp = round(Celsius, 1)
str_temp = str(temp)

print(date.today().strftime('%Y-%m-%d'))
print(format_add)
print (str(temp))



my_file = open("c:\Projects\\weather\\" + "weather.txt", "a+")
my_file.write(date.today().strftime('%Y-%m-%d') + "\n" + format_add + "\n" + str(temp) )


print(format_add)
print(formatted_add)
print(Celsius)
print (temp)
print(date.today().strftime('%Y-%m-%d'))


