from datetime import datetime

def date_to_week_day_conversion(dt_string):

    dt_object = datetime.strptime(dt_string, "%d%m%Y")
    day_num=dt_object.weekday()
    day_names={0:"Monday",1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    result = day_names[day_num]
    print("Week day is :",result)

dt_string = input("Enter the date: ")
date_to_week_day_conversion(dt_string)