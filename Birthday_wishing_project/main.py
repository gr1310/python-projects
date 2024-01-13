import random
import datetime as dt 
import smtplib

MY_EMAIL= "xyz@gmail.com"
MY_PASSWORD="abcdpass"

birthdays=[]

with open("mail_connection\Birthday_wishing_project\people.csv", 'r') as file:
    contents= file.read()
    birthdays= contents.split('\n')
print(birthdays)

msg_num= str(random.randint(1,3))

today= dt.datetime.now()
today_month= today.month
today_day= today.day

print(today_day, today_month)

for i in birthdays[1:]:
    data= i.split(',')
    # print(type(data[-1]), type(today_day))
    print(data)
    if(int(data[-2])==today_month and int(data[-1])==today_day):
        print("yes")
        with open("mail_connection\Birthday_wishing_project\msg"+msg_num+".txt",'r') as file:
            msg= file.read()
        final_msg= msg.replace("[Name]", data[0])
        print(final_msg)
        send_mail= data[1]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=send_mail,
                                msg="Subject:Happy Birthday!!\n\n"+final_msg)

