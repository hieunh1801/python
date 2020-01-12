from datetime import datetime, date

today = datetime.now() # 2020-01-12 10:07:07.099882

today = date.today() # 2020-01-12

today.month # 01
today.year # 22020
today.day # 12
# fromtimestamp => to date
timestamp = date.fromtimestamp(1326244364) # 2012-01-11



# date => str
now = datetime.now() # 2020-01-12 10:07:07.099882
s1 = now.strftime("%H:%M:%S") # 10:14:50. Type: str
s2 = now.strftime("%d/%m/%Y, %H:%M:%S") # 12/01/2020, 10:15:03. Type: str


# str => date
date_str = "18/01/2020" 
date_format = "%d/%m/%Y"
date_object = datetime.strptime(date_str, date_format) # 2020-01-18 00:00:00
print(date_object)