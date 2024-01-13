import requests
import smtplib
from datetime import datetime

MY_EMAIL= "xyz@gmail.com"
MY_PASSWORD="abc123"
MY_LAT= 26.846695
MY_LNG= -80.946167

# using API to find data about ISS on given longitude and latitude 
def is_iss_overhead():
    response= requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # print(response.json())
    data= response.json()

    longitude= float(data["iss_position"]["longitude"])
    latitude= float(data["iss_position"]["latitude"])

    if(MY_LAT-5<=latitude<= MY_LAT+5 and MY_LNG-5<=longitude<= MY_LNG+5):
        return True
    return False


# checking if it is night presently
def isNight():
    parameters={
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted":0,
    }

    time_now= datetime.now()

    response= requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    data= response.json()
    sunrise= int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset= int(data["results"]["sunset"].split('T')[1].split(":")[0])
    
    if(time_now.hour>=sunset or time_now.hour<sunrise):
        return True
    return False

# If it is night and iss is overhead, send mail
if is_iss_overhead() and isNight():
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Up\n\nThe ISS is above you in the sky"
    )

