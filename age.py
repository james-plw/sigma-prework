import datetime as dt


def age_calc(dob):
    today = dt.date.today()
    birthday = dob.replace(year=today.year)
    if today < birthday:  # -1 if they haven't had their birthday yet this year
        return today.year - dob.year - 1
    else:
        return today.year - dob.year


day = input('Please enter a DAY of birth (DD): ')
month = input('Please enter a MONTH of birth (MM): ')
year = input('Please enter a YEAR of birth (YYYY): ')
dob = dt.date(int(year), int(month), int(day))  # formatted as a date
print(age_calc(dob))
