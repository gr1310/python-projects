import requests
import smtplib
import datetime

MY_EMAIL= "xyz@gmail.com"
MY_PASSWORD= "abc123"

SEND_MAIL=MY_EMAIL

API_KEY= 'dummyapi'

MY_LAT= 53.8655
MY_LONG= 10.6866

OWM_Endpt= "https://api.openweathermap.org/data/2.5/forecast"

weather_params={
    "lat": MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY,
}
response= requests.get(url=OWM_Endpt, params=weather_params)
response.raise_for_status()

data= response.json()

will_rain=False

city_name= data['city']['name']

min_temp_night=200
min_temp_day=200

for i in range(40):
    rain_id=data['list'][i]['weather'][0]['id']
    if(int(rain_id)<700):
        will_rain=True
    time= ((data['list'][i]['dt_txt']).split(" ")[1])
    time_object = datetime.datetime.strptime(time, '%H:%M:%S').time()
    if(time_object.hour>=21 or time_object.hour<6):
        min_temp_night= min(int(data['list'][i]['main']['temp_min'])-273.15,min_temp_night)
    else:
        min_temp_day= min(int(data['list'][i]['main']['temp_min'])-273.15,min_temp_day)


if(min_temp_day<15):
    season="cold"
elif(min_temp_day>15 and min_temp_day<25):
    season="moderate temperature"
else:
    season="hot"

min_temp_day=str(min_temp_day)
min_temp_night= str(min_temp_night)

if(will_rain):
    message= "Subject:Weather Forcast\n\n Hey, it'll be raining today in "+city_name+" and it'll be "+season+", make sure to carry an umbrella!\n\n The minimum temperature for next 5 days will be,\n In day time: "+min_temp_day+" degrees celcius\n In night time: "+min_temp_night+" degrees celcius\n Have a nice day! \n\n Yours, Garima "
else:
    message="Subject:Weather Forcast\n\n Hey, it won't be raining today in "+city_name+" and it'll be "+season+".\n\n The minimum temperature for next 5 days will be,\n In day time: "+min_temp_day+" degrees celcius\n In night time: "+min_temp_night+" degrees celcius\n Have a nice day! \n\n Yours, Garima"

print(message)

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_MAIL, msg=message)