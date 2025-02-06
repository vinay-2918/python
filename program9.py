from  datetime import datetime, timedelta
today = datetime.today()
days_to_add = 5
new = today + timedelta(days=days_to_add)
print(f"todays date and time is {today}",today.strftime("%D-%M-%Y %H:%M:%S"))
print(f"after adding 5 days {new}" ,new.strftime("%D-%M-%Y %H:%M:%S"))