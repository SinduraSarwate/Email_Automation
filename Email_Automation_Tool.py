import schedule
from schedule import every,repeat
import time as tm
from datetime import time, timedelta, datetime
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()

sender = input("Sender: ")
receiver = input("Receiver:")

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n{message}"

s.login(sender,"nxzk qtex xlfu ceen")
s.sendmail(sender,receiver,text)
def work():
    s.sendmail(sender,receiver,text)
schedule.every(10).seconds.do(work)

while True:
    schedule.run_pending()
    tm.sleep(1)
