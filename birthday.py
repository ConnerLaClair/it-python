import datetime
from banner import banner

banner("Birthday","Paul Blart")

# Find out when you were born
# Figure out how many days until your birthday
# Print information about the birthday: Days ago, or Happy B-Day

def main():
    birthday = get_birthday_info()
    compute_days_between_dates()
    print_brithday_info()

def get_birthday_info():
    print("When were you born?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates():
    pass

def print_brithday_info():
    pass



main()