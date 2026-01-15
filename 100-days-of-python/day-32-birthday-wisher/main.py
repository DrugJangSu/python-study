# import smtplib

# my_email = "000000000000@gmail.com"
# password = "000000000000"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="000000000000@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# <yahoo>
# my_email = "000000000000@yahoo.com"
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
## yahoo app password is not available due to security and yahoo terms of use. sticking to Gmail for now.

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1997, month=8, day=28, hour=3)
# print(date_of_birth)



## Challenge 1 - Send Motivational Quotes on Mondays via Email-------------

# import smtplib
# import datetime as dt
# import random

# MY_EMAIL = "000000000000@gmail.com"
# MY_PASSWORD = "000000000000"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 3:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
    
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL, 
#                             to_addrs=MY_EMAIL, 
#                             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )




