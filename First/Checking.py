import Parcing_sites as P_s
import pandas
import datetime

daterange = P_s.data_range('03/02/2023','07/02/2023')
a = list()
i = 0
for simple_date in daterange:
    i =+ 1
    str_simple_data = str(simple_date)
    a.append(str(simple_date))
print(a)
