from datetime import datetime

def calculate_year():

    current_year = datetime.now().year

    name = input("Enter the name :")
    age = int(input("Enter the age :"))

    years_utill_100 = 100-age   

    year_untill = years_utill_100 + current_year 

    print(name,"will ndie at the age",year_untill)

calculate_year()



    

