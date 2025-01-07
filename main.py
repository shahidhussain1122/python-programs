def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 30

def day_of_week(day, month, year):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

def print_month_calendar(month, year):
    days = days_in_month(month, year)
    dow = day_of_week(1, month, year)
    
    print(f"{['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December'][month-1]} {year}")
    print("Mo Tu We Th Fr Sa Su")
    
    for i in range(dow):
        print("   ", end="")
    
    for day in range(1, days+1):
        print(f"{day:>2} ", end="")
        if (day + dow) % 7 == 0:
            print()
    
    print("\n")

def print_year_calendar(year):
    for month in range(1, 13):
        print_month_calendar(month, year)