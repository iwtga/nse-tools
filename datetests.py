import datetime
import calendar

# assuming input_date will be in the format dd-mm-yyyy
def isLastThursday(input_date):
    # storing the given day, month, year
    d, m, y = map(int, input_date.split('-'))

    # Creating a date instance of the same
    gDate = datetime.date(y, m, d)

    # Creating a timedelta of 7 days
    tdelta = datetime.timedelta(days=7)

    # Checking if the day is thursday
    if gDate.isoweekday() == 4:
        # Checking if adding 7 days takes us to the next month
        return (gDate + tdelta).month != m
    else:
        return False


# Assuming input month will be in the format mm
# Also assuming the year to be current year
def getLastThursday(input_month):
    # storing current year
    cur_year = datetime.date.today().year

    # storing current month
    m = int(input_month)

    # creating a calender instance
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # list of thursdays in that month
    l_of_thursdays = []

    # for each day in that month
    for i in cal.itermonthdays4(cur_year, m):

        # if the day is a thursday
        if i[1] == m and i[3] == 3:
            l_of_thursdays.append(i)
    
    #storing the last thursday
    last_thursday = l_of_thursdays[-1]

    # returning last thursday in mm-dd-yyyy
    return f'{last_thursday[2]}-{m}-{cur_year}'

if __name__ == '__main__':
    print(isLastThursday('25-03-2021'))
    print(getLastThursday('04'))